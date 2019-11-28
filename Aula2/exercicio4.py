#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha
print('='*50,'\n'*2)
titulo='FLORIANÓPOLIS/CHILE'
partida='Florianópolis(FLN)'
destino='Chile'
pp='Florianópolis, Brasil'
p0='18/12/19 | 00h30 | Tubarão'
p1='18/12/19 | 03h30 | Osório'
p2='18/12/19 | 06h30 | Porto Alegre'
p3='18/12/19 | 08h30 | Alegrete' 
p4='19/12/19 | 12h30 | Uruguaiana'
p5='19/12/19 | 14h30 | Santa Fé'
p6='19/12/19 | 16h30 | Villa Maria'
p7='19/12/19 | 18h30 | Rio Cuarto'
p8='19/12/19 | 20h30 | San Luis'
p9='19/12/19 | 22h30 | Mendonza'
d='Santiago, Chile' 
print('{}\nPonto de partida:{}\nParada 1:{}\nParada 2:{}\nParada 3:{}\nParada 4:{}\nParada 5:{}\nParada 6:{}\nParada 7:{}\nParada 8:{}\nParada 9:{}\nParada 10:{}\nDestino:{}'.format(titulo,pp,p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,d))
print('\n'*2,'='*50)