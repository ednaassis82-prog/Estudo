programa {
  real nota_1, nota_2, media
  cadeia nome
  funcao inicio() {

    //entrada

    escreva("Digite o nome do aluno: ")
    leia(nome)

    //processamento

    escreva("Digite sua primeira nota: ")
    leia(nota_1)
    escreva("Digite sua segunda nota: ")
    leia(nota_2)
    media = (nota_1 + nota_2) / 2
    escreva("A média do aluno ", nome , " é ", media, "\n")
    
    //saida

    se (media>= 7){
      escreva("\n O aluno teve um bom aproveitamento!")
    }
    senao{
      escreva("\n O aluno não teve um bom aproveitamento")
    }
    
    
  }
}
