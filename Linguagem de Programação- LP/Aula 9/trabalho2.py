
nome = input("digite meu nome")

idade =int(input("digite minha idade"))

with open("aula9.txt","w")as arquivo:
    arquivo.write(f"nome : {nome}\n")
    arquivo.write(f"idade : {idade}\n")





