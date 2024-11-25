# Libraries used in this module
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

import cryptography

# Libraries used by both scripts
from cryptography.fernet import Fernet

import base64
import os
import subprocess
import sys
import getpass

import ast

# Generates a key derivation function
# Adds a salt to the input
def getKeyDerivationFunction():
    # Salt the password so it cannot be attacked using rainbow tables
    # It cannot be attacked using precomputed tables because those tables
    # Are unlikely to have the salt added onto the end of the tested messages
    salt = b'\xea\x0cP!\xa4\xd7\xaa{f\xf7\x97\xdd\t\xb29`'

    # KDF - key derivation function
    # Compute the key that is associated with the password
    # Using a CHF (cryptographic hash function)
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf

def exists(filename):
    return os.path.isfile(filename)

if(__name__ == "__main__"):
    print("Whoops, you ran the shared.py! Nevermind")
