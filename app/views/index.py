# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Response


bp = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix="/"
)


@bp.route("/ok")
def ok():
    return "OK", 200


@bp.route("/robots.txt")
def robots():
    return Response(
        status=200,
        mimetype="text/plain",

        response="User-agent: *\n"
                 "Disallow: /"
    )
