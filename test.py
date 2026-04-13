#!/usr/bin/env python3
"""
Jin10 Skill Smoke Test
测试基础功能，不依赖真实 API
"""

import sys
import os
import io
import subprocess
from contextlib import redirect_stdout, redirect_stderr

# 添加当前目录到 path
sys.path.insert(0, os.path.dirname(__file__))


def test_import():
    """测试模块导入"""
    from jin10 import Jin10Client, Jin10Error
    from jin10.quotes import QuotesClient
    from jin10.flash import FlashClient
    from jin10.news import NewsClient
    from jin10.calendar import CalendarClient
    print("✓ 模块导入成功")


def test_client_init():
    """测试客户端初始化（不调用 API）"""
    from jin10 import Jin10Client
    from jin10.quotes import QuotesClient

    # 不传 token，应该从环境变量读取（如果没有则为空字符串）
    client1 = Jin10Client()
    assert client1.api_token == os.environ.get('JIN10_API_TOKEN', ''), "环境变量读取失败"

    # 传 token
    client2 = Jin10Client(api_token='test-token')
    assert client2.api_token == 'test-token', "token 参数读取失败"

    # 子模块客户端
    quotes = QuotesClient(api_token='test-token')
    assert quotes.api_token == 'test-token', "QuotesClient token 读取失败"

    # 子客户端共享状态
    client2.session_id = 'session-1'
    client2.initialized = True
    assert client2.quotes.session_id == 'session-1', "子客户端未共享 session_id"
    assert client2.flash.initialized is True, "子客户端未共享 initialized 状态"

    print("✓ 客户端初始化成功")


def test_no_recursion():
    """测试不会无限递归（mock 方式）"""
    from jin10.client import BaseClient

    # 创建一个不发送真实请求的测试客户端
    class MockClient(BaseClient):
        def __init__(self):
            super().__init__(api_token='test')
            self.call_count = 0

        def _do_request(self, payload):
            self.call_count += 1
            if self.call_count > 10:
                raise AssertionError("检测到无限递归！调用次数: {}".format(self.call_count))
            # 返回一个模拟的成功响应
            return {}

    client = MockClient()
    try:
        # 这会触发 initialize -> _do_request -> request -> initialize 的递归
        # 如果代码正确，initialize 应该直接调用 _do_request，不会递归
        client.initialize()
        print("✓ 无递归调用问题")
    except RecursionError:
        raise AssertionError("检测到 RecursionError！存在无限递归 bug。")


def test_missing_token_error():
    """测试缺少 token 时的报错更明确"""
    from jin10.client import BaseClient, Jin10Error

    client = BaseClient(api_token='')
    try:
        client._do_request({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {}})
        raise AssertionError("缺少 token 时未报错")
    except Jin10Error as e:
        assert 'Missing API token' in str(e)

    print("✓ 缺少 token 报错正常")


def test_format_methods():
    """测试格式化方法"""
    from jin10.quotes import QuotesClient
    from jin10.flash import FlashClient
    from jin10.news import NewsClient
    from jin10.calendar import CalendarClient

    # 模拟报价数据
    quote_data = {
        'data': {
            'code': 'XAUUSD',
            'name': '现货黄金',
            'close': 2000.5,
            'ups_price': 10.5,
            'ups_percent': 0.53,
            'open': 1990.0,
            'high': 2010.0,
            'low': 1985.0,
            'time': '2024-01-01 12:00:00'
        }
    }
    formatted = QuotesClient.format_quote(quote_data)
    assert '现货黄金' in formatted
    assert '2000.5' in formatted

    # 模拟快讯数据
    flash_data = {
        'data': {
            'items': [
                {'title': '测试快讯', 'time': '12:00', 'url': 'http://test.com'}
            ],
            'has_more': False
        }
    }
    formatted = FlashClient.format_flash_list(flash_data)
    assert '测试快讯' in formatted

    # 模拟日历数据
    calendar_data = {
        'data': [
            {'pub_time': '14:00', 'star': '3', 'title': '非农',
             'previous': '20', 'consensus': '18', 'actual': '19',
             'revised': '', 'affect_txt': '利多黄金'}
        ]
    }
    formatted = CalendarClient.format_calendar(calendar_data)
    assert '非农' in formatted

    print("✓ 格式化方法正常")


