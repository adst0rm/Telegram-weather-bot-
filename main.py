from aiogram import Bot, Dispatcher, executor, types
import python_weather
import asyncio
import os

#bot init 
bot = Bot(token="5720613212:AAG7OGTuFh_WiiVq-oVPwDrFtUAMBNXNQy4")
dp = Dispatcher(bot)


#echo
client = python_weather.Client(format=python_weather.IMPERIAL)
@dp.message_handler()
async def echo (message: types.Message):
	weather = await client.get(message.text)
	cel = round((weather.current.temperature - 32) / 1.8)

	
	resp_msg = f"Temperature : {cel} °\n" 
	resp_msg += f"Description : {weather.current.description}\n"
	if cel < 10:
		resp_msg += "It's cold outside"
	else:
		resp_msg += "It's hot outside"
	

	await message.answer(resp_msg)
	 
		

 

	

#run long-polling
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)