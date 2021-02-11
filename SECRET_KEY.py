# -*- coding: utf-8 -*-
from os import path
from secrets import token_bytes
from configparser import ConfigParser


if not path.exists(path.join("conf", "SECRET_KEY.ini")):
    parser = ConfigParser()
    parser.add_section("SECRET_KEY")
    parser.set(
        section="SECRET_KEY",
        option="SECRET_KEY",
        value=token_bytes(16).hex()
    )

    with open(path.join("conf", "SECRET_KEY.ini"), mode="w") as fp:
        parser.write(fp=fp)
else:
    print("SECRET_KEY 는 이미 만들어져 있습니다")
