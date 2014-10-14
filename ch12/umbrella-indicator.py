import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

ApiUrl = 'http://api.wunderground.com/api/YOUR_API_KEY/forecast/q/NY/New_York.json'

while True:
   r = requests.get(ApiUrl)
   forecast = r.json
   popValue = forecast['forecast']['txt_forecast']['forecastday'][0]['pop']
   popValue = int(popValue)

   if popValue >= 30:
      GPIO.output(25, GPIO.HIGH)
   else: 
      GPIO.output(25, GPIO.LOW)

   time.sleep(180) # 3 minutes