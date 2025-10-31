import random

def salvar_pontos(pontos_jogadores):
    with open("pontos_jogadores.txt", "w") as arquivo:
        for jogador, pontos in pontos_jogadores.items():
            arquivo.write(f"{jogador},{pontos}\n")

def carregar_pontos():
    pontos_jogadores = {}
    try:
        with open("pontos_jogadores.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, pontos = linha.strip().split(",")
                pontos_jogadores[nome] = int(pontos)
    except FileNotFoundError:
        pass
    return pontos_jogadores

def jogo(jogador_input, pontos_jogadores):
    balas = int(input("Quantas balas quer apostar? "))
    festim = int(input("Quantas balas falsas terão? "))

    SlotDaBalaReal = random.sample(range(1, festim + 1), balas)

    PontosApostados = balas / festim * 10
    PontosApostadosArredondados = round(PontosApostados)

    resultado = random.randint(1, festim)

    if resultado in SlotDaBalaReal:
        print("Tomou bala na fuça! Perdeu 10 pontos!")
        pontos_jogadores[jogador_input] -= 10  
    else:
        print(f"UFA! Você sobreviveu, ganhou {PontosApostadosArredondados} pontos.")
        pontos_jogadores[jogador_input] += PontosApostadosArredondados  

    salvar_pontos(pontos_jogadores)

pontos_jogadores = carregar_pontos()

while True:
    jogador_input = input("Quem quer jogar? ")

    if jogador_input in pontos_jogadores:
        print(f"Bem-vindo de volta, {jogador_input}! Você tem {pontos_jogadores[jogador_input]} pontos.")
    else:
        resposta = input("Jogador não encontrado. Deseja se cadastrar? (SIM/Não) ").strip().lower()

        if resposta in ["sim", "s", "yes", "y"]:
            pontos_jogadores[jogador_input] = 0
            print(f"{jogador_input} foi cadastrado com sucesso! Você tem {pontos_jogadores[jogador_input]} pontos.")
        else:
            print("Cadastro não realizado.")
            continue

    jogo(jogador_input, pontos_jogadores)

    jogar_novamente = input("Quer jogar novamente? (SIM/Não) ").strip().lower()
    
    if jogar_novamente not in ["sim", "s", "yes", "y"]:
        print("Obrigado por jogar! Até a próxima!")
        break
