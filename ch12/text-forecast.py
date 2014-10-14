import requests

ApiUrl = 'http://api.wunderground.com/api/YOUR_API_KEY/forecast/q/NY/New_York.json'

r = requests.get(ApiUrl)
forecast = r.json
print forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext']