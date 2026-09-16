# Função ASQLHANDLES( )

Armazena referências numéricas a todos os handles de instrução de conexão SQL ativos em uma matriz.

```foxpro
ASQLHANDLES(ArrayName [, nStatementHandle])
```

#### Parâmetros
 **ArrayName**
Especifica o nome de uma matriz para armazenar informações de handle de instrução. Se a matriz que você especificar não existir, o Visual FoxPro cria a matriz automaticamente. Se a matriz existir e não for grande o suficiente para armazenar as informações, o Visual FoxPro aumenta o tamanho da matriz automaticamente. Se a matriz for maior que o necessário, o Visual FoxPro trunca a matriz.
**nStatementHandle**
Preenche a matriz com handles de instrução que usam a mesma conexão compartilhada, incluindo nStatementHandle.

# Valor de retorno

Numérico. ASQLHANDLES( ) retorna o número de handles de instrução em uso. Se nenhum handle de instrução estiver disponível, ASQLHANDLES( ) retorna 0 e não modifica a matriz.

# Observações

Você pode usar referências a handles de instrução em outras funções SQL do Visual FoxPro, como SQLEXEC( ) e SQLDISCONNECT( ). Para obter mais informações, consulte SQLEXEC( ) Function e SQLDISCONNECT( ) Function.

Você pode criar e retornar novos handles de instrução usando as funções SQLCONNECT( ) e SQLSTRINGCONNECT( ). Para obter mais informações, consulte SQLCONNECT( ) Function e SQLSTRINGCONNECT( ) Function.
