# -*- coding: utf-8 -*-
from sys import exit

from conf import conf


# # # # # # # # # # # # # # # # # # # # # #

# DB 접속 정보 & 설정
try:
    SQLALCHEMY_DATABASE_URI = f"mysql://{conf['account']['user']}:{conf['account']['password']}" \
                              f"@{conf['database']['host']}/{conf['database']['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
except KeyError:
    print("데이터베이스 접속 정보를 불러오지 못함")
    exit(-1)

# # # # # # # # # # # # # # # # # # # # # #
