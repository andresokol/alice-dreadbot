import os

import aiohttp

TWITCH_API_KEY = os.getenv('TWITCH_API_KEY')

TWITCH_DREAD_URL = 'https://api.twitch.tv/helix/streams?user_login=dreadztv'
TWITCH_GAME_URL = 'https://api.twitch.tv/helix/games'

WELCOME_MESSAGE = 'Привет, я могу сказать, ' \
                  'стримит ли сейчас Андрей Dread Голубев.'

DEFAULT_MESSAGE = 'Не поняла'


async def _fetch_name() -> str:
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            TWITCH_DREAD_URL,
            headers={'Client-ID': TWITCH_API_KEY}
        )
    dread_data = await response.json()
    dread_data = dread_data['data'][0]

    game_id = dread_data['game_id']
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            TWITCH_GAME_URL,
            params={'id': game_id},
            headers={'Client-ID': TWITCH_API_KEY}
        )
    game_name = (await response.json())['data'][0]['name']
    return f'Дрюс катает в {game_name}'


async def prepare_response(request: dict) -> str:
    if not request['command']:
        return WELCOME_MESSAGE

    return await _fetch_name()
    # return DEFAULT_MESSAGE
