# import the module
import python_weather
import asyncio
import os

async def getweather():
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
    weather = await client.get("Aksay")

    cel = (weather.current.temperature - 32) / 1.8
  
    # returns the current day's forecast temperature (int)
    print(str(round(cel)) + "°C")

    print(weather.current.description)

    if cel<10:
      print("Weather is cold!")

    print(weather.location)
  
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
      print(forecast)
  
      # hourly forecasts
      for hourly in forecast.hourly:
        print(f' --> {hourly!r}')

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())