import aiohttp
import datetime as dt
import os

TWITCH_API_KEY = os.getenv('TWITCH_API_KEY')

TWITCH_DREAD_URL = 'https://api.twitch.tv/helix/streams?user_login=dreadztv'
TWITCH_GAME_URL = 'https://api.twitch.tv/helix/games'

UPDATE_DELTA = dt.timedelta(seconds=30)


class DreadCache:
    _data = None
    _updated = None

    async def _update_data(self):
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                TWITCH_DREAD_URL,
                headers={'Client-ID': TWITCH_API_KEY}
            )
        dread_data = await response.json()
        dread_data = dread_data['data'][0]

        game_id = dread_data['game_id']
        async with aiohttp.ClientSession() as session:
            game_list_response = await session.get(
                TWITCH_GAME_URL,
                params={'id': game_id},
                headers={'Client-ID': TWITCH_API_KEY}
            )
        game_list_response = await game_list_response.json()
        self._data = game_list_response['data'][0]['name']
        self._updated = dt.datetime.now()

    async def get_data(self):
        now = dt.datetime.now()

        if self._data is None or now - self._updated > UPDATE_DELTA:
            await self._update_data()

        return self._data
