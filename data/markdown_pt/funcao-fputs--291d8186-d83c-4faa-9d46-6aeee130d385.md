# Função FPUTS( )

Grava uma cadeia de caracteres, retorno de carro e quebra de linha em um arquivo aberto com uma função de arquivo de baixo nível.

```foxpro
FPUTS(nFileHandle, cExpression [, nCharactersWritten])
```

#### Parâmetros
 **nFileHandle**
Especifica o número do identificador de arquivo para o arquivo no qual FPUTS( ) grava dados.
**cExpression**
Especifica a expressão de caractere que FPUTS( ) grava no arquivo.
**nCharactersWritten**
Especifica o número de caracteres em cExpression a gravar no arquivo. FPUTS( ) grava toda a expressão de caractere cExpression no arquivo se você omitir nCharactersWritten . Se você incluir nCharactersWritten , nCharactersWritten caracteres são gravados no arquivo. Se nCharactersWritten for menor que o número de caracteres em cExpression , apenas nCharactersWritten caracteres são gravados no arquivo. Todo cExpression é gravado no arquivo se nCharactersWritten for igual ou maior que o número de caracteres em cExpression .

# Valor de retorno

Numeric

# Observações

FPUTS( ) retorna o número de bytes gravados no arquivo. Zero é retornado se FPUTS( ) não puder gravar no arquivo por qualquer motivo.
