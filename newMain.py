from unicodedata import name
from aiogram import Bot, Dispatcher, executor, types
from auth import token
import json
from aiogram.dispatcher.filters.state import State, StatesGroup

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет я бот хранящий твои контакты \nчто бы не засорять твой телефон, сохрани в меня")
    
@dp.message_handler(commands=['savecontacts'])
async def process_start_command(message: types.Message):
    await message.reply("Напиши контакт в строчку через пробел")
    
    @dp.message_handler()
    async def echo(message: types.Message):
        member = message.text
        
        with open("users.json", "r+", encoding='utf-8') as json_file:
            a = json.load(json_file)
            
        sep=' '
        result = [x for x in member.split(sep)]
        name = result[0]
        phone = result[1]
        a[name] = f"{phone}"
           
        with open("users.json", "r+", encoding='utf-8') as json_file:
            json.dump(a, json_file, indent=4)

        await message.reply("Контакт успешно сохранен")
    
    
@dp.message_handler(commands=['delcontacts'])
async def process_start_command(message: types.Message):
    await message.reply("Напиши имя кого вы хотетите удалить")
    
    @dp.message_handler()
    async def echo(message: types.Message):
        member = message.text
        
        with open("users.json", "r+", encoding='utf-8') as json_file:
            a = json.load(json_file)
        
        del a[f'{member}']
        json.dumps(a)
        with open("users.json", "w") as json_file:
            json.dump(a, json_file)
            
        await message.reply("Контакт успешно удален") 
        
@dp.message_handler(commands=['search'])
async def process_start_command(message: types.Message):
    await message.reply("Напиши имя кого вы хотетите увидеть")
    
    @dp.message_handler()
    async def echo(message: types.Message):
        namePoisc = message.text
        
        with open("users.json", "r+", encoding='utf-8') as json_file:
            a = json.load(json_file)
        
        await message.reply(a[str(namePoisc)]) 
            
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)