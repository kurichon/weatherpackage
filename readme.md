## 목적
이 프로젝트는 자연어로 입력된 질문을 통해 특정 위치와 날짜의 날씨 정보를 가져오는 Python 패키지입니다. 사용자로부터 질문을 받아, 해당 위치와 날짜를 추출한 후, OpenWeather API를 통해 날씨 정보를 반환합니다.

## 사용하기
1. **환경 설정**  
   - Python 3.8 이상이 필요합니다.
   - 필요한 패키지를 설치합니다:

     ```bash
     pip install -r requirements.txt
     ```

   - `.env` 파일을 프로젝트 루트에 생성하고, OpenWeather API 키를 추가합니다:

     ```env
     WEATHER_API_KEY=your_api_key_here
     ```

2. **패키지 사용 예시**  
   아래와 같이 패키지를 사용하여 날씨 정보를 쿼리할 수 있습니다:

   ```python
   from weather_package import query

   answer = query("내일 서울 날씨는 어때?")
   print(answer)  # Output: 서울의 내일 날씨는 ...입니다.
   
## 테스트 하기
- 테스트를 위해 pytest를 사용합니다. 
- tests/ 폴더 내에 있는 테스트 파일을 실행하여 기능을 검증할 수 있습니다.

```pytest tests/test_query.py```
- 테스트 결과
  - 테스트가 성공적으로 수행되면 모든 기능이 정상적으로 작동하고 있음을 의미합니다.
  - 실패한 테스트가 있을 경우, 에러 메시지를 참고하여 문제를 해결합니다.

## Package 만들기
- 패키지를 만들기 위해, 프로젝트의 루트 디렉토리에서 다음 명령어를 실행합니다:

```pip install -e .```
    
- 위 명령어는 패키지를 설치하고, 변경 사항이 있을 경우 즉시 반영할 수 있는 editable mode로 설치합니다.

이 패키지를 통해 자연어 처리와 날씨 API를 결합하여 보다 유용한 기능을 제공할 수 있습니다. 필요시 추가적인 기능이나 개선사항을 제안해주세요.