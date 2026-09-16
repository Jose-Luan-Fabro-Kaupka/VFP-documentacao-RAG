# Passando parâmetros para funções da API do Visual FoxPro

Frequentemente, as rotinas da API do Visual FoxPro exigirão parâmetros de uma estrutura de dados específica do Visual FoxPro. As seções a seguir fornecem uma lista dos tipos de dados do Visual FoxPro e estruturas de dados adicionais. Para as definições de tipo e definições de estrutura reais, consulte o arquivo Pro_ext.h.

# Tipos de dados da API do Visual FoxPro

Os seguintes tipos de dados são usados nas rotinas da API do Visual FoxPro.

| Tipo de dados | Descrição |
| --- | --- |
| EDLINE | O número de uma linha em um arquivo aberto em uma janela de edição. A primeira linha é 1. |
| EDPOS | A posição de deslocamento de um caractere em um arquivo aberto em uma janela de edição. A posição de deslocamento do primeiro caractere no arquivo ou campo memo é 0. |
| FCHAN | Canal de arquivo. Cada arquivo aberto pelo Visual FoxPro, ou pela API usando _FCreate( ) e _FOpen( ), recebe um FCHAN. |
| FPFI | Um ponteiro de 32 bits para uma função que retorna um inteiro. |
| ITEMID | Um identificador exclusivo atribuído a um único comando em um menu. |
| MENUID | Um identificador exclusivo atribuído a um menu. |
| MHANDLE | Um identificador exclusivo dado a cada bloco de memória alocado pelo Visual FoxPro, ou alocado pela API usando _AllocHand( ). Pode ser desreferenciado para seu ponteiro usando _HandToPtr( ). |
| NTI | Índice da tabela de nomes. Cada nome de variável e campo de tabela tem uma entrada nesta tabela. |
| WHANDLE | Handle de janela. Um identificador exclusivo atribuído a cada janela aberta pelo Visual FoxPro, ou aberta pela API usando _WOpen( ). |

> **Observação:** Como ponteiros FAR não são apropriados para compiladores de 32 bits, instruções #define em Pro_ext.h redefinem FAR, _far e __far como valores nulos.

# Estruturas de dados da API do Visual FoxPro

As principais estruturas de dados usadas na biblioteca de API do Visual FoxPro estão listadas na tabela a seguir.

| Estrutura | Descrição |
| --- | --- |
| EventRec | Uma estrutura usada para descrever o que o sistema está fazendo em um determinado momento. |
| FoxInfo | Usada em bibliotecas FLL para comunicação entre o Visual FoxPro e seu programa; não usada em arquivos .ocx. |
| FoxTable | Usada em bibliotecas FLL para comunicação entre o Visual FoxPro e seu programa; não usada em arquivos .ocx. |
| Locator | Uma estrutura usada para acessar valores de parâmetros (FLL) ou variáveis ou campos do Visual FoxPro (FLL e ocx). |
| ParamBlk | Usada em bibliotecas FLL para comunicação entre o Visual FoxPro e seu programa; não usada em arquivos .ocx. |
| Parameter | Usada em bibliotecas FLL para comunicação entre o Visual FoxPro e seu programa; não usada em arquivos .ocx. |
| Point | Uma estrutura que define as coordenadas horizontal e vertical de um único ponto na tela. As coordenadas são especificadas em linhas e colunas. |
| Rect | Uma estrutura que define as coordenadas de um retângulo na tela. O canto superior esquerdo do retângulo é definido por ( top , left ) e o canto inferior direito é definido por ( bottom -1, right -1). As coordenadas são especificadas em linhas e colunas. |
| Value | Uma estrutura usada para acessar valores de parâmetros (FLL) ou variáveis ou campos do Visual FoxPro (FLL e OCX). |
