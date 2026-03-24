# ENTRADA DE DADOS
print("--- Sistema de Planejamento de ADS ---")
nome = input("Digite seu nome: ")
semestre_atual = int(input("Qual semestre você está cursando? "))
mensalidade = float(input("Qual o valor da sua mensalidade? R$ "))

# CONSTANTE (Lógica: o curso de ADS geralmente tem 5 semestres)
TOTAL_SEMESTRES = 5

# PROCESSAMENTO
semestres_restantes = TOTAL_SEMESTRES - semestre_atual
# Considerando que cada semestre tem 6 meses:
meses_restantes = semestres_restantes * 6
investimento_total = meses_restantes * mensalidade

# SAÍDA
print("-" * 30)
print(f"Olá, {nome}!")
print(f"Faltam {semestres_restantes} semestre(s) para você se formar.")
print(f"O seu investimento total até o diploma será de: R$ {investimento_total:,.2f}")
print("-" * 30)
