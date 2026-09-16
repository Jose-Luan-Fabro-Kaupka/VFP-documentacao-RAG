# Comando APPEND

Adiciona um ou mais registros novos ao final de uma tabela.

```foxpro
APPEND [BLANK] [IN nWorkArea | cTableAlias] [NOMENU]
```

#### Parâmetros
 **BLANK**
Adiciona um registro em branco ao final da tabela atual. O Visual FoxPro não abre uma janela de edição quando você emite APPEND BLANK. Você pode editar o registro novo com BROWSE, CHANGE ou EDIT.
**IN nWorkArea**
Especifica a área de trabalho da tabela à qual um registro novo é anexado.
**IN cTableAlias**
Especifica o alias da tabela à qual um registro novo é anexado. Se você omitir nWorkArea e cTableAlias, um registro novo é anexado à tabela na área de trabalho atualmente selecionada. Se você emitir APPEND, um registro em branco é adicionado à tabela que você especificar com nWorkArea ou cTableAlias e a tabela é automaticamente selecionada. Se você emitir APPEND BLANK, um registro em branco é adicionado à tabela que você especificar com nWorkArea ou cTableAlias e a tabela não é selecionada.
**NOMENU**
Especifica que o título do menu Table é removido da barra de menus do sistema, impedindo alterações no formato da janela de edição.

# Observações

Quando você emite APPEND ou APPEND BLANK e uma tabela não está aberta na área de trabalho atualmente selecionada, a caixa de diálogo Open aparece para que você possa escolher uma tabela à qual anexar registros.

APPEND abre uma janela de edição para que você possa inserir dados em um ou mais registros novos. Quando você adiciona um registro novo, o Visual FoxPro atualiza quaisquer índices que estiverem abertos.

# Exemplo

O exemplo a seguir usa APPEND BLANK para criar uma tabela com 10 registros contendo valores aleatórios e então exibe os valores máximo e mínimo na tabela.

```foxpro
CLOSE DATABASES
CREATE TABLE curRandom (nValue N(3))
FOR nItem = 1 TO 10
   APPEND BLANK
   REPLACE nValue WITH 1 + 100 * RAND()
ENDFOR
CLEAR
LIST
SELECT MIN(nValue) as nMinimum, MAX(nValue) AS nMaximum;
   FROM curRandom INTO CURSOR curMinMax
? 'The minimum value is: ', nMinimum
? 'The maximum value is: ', nMaximum
CLOSE DATABASES
```
