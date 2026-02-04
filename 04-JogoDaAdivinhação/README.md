# 04 - Jogo da Adivinhação

Este é um clássico jogo "Adivinhe o Número" desenvolvido em Python para ser executado no terminal, com uma estrutura robusta que permite múltiplas partidas.

## ✨ Funcionalidades

* **Número Aleatório:** Sorteia um número secreto entre 1 e 100 a cada nova partida utilizando o módulo `random`.
* **Dicas Interativas:** Fornece dicas de "Mais alto!" ou "Mais baixo!" a cada palpite para guiar o jogador.
* **Limite e Contador de Tentativas:** O jogador tem 10 tentativas para acertar, e o programa informa o progresso a cada turno.
* **Validação de Entrada:** O programa utiliza `try-except` para garantir que não quebre caso o usuário digite um texto em vez de um número.
* **Opção de Jogar Novamente:** Sistema de controle de fluxo que permite reiniciar o jogo sem fechar o terminal.
 
## 🛠️ Tecnologias e Conceitos Praticados

-   **Python 3** e o módulo **`random`**.
-   Estrutura de jogo com um **loop `while` principal** e uma **função** para cada partida.
-   Tratamento de erros com **`try-except`**.

## 🚀 Como Executar

1.  Navegue até a pasta do projeto.
    ```bash
    cd 04-JogoDaAdivinhação
    ```
2.  Execute o script no terminal:
    ```bash
    python main.py
    ```
3.  Siga as instruções no terminal para jogar.
