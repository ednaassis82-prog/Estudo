programa {
real velocidade,valor_da_multa
inteiro excesso
  funcao inicio() {
//entrada
escreva("Digite a velocidade de um carro : ")
leia(velocidade)

//processamento

se(velocidade>80) {
excesso=velocidade-80
valor_da_multa=excesso*5




//saida
escreva("Digite se você foi multado ")
escreva(" Digite o excesso de velocidae em km/h", excesso)
escreva("\n Digite o valor da multa R$: ", valor_da_multa)
}

senao
escreva("Digite a velocidade dentro do limite. Dirije com Segurança \n ")



    
  }
}
