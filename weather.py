import requests
import os

def get_weather(city='Tokyo'):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja'
    res = requests.get(url)
    return res.json()

def suggest_outfit(temp):
    if temp >= 30:
        return "🔥 非常に暑いです。半袖・短パン・帽子・水分補給を忘れずに！"
    elif 27 <= temp < 30:
        return "🌤 暑い一日。半袖＋薄手の服でOK。"
    elif 24 <= temp < 27:
        return "👕 少し暑め。半袖やポロシャツで快適です。"
    elif 20 <= temp < 24:
        return "🌤 薄手の長袖やカーディガンがあると安心。"
    elif 17 <= temp < 20:
        return "🍂 長袖＋軽いジャケットで快適。"
    elif 13 <= temp < 17:
        return "🧥 肌寒いので上着が必要です。"
    elif 10 <= temp < 13:
        return "🥶 寒いです。厚手の上着を着ましょう。"
    elif temp < 10:
        return "❄️ 非常に寒いです。コート＋完全防寒を！"
    else:
        return "服装のアドバイスが難しい気温です。"

def umbrella_advice(weather_main):
    if weather_main in ['Rain', 'Drizzle', 'Thunderstorm']:
        return "☔ 雨が降りそうです。傘を持ちましょう！"
    elif weather_main in ['Clouds', 'Snow']:
        return "☁️ 折りたたみ傘があると安心です。"
    else:
        return "🌞 傘は必要なさそうです。"

def get_daily_message(city):
    data = get_weather(city)
    temp = data['main']['temp']
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    weather_main = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']

    outfit = suggest_outfit(temp)
    umbrella = umbrella_advice(weather_main)

    return f"""【今日の天気（{city}）】
🌡 現在：{temp:.1f}℃ / 最高：{temp_max:.1f}℃ / 最低：{temp_min:.1f}℃
☁️ 天気：{weather_desc}

👕 服装アドバイス：
{outfit}

☂️ 傘チェック：
{umbrella}
"""
