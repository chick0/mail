# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.module import error


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=__import__("config"))

    @app.after_request
    def set_header(response):
        response.headers['X-Frame-Options'] = "deny"  # Clickjacking
        response.headers['X-XSS-Protection'] = "1"    # Cross-site scripting
        response.headers['X-Powered-By'] = "chick_0"
        return response

    # DB 모델 등록
    __import__("models")

    # ORM 등록 & 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    from app import views
    for view_point in views.__all__:
        try:
            app.register_blueprint(   # 블루프린트 등록시도
                blueprint=getattr(getattr(views, view_point), "bp")
            )
        except AttributeError:        # 블루프린트 객체가 없다면
            print(f"[!] '{view_point}' 는 뷰 포인트가 아닙니다")

    # 오류 핸들러
    app.register_error_handler(400, error.bad_request)
    app.register_error_handler(401, error.unauthorized)
    app.register_error_handler(403, error.forbidden)
    app.register_error_handler(404, error.page_not_found)
    app.register_error_handler(405, error.method_not_allowed)
    app.register_error_handler(408, error.request_timeout)

    app.register_error_handler(500, error.internal_server_error)

    return app
