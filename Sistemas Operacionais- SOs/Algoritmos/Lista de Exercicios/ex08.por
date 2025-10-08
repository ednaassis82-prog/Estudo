programa {
  real metros,km,hm,dam,dm,cm,mm
  funcao inicio() {
// entrada

 escreva("Digite a distância em metros : ") 
 leia(metros)

//processamento

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000

//saida
escreva(" A distância de " , metros, " \n " )
escreva(km,"km \n " )
escreva(hm,"hm \n " )
escreva(dam, "dam \n ")
escreva(dm, "dm \n " )
escreva(cm, "cm \n " )
escreva(mm, "mm \n " )

  }
}
