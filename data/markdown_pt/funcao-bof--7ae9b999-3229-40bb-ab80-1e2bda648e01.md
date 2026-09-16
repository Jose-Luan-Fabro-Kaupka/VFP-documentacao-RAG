# Função BOF( )

Determina se o ponteiro de registro está posicionado no início de uma tabela.

```foxpro
BOF([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da work area para uma tabela aberta em outra work area.
**cTableAlias**
Especifica o alias da tabela para uma tabela aberta em outra work area. Se a tabela que você deseja testar para uma condição de início de arquivo estiver aberta em uma work area diferente da work area selecionada atualmente, use esses argumentos opcionais para especificar o número da work area ou o alias da tabela para a tabela. Se uma tabela não estiver aberta na work area que você especificar, BOF( ) retorna false (.F.).

# Valor de retorno

Logical

# Observações

Use BOF( ) para testar uma condição de início de arquivo para uma tabela. BOF( ) retorna true (.T.) se você tentou mover o ponteiro de registro para uma posição antes do primeiro registro na tabela.

# Exemplo

O exemplo a seguir abre a tabela `customer` e lista o nome da empresa uma página por vez, começando com o último registro na tabela. A listagem continua até que o início do arquivo seja atingido ou até que você escolha Cancel.

```foxpro
CLOSE DATABASES
CLEAR
OPEN DATABASE (HOME() + "samples\data\testdata")
USE customer
GO BOTTOM
local recCtr, btnValue
recCtr = 0
btnValue = 1
DO WHILE btnValue = 1 AND NOT BOF()
 ? "Company : " + company
 recCtr = recCtr + 1
 if (recCtr % 20) = 0 then
  btnValue =MESSAGEBOX ("Click OK to continue, Cancel to quit.",33)
  clear
 endif
 Skip -1    && Move up one record
ENDDO
=MESSAGEBOX("Listing complete.",48)
```
