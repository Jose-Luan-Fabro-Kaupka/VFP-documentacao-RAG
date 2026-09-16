# Função LEFT( )

Retorna um número especificado de caracteres de uma expressão de caracteres, começando com o caractere mais à esquerda.

```foxpro
LEFT(cExpression, nExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres da qual LEFT( ) retorna caracteres.
**nExpression**
Especifica o número de caracteres retornados da expressão de caracteres. Se nExpression for maior que o comprimento de cExpression, toda a expressão de caracteres é retornada. Se nExpression for negativo ou 0, LEFT( ) retorna uma cadeia de caracteres vazia. LEFT( ) usa uma posição inicial de 1 e é idêntico a SUBSTR( ).

# Valor de retorno

Character. LEFT( ) retorna uma cadeia de caracteres.

# Exemplo

O exemplo a seguir usa duas maneiras diferentes de exibir o resultado de cadeia de caracteres da função LEFT( ), que retorna as quatro primeiras letras na cadeia de caracteres "Redmond, WA":

```foxpro
? LEFT('Redmond, WA', 4)          && Displays the string, Redm.
myString = LEFT('Redmond, WA', 4) && Stores result in myString.
? myString                        && Displays result in myString.
```

Para obter mais informações, consulte Comando ? | ??.
