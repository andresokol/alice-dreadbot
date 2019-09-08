WELCOME_MESSAGE = 'Привет, я могу сказать, ' \
                  'стримит ли сейчас Андрей Dread Голубев.'
DEFAULT_MESSAGE = 'Не поняла'


async def prepare_response(request: dict) -> str:
    if not request['command']:
        return WELCOME_MESSAGE

    game_name = await request.app.dread_cache.get_data()
    return f'Дред стримит {game_name}'
