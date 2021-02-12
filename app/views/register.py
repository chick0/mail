# -*- coding: utf-8 -*-
from os import urandom
from secrets import token_bytes
from hashlib import sha384

from flask import Blueprint
from flask import abort
from flask import request
from sqlalchemy.exc import IntegrityError

from app import db
from models import Client
from app.module import aes256, mail, send


bp = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix=f"/{__name__.split('.')[-1]}"
)


def add_to_database(email: str, secret: str):
    idx = urandom(18).hex()

    try:
        db.session.add(Client(
            idx=idx,
            email=email,
            secret=sha384(secret.encode()).hexdigest()
        ))
        db.session.commit()

        return idx
    except IntegrityError:
        return add_to_database(email, secret)


@bp.route("", methods=['POST'])
def add_client():
    secret = token_bytes(20).hex()

    email = request.form.get("email")
    if email is None or "@" not in email:
        abort(400)

    worker = aes256.AESCipher()
    idx = add_to_database(
        email=worker.encrypt(plaintext=email),
        secret=sha384(secret.encode()).hexdigest()
    )

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
