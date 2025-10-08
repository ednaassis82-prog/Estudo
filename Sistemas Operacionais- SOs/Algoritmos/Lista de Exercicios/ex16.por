programa {


inteiro,cigarros_por_dias, anos_fumando
real total_de_cigarros,minutos_perdidos,dias_perdidos


  funcao inicio() {

  //entrada
 escreva("Digite quantos cigarros você fuma por dia.")  
 leia(cigarros_por_dia) 
 escreva("Digite quantos anos você fuma.")
 leia(anos_fumando)

 //processamento
 total_cigarros=cigarros_por_dias*anos_fumando*365
 minutos_perdidos=total_de_cigarros*10
 dias_perdidos=minutos_perdidos/(24*60)

 //saida
 escreva("Digite o total de cigarros fumados por dia",total_de_cigarros)
 escreva("\n Em vida o fumante perderá em dias?", dias_perdidos)





  }
}
