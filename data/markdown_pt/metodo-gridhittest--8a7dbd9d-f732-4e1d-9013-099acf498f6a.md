# Método GridHitTest

Retorna, como parâmetros de saída, os componentes de um controle grid correspondentes a coordenadas horizontais (X) e verticais (Y) especificadas.

```foxpro
Grid.GridHitTest(nXCoord_In, nYCoord_In
   [, nWhere_Out [, nRelRow_Out [, nRelCol_Out [, nView_Out]]]])
```

#### Parâmetros
 **nXCoord_In**
Especifica a posição horizontal (X) em pixels dentro do formulário que contém o grid.
**nYCoord_In**
Especifica a posição vertical (Y) em pixels dentro do formulário que contém o grid.
**nWhere_Out**
Um parâmetro de saída que contém um valor correspondente ao componente do grid na posição especificada com nXCoord_In e nYCoord_In . A tabela a seguir lista os valores para @nWhere_Out e o componente do grid correspondente. @nWhere_Out Componente do grid 0 Um componente do grid que não pode ser determinado. 1 Cabeçalho de coluna. 2 Entre cabeçalhos de coluna. 3 Célula. 4 Reservado. 5 SplitBar. 6 Marcador de exclusão de registro. 7 Reservado 8 Reservado. 9 Reservado. 10 Reservado. 11 Caixa no canto superior esquerdo. 12 Marcador de registro. 13 Área de dimensionamento do cabeçalho de coluna. 14 Área de dimensionamento de linha. 15 Reservado. 16 Barra de rolagem horizontal. 17 Barra de rolagem vertical.
**nRelRow_Out**
Um parâmetro de saída contendo a linha relativa do grid no ponto especificado.
**nRelCol_Out**
Um parâmetro de saída contendo a coluna relativa do grid no ponto especificado.
**nView_Out**
Um parâmetro de saída contendo um valor correspondente ao painel do grid que contém o ponto especificado. Se o grid estiver dividido em dois painéis, este parâmetro contém 0 se o ponto especificado estiver no painel esquerdo, e contém 1 se o ponto especificado estiver no painel direito. Se o grid não estiver dividido em painéis separados, este parâmetro contém 1.

# Observações

Aplica-se a: Controle Grid

O método GridHitTest( ) retorna true (.T.) se o ponto especificado estiver dentro do grid; caso contrário, false (.F.) é retornado.

O método GridHitTest( ) pode ser usado durante eventos de mouse ou eventos de destino de soltar OLE para determinar onde o ponteiro do mouse está posicionado sobre o grid. Os parâmetros nRelRow_Out e nRelCol_Out podem ser passados ao método ActivateCell( ) para ativar uma célula específica no grid.
