WELCOME_MESSAGE = 'Привет, я могу сказать, ' \
                  'что сейчас стримит Андрей Dread Голубев.'
DEFAULT_MESSAGE = 'Не поняла'
FAREWELL_MESSAGE = 'Пока!'

STOP_WORDS = ['стоп', 'хватит', 'остановись', 'спасибо', 'выход', 'прекрати']


async def prepare_response(request: dict, dread_cache) -> (str, bool):
    if not request['command']:
        return WELCOME_MESSAGE, False

    for word in STOP_WORDS:
        if word in request['nlu']['tokens']:
            return FAREWELL_MESSAGE, True

    game_name = await dread_cache.get_data()
    return f'Дред стримит {game_name}', False
