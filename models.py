# -*- coding: utf-8 -*-

from sqlalchemy import func

from app import db


class Auth(db.Model):
    idx = db.Column(         # 인증 고유 아이디
        db.String(16),
        unique=True,
        primary_key=True,
        nullable=False
    )

    client_id = db.Column(   # 인증을 요청한 서비스의 아이디
        db.String(36),
        nullable=False
    )

    email = db.Column(       # 이메일, sha384
        db.String(96),
        nullable=False
    )

    register = db.Column(    # 인증 요청 등록 시간
        db.DateTime,
        default=func.now(),
        nullable=False
    )

    token = db.Column(       # 인증 토큰
        db.Integer,
        nullable=False
    )

    def __init__(self, idx: str, client_id: str, email: str, token: int):
        self.idx = idx
        self.client_id = client_id
        self.email = email
        self.token = token

    def __repr__(self):
        return f"<Auth idx={self.idx!r}, client_id={self.client_id!r}>"


class Client(db.Model):
    idx = db.Column(         # 인증 서비스를 이용하는 클라이언트 아이디
        db.String(36),
        unique=True,
        primary_key=True,
        nullable=False
    )

    secret = db.Column(      # 비밀 키
        db.String(40),
        nullable=False
    )

    email = db.Column(       # 비밀 키
        db.String(128),
        nullable=False
    )

    activate = db.Column(    # 계정 활성화 여부
        db.Boolean,
        nullable=False,
        default=False
    )

    def __init__(self, idx: str, secret: str, email: str):
        self.idx = idx
        self.secret = secret
        self.email = email

    def __repr__(self):
        return f"<Client idx={self.idx!r}>"
