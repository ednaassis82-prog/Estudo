programa {

   real Largura, Altura, Area, Litros

  funcao inicio() {
     //entrada
     escreva ("Qual a largura da sua parede ? : ")
     leia (Largura)

     
     escreva ("E qual a altura da sua parede ? : ")
     leia (Altura)

     //processamento

      Area= Largura*Altura
      Litros= Area/2
      
     //Saída
      escreva ("A área a ser pintada da sua parede  é ", Area, " em ", Litros, " litros de tinta.")
 
  }
}
