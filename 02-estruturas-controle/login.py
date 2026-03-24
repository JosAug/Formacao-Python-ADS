# VARIÁVEIS DE CONFIGURAÇÃO
senha_correta = "Dev2026"
tentativas_restantes = 3

print("--- Sistema Interno da Empresa ---")

# LAÇO DE REPETIÇÃO: Enquanto houver tentativas, o loop continua rodando
while tentativas_restantes > 0:
    senha_digitada = input(f"Digite sua senha (Tentativas restantes: {tentativas_restantes}): ")
    
    # DESVIO CONDICIONAL: Checando se a senha bate
    if senha_digitada == senha_correta:
        print("\nAcesso concedido! Bem-vindo ao painel.")
    tentativas_restantes -= 1 # Se chegou aqui é por que errou então extraímos 1

    if tentativas_restantes > 0:
        print("Senha incorreta.")
        print("-" * 20)
    # Verificamos se agora é a última chance
    if tentativas_restantes == 1:
        print ("CUIDADO: ÚLTIMA TENTATIVA ANTES DO BLOQUEIO!")

# LÓGICA DE BLOQUEIO: Se o loop acabou e as tentativas chegaram a zero
if tentativas_restantes == 0:
    print("ALERTA: Conta bloqueada por excesso de tentativas falhas. Contate o suporte.")
