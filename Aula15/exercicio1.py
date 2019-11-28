nome=str(input('Digite seu nome:'))
arquivo=open('exercicio1.txt','a')
arquivo.write(f'{nome}\n')
arquivo.close