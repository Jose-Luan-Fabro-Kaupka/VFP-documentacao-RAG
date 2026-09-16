# Função RECCOUNT( )

Retorna o número de registros na tabela atual ou especificada.

```foxpro
RECCOUNT([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da área de trabalho para uma tabela aberta em outra área de trabalho. RECCOUNT( ) retorna 0 se uma tabela não estiver aberta na área de trabalho que você especificar.
**cTableAlias**
Especifica o alias da tabela para uma tabela aberta em outra área de trabalho.

# Valor de retorno

Numeric

# Observações

O valor que RECCOUNT( ) retorna não é afetado por SET DELETED e SET FILTER.

RECCOUNT( ) sem os argumentos opcionais nWorkArea ou cTableAlias retorna o número de registros na tabela na área de trabalho selecionada atualmente.

# Exemplo

No exemplo a seguir, o Microsoft Visual FoxPro compara o espaço disponível em disco com a quantidade necessária para classificar `customer`.

```foxpro
*** Check DISKSPACE before a SORT ***
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
*** Get size of table header ***
gnTableHead = HEADER()
*** Calculate size of table ***
gnFileSize = gnTableHead + (RECSIZE() * RECCOUNT() + 1)
IF DISKSPACE() > (gnFileSize * 3)
   WAIT WINDOW 'Sufficient diskspace to sort.'
ELSE
   WAIT WINDOW 'Insufficient diskspace. Sort cannot be done.'
ENDIF
```
