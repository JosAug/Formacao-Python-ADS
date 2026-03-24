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
        break  # O comando 'break' destrói o loop imediatamente, parando a repetição
    else:
        tentativas_restantes -= 1  # Isso é o mesmo que: tentativas_restantes = tentativas_restantes - 1
        print("Senha incorreta.\n")

# LÓGICA DE BLOQUEIO: Se o loop acabou e as tentativas chegaram a zero
if tentativas_restantes == 0:
    print("ALERTA: Conta bloqueada por excesso de tentativas falhas. Contate o suporte.")
