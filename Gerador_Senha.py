# Importando bibliotecas para fazer tratamento de string e gerar caracteres aleatórios
import random
import string

def generate_password():
    # Parte fixa da senha
    password = "Wlist"

    # Escolher 2 números aleatórios
    random_numbers = ''.join(random.choices(string.digits, k=2))
    password += random_numbers

    # Completar a senha com números e caracteres aleatórios até atingir o comprimento mínimo de 12, começando a partir do índice 10
    while len(password) < 12:
        characters = string.digits + string.ascii_letters
        random_char = random.choice(characters)
        password += random_char

    return password

# Gera e imprime uma senha
password = generate_password()
print("Senha gerada:", password)
