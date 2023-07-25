from django.core.management.base import BaseCommand
from aiogram import executor

from tg_bot.handlers import dp


class Command(BaseCommand):
    help = 'Start telegram bot: python manage.py start_bot'

    def handle(self, *args, **options):
        print("***Telegram Bot started...")
        executor.start_polling(dp, skip_updates=True)



