# Função AERROR( )

Cria um array variável contendo informações sobre o erro mais recente do Visual FoxPro, OLE ou ODBC.

```foxpro
AERROR(ArrayName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array que AERROR( ) deve criar.

# Valor de retorno

Numeric. AERROR( ) retorna o número de linhas no array.

# Observações

AERROR( ) cria um array com sete colunas contendo informações sobre o erro. O tipo de erro ocorrido determina o número de linhas no array.

> **Observação:** Se nenhum erro ocorreu, AERROR( ) não cria o array.

Quando ocorre um erro do Visual FoxPro, o array contém uma linha. A tabela a seguir descreve o conteúdo de cada elemento.

| Número do elemento | Descrição |
| --- | --- |
| 1 | Numeric. O número do erro. Idêntico ao valor retornado por ERROR( ). |
| 2 | Character. O texto da mensagem de erro. Idêntico ao valor retornado por MESSAGE( ). |
| 3 | O valor nulo. No entanto, se o erro tiver um parâmetro de erro adicional, contém o texto do parâmetro de erro. Quase idêntico ao valor retornado por SYS(2018), a diferença sendo que AERROR( ) retorna maiúsculas e minúsculas misturadas, mas SYS(2018) retorna tudo em maiúsculas. |
| 4 | O valor nulo. No entanto, conforme apropriado, contém o número da área de trabalho em que o erro ocorreu. |
| 5 | O valor nulo. No entanto, se um trigger falhou (erro 1539), contém um dos seguintes valores numéricos:1 – Falha no trigger de inserção.2 – Falha no trigger de atualização.3 – Falha no trigger de exclusão. |
| 6 | O valor nulo. |
| 7 | O valor nulo. |

Quando ocorrem erros OLE numerados 1427 ou 1429, o array contém uma linha. A tabela a seguir descreve o conteúdo de cada elemento.

| Número do elemento | Descrição |
| --- | --- |
| 1 | Numeric. Contém 1427 ou 1429. |
| 2 | Character. O texto da mensagem de erro do Visual FoxPro. |
| 3 | Character. O texto da mensagem de erro OLE. |
| 4 | Character. O nome do aplicativo (por exemplo, Microsoft Excel). |
| 5 | O valor nulo ou Character. Contém o nome do arquivo de Ajuda do aplicativo onde podem ser encontradas mais informações sobre o erro, se as informações estiverem disponíveis no aplicativo; caso contrário, contém o valor nulo. |
| 6 | O valor nulo ou Character. Contém o ID de contexto de Ajuda do tópico de Ajuda apropriado, se as informações estiverem disponíveis no aplicativo; caso contrário, contém o valor nulo. |
| 7 | Numeric. Um número de exceção OLE 2.0. |

Quando ocorre um erro ODBC numerado 1526, o array contém uma ou mais linhas, uma linha para cada erro ODBC. A tabela a seguir descreve o conteúdo de cada elemento.

| Número do elemento | Descrição |
| --- | --- |
| 1 | Numeric. Contém 1526. |
| 2 | Character. O texto da mensagem de erro. |
| 3 | Character. O texto da mensagem de erro ODBC. |
| 4 | Character. O SQL state ODBC atual. |
| 5 | Numeric. O número do erro da fonte de dados ODBC. |
| 6 | Numeric. O handle de conexão ODBC. |
| 7 | O valor nulo. |

# Exemplo

O exemplo a seguir usa ON ERROR para especificar uma rotina de tratamento de erros chamada `errhand`. Um erro é gerado emitindo um comando com erro de ortografia (BRWS). A rotina de tratamento de erros `errhand` usa AERROR( ) para criar um array contendo informações de erro, e essas informações são então exibidas.

```foxpro
ON ERROR DO errhand     && errhand is the error handler procedure
BRWS  && Causes a syntax error
ON ERROR  && Restore system error handler
PROCEDURE errhand
   = AERROR(aErrorArray)  && Data from most recent error
   CLEAR
   ? 'The error provided the following information'  && Display message
   FOR n = 1 TO 7  && Display all elements of the array
      ? aErrorArray(n)
   ENDFOR
```
