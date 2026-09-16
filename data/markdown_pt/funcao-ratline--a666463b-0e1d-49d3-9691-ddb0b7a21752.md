# Função RATLINE( )

Retorna o número da linha da última ocorrência de uma expressão de caracteres dentro de outra expressão de caracteres ou campo memo, contando a partir da última linha.

```foxpro
RATLINE(cSearchExpression, cExpressionSearched)
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caracteres que RATLINE( ) procura em cExpressionSearched.
**cExpressionSearched**
Especifica a expressão de caracteres que RATLINE( ) pesquisa. As expressões de caracteres cSearchExpression e cExpressionSearched podem ser campos memo de qualquer tamanho. Use MLINE( ) para retornar a linha que contém cSearchExpression. Dica RATLINE() oferece uma maneira conveniente de pesquisar campos memo.

# Valor de retorno

Numérico

# Observações

RATLINE( ), o inverso da função ATLINE( ), pesquisa uma expressão de caracteres cExpressionSearched, começando com o último caractere em cExpressionSearched, pela ocorrência de cSearchExpression.

Se a pesquisa for bem-sucedida, RATLINE( ) retorna o número da linha onde a correspondência ocorre. Se a pesquisa não for bem-sucedida, RATLINE( ) retorna 0.

A pesquisa realizada por RATLINE( ) diferencia maiúsculas de minúsculas.

> **Cuidado:** O número da linha que RATLINE() retorna é determinado pelo valor de SET MEMOWIDTH, mesmo se cExpressionSearched não for um campo memo. Para obter mais informações, consulte SET MEMOWIDTH.

# Exemplo

No exemplo a seguir, RATLINE( ) retorna o número da linha da última linha no campo memo `notes` que contém a palavra "graduated." MLINE( ) usa esse valor para retornar o conteúdo da linha.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE employee  && Opens Employee table
STORE 'graduated' TO gcString
STORE MLINE(notes, RATLINE(gcString, notes)) TO gnFileLine
? gnFileLine
```
