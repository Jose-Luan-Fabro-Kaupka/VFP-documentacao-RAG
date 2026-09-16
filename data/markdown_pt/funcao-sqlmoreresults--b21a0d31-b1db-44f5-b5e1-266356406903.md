# Função SQLMORERESULTS( )

Copia outro conjunto de resultados para um cursor do Visual FoxPro se mais conjuntos de resultados estiverem disponíveis.

```foxpro
SQLMORERESULTS(nStatementHandle [, cCursorName [, aCountInfo]]))
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado por SQLCONNECT( ).
**cCursorName**
Especifica o nome do cursor do Visual FoxPro para o qual o conjunto de resultados é enviado. Se você não incluir um nome de cursor, o Visual FoxPro usa o nome padrão SQLRESULT. Para vários conjuntos de resultados, novos nomes de cursor são derivados anexando um número incrementado ao nome do primeiro cursor.
**aCountInfo**
Especifica o nome da matriz a ser preenchida com informações de contagem de linhas. Se a matriz não existir, ela é criada. A matriz tem duas colunas: 1 – Alias, 2 –Count. Coluna Conteúdo da matriz Tipo de dados Descrição Alias 0 Caractere Indica que o comando SQL não retornou nenhum resultado. Nenhum registro foi retornado ou o comando SQL falhou antes que os resultados pudessem ser retornados. (chamada final SQLMORERESULTS) ou a execução falhou antes que qualquer resultado pudesse ser processado. Pode estar apenas na primeira linha. A coluna Count da linha contém o valor -1. Cadeia de caracteres em maiúsculas não vazia Caractere Alias do cursor – destino para a operação de busca de registros. A coluna Count da linha contém o número de registros buscados ou -1 se a busca falhou. Se Count for -1, o cursor pode não ter sido criado. Durante a execução assíncrona, o processo de busca para um cursor pode ser dividido entre várias chamadas SQLMORERESULTS ou SQLEXEC; cada chamada retorna sua própria contagem de busca para o cursor. Cadeia de caracteres vazia Caractere Indica que o comando SQL (INSERT, UPDATE ou DELETE) não retornou um conjunto de resultados. Count Número de registros afetados ou buscados. Inteiro Indica o número de registros afetados conforme retornado pela função ODBC SQLRowCount. Retorna -1 se o número de registros não estiver disponível.

# Valor de retorno

Numérico. SQLMORERESULTS( ) retorna 0 se a instrução SQL ainda estiver em execução, retorna 1 se terminou a execução e retorna 2 se não houver mais dados. No modo não em lote, SQLMORERESULTS( ) deve ser chamado após cada chamada SQLEXEC( ) bem-sucedida até que SQLMORERESULTS( ) retorne 2 (nenhum dado encontrado). A configuração da opção de modo em lote de SQLSETPROP( ) determina se SQLEXEC( ) executa uma instrução SQL em modo em lote ou não em lote.

SQLMORERESULTS( ) retorna – 1 se ocorrer um erro em nível de conexão e retorna – 2 se ocorrer um erro em nível de ambiente.

# Observações

SQLMORERESULTS( ) determina se mais conjuntos de resultados estão disponíveis de uma instrução SQL executada com SQLEXEC( ) em modo não em lote. Se mais conjuntos de resultados estiverem disponíveis, eles são copiados para um cursor do Visual FoxPro, um conjunto por vez.

SQLMORERESULTS( ) é uma das quatro funções que você pode executar de forma síncrona ou assíncrona. A configuração assíncrona de SQLSETPROP( ) determina se essas funções executam de forma síncrona ou assíncrona. No modo assíncrono, você deve chamar SQLMORERESULTS( ) repetidamente até que retorne um valor diferente de 0 (ainda em execução).

# Exemplo

O exemplo a seguir assume que SQLCONNECT( ) foi emitido com sucesso e seu valor de retorno foi armazenado em uma variável de memória chamada `gnHandle`. SQLSETPROP( ) é usado para definir a propriedade BatchMode como False (.F.) para que os conjuntos de resultados individuais possam ser recuperados.

SQLMORERESULTS( ) é emitido duas vezes para criar dois cursores contendo os resultados da consulta SQLEXEC( ). SET é usado para exibir a janela View e os cursores criados por SQLEXEC( ).

```foxpro
= SQLSETPROP(gnHandle, 'BatchMode', .F.)  && Individual result sets
= SQLEXEC(gnHandle, 'SELECT * FROM authors;
   SELECT * FROM titles')
= SQLMORERES(gnHandle)  && First result set
= SQLMORERES(gnHandle)  && Second result set
```
