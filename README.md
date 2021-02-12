# Mail!
이메일 인증 API

# 사용방법
1. 데이터베이스 셋팅 후 `conf/database.ini` 파일 수정
2. smtp 셋팅 후 `conf/smtp.ini` 파일 수정
   - smtp 서버는 SSL을 사용하고 있습니다
3. `SECRET_KEY.py`를 실행해 암호화 키를 생성 (1회)
4. `/register` 엔드포인트에 요청을 보내서 클라이언트 생성
   - 요청 방식은 POST
   - form 방식으로 API 소유자의 이메일을 전송함
5. 해당 클라이언트를 활성화 한다
   - 테이블에서 `activate` 값을 `1(true)`로 변경
6. `/api/send` 에 요청을 보낸다
   - 요청 방식은 POST
   - form 방식으로 검증할 이메일과 클라이언트의 아이디를 전송함
   - `Authorization` 헤더에 클라이언트 시크릿을 보낸다
      - `type` 은 `Bearer`

# 추가
- 해당 API 서버 사용시 이 [파일](https://gist.github.com/chick0/22c6440322981b5d874a64a03c70b67f) 참고
