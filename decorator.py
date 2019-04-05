import datetime
import requests
import logging
logging.basicConfig(handlers=[logging.FileHandler('log_out.txt', 'w', 'utf-8')],
                    level=logging.DEBUG)


API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def decorator(old_func):
    def new_func(*args, **kwargs):
        start = datetime.datetime.now()
        logging.debug('Время вызова: ' + str(start))
        logging.debug('Имя функции: ' + old_func.__name__)
        logging.debug('Аргументы вызова: ' + str(args))
        out = old_func(*args, **kwargs)
        logging.debug('Возвращаемое значение: ' + str(out))
        return out
    return new_func


@decorator
def translate_it(path_in, path_out, lang_in, to_lang = 'ru'):
    text = ''

    with open(path_in, 'r', encoding='utf-8') as file:
       for line in file:
           text += line

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang_in +'-' + to_lang
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    out_data = json_['text'][0]

    with open(path_out, 'w', encoding='utf-8') as output:
        output.write(out_data)


def main():
    translate_it('DE.txt', 'translation.txt', 'de')


main()
