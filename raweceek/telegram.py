import os

import httpx

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


async def send_message(message: str):
    async with httpx.AsyncClient() as client:
        # change chat id to get from db
        # params to get from config
        params = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'MarkdownV2',
                  'disable_notification': True}
        r = await client.get(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
            params=params,
        )
        # add logging
        if r.status_code != 200:
            print('shit')