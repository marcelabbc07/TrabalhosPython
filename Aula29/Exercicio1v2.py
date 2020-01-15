Fortwo=[]
Embarcado=[]
#Terminal=['Piloto','Oficial 1','Oficial 2','Chefe de Serviço','Comissária 1','Comissária 2','Policial','Prisioneiro']
Terminal = []

def viagens(Terminal):
    if 'Policial' in Terminal[1] and 'Prisioneiro' in Terminal[2]:
        Fortwo.insert(1, Terminal.pop(2))
        Fortwo.insert(0, Terminal.pop(1)) 
        atualizar_arquivo(Terminal)
        print(f'Fortwo:{Fortwo}\nTerminal:{Terminal}')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado)
        Embarcado.append(Fortwo.pop(0))
        atualizar_embarcado(Embarcado)
        Terminal.insert(1, Embarcado.pop(2))
        atualizar_arquivo(Terminal)
        print(f'Embarcado:{Embarcado}\nTerminal:{Terminal}\n')
    else:
        Fortwo.append(Terminal.pop(0))
        Fortwo.append(Terminal.pop(0))
        atualizar_arquivo(Terminal)
        if 'Chefe de Servico' in Fortwo[1]:
            Fortwo.insert(0, Fortwo.pop(1))
        print(f'Fortwo:{Fortwo}\nTerminal:{Terminal}')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado)
        Terminal.insert(0, Fortwo.pop(0))
        if len(Terminal) == 1:
            Embarcado.append(Terminal.pop(0))
            atualizar_embarcado(Embarcado)
        atualizar_arquivo(Terminal)
        print(f'Embarcado:{Embarcado}\nTerminal:{Terminal}\n')

def ler_arquivo():
    arq = open('Aula29/Terminal.txt','r')
    for i in arq:
        i.strip().split()
        Terminal.append(i)
    arq.close()
    return Terminal

def atualizar_arquivo(Terminal):
    arq = open('Aula29/Terminal2.txt','w')
    arq.write(''.join(Terminal))

def atualizar_embarcado(Embarcado):
    arq = open('Aula29/Embarcado.txt','w')
    arq.write(''.join(Embarcado))



Terminal = ler_arquivo()
print(f'Terminal:{Terminal}\n')

for i in range(1,8):
    print(f'--------Viagem {i}--------')
    viagens(Terminal)

