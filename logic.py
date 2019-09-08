WELCOME_MESSAGE = 'Привет, я могу сказать, ' \
                  'стримит ли сейчас Андрей Dread Голубев.'

DEFAULT_MESSAGE = 'Не поняла'


async def prepare_response(request: dict) -> str:
    if not request['command']:
        return WELCOME_MESSAGE

    return DEFAULT_MESSAGE
