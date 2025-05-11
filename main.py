import random
import json
import datetime

date = datetime.date.today().strftime("%d-%m-%Y")
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'
length = 12
password = ''

""" 🔐 Modo com salvamento no arquivo .txt """
for i in range(length):
    random_index = random.randint(0, len(charset) - 1)
    password += charset[random_index]
print(password)
question = input('Você quer guardar essa senha em um arquivo .txt? (s - Sim) ou (n - Não) ')


if question.lower() == 's':
    name = input('Coloque o nome da senha: ')
    passwords = {
        "nome": name,
        "senha_gerada": password,
        "data_registro": date
        }
    with open("password.txt", 'a') as arquivo:
        json.dump(passwords, arquivo)
        arquivo.write("\n")
    print(f"Dados salvos com sucesso no arquivo password.txt ")
else:
    print('ok')

""" 🏃 Modo rápido (sem interação)
for i in range(length):
    random_index = random.randint(0, len(charset) - 1)
    password += charset[random_index]
print(password)
"""