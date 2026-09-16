# Função SQLCOLUMNS( )

Armazena uma lista de nomes de colunas e informações sobre cada coluna da tabela da fonte de dados especificada em um cursor do Visual FoxPro.

```foxpro
SQLCOLUMNS(nStatementHandle, cTableName
    [, "FOXPRO" | "NATIVE"] [, cCursorName])
```

#### Parâmetros
 **nStatementHandle**
Especifica um identificador de instrução ativo.
**cTableName**
Especifica o nome da tabela da qual os nomes das colunas são retornados. TableName pode conter os caracteres curinga ? e *. O ponto de interrogação (?) corresponde a qualquer caractere único e o asterisco (*) corresponde a qualquer número de caracteres.
**FOXPRO | NATIVE**
Especifica o formato das informações de coluna no conjunto de resultados. Coloque FOXPRO ou NATIVE entre aspas. A opção de formato NATIVE armazena informações de coluna para tabelas no mesmo formato da fonte de dados. A opção de formato FOXPRO armazena as informações de coluna no mesmo formato usado para a tabela ou cursor do Visual FoxPro que seria criado se você importasse a tabela da fonte de dados para o Visual FoxPro. Se você omitir FOXPRO ou NATIVE, a opção de formato assume o padrão FOXPRO. A tabela a seguir mostra as colunas no conjunto de resultados para o formato FOXPRO. Nome da coluna Descrição Field_name Nome da coluna Field_type Tipo de dados da coluna Field_len Comprimento da coluna Field_dec Número de casas decimais As colunas no conjunto de resultados para o formato NATIVE dependem da fonte de dados. Se a tabela especificada com cTableName não existir e o formato estiver definido como NATIVE, SQLCOLUMNS( ) retorna true (.T.) e cria uma tabela ou cursor vazio. Se a tabela especificada com cTableName não existir e o formato estiver definido como FOXPRO, SQLCOLUMNS( ) retorna false (.F.).
**cCursorName**
Especifica o nome do cursor do Visual FoxPro para o conjunto de resultados. Se você não incluir um nome de cursor, o Visual FoxPro usa o nome padrão SQLRESULT.

# Valor de retorno

Numeric ou Logical. SQLCOLUMNS( ) retorna 1 se o cursor for criado com sucesso, 0 se SQLCOLUMNS( ) ainda estiver em execução, – 1 se ocorrer um erro no nível de conexão e – 2 se ocorrer um erro no nível de ambiente.

# Observações

SQLCOLUMNS( ) é uma das quatro funções que você pode executar de forma síncrona ou assíncrona. A configuração Asynchronous de SQLSETPROP( ) determina se essas funções são executadas de forma síncrona ou assíncrona. No modo assíncrono, você deve chamar SQLCOLUMNS( ) repetidamente até que um valor diferente de false (.F.) (ainda em execução) seja retornado.

# Exemplo

O exemplo a seguir assume que SQLCONNECT( ) foi emitido com sucesso e seu valor de retorno foi armazenado em uma variável de memória chamada `gnHandle`. SQLCOLUMNS( ) é usado para criar um cursor chamado `MyCursor` contendo informações sobre as colunas na tabela `authors`.

```foxpro
= SQLCOLUMNS(gnHandle, 'authors', 'FOXPRO', 'MyCursor')
```
