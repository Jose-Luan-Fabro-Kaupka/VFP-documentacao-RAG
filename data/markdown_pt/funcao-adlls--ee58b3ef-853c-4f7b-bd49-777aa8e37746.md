# Função ADLLS( )

Retorna uma matriz contendo os nomes das funções carregadas por DECLARE DLLs.

```foxpro
ADLLS(ArrayName)
```

#### Parâmetros
 **Arrayname**
Especifica o nome da matriz. Se a matriz especificada não existir, o Visual FoxPro a cria automaticamente. Se a matriz existir e não for grande o suficiente para conter todas as funções carregadas por DECLARE DLLS, o Visual FoxPro aumenta automaticamente o tamanho da matriz para acomodar as informações. Se a matriz for maior do que o necessário, o Visual FoxPro a trunca. Se nenhuma função DLL foi declarada, a matriz não é criada e uma matriz existente não é modificada.

# Valor de retorno

Numérico

# Observações

O valor numérico retornado pela função ADLLS especifica o número de funções carregadas por DLL. Se nenhum alias for fornecido, o segundo elemento retorna o mesmo valor que o primeiro (nome da função).

A matriz criada pela função ADLLS tem o seguinte formato:

| Coluna | Informação do campo | Tipo de dados |
| --- | --- | --- |
| 1 | Function Name | Character |
| 2 | Function Alias | Character |
| 3 | Library Name | Character |

Para obter detalhes sobre como declarar funções, consulte DECLARE - DLL Command.
