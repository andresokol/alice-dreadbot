from aiohttp import web
import asyncio
import os
import uvloop

import handlers

PORT = os.getenv('PORT', 8080)


def create_app() -> web.Application:
    app = web.Application()

    app.router.add_get('/', handlers.ping)
    app.router.add_get('/alice-twitch/', handlers.alice_twitch_get)
    app.router.add_post('/alice-twitch/', handlers.alice_twitch_post)

    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = create_app()
    web.run_app(app=app, port=PORT)
