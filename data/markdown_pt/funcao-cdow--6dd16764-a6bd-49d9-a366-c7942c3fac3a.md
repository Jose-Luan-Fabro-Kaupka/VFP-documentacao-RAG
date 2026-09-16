# Função CDOW( )

Retorna o dia da semana de uma expressão Date ou DateTime fornecida.

```foxpro
CDOW(dExpression | tExpression)
```

#### Parâmetros
 **dExpression**
Especifica a data da qual CDOW( ) retorna o dia.
**tExpression**
Especifica o datetime do qual CDOW( ) retorna o dia.

# Valor de retorno

Caractere

# Observações

CDOW( ) retorna o nome do dia da semana como uma cadeia de caracteres no formato de substantivo próprio.

# Exemplo

```foxpro
STORE {^1998-02-16} TO gdDate
CLEAR
? CDOW(gdDate)  && Displays Monday
```
