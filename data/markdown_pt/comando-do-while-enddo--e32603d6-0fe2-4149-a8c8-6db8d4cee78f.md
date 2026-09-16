# Comando DO WHILE ... ENDDO

Executa um conjunto de comandos dentro de um loop condicional.

```foxpro
DO WHILE lExpression
      Commands
   [LOOP]
   [EXIT]
ENDDO
```

#### Parâmetros
 **lExpression**
Especifica uma expressão lógica cujo valor determina se os comandos entre DO WHILE e ENDDO são executados. Enquanto lExpression for avaliada como verdadeira (.T.), o conjunto de comandos é executado.
**Commands**
Especifica o conjunto de comandos do Visual FoxPro a ser executado enquanto lExpression for avaliada como verdadeira (.T.).
**LOOP**
Retorna o controle do programa diretamente para DO WHILE. LOOP pode ser colocado em qualquer lugar entre DO WHILE e ENDDO.
**EXIT**
Transfere o controle do programa de dentro do loop DO WHILE para o primeiro comando após ENDDO. EXIT pode ser colocado em qualquer lugar entre DO WHILE e ENDDO.

# Observações

Os comandos entre DO WHILE e ENDDO são executados enquanto a expressão lógica lExpression permanecer verdadeira (.T.). Cada instrução DO WHILE deve ter uma instrução ENDDO correspondente.

Comentários podem ser colocados após DO WHILE e ENDDO na mesma linha. Os comentários são ignorados durante a compilação e a execução do programa.

# Exemplo

No exemplo a seguir, o número de produtos em estoque com preço superior a US$ 20 é totalizado no loop DO WHILE até que o final do arquivo (EOF) seja encontrado. O loop DO WHILE é encerrado e o total é exibido.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE products  && Opens Products table
SET TALK OFF
gnStockTot = 0
DO WHILE .T.  && Begins loop
   IF EOF()
      EXIT
   ENDIF
   IF unit_price < 20
      SKIP
      LOOP
   ENDIF
   gnStockTot = gnStockTot + in_stock
   SKIP
ENDDO     && Ends loop
CLEAR
? 'Total items in stock valued over 20 dollars:'
?? gnStockTot
```
