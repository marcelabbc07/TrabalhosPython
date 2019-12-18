# Aula 28 - 17-12-2019
# Revisão de listas, arquivo

# 1) Faça um programa de sorteio de alunos.
# Especificações:
# - Deve sortear um aluno por vez.
# - O programa deve garantir que todos os alunos sejam sorteados antes de reiniciar
# o sorteio.
# - O programa deve garantir que mesmo que ele seja fechado, o sorteio dos alunos só
# seja reiniciado quando todos os alunos forem sorteados.
# - Faça um menu para o program e de destaque para o aluno sorteado.
import random
sorteado = int( random.randint(1,12) )
print('='*50,'\n'*3)
print(f'O numero sorteado foi:{sorteado}')
with open('Aula28/alunos.txt','r') as alunos:
    contador=1
    for i in alunos:   
        if contador==sorteado:
            print(f'Aluno:{i}')
        contador+=1 
print('\n'*3,'='*50)





# Dica: 
# Ovo de pascua
# O "import os" pode habiliar alguns comandos como o os.system() que pode passar comando 
# do DOS, shell script do python para o terminal.
# 
# Como vocês ainda não sabem o que é o import e como ele funciona, então o pode-se trocar por:
# 
# from os import system
# system('dir')
#
# Agora imagine se usar o system('cls') para windows ou system('clear') para linux
# o cls/clear apaga o que foi impresso anteriormente na tela do terminal.
# 
# 
# :-)
# Poste no grupo do whatsapp #ACHEI! se vc ler esta mensagem! 
# (ninguem achou este ovo de pascua!)

