from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64
import secrets
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_key():
    key = input("Digite a chave AES (pressione Enter para gerar uma chave aleatória): ")

    if not key:
        key = secrets.token_hex(16)  # Gera uma chave aleatória de 16 bytes em formato hexadecimal

    while len(key) not in [32, 64]:
        print("A chave deve ter 32 ou 64 caracteres hexadecimais.")
        key = input("Digite novamente a chave AES: ")

    return key


def pad(text):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text) + padder.finalize()
    return padded_data


def unpad(text):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(text) + unpadder.finalize()
    return unpadded_data


def encrypt(key, plaintext):
    plaintext = pad(plaintext.encode('utf-8'))
    key = bytes.fromhex(key)
    iv = os.urandom(16)  # Gera um IV (Initialization Vector) aleatório
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt(key, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    key = bytes.fromhex(key)
    iv = ciphertext[:16]  # Extrai o IV do início da mensagem cifrada
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad(decrypted_text).decode('utf-8')


def main():
    while True:
        clear_screen()
        print("Escolha uma opção:")
        print("C = Cifrar")
        print("D = Decifrar")
        print("S = Sair")

        opcao = input("Digite a opção desejada: ").upper()

        if opcao == 'S':
            break
        elif opcao == 'C':
            mensagem = input("Digite a mensagem para cifrar: ")
            chave = get_key()

            mensagem_cifrada = encrypt(chave, mensagem)
            print(f"Mensagem cifrada: {mensagem_cifrada}")
        elif opcao == 'D':
            mensagem_cifrada = input("Digite a mensagem cifrada para decifrar: ")
            chave = get_key()

            try:
                mensagem_decifrada = decrypt(chave, mensagem_cifrada)
                print(f"Mensagem decifrada: {mensagem_decifrada}")
            except Exception as e:
                print(f"Erro ao decifrar a mensagem: {e}")
        else:
            print("Opção inválida.")

        input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
