# -*- coding: utf-8 -*-
from os import urandom
from secrets import token_bytes

from flask import Blueprint
from flask import abort
from flask import request

from app import db
from models import Client
from app.module import aes256, mail, send


bp = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix=f"/{__name__.split('.')[-1]}"
)


@bp.route("", methods=['POST'])
def add_client():
    idx = urandom(18).hex()
    secret = token_bytes(20).hex()

    email = request.form.get("email")
    if email is None or "@" not in email:
        abort(400)

    worker = aes256.AESCipher()
    client = Client(
        idx=idx,
        email=worker.encrypt(plaintext=email),
        secret=secret
    )
    db.session.add(client)
    db.session.commit()

    mail.send(
        to_address=email,
        message=f"{secret}",
        title="API 사용시에 사용하는 API Secret 키 입니다"
    )

    return send.send(
        code=200,
        response=dict(
            idx=idx,
            message="Check your email",
        )
    )
