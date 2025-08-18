numero = [2,5,10,1,4,9,22,100,3]
print(len(numero)) #"len" descreve o tamanho da lista

print(min(numero)) #"min" descreve o menor numero da lista
print(max(numero)) # "max" descreve o maior numero da lista
print(sum (numero)) # "sun" descreve a soma de todos elementos da lista
print(sorted(numero)) # "sorted" organiza do menor para o maior
print(sorted(numero,reverse=True)) #"reverse= true" organização de forma decrescente
print(numero[1]) # "mostra o numero que esta na posição"
print(100 in numero) # "mostra a função True,se o numero está na lista como verdadeiro ou falso"
print(30 in numero)
print(numero) # mostra a lista como está
print(numero[2:8]) # "serve para fazer o fatiamentoda lista, inicio e fim".começa no segundo da listae termina no setimo"
print(numero[2:]) # "o faztiamento"

del (numero[1]) #"a função del deleta o indice da posição que você quer deletar"
numero.append(101) # "adiciona um numero no final da lista"
print(numero)