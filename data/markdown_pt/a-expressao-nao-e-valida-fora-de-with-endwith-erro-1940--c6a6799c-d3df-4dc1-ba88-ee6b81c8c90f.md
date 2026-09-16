# A expressão não é válida fora de WITH/ENDWITH (Erro 1940)

Você pode usar uma expressão da forma .property=some_value somente dentro de uma construção do comando WITH ... ENDWITH.
 - Este erro também pode ocorrer se você estiver usando .NULL. como uma expressão. Coloque aspas em torno de .NULL. para evitar que seja identificado como uma propriedade.
- Você pode ter esquecido um ponto final com um valor como true (.T.), false (.F.) ou um valor nulo (.NULL.) Verifique se há pontos correspondentes em ambos os lados da constante.
