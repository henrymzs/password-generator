# 🔐 Password Generator

## 🚀 Modes of use
This project can be used in **two ways**:

1️⃣ Quick mode → Just generates the password and prints it on the terminal.
2️⃣ Interactive mode → Asks the user if they want to save the password and saves it in a .txt file.

- Example:

```sh
{"senha_gerada": "3s6Umxva@qm@"}
{"senha_gerada": "gtGcq!6Mrvc8"}
{"senha_gerada": "!zZ8pjWQlJwx"}
```
---

### You can modify the part you want to use in your code.

How will you do this? Example below:

### ✅ Quick mode
Runs directly and **displays the password**, without interactions:

```sh
""" 🏃 Modo rápido (sem interação)
for i in range(length):
    random_index = random.randint(0, len(charset) - 1)
    password += charset[random_index]
print(password)
"""
```

Just remove the comments from this code block and place the other code block with comments

### ✅ Interactive mode

Runs directly **displays the password** and saves it to a .txt file with interactions:

```sh
""" 🔐 Modo com salvamento no arquivo .txt 
for i in range(length):
    random_index = random.randint(0, len(charset) - 1)
    password += charset[random_index]
print(password)
question = input('Você quer guardar essa senha em um arquivo .txt? (s - Sim) ou (n - Não) ')

if question == 's' or question == 'S':
    passwords = {
        "senha_gerada": password
        }
    with open("password.txt", 'a') as arquivo:
        json.dump(passwords, arquivo)
        arquivo.write("\n")
    print(f"Dados salvos com sucesso no arquivo password.txt ")
else:
    print('ok')
"""
```

Just remove the comments from this block of code and place the other block of code with comments.
