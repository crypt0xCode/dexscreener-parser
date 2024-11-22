#region Import.
import json
import requests
from bs4 import BeautifulSoup as BS
import logging
from logging import FileHandler, Formatter
import config
#endregion
'''
DEX Screener's HTML parser on BS4 + Requests.
'''


logger = config.logger
logger.info("Starting application.")

msg: str = ''
exception_msg: str = ''

def main():
    logger.debug("Starting application.")
    print("Starting DEX Screener parser.")

    msg = f"\nCurrent useragent: {config.user_agent}."
    print(msg)
    logger.debug(msg)

    # Send GET request.
    request = requests.get(config.url, headers=config.headers)
    file_path: str = './tokens.json'

    # Save json format as dump.
    with open(file_path, 'w') as f:
        json.dump(request.json(), f, indent=4)

    # Load json from dump.
    tokens_json: str = ''
    with open(file_path, 'r') as f:
        tokens_json = json.load(f)

    # Get tokens data from json.
    list_tokens = list(tokens_json)
    for token in list_tokens:
        token_data = {}
        for key, value in token.items():
            token_data[key] = value
        print(token_data)

if __name__ == '__main__':
    main()