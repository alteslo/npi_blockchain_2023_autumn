from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def generate_keys():
    """Генерация ключей"""
    private_key = rsa.generate_private_key(
        backend=default_backend(), public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_data(public_key, data):
    """Шифрование данных с использованием публичного ключа"""
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data


def decrypt_data(private_key, encrypted_data):
    """Дешифрование данных с использованием приватного ключа"""
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode()


# Пример использования
private_key, public_key = generate_keys()
data = "Секретная информация"

encrypted_data = encrypt_data(public_key, data)
decrypted_data = decrypt_data(private_key, encrypted_data)


print("Исходные данные:", data)
print("Зашифрованные данные:", encrypted_data)
print("Расшифрованные данные:", decrypted_data)
