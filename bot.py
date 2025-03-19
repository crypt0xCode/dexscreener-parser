#region Import.
import time

import aiogram.utils.markdown
from aiogram.enums import ParseMode

import config
import json
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties

from pathlib import Path
from main import import_from_json
from main import print_step_with_new_line
#endregion
'''
Parser's bot which send structured info about each token to Telegram chat.
'''

logger = config.logger
logger.info('Starting application.')

msg: str = ''
exception_msg: str = ''

BOT_TOKEN = 'SET_YOUR_BOT_API_TOKEN'
dp = Dispatcher()


async def convert_token_data(token_json: str) -> str:
    """
    Show each token data in HTML parsed format to Telegram.
    :param token_json: token JSON data.
    :return: HTML parsed Telegram format.
    """
    data_dict: {} = dict(token_json['pairs'][0])
    # Return structured data with HTML tags.
    structured_token_data: str = f'''
<b>General Info</b>
chainId: {data_dict['chainId']}
dexId: {data_dict['dexId']}
url: <a href="{data_dict['url']}">*click*</a>
pairAddress: {data_dict['pairAddress']}
marketCap: {data_dict['marketCap']}

<b>Base Token Info</b>
address: {data_dict['baseToken']['address']}
description: {data_dict['baseToken']['name']}
ticker: ${data_dict['baseToken']['symbol']}

<b>Price Info</b>
priceNative: {data_dict['priceNative']}
priceUSD: {data_dict['priceUsd']}

<b>Transactions Info</b>
<i>buys | sells</i>
m5: {data_dict['txns']['m5']['buys']} | {data_dict['txns']['m5']['sells']}
h1: {data_dict['txns']['h1']['buys']} | {data_dict['txns']['h1']['sells']}
h6: {data_dict['txns']['h6']['buys']} | {data_dict['txns']['h6']['sells']}
h24: {data_dict['txns']['h24']['buys']} | {data_dict['txns']['h24']['sells']}

<b>Volume Info</b>
m5: {data_dict['volume']['m5']}
h1: {data_dict['volume']['h1']}
h6: {data_dict['volume']['h6']}
h24: {data_dict['volume']['h24']}

<b>Price Change Info</b>
m5: {data_dict['priceChange']['m5']}
h1: {data_dict['priceChange']['h1']}
h6: {data_dict['priceChange']['h6']}
h24: {data_dict['priceChange']['h24']}

<b>Liquidity Info</b>
USD: {data_dict['liquidity']['usd']}
base: {data_dict['liquidity']['base']}
quote: {data_dict['liquidity']['quote']}
    '''
    return structured_token_data


# Main bot handler.
@dp.message(Command('start'))
async def start_handler(message: types.Message):
    global msg
    msg = 'Starting parser bot.'
    print_step_with_new_line(msg)
    logger.info(msg)
    while(True):
        try:
            for item in sorted(Path(config.TOKENS_INFO_FOLDER_FILE_PATH).iterdir()):
                token_json = import_from_json(item) # load data from .json file
                reply: str = await convert_token_data(token_json)

                current_token_name = (dict(token_json)
                        ['pairs']
                        [0]
                        ['baseToken']
                        ['symbol']
                )
                msg = f'Successfully import token {current_token_name} info'
                print_step_with_new_line(msg)
                logger.info(msg)

                await message.answer(text=reply, parse_mode=ParseMode.HTML)
                time.sleep(10)

        except Exception as ex:
            msg = f'Error while send token data to Telegram. See logs for details. . .'
            print_step_with_new_line(msg)
            logger.error(str(ex))
            continue


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
