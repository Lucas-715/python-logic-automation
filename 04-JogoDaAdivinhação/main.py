# Pasta: 04-JogoDaAdivinhação
# Projeto: Jogo da Adivinhação de Números
# Desenvolvido por: Lucas Almeida

import random

def iniciar_partida():
    """Executa uma rodada única do jogo com 10 tentativas."""
    print("\n--- Nova Partida! ---")
    print("Eu pensei em um número entre 1 e 100. Você tem 10 tentativas.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while tentativas < 10:
        try:
            palpite = int(input(f"\nTentativa {tentativas + 1}/10 - Qual o seu palpite? "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Mais alto!")
            elif palpite > numero_secreto:
                print("Mais baixo!")
            else:
                print(f"✨ Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
                return True
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números.")

    print(f"\nFim das tentativas! O número secreto era {numero_secreto}.")
    return False

def main():
    while True:
        iniciar_partida()
        
        jogar_novamente = input("\nDeseja jogar novamente? [S/N]: ").strip().upper()
        if jogar_novamente != "S":
            print("\nObrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()
