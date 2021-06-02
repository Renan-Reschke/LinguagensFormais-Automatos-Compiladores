"""
@author: Guilherme Samuel de Souza Barbosa 19.00012-0 
@author: Felipe Freitas Villani 19.01370-0 
@author: Renan Scheidt Reschke 19.02009-0
"""

import sys

# Leitura do arquivo m.dfa
with open('m.dfa') as dfa_file:
    dfa_data = dfa_file.read()
dfa = eval(dfa_data)

# Entrada da cadeia
try:
    entrada = input("Digite a cadeia: ")
except (KeyboardInterrupt, EOFError):
    print("Programa finalizado pelo usuario!")
    sys.exit()

while( entrada != "-1"):
    entrada_bckp = entrada
    estado = dfa['initial_state']
    aceitar = False
    while len(entrada) > 0:
        c = entrada[0]
        entrada = entrada[1:]

        if c not in dfa['sigma']:
            print('O símbolo', c, 'não pertence ao alfabeto do autômato!')
            entrada = c + entrada
            break

        if estado not in dfa['states']:
            print('O estado', estado,'não pertence ao conjunto de estados do autômato!')
            break

        try:
            print("(%i, '%c') -> %i" % (estado, c, dfa['delta'][(estado, c)]))
            estado = dfa['delta'][(estado, c)]            
        except KeyError:
            print('Não foi possível realizar a transição do estado', estado, 'com entrada ', c)
            break
    
    if estado in dfa['final_states'] and entrada == "":
        aceitar = True
    
    if aceitar:
        print('A cadeia', entrada_bckp, 'foi aceita pelo autômato!')
    else:
        print('A cadeia', entrada_bckp, 'foi rejeitada pelo autômato!')
        
    try:
        entrada = input("Digite a cadeia: ")
    except (KeyboardInterrupt, EOFError):
        print("Programa finalizado pelo usuario!")
        sys.exit()