from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from commands import get_config, start, stop, allmsg


router = Router()

@router.message(Command("getconfig"))
async def start_handler(msg: Message): await get_config(msg)

@router.message(Command("setmetod"))
async def start_handler(msg: Message): await set_generate_metod(msg)

@router.message(Command("resetkey"))
async def start_handler(msg: Message): await resetkey(msg)


@router.message(Command("start"))
async def start_handler(msg: Message): await start(msg)


@router.message(Command("stop"))
async def stop_hundel(msg: Message): await stop(msg)


@router.message()
async def message_handler(msg: Message): await allmsg(msg)


