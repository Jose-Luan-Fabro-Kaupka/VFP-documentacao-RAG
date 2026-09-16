# Função MESSAGE( )

Retorna a mensagem de erro atual ou a linha do programa que causou o erro.

```foxpro
MESSAGE([1])
```

#### Parâmetros
 **[1]**
Retorna o código-fonte do programa que causou o erro se MESSAGE( ) estiver incluído em uma rotina ON ERROR. Observe que MESSAGE(1) não está disponível no runtime. Se o código-fonte do programa não estiver disponível, MESSAGE(1) retorna um dos seguintes: a linha inteira do programa se a linha for macro-substituída. Um comando se a linha contiver um comando sem cláusulas adicionais. Um comando seguido de três pontos (...) se a linha contiver um comando e cláusulas adicionais.

# Valor de retorno

Character. MESSAGE( ) retorna a mensagem de erro atual como uma cadeia de caracteres ou o conteúdo da linha do programa que causou o erro.

# Observações

Diferentemente de ERROR( ), MESSAGE( ) não é redefinido por RETURN ou RETRY.

# Exemplo

O exemplo a seguir exibe a saída usando a função MESSAGE( ).

```foxpro
ON ERROR DO Errhand
*** The next line should generate an error ***
USE Nodatabase
ON ERROR     && Restore system error handler.
PROCEDURE Errhand
? 'Line of code with error: ' + MESSAGE(1)
? 'Error number: ' + STR(ERROR())
? 'Error message: ' + MESSAGE()
```
