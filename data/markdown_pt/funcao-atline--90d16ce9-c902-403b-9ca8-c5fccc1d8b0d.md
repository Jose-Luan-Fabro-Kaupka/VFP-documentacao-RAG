# Função ATLINE( )

Retorna o número da linha da primeira ocorrência de uma expressão de caracteres ou campo memo dentro de outra expressão de caracteres ou campo memo, contando a partir da primeira linha.

```foxpro
ATLINE(cSearchExpression, cExpressionSearched)
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caracteres que o Microsoft Visual FoxPro procura em cExpressionSearched .
**cExpressionSearched**
Especifica a expressão de caracteres que cSearchExpression procura. Tanto cSearchExpression quanto cExpressionSearched podem ser campos memo de qualquer tamanho. Use MLINE( ) para retornar a linha que contém a expressão de caracteres correspondente como uma cadeia de caracteres. Dica ATLINE() oferece uma maneira conveniente de pesquisar campos memo.

# Valor de retorno

Numérico

# Observações

ATLINE( ) pesquisa a segunda expressão de caracteres pela ocorrência da primeira expressão de caracteres. ATLINE( ) realiza uma pesquisa que diferencia maiúsculas de minúsculas. Use ATCLINE( ) para realizar uma pesquisa que não diferencia maiúsculas de minúsculas.

Se a pesquisa for bem-sucedida, ATLINE( ) retorna o número da linha onde a correspondência ocorre. Se a pesquisa não for bem-sucedida, ATLINE( ) retorna 0.

O número da linha que ATLINE( ) retorna é determinado pelo valor de SET MEMOWIDTH, mesmo se cExpressionSearched não for um campo memo. Para mais informações, consulte Comando SET MEMOWIDTH.

# Exemplo

O Exemplo 1 localiza a primeira vez que uma cadeia de caracteres ocorre em um campo memo, exibe o primeiro e o último nome do funcionário e a linha do memo que contém a cadeia de caracteres.

O Exemplo 2 demonstra como a largura do memo afeta ATLINE( ).

```foxpro
* Example 1
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee  && Open employee table
CLEAR
STORE 'Japanese' TO gcFindString  && Case sensitive
LOCATE FOR ATLINE(gcFindString, notes) != 0
? First_Name
?? Last_Name
? MLINE(notes, ATLINE(gcFindString, notes))
* Example 2
STORE '1234567890ABCDEFGHIJ' TO gcString
SET MEMOWIDTH TO 20
? ATLINE('AB', gcString)  && Displays 1
SET MEMOWIDTH TO 10
? ATLINE('AB', gcString)  && Displays 2
```
