# olivia-chan a telegram group managing bot by olivia!:)
# telegram: https://telegram.me/oliviant,
# copyright: olivia-chan 2022

import asyncio
import importlib
import re
from contextlib import closing, suppress

from uvloop import install
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from olivia import(
  BOT_NAME,
  BOT_USERNAME,
  LOG_GROUP_ID,
  aiohttpsession,
  app,
  log,
)
from olivia.modules import ALL_MODULES
