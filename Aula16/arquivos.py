from faixa import *
#cadastro de playlist
#lendo música, artista e álbum
musica=(input('Digite o nome da música:'))
album=(input('Digite o nome do álbum:'))
artista=(input('Digite o nome do artista:'))
faixa1=criar_faixa(musica,album,artista)
salvar_faixa(faixa1)
for faixa in ler_faixa():
    print(f"{faixa['musica']} - {faixa['album']} - {faixa['artista']}")
