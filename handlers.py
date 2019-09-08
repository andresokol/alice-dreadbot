from aiohttp import web

import logic


async def ping(request) -> web.Response:
    game_name = await request.app.dread_cache.get_data()
    return web.json_response({'playing': game_name})


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
            'text': await logic.prepare_response(body['request'])
        }
    }
    return web.json_response(response)
