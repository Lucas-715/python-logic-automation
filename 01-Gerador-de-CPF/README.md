# 01 - Gerador e Validador de CPF

Este script em Python gera um número de CPF completo e válido. Ele oferece dois modos de operação: um totalmente automático e um manual, onde o usuário fornece os 9 primeiros dígitos.

## ✨ Funcionalidades

-   **Modo Automático:** Gera os 9 primeiros dígitos aleatoriamente e calcula os 2 dígitos verificadores para formar um CPF válido.
-   **Modo Manual:** Solicita que o usuário digite os 9 primeiros dígitos e, em seguida, calcula os 2 dígitos verificadores para completar o CPF.
-   **Validação Final:** Ao final, uma função simples verifica se o CPF gerado possui 11 dígitos e se não são todos números repetidos.

## 🚀 Como Executar

1.  Navegue até a pasta do projeto.
    ```bash
    cd 01-Gerador-de-CPF
    ```
3.  Execute o script no terminal:
    ```bash
    python main.py
    ```
4.  O programa irá perguntar se você deseja o modo automático (1) ou manual (2). Siga as instruções no terminal.

## 💡 Pontos de Melhoria Futura

Este projeto foi mantido em sua forma original como um exercício para futuras refatorações. Possíveis melhorias incluem:
-   Refatorar o cálculo dos dígitos verificadores em uma função única para evitar repetição de código.
-   Adicionar validação de entrada no modo manual para garantir que o usuário digite exatamente 9 números.
-   Aprimorar a função `validar_cpf` para que ela retorne `True` ou `False` em vez de apenas imprimir o resultado, tornando-a mais reutilizável.
