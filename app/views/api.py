# -*- coding: utf-8 -*-
from os import urandom
from hashlib import sha384
from datetime import datetime, timedelta

from flask import Blueprint
from flask import abort
from flask import request
from sqlalchemy.exc import IntegrityError

from app import db
from models import Auth, Client
from app.module import mail, send
from app.module.token import get


bp = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix=f"/{__name__.split('.')[-1]}"
)


def add_to_database(idx: str, client_id: str, email: str, token: int):
    try:
        db.session.add(Auth(
            idx=idx,
            client_id=client_id,
            email=email,
            token=token
        ))
        db.session.commit()
    except IntegrityError:
        add_to_database(idx, client_id, email, token)


@bp.route("/send", methods=['POST'])
def _send():
    idx = urandom(8).hex()
    token = get(length=6)

    email = request.form.get("email")
    client_id = request.form.get("client_id")
    _type, secret = request.headers.get("Authorization").split(" ")

    if email is None or client_id is None or secret is None:
        abort(400)

    if _type not in ["Bearer", "bearer"]:
        abort(401)

    client = Client.query.filter_by(
        idx=client_id,
        secret=sha384(secret.encode()).hexdigest()
    ).first()

    if client is None or client.activate is False:
        abort(401)

    add_to_database(
        idx=idx,
        client_id=client_id,
        email=sha384(email.encode()).hexdigest(),
        token=int("".join(token))
    )

    mail.send(
        to_address=email,
        message=" ".join(token)
    )

    return send.send(
        code=200,
        response=dict(
            idx=idx,
            message="Token sent",
        )
    )


@bp.route("/verify")
def verify():
    idx = request.args.get("idx")
    client_id = request.args.get("client_id")
    token = request.args.get("token")

    if idx is None or client_id is None or token is None:
        abort(400)

    auth = Auth.query.filter_by(
        idx=idx,
        client_id=client_id,
        token=token
    ).first()
    if auth is None:
        abort(401)

    if auth.register + timedelta(hours=1) >= datetime.now():
        return send.send(
            code=200,
            response=dict(
                message="OK"
            )
        )
    else:
        abort(408)
