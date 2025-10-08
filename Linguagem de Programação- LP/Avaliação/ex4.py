nome1=str(input("Digite o primeiro nome"))
nome2=str(input("Digite o segundo nome"))
nome3=str(input("Digite o terceeiro nome"))




with open("alunos.txt", "w")as arquivo:
    arquivo.write(f"{nome1}\n")

with open("alunos.txt", "w")as arquivo:
    arquivo.write(f"{nome2}\n")

with open("alunos.txt", "w")as arquivo:
    arquivo.write(f"{nome3}\n")
    
print("Dados gravados co sucesso no arquivo alunos.txt!") 