import asyncio
from helpers.filters import command
from config import BOT_NAME, SUPPORT_GROUP, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Client.on_message(command("help") & filters.private & ~filters.group & ~filters.edited)
async def help_cmd(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZIiVngABAoCAYqWU-JzBZtfz14vr_DfDkJyy7X8AAjYGAAIsk1lUo7RMhQfOm28eBA")
