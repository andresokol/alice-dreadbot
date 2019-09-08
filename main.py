from aiohttp import web
import asyncio
import os
import uvloop

PORT = os.getenv('PORT', 8080)


async def ping(request) -> web.Response:
    return web.json_response({'status': 'ok'})


async def alice_twitch_get(request) -> web.Response:
    print('ok')
    return web.json_response({})


async def alice_twitch_post(request) -> web.Response:
    body = await request.json()
    response = {
        'version': body['version'],
        'session': body['session'],
        'response': {
            'end_session': False,
            'text': 'Лол'
        }
    }
    return web.json_response(response)


def create_app() -> web.Application:
    app = web.Application()

    app.router.add_get('/', ping)
    app.router.add_get('/alice-twitch/', alice_twitch_get)
    app.router.add_post('/alice-twitch/', alice_twitch_post)

    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = create_app()
    web.run_app(app=app, port=PORT)
