# Função APRINTERS( )

Armazena informações sobre impressoras atualmente disponíveis em uma matriz.

> **Observação:** O comportamento desta função é específico do SO (sistema operacional). O Visual FoxPro pode ou não verificar se as impressoras estão realmente conectadas ao seu computador quando prepara esta lista, e a lista pode incluir todas as impressoras instaladas como configurações de impressora, ou apenas aquelas disponíveis na rede atual.

```foxpro
APRINTERS(ArrayName [, nValue])
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz contendo informações sobre impressoras. Observação Se a matriz que você incluir não existir, o Visual FoxPro cria automaticamente a matriz. Se a matriz existir, mas não for grande o suficiente para conter todas as informações, o Visual FoxPro aumenta o tamanho da matriz para acomodar as informações. Se a matriz for maior do que o necessário, o Visual FoxPro trunca a matriz. Se a matriz existir, mas APRINTERS( ) retornar 0 porque nenhuma impressora está disponível, a matriz permanece inalterada. Se a matriz não existir e APRINTERS( ) retornar 0, a matriz não é criada.
**[, nValue ]**
Especifica um valor que cria uma matriz de duas colunas ou cinco colunas. Cada linha na matriz contém informações sobre uma impressora. A tabela a seguir descreve os possíveis valores de nValue . nValue Descrição 0 ou omitido Retorna uma matriz de duas colunas contendo os seguintes itens começando pela primeira coluna: Nome da impressora. Nome da porta à qual a impressora está conectada. 1 Retorna uma matriz de cinco colunas contendo os seguintes itens começando pela primeira coluna: Nome da impressora. Nome da porta à qual a impressora está conectada. Nome do driver da impressora. Comentário da impressora. Localização da impressora.

# Valor de retorno

Numérico. APRINTERS( ) retorna o número de linhas na matriz ou 0 quando nenhuma impressora está disponível.

# Exemplo

O exemplo a seguir cria uma matriz nomeada `gaPrinters` se alguma impressora estiver disponível e exibe informações sobre essas impressoras. Caso contrário, exibe uma mensagem indicando que APRINTERS( ) não consegue recuperar informações sobre nenhuma impressora.

```foxpro
IF APRINTERS(gaPrinters) > 0
   CLEAR  && clear the current output window
   DISPLAY MEMORY LIKE gaPrinters && show the contents of the array
ELSE
   WAIT WINDOW 'No printers found.'
ENDIF
```
