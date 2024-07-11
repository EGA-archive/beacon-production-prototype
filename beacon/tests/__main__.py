from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import web
from beacon.__main__ import control
from beacon.logs.logs import log_with_args
import logging
import json
import unittest

def create_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/control', control)])
    return app

# loop_context is provided as a utility. You can use any
# asyncio.BaseEventLoop class in its place.

class TestApp(unittest.TestCase):
    def test_main_check_control_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_check_control_endpoint_is_working():
                resp = await client.get("/control")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'status': 2}) == text
            loop.run_until_complete(test_check_control_endpoint_is_working())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()