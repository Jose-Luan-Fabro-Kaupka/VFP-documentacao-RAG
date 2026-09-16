# Função RECSIZE( )

Retorna o tamanho (largura) de um registro de tabela.

```foxpro
RECSIZE([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da área de trabalho de uma tabela aberta em outra área de trabalho. RECSIZE( ) retorna 0 se nenhuma tabela estiver aberta na área de trabalho especificada.
**cTableAlias**
Especifica o alias da tabela aberta em outra área de trabalho.

# Valor de retorno

Numérico

# Observações

RECSIZE( ) emitido sem os argumentos opcionais nWorkArea ou cTableAlias retorna o tamanho do registro da tabela na área de trabalho atualmente selecionada.

# Exemplo

No exemplo a seguir, o Microsoft Visual FoxPro compara o espaço disponível em disco com o necessário para classificar `customer`.

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
