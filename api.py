import requests
import json
from datetime import datetime


api_key = "346d0fc8-2629-4a2e-8058-2c2c02140d3f" 
country = "RU"
year = 2025
month = 3
url = "https://holidayapi.com/v1/holidays"
params = {'key': api_key, 'country': country, 'year': year, 'month': month}

response = requests.get(url, params=params, timeout=10)
data = response.json()
    
holidays = data.get('holidays', []) if isinstance(data, dict) else []
    
with open('holidays.json', 'w', encoding='utf-8') as f:
    json.dump(holidays, f, ensure_ascii=False, indent=2)

if month == 0: 
  print(f"\n Праздники {country} за весь год ({len(holidays)} шт.):\n")
else:
  print(f"\n Праздники {country} в {month}.{year} ({len(holidays)} шт.):\n")

for i, h in enumerate(holidays, 1):
  if isinstance(h, dict):
    date = datetime.strptime(h.get('date', ''), '%Y-%m-%d') 
    print(f"{i}. {h.get('name')}")
    if date:
      print(f"   {date.strftime('%d %B %Y')}")
      print()
  
  if not holidays:
    print("В этом месяце нет государственных праздников или данные недоступны для бесплатного аккаунта.\n")