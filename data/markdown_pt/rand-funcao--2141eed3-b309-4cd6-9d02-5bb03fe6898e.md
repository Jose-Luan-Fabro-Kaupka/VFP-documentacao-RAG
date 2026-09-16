# RAND( ) Função

Retorna um número aleatório entre 0 e 1.

```foxpro
RAND([nSeedValue])
```

#### Parâmetros
 **nSeedValue**
Especifica o valor inicial que determina a sequência de valores que RAND( ) retorna. RAND( ) retorna a mesma sequência de números aleatórios se você usar o mesmo valor inicial para nSeedValue na primeira vez que emitir RAND( ) seguido por chamadas de função RAND( ) subsequentes sem nSeedValue . Se nSeedValue for negativo na primeira vez que você emitiu RAND( ), um valor inicial do relógio do sistema será usado. Para obter a sequência mais aleatória de números, emita RAND( ) inicialmente com um argumento negativo e depois emita RAND( ) sem argumento. Se você omitir nSeedValue , RAND( ) usará um valor inicial padrão de 100.001.

# Valor de retorno
Numérico

# Exemplo
O primeiro exemplo abaixo usa RAND( ) para criar uma tabela com 10 registros contendo valores aleatórios e, em seguida, usa MIN( ) e MAX( ) para exibir os valores máximo e mínimo na tabela.

O segundo exemplo abaixo exibe um número aleatório que fica entre dois valores, 1 e 10.

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
CLEAR
gnLower = 1
gnUpper = 10
? INT((gnUpper - gnLower + 1) * RAND() + gnLower)
```
