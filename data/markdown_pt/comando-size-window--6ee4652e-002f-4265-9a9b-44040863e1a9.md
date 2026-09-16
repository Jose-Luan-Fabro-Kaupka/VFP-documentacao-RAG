# Comando SIZE WINDOW

Altera o tamanho de uma janela criada com DEFINE WINDOW ou de uma janela de sistema do Visual FoxPro.

```foxpro
SIZE WINDOW WindowName TO nRow1, nColumn1 | BY nRow2, nColumn2
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela cujo tamanho você deseja alterar. Para alterar o tamanho de uma janela de sistema, coloque o nome completo da janela de sistema entre aspas. Por exemplo, para aumentar o tamanho da janela Command em 1 linha e 1 coluna, execute o seguinte comando: SIZE WINDOW 'Command Window' BY 1,1 Você só pode alterar o tamanho das janelas Command, Debug e Trace.
**TO nRow1 , nColumn1**
Altera o tamanho de uma janela para um tamanho específico. nRow1 e nColumn1 especificam, respectivamente, as novas coordenadas de linha e coluna do canto inferior direito da janela em relação ao canto superior esquerdo da janela.
**BY nRow2 , nColumn2**
Altera o tamanho de uma janela em relação ao seu tamanho atual. nRow2 e nColumn2 especificam a alteração de tamanho da janela em linhas e colunas, em relação às coordenadas atuais de linha e coluna do canto inferior direito da janela.

# Observações

Se uma janela definida pelo usuário foi criada, seu tamanho pode ser alterado; ela não precisa estar ativa ou visível.
