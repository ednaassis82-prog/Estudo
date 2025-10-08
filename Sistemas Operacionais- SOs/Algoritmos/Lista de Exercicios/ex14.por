programa {

  real km_percorridos
  inteiro dias 
  real valor_km, valor_dias, total
funcao inicio() {

//entrada

  escreva (" Digite os km percorrridos : ")
  leia (km_percorridos)

  escreva (" Digite os dias percorridos : ")
  leia (dias)

//processamento

  valor_dias = dias * 90
  valor_km = km_percorridos * 0.20
  total = valor_dias + valor_km

  //saida

  escreva ("O preço total a pagar é : ", total )

  }
}
