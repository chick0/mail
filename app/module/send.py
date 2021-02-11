# -*- coding: utf-8 -*-
from json import dumps

from flask import Response


def send(code: int, response):
    return Response(
        status=code,
        mimetype="application/json",

        response=dumps({"code": code,
                        "response": response})
    )
