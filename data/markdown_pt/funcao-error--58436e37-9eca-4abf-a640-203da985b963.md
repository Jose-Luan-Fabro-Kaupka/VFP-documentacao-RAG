# Função ERROR( )

Retorna o número do erro que acionou uma rotina ON ERROR.

```foxpro
ERROR()
```

# Valor de retorno

Numérico

# Observações

ERROR( ) retorna o número do erro mais recente. Uma rotina ON ERROR deve estar ativa para que ERROR( ) retorne um valor diferente de 0.

Quando um erro é capturado durante a execução do programa, o tipo de erro pode ser retornado por ERROR( ) em uma rotina ON ERROR. A mensagem de erro correspondente pode ser retornada por MESSAGE( ).

O valor retornado por ERROR( ) é redefinido por RETURN ou RETRY.

# Exemplo

O exemplo a seguir demonstra uma rotina simples de tratamento de erros que exibe uma mensagem quando ocorre um erro.

```foxpro
CLEAR
ON ERROR DO errhand WITH ERROR(), MESSAGE()
*** The next line generates an error - there is no BRWSE command
BRWSE
ON ERROR
RETURN
*** Error handler ***
PROCEDURE errhand
PARAMETER errnum,message
? Message
? 'Error number: '+ ALLTRIM(STR(Errnum))
RETURN
```
