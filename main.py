#region Import.
import time

import config
import requests
import json

from requests import Response, Request
from pathlib import Path

from config import LATENCY

#endregion
'''
DEX Screener's parser on requests and DEX Screener API.
'''


def clear_folder(path: Path) -> None:
    """
    Clear folder from old top tokens API request.
    :param path: folder path.
    :return: None.
    """
    for item in path.iterdir():
        if item.is_file():
            item.unlink()
        else:
            clear_folder(item)
    logger.info(f'Clear old data from {Path} folder.')


def print_step_with_new_line(message: str = '') -> None:
    print(message + '\n')


def json_to_dict(json_format: str) -> {}:
    """
    Parse json format to Python dictionary.
    :param json_format: text as string.
    :return: dict.
    """
    dict_format = {}
    for key, value in dict(json_format).items():
        dict_format[key] = value
    return dict_format


# Send GET request.
def send_get_request(url: str, headers: {}) -> Response:
    return requests.get(url, headers=headers)


def export_to_json(file_path: str, response: Response) -> None:
    """
    Save parsed content to .json file.
    :param file_path: filepath.
    :param response: json response.
    :return: None.
    """
    # Save json format as dump.
    with open(file_path, 'w') as f:
        json.dump(response.json(), f, indent=4)


def import_from_json(file_path: str) -> str:
    """
    Load parsed content from .json file.
    :param file_path: filepath.
    :return: string.
    """
    # Load json from dump.
    with open(file_path, 'r') as f:
        loader = json.load(f)
    json_content = loader
    return json_content

logger = config.logger
logger.info('Starting application.')

msg: str = ''
exception_msg: str = ''

def main():
    global msg
    msg = 'Starting DEX Screener parser.'
    print_step_with_new_line(msg)
    logger.debug(msg)

    msg = f'Current useragent: {config.user_agent}.'
    print_step_with_new_line(msg)
    logger.debug(msg)

    while (True):
        # Send boosts tokens GET request.
        try:
            # Check ./tokens-info/ folder existing.
            if not Path(config.TOKENS_INFO_FOLDER_FILE_PATH).exists():
                Path(config.TOKENS_INFO_FOLDER_FILE_PATH).mkdir(parents=True, exist_ok=False)
            # Clear old parsed data from ./tokens-info/.
            if any(Path(config.TOKENS_INFO_FOLDER_FILE_PATH).iterdir()):
               clear_folder(Path(config.TOKENS_INFO_FOLDER_FILE_PATH))

            response = send_get_request(config.token_boosts_url, headers=config.headers)
            msg = f'GET to: {config.token_boosts_url}. Status code: {response.status_code}'
            print_step_with_new_line(msg)
            logger.debug(msg)
            response.raise_for_status()

            export_to_json(config.ALL_TOKENS_FILE_PATH, response)
            msg = f'Successfully export all tokens info to {config.ALL_TOKENS_FILE_PATH}'
            print_step_with_new_line(msg)
            logger.info(msg)

            tokens_json = import_from_json(config.ALL_TOKENS_FILE_PATH)
            msg = f'Successfully import all tokens info from {config.ALL_TOKENS_FILE_PATH}'
            print_step_with_new_line(msg)
            logger.info(msg)

            # Get tokens data from json.
            msg = 'Starting of parsing of each token'
            list_tokens = list(tokens_json)
            for token in list_tokens:
                # Create dict for save current token data.
                current_token_data = json_to_dict(token)

                # Get additional info about current token.
                config.set_token_address(current_token_data['tokenAddress'])
                response = send_get_request(config.token_info_url, headers=config.headers)
                msg = f'GET to: {config.token_info_url}. Status code: {response.status_code}'
                logger.debug(msg)
                response.raise_for_status()

                # Save additional info about current token in .json format.
                current_token_name = (response.json()
                      ['pairs']
                      [0]
                      ['baseToken']
                      ['symbol']
                )
                config.set_token_name(current_token_name) # get token's ticker
                export_to_json(config.TOKENS_INFO_FOLDER_FILE_PATH + config.current_token_file_path, response)
                msg = (f"Successfully export token {current_token_name} info with address {current_token_data['tokenAddress']} "
                    f"to {config.current_token_file_path}")
                print_step_with_new_line(msg)
                logger.info(msg)

            time.sleep(config.LATENCY)

        except Exception as ex:
            msg = f'Error while parsing tokens. See logs for details. . .'
            print_step_with_new_line(msg)
            logger.error(str(ex))


if __name__ == '__main__':
    print(config.LOGO)
    main()
    logger.info('Close application.')