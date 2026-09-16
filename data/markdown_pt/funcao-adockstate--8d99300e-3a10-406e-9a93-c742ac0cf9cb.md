# Função ADOCKSTATE( )

Recupera o estado de encaixe de qualquer formulário encaixável, janela do Ambiente de Desenvolvimento Integrado (IDE) ou barra de ferramentas. Somente para formulários, você pode usar o método GetDockState. ADOCKSTATE( ) está disponível em tempo de execução.

```foxpro
ADOCKSTATE( ArrayName [, nType | nExtended])
```

#### Parâmetros
 **ArrayName**
Especifica uma matriz com uma ou mais linhas contendo o estado de encaixe de itens encaixáveis. Observação Tanto barras de ferramentas do sistema quanto definidas pelo usuário podem aparecer na matriz. Um formulário aparece na matriz somente se a propriedade Dockable do formulário estiver definida com um valor maior que 0. A tabela a seguir ilustra as informações contidas na matriz. Elemento Descrição 1 Nome do formulário, janela do IDE ou barra de ferramentas. Para barras de ferramentas definidas pelo usuário, o primeiro elemento contém o valor da propriedade Caption dessa barra de ferramentas. 2 Estado de encaixe: 1 - Encaixado 0 - Desencaixado 3 Posição de encaixe. Para valores de formulário e barra de ferramentas, consulte DockPosition Property. Para janelas, consulte DOCK Command. 4 Objeto de destino com o qual o objeto especificado está encaixado. Este elemento não se aplica a barras de ferramentas, a menos que estejam encaixadas na janela principal do Visual FoxPro. Para barras de ferramentas ou janelas encaixadas na janela principal do Visual FoxPro, o quarto elemento contém o nome da janela principal do Visual FoxPro, que você pode recuperar usando a propriedade Caption de _VFP. Se uma janela ou barra de ferramentas não estiver encaixada, o quarto elemento contém uma cadeia de caracteres vazia. Observação Se uma barra de ferramentas aparecer entre a área de trabalho do Visual FoxPro e uma janela encaixada na área de trabalho do Visual FoxPro, o quarto elemento contém o nome da barra de ferramentas. 5 Referência de objeto ao formulário ou barra de ferramentas de encaixe. Aplica-se somente ao encaixar formulários ou barras de ferramentas definidos pelo usuário; caso contrário, este elemento contém uma cadeia de caracteres vazia (janela do IDE). 6 Referência de objeto ao objeto de destino se for um formulário definido pelo usuário. Se o objeto de destino for a janela principal do Visual FoxPro, este elemento contém uma referência de objeto à variável de sistema _SCREEN. Caso contrário, este elemento contém uma cadeia de caracteres vazia (janela do IDE).
**nType**
Especifica um ou mais itens para os quais você deseja que ADOCKSTATE( ) retorne informações de estado de encaixe. A tabela a seguir lista os valores de nType. nType Descrição 0 Retornar todas ou nenhuma janela. (Padrão) 1 Retornar somente janelas do IDE. 2 Retornar somente barras de ferramentas. 3 Retornar somente formulários definidos pelo usuário.
**nExtended**
Especifica o número de elementos a retornar na matriz. A tabela a seguir lista os valores de nExtended. nExtended Descrição 0 Retornar uma matriz de quatro elementos para janelas e barras de ferramentas. 1 Retornar uma matriz de seis elementos para formulários.

# Valor de retorno

Tipo de dados Numeric. ADOCKSTATE( ) retorna o número de linhas preenchidas ou 0 se nenhuma for encontrada.

# Observações

Para janelas encaixadas por guias, a janela mais à esquerda é a janela âncora e contém detalhes sobre como todo o contêiner está encaixado. O Visual FoxPro percorre as janelas da esquerda para a direita. Para janelas encaixadas por vínculo, a janela superior esquerda em um contêiner encaixado por vínculo contém detalhes sobre como todo o contêiner está encaixado.

As regras a seguir determinam a ordem de encaixe:
 - O Visual FoxPro percorre o contêiner encaixado por vínculo começando pela janela superior esquerda.
- O Visual FoxPro percorre as janelas de cima para baixo, da esquerda para a direita. Um contêiner encaixado por vínculo pode consistir em vários contêineres internos. Assim, a ordenação das janelas na matriz ADOCKSTATE( ) pode parecer diferente.
- A posição contida no terceiro elemento da matriz é relativa à janela referenciada no primeiro elemento da matriz.
- O Visual FoxPro percorre primeiro todas as janelas encaixadas por vínculo e depois as janelas encaixadas por guias. Essencialmente, o Visual FoxPro faz duas passagens por um contêiner vinculado. O Visual FoxPro inclui somente a janela encaixada por guias mais à esquerda na primeira passagem para janelas encaixadas por vínculo.
- O Visual FoxPro percorre um contêiner encaixado por guias da esquerda para a direita.

