# -*- coding: utf-8 -*-
from base64 import urlsafe_b64encode, urlsafe_b64decode

from Cryptodome import Random
from Cryptodome.Util import Padding
from Cryptodome.Cipher import AES

from conf import conf


class AESCipher:
    def __init__(self):
        self.key = conf['SECRET_KEY']['secret_key'].encode()

    def encrypt(self, plaintext: str):
        padded_plaintext = Padding.pad(
            data_to_pad=plaintext.encode("utf-8"),
            block_size=AES.block_size
        )
        iv = Random.new().read(AES.block_size)

        cipher = AES.new(
            key=self.key,
            mode=AES.MODE_CBC,
            iv=iv
        )
        ciphertext = cipher.encrypt(padded_plaintext)

        return urlsafe_b64encode(iv + ciphertext).decode("utf-8")

    def decrypt(self, ciphertext: str):
        ciphertext = urlsafe_b64decode(ciphertext.encode("utf-8"))
        iv = ciphertext[:AES.block_size]

        cipher = AES.new(
            key=self.key,
            mode=AES.MODE_CBC,
            iv=iv
        )
        padded_plaintext = cipher.decrypt(ciphertext[AES.block_size:])

        return Padding.unpad(
            padded_data=padded_plaintext,
            block_size=AES.block_size
        ).decode("utf-8")
