programa {

  cadeia produto_1,produto_2
  inteiro quantidade_1,quantidade_2
  real preco_1,preco_2,subtotal_1,subtotal_2,soma


  funcao inicio() {

  //entrada
  escreva("--- Supermercado Preço Bom ---")
  escreva( "Vamos registrar sua compra! ")
  escreva("\n")

  escreva("---Produto 1---\n")
  escreva( "Digite qual o nome do produto : ")
  leia(produto_1)
  escreva ( "Digite a quantidade : ")
  leia (quantidade_1)
  escreva("Digite o preço unitário : ")
  leia(preco_1)
  escreva("\n")

  escreva("---Produto 2---\n")
  escreva( "Digite qual o nome do produto : ")
  leia(produto_2)
  escreva ( "Digite a quantidade : ")
  leia (quantidade_2)
  escreva("Digite o preço unitário : ")
  leia(preco_2)
  escreva("\n")

//processamento
subtotal_1=preco_1*quantidade_1
subtotal_2=preco_2*quantidade_2
soma=subtotal_1+subtotal_2

//saida
  escreva("---RECIBO DA COMPRA---\n" )
  escreva("item : " , produto_1, "\n" )
  escreva("Qtde : " , quantidade_1 , "| Preço Unit : ", preco_1 , "|Subtotal:  ", subtotal_1 ,  "\n")
  escreva("item : ", produto_2,"\n")
  escreva("Qtde : " , quantidade_2 , "| Preço Unit : ", preco_2 , "|Subtotal:  ", subtotal_2 ,  "\n")
  

  // VALOR TOTAL DA COMPRA

  escreva("------------------------------- \n")
  escreva(" VALOR TOTAL DA COMPRA : R$ " ,soma,".00 \n")
  escreva("------------------------------- \n")
  

    
  }
}
