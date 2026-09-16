# Função FWRITE( )

Grava uma cadeia de caracteres em um arquivo aberto com uma função de arquivo de baixo nível.

```foxpro
FWRITE(nFileHandle, cExpression [, nCharactersWritten])
```

#### Parâmetros
 **nFileHandle**
Especifica o número do identificador de arquivo para o arquivo no qual FWRITE( ) grava.
**cExpression**
Especifica a expressão de caractere que FWRITE( ) grava no arquivo especificado com nFileHandle.
**nCharactersWritten**
FWRITE( ) grava toda a expressão de caractere no arquivo, a menos que você inclua nCharactersWritten. Quando você inclui nCharactersWritten, nCharactersWritten caracteres são gravados no arquivo. Se nCharactersWritten for menor que o número de caracteres em cExpression, apenas nCharactersWritten caracteres são gravados no arquivo. Todos os caracteres em cExpression são gravados no arquivo se nCharactersWritten for igual ou maior que o número de caracteres em cExpression.

# Valor de retorno

Numérico

# Observações

Diferentemente de FPUTS( ), FWRITE( ) não coloca um retorno de carro e uma quebra de linha no final da cadeia de caracteres.

FWRITE( ) retorna o número de bytes gravados no arquivo. Se FWRITE( ) não conseguir gravar no arquivo por qualquer motivo, 0 é retornado.
