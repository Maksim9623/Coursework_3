import base64
from _datetime import datetime, timedelta
import hashlib
import hmac

import jwt
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')

# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)


def compare_password(password1, password2):
    return hmac.compare_digest(password1, password2)


def generate_tokens(user):
    payload = {
        'email': user['email'],
        'id': user['id'],
        'exp': datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    }

    access_token = jwt.encode(
        payload=payload,
        key=current_app.config['SECRET_KEY'],
        algorithm=current_app.config['JWT_ALGO']
    )

    payload['exp'] = datetime.utcnow() + timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    refresh_token = jwt.encode(
        payload=payload,
        key=current_app.config['SECRET_KEY'],
        algorithm=current_app.config['JWT_ALGO']
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def update_refresh_token(refresh_token):
    return jwt.decode(
        jwt=refresh_token,
        key=current_app.config['JWT_SECRET'],
        algorithm=current_app.config['JWT_ALGO']
        )
