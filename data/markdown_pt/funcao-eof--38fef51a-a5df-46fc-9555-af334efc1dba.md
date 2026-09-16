# Função EOF( )

Determina se o ponteiro de registro está posicionado após o último registro na tabela atual ou especificada.

```foxpro
EOF([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da área de trabalho da tabela.
**cTableAlias**
Especifica o alias da tabela. EOF( ) retorna false (.F.) se uma tabela não estiver aberta na área de trabalho especificada. Se você não especificar uma área de trabalho ou alias, a tabela aberta na área de trabalho selecionada no momento é testada para a condição de fim da tabela.

# Valor de retorno

Logical

# Observações

EOF( ) retorna true (.T.) se o ponteiro de registro atingir o fim do arquivo da tabela (EOF). O fim da tabela é atingido quando o ponteiro de registro passa do último registro na tabela. Por exemplo, quando um FIND, LOCATE ou SEEK não tem êxito, o Visual FoxPro move o ponteiro de registro após o último registro, e EOF( ) retorna true (.T.). EOF( ) retorna false (.F.) se o ponteiro de registro não estiver no fim da tabela.

# Exemplo

O exemplo a seguir abre a tabela `customer` e lista o nome da empresa uma página por vez até que o fim do arquivo seja atingido ou você escolha Cancel.

```foxpro
CLOSE DATABASES
CLEAR
OPEN DATABASE (HOME() + "samples\data\testdata")
USE customer
GO TOP
local recCtr, btnValue
recCtr = 0
btnValue = 1
DO WHILE btnValue = 1 AND NOT EOF()
  ? "Company : " + company
  recCtr = recCtr + 1
  if (recCtr % 20) = 0 then
    btnValue =MESSAGEBOX ("Click OK to continue, ;
     Cancel to quit.",33)
    clear
  endif
  Skip 1    && Move down one record
ENDDO
=MESSAGEBOX("Listing complete.",48)
```
