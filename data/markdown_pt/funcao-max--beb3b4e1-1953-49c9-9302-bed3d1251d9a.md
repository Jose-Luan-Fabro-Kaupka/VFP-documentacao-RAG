# Função MAX( )

Avalia um conjunto de expressões e retorna a expressão com o valor máximo.

```foxpro
MAX(eExpression1, eExpression2 [, eExpression3 ...])
```

#### Parâmetros
 **eExpression1 , eExpression2 [, eExpression3 ...]**
Especificam as expressões das quais você deseja que MAX( ) retorne a expressão com o valor mais alto. Todas as expressões devem ser do mesmo tipo de dados.

# Valor de retorno

Caractere, Numérico, Moeda, Double, Float, Data ou DateTime

# Exemplo

O exemplo a seguir usa APPEND BLANK para criar uma tabela com 10 registros contendo valores aleatórios e depois usa MIN( ) e MAX( ) para exibir os valores máximo e mínimo na tabela.

```foxpro
CLOSE DATABASES
CREATE TABLE Random (cValue N(3))
FOR nItem = 1 TO 10  && Append 10 records,
   APPEND BLANK
   REPLACE cValue WITH 1 + 100 * RAND()  && Insert random values
ENDFOR
CLEAR
LIST  && Display the values
gnMaximum = 1  && Initialize minimum value
gnMinimum = 100  && Initialize maximum value
SCAN
   gnMinimum = MIN(gnMinimum, cValue)
   gnMaximum = MAX(gnMaximum, cValue)
ENDSCAN
? 'The minimum value is: ', gnMinimum  && Display minimum value
? 'The maximum value is: ', gnMaximum  && Display maximum value
```
