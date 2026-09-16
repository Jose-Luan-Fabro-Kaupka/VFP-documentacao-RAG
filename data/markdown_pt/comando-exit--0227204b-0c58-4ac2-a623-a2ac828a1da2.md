# Comando EXIT

Sai de uma estrutura DO WHILE, FOR, SCAN ou TRY…CATCH…FINALLY.

```foxpro
EXIT
```

# Observações

O comando EXIT transfere o controle de dentro da estrutura para o comando imediatamente posterior a ela.

# Exemplo

No exemplo a seguir, o número de produtos em estoque com preço superior a 20 dólares é totalizado no laço DO WHILE até o fim do arquivo (EOF). O laço é encerrado e o total é exibido.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE products  && Opens Products table
SET TALK OFF
gnStockTot = 0
DO WHILE .T.     && Beginning of loop
   IF EOF()
      EXIT
   ENDIF
   IF unit_price < 20
      SKIP
      LOOP
   ENDIF
   gnStockTot = gnStockTot + in_stock
   SKIP
ENDDO  && End of loop
CLEAR
? 'Total items in stock valued over 20 dollars:'
?? gnStockTot
```
