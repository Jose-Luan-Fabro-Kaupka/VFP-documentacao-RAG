# Função USED( )

Determina se um alias está em uso ou se uma tabela está aberta em uma área de trabalho específica.

```foxpro
USED([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea | cTableAlias**
Especifica a área de trabalho ou alias de uma tabela. USED( ) retorna um valor lógico true (.T.) se uma tabela estiver aberta na área de trabalho que você especificar com nWorkArea ; caso contrário, um valor lógico false (.F.) é retornado. USED( ) retorna um valor lógico true (.T.) se um alias estiver em uso com o alias que você especificar com cTableAlias ; caso contrário, false (.F.) é retornado. Se você omitir nWorkArea e cTableAlias , USED( ) retorna um valor lógico true (.T.) se uma tabela estiver aberta na área de trabalho atualmente selecionada; caso contrário, false (.F.) é retornado.

# Valor de retorno

Logical

# Observações

USED( ) pode determinar se um alias está em uso ou se uma tabela está aberta em uma área de trabalho específica.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
SELECT A
USE customer  && Opens Customer table
SELECT B
USE orders  && Opens Orders table
SELECT C
USE employee  && Opens Employee table
? USED('A')  && Displays .T.
? USED('B')  && Displays .T.
? USED(4)  && Displays .F.
```
