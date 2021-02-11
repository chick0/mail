# -*- coding: utf-8 -*-
from random import shuffle


def get(length: int = 6):
    token = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    shuffle(token)

    return token[:length]
