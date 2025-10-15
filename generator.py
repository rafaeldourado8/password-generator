import secrets
import string

def generator_pass(size=16):
    '''Gera uma senha segura com o comprimento especificado, garantindo
        a inclusão de letras maiúsculas, minúsculas, números e símbolos'''
    if size < 8:
        raise ValueError("O comprimento da senha deve ser de no mínimo 8 caracteres.")
    
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    password_minimun = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos),
 ]

    join_password = letras_maiusculas + letras_minusculas + numeros + simbolos
    password_remainder = [secrets.choice(join_password)for _ in range(size - len(password_minimun))] 

    password_list = password_remainder + password_minimun
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


if __name__ == "__main__":
    try:
        nova_senha = generator_pass(20)
        print(f"Senha Gerada: {nova_senha}")
    except ValueError as e:
        print(f"Erro: {e}")
