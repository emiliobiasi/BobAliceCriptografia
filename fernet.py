import base64
import hashlib
from cryptography.fernet import Fernet


def gerar_chave_fernet(chave: bytes) -> bytes:
    assert isinstance(chave, bytes)
    hlib = hashlib.md5()
    hlib.update(chave)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


def cifra(txtchave, message):
    key = gerar_chave_fernet(txtchave.encode('utf-8'))
    fernet = Fernet(key)
    texto_cifrado = fernet.encrypt(message.encode('utf-8'))
    return texto_cifrado


def decifra(txtchave, message):
    key = gerar_chave_fernet(txtchave.encode('utf-8'))
    fernet = Fernet(key)
    texto_decifrado = fernet.decrypt(message).decode('utf-8')
    return texto_decifrado


