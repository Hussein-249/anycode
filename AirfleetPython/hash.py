import os, logging, hashlib

def hashPassword(plaintext: str):

    hash = hashlib.sha512

    hash.update(salt() + + plaintext.encode())

    hashed_password = hash.hexdigest()

    logging.debug("Password has been successfully hashed.")

    return hashed_password


def salt():
    salt = os.urandom(64)
    return salt

