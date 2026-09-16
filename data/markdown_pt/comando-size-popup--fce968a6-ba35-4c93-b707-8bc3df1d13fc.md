# Comando SIZE POPUP

Altera o tamanho de um menu criado com DEFINE POPUP.

```foxpro
SIZE POPUP MenuName TO nRow1, nColumn1 | BY nRow2, nColumn2
```

#### Parâmetros
 **MenuName**
Especifica o nome do menu cujo tamanho você deseja alterar.
**TO nRow1 , nColumn1**
Altera o tamanho de um menu para um tamanho específico. nRow1 e nColumn1 especificam as novas coordenadas de linha e coluna, respectivamente, do canto inferior direito do menu.
**BY nRow2 , nColumn2**
Altera o tamanho de um menu em relação ao seu tamanho atual. nRow2 e nColumn2 especificam a alteração de tamanho do menu em linhas e colunas, em relação às coordenadas atuais de linha e coluna do canto inferior direito do menu.

# Observações

Se um menu definido pelo usuário foi criado, seu tamanho pode ser alterado; ele não precisa estar ativo ou visível.

# Exemplo

Este exemplo cria um menu contendo arquivos com extensão .prg e move, amplia e reduz o menu antes de fechá-lo.

```foxpro
CLEAR
DEFINE POPUP popMovIn FROM 2,2 TO 7, 14 PROMPT FILES LIKE *.PRG ;
   TITLE 'Programs'
ACTIVATE POPUP popMovIn NOWAIT
=CHRSAW(2)
MOVE POPUP popMovIn BY 5,5     && Move popup down
=CHRSAW(2)
SIZE POPUP popMovIn BY 5,5  && Enlarge the popup
=CHRSAW(2)
SIZE POPUP popMovIn BY -5,-5  && Shrink the popup
=CHRSAW(2)
MOVE POPUP popMovIn BY -5,-5  && Move popup up
=CHRSAW(2)
DEACTIVATE POPUP popMovIn
RELEASE POPUP popMovIn
```
