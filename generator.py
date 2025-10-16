import secrets
import string
import argparse
import bcrypt
import pyperclip

def gerar_senha_segura(comprimento: int = 16) -> str:
    """
    Gera uma senha segura de forma concisa, garantindo a inclusão
    de todos os conjuntos de caracteres necessários.
    """
    if comprimento < 8:
        raise ValueError("O comprimento da senha deve ser de no mínimo 8 caracteres.")

    charsets = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    )

    senha_chars = [secrets.choice(cs) for cs in charsets]

    todos_os_chars = "".join(charsets)
    senha_chars += [secrets.choice(todos_os_chars) for _ in range(comprimento - len(senha_chars))]

    secrets.SystemRandom().shuffle(senha_chars)
    return "".join(senha_chars)

def criar_hash_senha(senha: str) -> bytes:
    """Cria um hash seguro de uma senha usando bcrypt."""
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def verificar_senha(senha: str, hash_armazenado: bytes) -> bool:
    """Verifica se uma senha fornecida corresponde a um hash armazenado."""
    return bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado)


def main():
    """Função principal para executar o gerador de senhas via linha de comando."""
    parser = argparse.ArgumentParser(
        description="Gerador de Senhas Seguras e Hasher v2025 (Versão Compacta)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-l", "--length", type=int, default=16, help="Define o comprimento da senha. Padrão: 16")
    parser.add_argument("--no-hash", action="store_true", help="Apenas gera a senha, sem criar o hash.")
    parser.add_argument("-c", "--copy", action="store_true", help="Copia a senha gerada para a área de transferência.")

    args = parser.parse_args()

    try:
        senha_gerada = gerar_senha_segura(args.length)
        print(f"Senha Gerada: {senha_gerada}")
        
        if args.copy:
            pyperclip.copy(senha_gerada)
            print("Copiada para a área de transferência!")

        if not args.no_hash:
            hash_gerado = criar_hash_senha(senha_gerada)
            print(f"Hash Bcrypt: {hash_gerado.decode('utf-8')}")
            is_valid = verificar_senha(senha_gerada, hash_gerado)
            print(f"Verificação: {'Sim' if is_valid else 'Não'}")

    except (ValueError, pyperclip.PyperclipException) as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()