# Função LIKE( )

Determina se uma expressão de caracteres corresponde a outra expressão de caracteres.

```foxpro
LIKE(cExpression1, cExpression2)
```

#### Parâmetros
 **cExpression1**
Especifica a expressão de caracteres que LIKE( ) compara com cExpression2 . cExpression1 pode conter curingas como * e ?. O ponto de interrogação (?) corresponde a qualquer caractere único em cExpression2 e o asterisco (*) corresponde a qualquer número de caracteres. Você pode misturar qualquer número de curingas em qualquer combinação em cExpression1 .
**cExpression2**
Especifica a expressão de caracteres que LIKE( ) compara com cExpression1 . cExpression2 deve corresponder a cExpression1 letra por letra para que LIKE( ) retorne true (.T.).

# Valor de retorno

Lógico

# Observações

LIKE( ) retorna true (.T.) se cExpression1 corresponder a cExpression2; caso contrário, retorna false (.F.).

SET COMPATIBLE determina como LIKE( ) avalia cExpression1 e cExpression2. Se SET COMPATIBLE estiver definido como ON ou DB4, cExpression1 e cExpression2 têm todos os espaços em branco à direita removidos antes de serem comparados. Se SET COMPATIBLE estiver definido como OFF ou FOXPLUS, quaisquer espaços em branco à direita em cExpression1 e cExpression2 são usados na comparação.

# Exemplo

No exemplo a seguir, todos os nomes de produtos na tabela `products` com as duas primeiras letras "Ch" são exibidos.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE products  && Open Products table
CLEAR
? 'All product names with first two letters Ch:'
?
SCAN FOR LIKE('Ch*', prod_name)
   ? prod_name
ENDSCAN
USE
```
