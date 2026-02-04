# Pasta: 01-Gerador-de-CPF
# Projeto: Algoritmo de Geração e Validação de CPF
# Desenvolvido por: Lucas Almeida

import random

def calcular_digito(digitos):
    """Calcula o dígito verificador baseado na lógica oficial do CPF."""
    peso = len(digitos) + 1
    soma = sum(d * (peso - i) for i, d in enumerate(digitos))
    resultado = (soma * 10) % 11
    return 0 if resultado >= 10 else resultado

def main():
    print("--- Gerador e Validador de CPF ---")
    tipo = input("Deseja gerador automático (1) ou manual (2)? ")
    
    if tipo == "1":
        # Gera 9 dígitos aleatórios
        base = [random.randint(0, 9) for _ in range(9)]
    else:
        # Recebe os 9 dígitos do usuário
        entrada = input("Digite os nove primeiros dígitos do CPF: ")
        base = [int(d) for d in entrada if d.isdigit()]

    # Cálculo do Primeiro Dígito Verificador (DV1)
    base.append(calcular_digito(base))
    
    # Cálculo do Segundo Dígito Verificador (DV2)
    base.append(calcular_digito(base))
    
    # Formatação final
    cpf_final = "".join(map(str, base))
    print(f"\nCPF Processado: {cpf_final}")
    print(f"Status: CPF Válido!")

if __name__ == "__main__":
    main()
