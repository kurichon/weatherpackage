import os
from datetime import datetime, timedelta
import pytest
import requests_mock
from weatherpkg import api

# Mock .env loading
os.environ['WEATHER_API_KEY'] = "fake_api_key"

# Test extract_location function
def test_extract_location():
    assert api.extract_location("서울의 날씨는 어때?") == "서울"
    assert api.extract_location("부산의 날씨 알려줘") == "부산"
    assert api.extract_location("날씨는 어때?") is None

# Unit test for extract_date
def test_extract_date():
    assert api.extract_date("내일 서울 날씨는 어때?") == "내일"
    assert api.extract_date("2024년 10월 25일 서울 날씨") == "2024년 10월 25일"
    assert api.extract_date("서울의 날씨는 어때?") is None

# Unit test for format_date_to_unix_format
def test_format_date_to_unix_format():
    date_str = "2024-11-01"
    assert api.format_date_to_unix_format(date_str) == int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())

# Unit test for format_date_to_YYYY_MM_DD
def test_format_date_to_YYYY_MM_DD():
    assert api.format_date_to_YYYY_MM_DD("내일")  == (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d") # Should return a valid date based on today
    assert api.format_date_to_YYYY_MM_DD("다음 주") ==(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d") # Should return a valid date based on today

# Unit test for romanize_location
def test_romanize_location():
    assert api.romanize_location("서울") == "seoul"
    assert api.romanize_location("부산") == "busan"

# Mock the weather API response
#@pytest.fixture
#def mock_get_weather():
#    with requests_mock.Mocker() as m:
        # Set up the mock URL
#        fake_url = 'https://api.openweathermap.org/data/2.5/weather'
#        m.get(fake_url, json={
#            'weather': [{'description': '맑음'}],
#            'main': {'temp': 25}
#        }, status=200)
#
#        # Call the query function with a test question
#        response = api.query("내일 서울 날씨는 어때?")
#
#        # Assert the expected response
#        assert response == "서울의 내일 날씨는 맑음이며, 기온은 25도입니다."  # Adjust the date based on your logic
#
# Unit test for get_weather
#def test_get_weather(mock_get_weather):
#    result = api.get_weather("Seoul", 1698883200, "내일", "서울")
#    assert "서울의 내일 날씨는 맑음이며, 기온은 20.5도입니다." in result

# Test for main query function
#def test_query_with_valid_input(mock_get_weather):
#    question = "내일 서울 날씨 알려줘"
#    result = api.query(question)
#    assert "서울의 내일 날씨는 맑음이며, 기온은 20.5도입니다." in result

def test_query_with_missing_location():
    question = "내일 날씨 알려줘"
    result = api.query(question)
    assert result == "위치 정보를 찾을 수 없습니다. 다시 입력해 주세요."

def test_query_with_missing_date():
    question = "서울 날씨 알려줘"
    result = api.query(question)
    assert result == "날짜 정보를 찾을 수 없습니다. 다시 입력해 주세요."