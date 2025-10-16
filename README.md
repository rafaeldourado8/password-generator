# Gerador de Senhas Seguras e Hasher (Python)

Este é um script de linha de comando (CLI) construído em Python para gerar senhas fortes e criptograficamente seguras. O projeto também inclui funcionalidades para criar e verificar hashes de senhas usando o algoritmo bcrypt, demonstrando as melhores práticas de armazenamento seguro de senhas para 2025.

## Funcionalidades

* **Geração Segura**: Utiliza o módulo `secrets` do Python para garantir aleatoriedade criptograficamente segura.
* **Complexidade Garantida**: Assegura que cada senha gerada contenha pelo menos uma letra maiúscula, uma minúscula, um número e um símbolo.
* **Hashing Robusto**: Emprega a biblioteca `bcrypt` para criar hashes "salgados" (salted hashes), a forma correta de se armazenar senhas.
* **Interface de Linha de Comando**: Usa `argparse` para uma experiência de usuário amigável, com opções para customizar o comprimento da senha, copiar para a área de transferência e mais.

## Tecnologias Utilizadas

* Python 3
* `secrets` (Biblioteca Padrão)
* `bcrypt`
* `pyperclip`
* `argparse` (Biblioteca Padrão)

## Como Usar

1.  **Clone o repositório:**
    ```bash"'
    cd password-generator
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    *(Você precisará criar um arquivo `requirements.txt` com `pip freeze > requirements.txt`)*

3.  **Execute o script:**

    * Gerar uma senha padrão (16 caracteres) com hash:
        ```bash
        python passgen.py
        ```

    * Gerar uma senha de 32 caracteres e copiá-la para o clipboard:
        ```bash
        python passgen.py -l 32 -c
        ```

    * Para ver todas as opções:
        ```bash
        python passgen.py --help
        ```