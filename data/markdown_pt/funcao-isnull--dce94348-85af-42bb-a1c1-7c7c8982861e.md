# Função ISNULL( )

Retorna true (.T.) se uma expressão for avaliada como um valor nulo; caso contrário, ISNULL( ) retorna false (.F.).

```foxpro
ISNULL(eExpression)
```

#### Parâmetros
 **eExpression**
Especifica a expressão a ser avaliada.

# Valor de retorno

Logical

# Observações

Use ISNULL( ) para determinar se o conteúdo de um campo, variável de memória ou elemento de matriz contém um valor nulo, ou se uma expressão é avaliada como um valor nulo.

# Exemplo

No exemplo a seguir, ISNULL( ) é usado para verificar um valor nulo.

```foxpro
STORE .NULL. TO mNullvalue  && Store a null value to a memory variable
CLEAR
? mNullvalue  && Display the value of the memory variable
? ISNULL(mNullvalue)  && Returns .T., indicating a null value
? TYPE('mNullvalue')     && Returns L, indicating a logical value
? (mNullvalue = .NULL.)  && Returns .NULL., bad test for null values
```