Se o terceiro elemento na matriz estiver definido como -1 (não encaixado), o contêiner não está encaixado. Se o contêiner estiver encaixado na área de trabalho, o terceiro elemento na matriz contém a posição em que o contêiner está encaixado na área de trabalho do Visual FoxPro conforme referenciado no quarto elemento da matriz.

Por exemplo, o código a seguir cria uma matriz, abre e encaixa várias janelas e produz uma matriz conforme mostrado:

```foxpro
CLEAR ALL
PUBLIC aa
DIMENSION aa[1]
ACTIVATE WINDOW Command
ACTIVATE WINDOW Trace
ACTIVATE WINDOW Document
ACTIVATE WINDOW Properties
ACTIVATE WINDOW Watch
ACTIVATE WINDOW Locals
SET
DOCK WINDOW View POSITION -1
DOCK WINDOW Command POSITION -1
DOCK WINDOW Trace POSITION -1
DOCK WINDOW Document POSITION -1
DOCK WINDOW Properties POSITION -1
DOCK WINDOW Watch POSITION -1
DOCK WINDOW Command POSITION 1 WINDOW View
DOCK WINDOW Trace POSITION 1 WINDOW Command
DOCK WINDOW Document POSITION 3 WINDOW View
DOCK WINDOW Properties POSITION 3 WINDOW Trace
DOCK WINDOW Watch POSITION 4 WINDOW Command
DOCK WINDOW Locals POSITION 3 WINDOW Command
ADOCKSTATE(aa,1)
```

A matriz resultante aparece da seguinte forma:

| Row | First element | Second element | Third element | Fourth element |
| --- | --- | --- | --- | --- |
| 1 | Trace | 1 | -1 | |
| 2 | Properties | 1 | 3 | Trace |
| 3 | Watch | 1 | 2 | Trace |
| 4 | Locals | 1 | 3 | Watch |
| 5 | View | 1 | 2 | Watch |
| 6 | Document View | 1 | 3 | View |
| 7 | Command | 1 | 4 | Watch |

O Visual FoxPro exibe informações de encaixe para janelas do depurador no depurador. Se uma janela estiver desencaixada, o Visual FoxPro mostra o nome, o estado de encaixe (0) e a posição (-1). Se uma janela estiver encaixada, o Visual FoxPro mostra somente o nome, o estado de encaixe (1), a posição e a janela ("Visual FoxPro Debugger").

Historicamente, em versões anteriores do Visual FoxPro, a janela Data Session sempre foi chamada de janela View. Além disso, a linguagem usada para controlar essa janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a essa janela como janela View. O Visual FoxPro continua a se referir à janela View para a função ADOCKSTATE( ).

# Exemplo

O exemplo a seguir mostra os resultados de retorno de ADOCKSTATE( ) quando nenhuma barra de ferramentas ou janela foi encaixada anteriormente, por exemplo, após excluir os arquivos de recurso FoxUser ou quando o Visual FoxPro é instalado recentemente. Certifique-se de que a janela Command está aberta.

```foxpro
CLEAR
dockNum = ADOCKSTATE(dockState)
? dockNum   && Returns 2 because Standard toolbar also exists.
? dockState(1,1)  && Outputs "COMMAND".
? dockState(1,4)  && Outputs an empty string because the Command
                && window is not docked.
? dockState(2,1)  && Outputs "Standard".
? dockState(2,4)  && Outputs "Microsoft Visual FoxPro" because the
                && Standard toolbar is docked to the Microsoft
                && Visual FoxPro desktop.
```

O exemplo a seguir mostra como usar o comando DOCK para encaixar a janela Command na janela da área de trabalho do Visual FoxPro e usar ADOCKSTATE( ) para obter o estado de encaixe da janela Command. Primeiro, certifique-se de que a janela Command está aberta. Depois de encaixar a janela Command, você pode ver que as janelas Standard toolbar e Command estão encaixadas na janela da área de trabalho do Microsoft Visual FoxPro. A posição das barras de ferramentas ou janelas na matriz retornada por ADOCKSTATE( ) pode variar dependendo da ordem em que as barras de ferramentas ou janelas são encaixadas.

```foxpro
CLEAR
DOCK WINDOW Command POSITION 0
dockNum = ADOCKSTATE(dockState)
? dockNum   && Returns 2 because Standard toolbar also exists.
? dockState(1,1)  && Outputs "Standard".
? dockState(1,4)  && Outputs "Microsoft Visual FoxPro".
? dockState(2,1)  && Outputs "COMMAND".
? dockState(2,4)  && Outputs "Microsoft Visual FoxPro".
```