def test_cli():
    """测试 CLI 分发逻辑"""
    import jin10.cli as cli

    class FakeQuotes:
        def get_codes(self):
            return {'data': ['XAUUSD', 'USOIL']}

        def get_quote(self, code):
            return {
                'data': {
                    'code': code,
                    'name': '现货黄金',
                    'close': 2000.5,
                    'ups_price': 10.5,
                    'ups_percent': 0.53,
                    'open': 1990.0,
                    'high': 2010.0,
                    'low': 1985.0,
                    'time': '2024-01-01 12:00:00',
                }
            }

    class FakeFlash:
        def list(self, cursor=None):
            return {'data': {'items': [{'title': '最新快讯', 'time': '12:00', 'url': ''}], 'has_more': False}}

        def search(self, keyword):
            return {'data': {'items': [{'title': keyword, 'time': '12:00', 'url': ''}], 'has_more': False}}

    class FakeNews:
        def list(self, cursor=None):
            return {'data': {'items': [{'title': '最新资讯', 'time': '12:00', 'introduction': '摘要', 'url': ''}], 'has_more': False}}

        def search(self, keyword, cursor=None):
            return {'data': {'items': [{'title': keyword, 'time': '12:00', 'introduction': '摘要', 'url': ''}], 'has_more': False}}

        def get(self, id):
            return {'data': {'id': id, 'title': '详情', 'introduction': '摘要', 'content': '正文', 'time': '12:00', 'url': ''}}

    class FakeCalendar:
        def list(self):
            return {'data': [{'pub_time': '14:00', 'star': '3', 'title': '非农', 'previous': '20', 'consensus': '18', 'actual': '19'}]}

        def get_high_importance(self):
            return [{'pub_time': '14:00', 'star': '3', 'title': '非农', 'previous': '20', 'consensus': '18', 'actual': '19'}]

        def search(self, keyword):
            return [{'pub_time': '14:00', 'star': '3', 'title': keyword, 'previous': '20', 'consensus': '18', 'actual': '19'}]

    class FakeClient:
        def __init__(self):
            self.quotes = FakeQuotes()
            self.flash = FakeFlash()
            self.news = FakeNews()
            self.calendar = FakeCalendar()

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        code = cli.run_command(cli.build_parser().parse_args(['--format', 'json', 'quote', 'XAUUSD']), FakeClient())
    assert code == 0
    assert 'XAUUSD' in stdout.getvalue()

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        code = cli.run_command(cli.build_parser().parse_args(['--format', 'text', 'calendar', '--high-importance']), FakeClient())
    assert code == 0
    assert '非农' in stdout.getvalue()

    stderr = io.StringIO()
    original_client = cli.Jin10Client
    cli.Jin10Client = lambda: (_ for _ in ()).throw(cli.Jin10Error('boom'))
    try:
        with redirect_stderr(stderr):
            code = cli.main(['quote', 'XAUUSD'])
        assert code == 1
        assert 'boom' in stderr.getvalue()
    finally:
        cli.Jin10Client = original_client

    print("✓ CLI 正常")


def test_bundled_launcher():
    """测试随 skill 分发的脚本入口"""
    launcher = os.path.join(os.path.dirname(__file__), 'scripts', 'jin10.py')
    result = subprocess.run(
        [sys.executable, launcher, '--help'],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, "launcher 执行失败"
    assert 'Jin10 财经数据 CLI' in result.stdout, "launcher 未正确输出帮助信息"
    print("✓ 自带脚本入口正常")


def main():
    print("=== Jin10 Skill Smoke Test ===\n")

    try:
        test_import()
        test_client_init()
        test_no_recursion()
        test_missing_token_error()
        test_format_methods()
        test_cli()
        test_bundled_launcher()
        print("\n✅ 所有测试通过")
        return 0
    except AssertionError as e:
        print("\n❌ 测试失败: {}".format(e))
        return 1
    except Exception as e:
        print("\n❌ 错误: {}".format(e))
        return 1


if __name__ == '__main__':
    sys.exit(main())
