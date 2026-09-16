# Função MINUTE( )

Retorna a porção de minutos de uma expressão DateTime.

```foxpro
MINUTE(tExpression)
```

#### Parâmetros
 **tExpression**
Especifica a expressão DateTime da qual a porção de minutos é retornada.

# Valor de retorno

Numeric

# Exemplo

O exemplo a seguir exibe a porção de minutos da hora atual e a porção de minutos de uma hora específica.

```foxpro
CLEAR
? MINUTE(DATETIME())
? MINUTE({^1998-02-16 10:42a})  && Displays 42
```
