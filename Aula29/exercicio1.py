# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de bordo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

# # tecnica=(piloto,oficial1,oficial2)
# # cabine=(chefe_servico,comissaria1,comissaria2)
# # policial,prisioneiro
# 1-Fortwo move piloto,chefe_servico
# 2-embarca piloto
# 3-volta com chefe_servico
# 4-move chefe_servicob,comissaria1
# 5-embarca chefe_servico
# 6-volta comissaria1
# 7-move comissaria1,comissaria2
# 8-embarca comissaria1
# 9-volta comissaria2
# 10-move comissaria2,oficial1
# 11-embarca comissaria2
# 12-volta oficial1,piloto
# 13-move policial,prisioneiro
# 14-embarca policial,prisioneiro
# 15-volta comissaria2
# 16-move comissaria2,oficial1
# 17-embarca comissaria2
# 18-volta oficial1
# 19-move oficial1,piloto
# 20-embarca piloto
# 21-volta oficial1
# 22-move oficial1,oficial2
# 23-embarca oficial1,oficial2
Fortwo=[]
Embarcado=[]
Terminal=['Piloto','Oficial 1','Oficial 2','Chefe de Serviço','Comissária 1','Comissária 2','Policial','Prisioneiro']
Fortwo.append(Terminal[0])
Fortwo.append(Terminal[3])
print(Fortwo)
Fortwo.clear()







