# Função ATCLINE( )

Retorna o número da linha da primeira ocorrência de uma expressão de caracteres ou campo memo dentro de outra expressão de caracteres ou campo memo, sem considerar maiúsculas ou minúsculas dos caracteres em qualquer uma das expressões.

```foxpro
ATCLINE(cSearchExpression, cExpressionSearched)
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caracteres que ATCLINE( ) procura em cExpressionSearched.
**cExpressionSearched**
Especifica a expressão de caracteres em que cSearchExpression procura. Tanto cSearchExpression quanto cExpressionSearched podem ser campos memo de qualquer tamanho. Use MLINE( ) para retornar a linha que contém a expressão de caracteres correspondente. Dica ATCLINE() oferece uma maneira conveniente de pesquisar campos memo.

# Valor de retorno

Numeric

# Observações

Se a pesquisa for bem-sucedida, ATCLINE( ) retorna o número da linha que contém a primeira expressão de caracteres. Se a pesquisa não for bem-sucedida, ATCLINE( ) retorna 0.

O número da linha que ATCLINE( ) retorna é determinado pelo valor de SET MEMOWIDTH, mesmo se cExpressionSearched não for um campo memo. Para obter mais informações, consulte SET MEMOWIDTH Command.

Use ATLINE( ) para realizar uma pesquisa que diferencia maiúsculas de minúsculas.

# Exemplo

O Exemplo 1 localiza a primeira vez que uma cadeia de caracteres ocorre em um campo memo, exibe o primeiro e o último nomes do funcionário e a linha do memo que contém a cadeia de caracteres.

O Exemplo 2 demonstra como a largura do memo afeta ATCLINE( ).

```foxpro
* Example 1
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee  && Open employee table
CLEAR
STORE 'JAPANESE' TO gcFindString  && Case insensitive
LOCATE FOR ATCLINE(gcFindString, notes) != 0
? First_Name
?? Last_Name
? MLINE(notes, ATCLINE(gcFindString, notes))
* Example 2
STORE '1234567890ABCDEFGHIJ' TO gcString
SET MEMOWIDTH TO 20
? ATCLINE('AB', gcString)  && Displays 1
SET MEMOWIDTH TO 10
? ATCLINE('AB', gcString)  && Displays 2
```
