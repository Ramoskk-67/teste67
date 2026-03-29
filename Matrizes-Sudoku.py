# 2 MATRIZES UMA COMPLETA JÁ PREENCHIDA E UMA AINDA A PREENCHER
""""
jogo = [["   ","A","B","C","D","E","F","G","H","I"],
        ["(0)", "X", "X", "7", "X", "X", "9", "X", "5", "X"],
        ["(1)", "3", "X", "X", "X", "8", "X", "4", "6", "X"],
        ["(2)", "X", "4", "X", "X", "1", "X", "X", "X", "3"],
        ["(3)", "X", "X", "X", "X", "X", "X", "X", "2", "7"],
        ["(4)", "X", "5", "X", "X", "X", "2", "1", "X", "X"],
        ["(5)", "X", "X", "X", "X", "3", "X", "X", "X", "X"],
        ["(6)", "7", "X", "X", "X", "X", "7", "2", "X", "4"],
        ["(7)", "X", "6", "X", "X", "X", "X", "X", "X", "X"],
        ["(8)", "2", "X", "X", "X", "X", "6", "X", "8", "1"]] 
"""
jogo = [["   ","A","B","C","D","E","F","G","H","I"],
        ["(0)", "5","3","4","6","7","8","9","1","2"],
        ["(1)", "6","7","2","1","9","5","3","4","8"],
        ["(2)", "1","9","8","3","4","2","5","6","7"],
        ["(3)", "8","5","9","7","6","1","4","2","3"],
        ["(4)", "4","2","6","8","5","3","7","9","1"],
        ["(5)", "7","1","3","9","2","4","8","5","6"],
        ["(6)", "9","6","1","5","3","7","2","8","4"],
        ["(7)", "2","8","7","4","1","9","6","3","5"],
        ["(8)", "3","4","5","2","8","6","1","7","9"]]

# LISTA PARA ARMAZENAR O VALOR ESCOLHIDO DA LINHA E DA COLUNA 
valor_linha = []
valor_coluna = []

# FUNÇAO PARA ORGANIZAR VISUALMENTE A MATRIZ JOGO
def tabuleiro():
    for linha in jogo:
        print(" | ".join(linha))
        
# # FUNÇAO PARA ESCOLHER LINHA         
def escolher_linha():
    while True:
        escolha_linha = input("\ndigite o número da linha (0 até 8) ou (v) para verificar : ").strip()
        if escolha_linha.isdigit() and escolha_linha in "012345678":
            print(f"\nlinha {escolha_linha} selecionada!\n")
            valor_linha.append(int(escolha_linha))
            break
        if escolha_linha.isalpha() and escolha_linha.upper() in "V":
            verificar_vencedor()
        else:
            print("digite uma linha válida (0 até 8)")
            
# FUNÇAO PARA ESCOLHER COLUNA            
def escolher_coluna():
    while True:
        escolha_coluna = input("digite a letra da coluna (A até I): ").strip().upper()
        if escolha_coluna.isalpha() and escolha_coluna in "ABCDEFGHI":
            print(f"coluna {escolha_coluna} selecionada!\n")
            valor_coluna.append("ABCDEFGHI".index(escolha_coluna) + 1)
            break
        if escolha_coluna.isalpha() and escolha_coluna.upper() in "V":
            verificar_vencedor()
        else:
            print("digite uma coluna válida (A até I)")

# FUNÇAO PARA ADICIONAR VALORES 
def adicionar_valores():
    while True:
        tabuleiro()
        valores = input("\ndigite o número que deseja adicionar (1 até 9) ou (V) para verificar: ").strip()
        if valores.isdigit() and valores in "123456789":
            linha = valor_linha[-1] + 1  
            coluna = valor_coluna[-1]
            if jogo[linha][coluna] != "X":
                print(f"essa posição já tem um valor fixo que não pode ser editado\n")
                return menu()

            jogo[linha][coluna] = valores
            print(f"valor '{valores}' adicionado com sucesso na posição linha {valor_linha[-1]} coluna {valor_coluna[-1]}!\n")
            print("tabuleiro atualizado:")
            return menu()
            
# FUNÇAO PARA VERIFICAR VENCEDOR
def verificar_vencedor():
    for i in range(1, 10):
        for j in range(1, 10): 
            if jogo[i][j] == "X": 
                print("o tabuleiro ainda está incompleto")
                tabuleiro()  
                return  

    for i in range(1, 10):  
        numeros = []  
        for j in range(1, 10):  
            valor = jogo[i][j]  
            if valor in numeros:  
                print(f"tem número repetido na linha {i-1}.")
                tabuleiro()
                return
            numeros.append(valor) 

    for j in range(1, 10): 
        numeros = []
        for i in range(1, 10): 
            valor = jogo[i][j]
            if valor in numeros:
                print(f"tem número repetido na coluna {j}.")
                tabuleiro()
                return
            numeros.append(valor)
            
    for linha_inicio in (1, 4, 7):
        for coluna_inicio in (1, 4, 7):
            numeros = []

            for i in range(linha_inicio, linha_inicio + 3):
                for j in range(coluna_inicio, coluna_inicio + 3):

                    valor = jogo[i][j]

                    if valor != "X" and valor in numeros:
                        print("tem número repetido em um bloco 3x3")
                        tabuleiro()
                        return

                    if valor != "X":
                        numeros.append(valor)

    print("parabéns! você completou o jogo!")
    tabuleiro()
    exit()
# FUNÇAO MENU QUE CHAMA TODAS AS OUTRAS FUNÇÕES 
def menu():
    tabuleiro()
    escolher_linha()
    escolher_coluna()
    print(f"linha selecionada: {valor_linha}")
    print(f"coluna selecionada: {valor_coluna}")
    adicionar_valores()
    
# INICIALIZA    
menu()