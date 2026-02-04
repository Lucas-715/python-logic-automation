# Pasta: 02-Calendario
# Projeto: Visualizador de Calendário Interativo
# Desenvolvido por: Lucas Almeida

import calendar

def obter_entrada_valida(prompt, min_val, max_val):
    """Garante que o usuário digite um número inteiro dentro de um intervalo."""
    while True:
        try:
            valor = int(input(prompt))
            if min_val <= valor <= max_val:
                return valor
            print(f"Erro: O valor deve estar entre {min_val} e {max_val}.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números.")

def exibir_calendario():
    print("- Visualizador de Calendário -")
    
    # Validação de ano (ex: entre 1 e 9999) e mês (1 a 12)
    ano = obter_entrada_valida("Digite o Ano (ex: 2026): ", 1, 9999)
    mes = obter_entrada_valida("Digite o Mês (1-12): ", 1, 12)

    # Design e exibição
    print("\n" + "="*20)
    print(calendar.month(ano, mes))
    print("="*20)

if __name__ == "__main__":
    exibir_calendario()
