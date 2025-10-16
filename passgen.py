# ==============================================================================
# Gerador de Senhas Seguras e Hasher v2025
#
# Um script de linha de comando para gerar senhas fortes e criptograficamente
# seguras, com a funcionalidade de criar hashes usando o algoritmo bcrypt.
# Ideal para portfólios de desenvolvimento.
# ==============================================================================

# --- Importações ---
import secrets
import string
import argparse
import bcrypt
import pyperclip

# --- Funções Principais ---

def gerar_senha_segura(comprimento: int = 16) -> str:
    """
    Gera uma senha segura com o comprimento especificado, garantindo
    a inclusão de letras maiúsculas, minúsculas, números e símbolos.

    Args:
        comprimento (int): O comprimento desejado para a senha. Padrão é 16.

    Returns:
        str: A senha segura gerada.

    Raises:
        ValueError: Se o comprimento for menor que 8.
    """
    if comprimento < 8:
        raise ValueError("O comprimento da senha deve ser de no mínimo 8 caracteres.")

    # Define os conjuntos de caracteres possíveis
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # Garante que a senha contenha pelo menos um de cada tipo usando secrets.choice
    senha_minima = [
        secrets.choice(letras_minusculas),
        secrets.choice(letras_maiusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos),
    ]

    # Preenche o restante da senha com uma combinação de todos os caracteres
    combinacao_total = letras_minusculas + letras_maiusculas + numeros + simbolos
    senha_restante = [secrets.choice(combinacao_total) for _ in range(comprimento - len(senha_minima))]

    # Junta as duas partes e embaralha para garantir a aleatoriedade da posição
    lista_senha = senha_minima + senha_restante
    secrets.SystemRandom().shuffle(lista_senha)

    return "".join(lista_senha)

def criar_hash_senha(senha: str) -> bytes:
    """
    Cria um hash seguro de uma senha usando bcrypt.

    Args:
        senha (str): A senha em texto plano.

    Returns:
        bytes: O hash da senha, pronto para ser armazenado.
    """
    senha_bytes = senha.encode('utf-8')
    sal = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, sal)
    return hash_senha

def verificar_senha(senha: str, hash_armazenado: bytes) -> bool:
    """
    Verifica se uma senha fornecida corresponde a um hash armazenado.

    Args:
        senha (str): A senha em texto plano a ser verificada.
        hash_armazenado (bytes): O hash que foi previamente armazenado.

    Returns:
        bool: True se a senha corresponder ao hash, False caso contrário.
    """
    senha_bytes = senha.encode('utf-8')
    return bcrypt.checkpw(senha_bytes, hash_armazenado)


# --- Função de Execução e Interface de Linha de Comando ---

def main():
    """
    Função principal para executar o gerador de senhas via linha de comando.
    """
    parser = argparse.ArgumentParser(
        description="Gerador de Senhas Seguras e Hasher v2025",
        formatter_class=argparse.RawTextHelpFormatter  # Melhora a formatação do texto de ajuda
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Define o comprimento da senha. Padrão: 16"
    )
    parser.add_argument(
        "--no-hash",
        action="store_true",  # Se o argumento for passado, o valor se torna True
        help="Apenas gera e exibe a senha, sem criar o hash."
    )
    parser.add_argument(
        "-c", "--copy",
        action="store_true",
        help="Copia a senha gerada para a área de transferência."
    )

    args = parser.parse_args()

    try:
        # 1. Gerar a senha
        senha_gerada = gerar_senha_segura(args.length)
        print("✅ Senha gerada com sucesso!")
        print("-" * 30)
        print(f"Senha: {senha_gerada}")
        print("-" * 30)

        # 2. Copiar para a área de transferência, se solicitado
        if args.copy:
            pyperclip.copy(senha_gerada)
            print("📋 Senha copiada para a área de transferência!")

        # 3. Gerar e exibir o hash, a menos que desabilitado
        if not args.no_hash:
            hash_gerado = criar_hash_senha(senha_gerada)
            print("\n🔒 Hash Bcrypt (para armazenamento seguro):")
            # Decodificamos para exibir como string, mas armazene o valor em bytes ou base64
            print(hash_gerado.decode('utf-8'))
            print("-" * 30)

            # Demonstração da verificação para provar que funciona
            is_valid = verificar_senha(senha_gerada, hash_gerado)
            print(f"Verificação de demonstração: A senha corresponde ao hash? {'Sim' if is_valid else 'Não'}")

    except (ValueError, pyperclip.PyperclipException) as e:
        print(f"❌ Erro: {e}")


# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    main()