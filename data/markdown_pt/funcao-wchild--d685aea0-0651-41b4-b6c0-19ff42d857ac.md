# Função WCHILD( )

Retorna o número de janelas filhas em uma janela pai ou os nomes das janelas filhas na ordem em que estão empilhadas na janela pai.

```foxpro
WCHILD([WindowName] [nChildWindow])
```

#### Parâmetros
 **WindowName**
Especifica uma janela diferente da janela de saída ativa para a qual WCHILD( ) retorna o número de janelas filhas. O número de janelas filhas na janela especificada é retornado se você incluir apenas um nome de janela sem a expressão numérica nChildWindow. Se você incluir WindowName e nChildWindow, WCHILD( ) retorna os nomes das janelas filhas na janela especificada. Se você incluir WindowName e nChildWindow, separe WindowName e nChildWindow com uma vírgula. Você também pode incluir a cadeia de caracteres vazia em WindowName para especificar a janela principal do Visual FoxPro.
**nChildWindow**
Especifica uma expressão numérica incluída para retornar os nomes das janelas filhas na janela de saída ativa quando você omite WindowName. A expressão numérica nChildWindow pode ser 0 ou qualquer valor positivo. O nome da janela filha na base da pilha de janelas filhas na janela de saída atual é retornado se nChildWindow for 0. Se nChildWindow for um número positivo, WCHILD( ) retorna o nome da próxima janela filha na pilha de janelas. O nome da próxima janela filha na pilha é retornado se você emitir WCHILD( ) novamente com um número positivo, e assim por diante. A cadeia de caracteres vazia é retornada se WCHILD( ) for chamado mais vezes do que o número de janelas filhas na janela pai. Para obter mais informações sobre empilhamento de janelas, consulte ACTIVATE WINDOW. Observação No Visual FoxPro para Windows, se a janela principal do Visual FoxPro estiver ativa, todas as janelas são filhas da janela principal do Visual FoxPro. No Visual FoxPro, barras de ferramentas que não estão encaixadas na borda da janela principal do Visual FoxPro são filhas da janela principal do Visual FoxPro. Emitir uma série de funções WCHILD() com números positivos retorna os nomes das janelas ativas e barras de ferramentas. Se você incluir WindowName e nChildWindow, separe WindowName e nChildWindow com uma vírgula.

# Valor de retorno

Caractere ou Numérico

# Observações

Você pode criar uma janela (a janela pai) e colocar outras janelas (janelas filhas) dentro dela. Incluir a cláusula IN ou IN WINDOW em DEFINE WINDOW cria uma janela filha dentro da janela pai. Uma janela filha criada e ativada dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai é movida, a janela filha se move com ela.

O número de janelas filhas na janela de saída ativa é retornado se você emitir WCHILD( ) sem argumentos.
