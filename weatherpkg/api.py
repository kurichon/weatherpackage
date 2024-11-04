import os
from dotenv import load_dotenv

#date parsing
from datetime import datetime
import dateparser

from konlpy.tag import Kkma #location

#openweather api call
import requests
from korean_romanizer.romanizer import Romanizer #romanize Korean for api call
#location tagger using Kkma
tagger = Kkma()

# Load environment variables from .env file
load_dotenv()

def query(question: str) -> str:
    location = extract_location(question)
    nlp_date = extract_date(question)
    #errors
    if not location:
        return "위치 정보를 찾을 수 없습니다. 다시 입력해 주세요."
    if not nlp_date:
        return "날짜 정보를 찾을 수 없습니다. 다시 입력해 주세요."
    formatted_date = format_date_to_YYYY_MM_DD(nlp_date)
    unix_date = format_date_to_unix_format(formatted_date)
    romanized_location = romanize_location(location)
    #print(romanized_location)
    #print (formatted_date)
    return get_weather(romanized_location,unix_date,nlp_date,location)

def extract_location(question: str) -> str:
    tokens = tagger.morphs(question)
    pos_tags = tagger.pos(question)

    entities = []
    for word, (token, tag) in zip(tokens, pos_tags):
        if tag in ['NNP', 'NNG'] and token in ['서울', '부산', '제주도']:  # Add more locations here
            entities.append((token))
            return entities[0]
    return None
def extract_date(question: str) -> datetime | None:
    import re
    date_pattern = re.compile(
        r'(\d{1,4}년\s*\d{1,2}월\s*\d{1,2}일|\d{1,2}일|\d{1,2}월\s*\d{1,2}일|\d{1,4}년|\d{1,2}일의\s*주|\d{1,2}월|\b내일\b|\b다음\s*주\b)',
        re.IGNORECASE)
    # Find all matches in the text
    found_dates = date_pattern.findall(question)
    if (found_dates):
        return found_dates[0]
    return None
def format_date_to_unix_format(parsed_date):
    if parsed_date:
        date_time = datetime.strptime(parsed_date, "%Y-%m-%d")
        unix_timestamp = int(date_time.timestamp()) # Format to YYYY-MM-DD to unix format
        return unix_timestamp
    else:
        return None

def format_date_to_YYYY_MM_DD(nlp_date):
    parsed_date = dateparser.parse(nlp_date, languages=['ko'])
    if (parsed_date):
        return parsed_date.strftime("%Y-%m-%d")
    return None

def romanize_location(location):
    r = Romanizer(location)
    output = r.romanize()
    return output


def get_weather(location,date,nlp_date,kr_location):
    api_key = os.getenv('WEATHER_API_KEY')  # Fetch from environment variable
    # Fetch historical weather data, Unix timestamp format, English text
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&dt={date}&appid={api_key}&lang=kr&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{kr_location}의 {nlp_date} 날씨는 {weather_desc}이며, 기온은 {temperature}도입니다."
    else:
        return f"{kr_location}에 대한 날씨 정보를 가져올 수 없습니다."
