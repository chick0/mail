# -*- coding: utf-8 -*-

from app.module.send import send


def bad_request(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Bad Request"
        )
    )


def unauthorized(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Unauthorized"
        )
    )


def forbidden(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Forbidden"
        )
    )


def page_not_found(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Not Found"
        )
    )


def method_not_allowed(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Method Not Allowed"
        )
    )


def request_timeout(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Request Timeout"
        )
    )


def internal_server_error(error):
    return send(
        code=getattr(error, "code"),
        response=dict(
            error="Internal Server Error"
        )
    )
