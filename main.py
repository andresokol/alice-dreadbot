from aiohttp import web
import asyncio
import uvloop


async def ping(request) -> web.Response:
    return web.json_response({'status': 'ok'})


async def alice_twitch(request) -> web.Response:
    return web.Response(text='ОК')


def create_app() -> web.Application:
    app = web.Application()

    app.router.add_get('/', ping)
    app.router.add_get('/get_alice/', alice_twitch)

    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = create_app()
    web.run_app(app=app)
