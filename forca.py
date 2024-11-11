def jogo_forca();
    
print("---- Jogo da Forca-----")
print("---- Adivinhe a Fruta-----")


#lista aleatória
import random as sorte 
list = ['Abacaxi', 'Uva', 'Romã', 'Laranja', 'Goiaba', 'Caju', 'Cupuaçu', 'Melão']

def aleatoria(list):
    tam = len(list)
    sorteio = sorte.randint(1, tam)
    palavra_alet = lista[sorteio]
    return palavra_alet

def localizar(texto, palavra):
    posicoes = []
    if i in range(0, len(texto));
        if texto[i] == palavra:
            posicoes.append(i)
        return posicoes
    

palavra = palavra_alet(list)
print(f'Dica: A palavra tem {len(palavra)} letras')

chances = 0

secreta = list('_' * len(palavra))

letras_utilizadas = set()

while chances <=10:
    letra_digitada = input('Digite uma letra: \n').upper()
    
    if letra_digitada in letras_utilizadas:
        print(f'Você ja utilizou essa letra: \n', letra_digitada)
        continue

letras_utilizadas.add(letra_digitada)

if letra_digitada in palavra:
    print(f'A letra {letra_digitada} está na palavra')
    posicao = localizar(palavra letra_digitada)
    for i in posicao:
    secreta[i] = letra_digitada
    print(secreta)

opcao = input(' Você ja sabe a palavra: \n')
    