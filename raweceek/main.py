import asyncio

from raweceek.cldr import get_events
from raweceek.telegram import send_message


async def start():
    races = await get_events()
    if races:
        message = '*IT\'S A RAWE CEEK*\n\n\n'
        for r in races:
            message += r + '\n\n'

        await send_message(message)


if __name__ == '__main__':
    asyncio.run(start())
