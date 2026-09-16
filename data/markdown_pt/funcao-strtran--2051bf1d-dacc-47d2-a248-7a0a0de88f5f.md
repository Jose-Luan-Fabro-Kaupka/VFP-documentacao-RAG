# Função STRTRAN( )

Pesquisa uma expressão de caracteres ou campo de memo em busca de uma segunda expressão de caracteres ou campo de memo e substitui cada ocorrência por uma terceira expressão ou campo. Você pode especificar onde a substituição começa e quantas substituições serão feitas.

```foxpro
STRTRAN(cSearched, cExpressionSought [, cReplacement
   [, nStartOccurrence [, nNumberOfOccurrences [, nFlags]]]])
```

#### Parâmetros
 **cSearched**
Especifica a expressão de caracteres na qual pesquisar. cSearched pode ser um campo de memo, campo blob ou expressão varbinary.
**cExpressionSought**
Especifica a expressão a pesquisar em cSearched. A pesquisa diferencia maiúsculas de minúsculas. cExpressionSought pode ser um campo de memo, campo blob ou expressão varbinary.
**cReplacement**
Especifica a expressão que substituirá cada ocorrência de cExpressionSought em cSearched. Se for omitido, cada ocorrência será substituída por uma cadeia vazia. cReplacement também pode ser um campo de memo, campo blob ou expressão varbinary.
**nStartOccurrence**
Especifica qual ocorrência de cExpressionSought será substituída primeiro. Por exemplo, se nStartOccurrence for 4, a substituição começará na quarta ocorrência e as três primeiras permanecerão inalteradas. Se omitido, o padrão será a primeira ocorrência.
**nNumberOfOccurrences**
Especifica o número de ocorrências a substituir. Se omitido, todas as ocorrências a partir daquela indicada por nStartOccurrence serão substituídas.

> **Observação:** Para especificar somente nFlags junto com os parâmetros obrigatórios, informe uma cadeia vazia em cReplacement e –1 nos parâmetros numéricos opcionais que devem ser ignorados.
 **nFlags**
Especifica a diferenciação entre maiúsculas e minúsculas: 0 — pesquisa diferencia maiúsculas e minúsculas, e a substituição usa o texto exato de cReplacement (padrão; –1 também seleciona esse comportamento); 1 — pesquisa sem diferenciação e substituição exata; 2 — pesquisa com diferenciação e a capitalização de cReplacement é alterada para corresponder à cadeia encontrada; 3 — pesquisa sem diferenciação e a capitalização de cReplacement é alterada para corresponder à cadeia encontrada. A capitalização só muda quando a cadeia encontrada está toda em maiúsculas, toda em minúsculas ou com iniciais maiúsculas.

# Valor de retorno

Character ou Varbinary.
 STRTRAN( ) retorna a cadeia de caracteres ou varbinary resultante. O tipo de dados do resultado é derivado do tipo do primeiro parâmetro.

# Exemplo

O exemplo armazena "abracadabra" em gcString usando STORE. STRTRAN( ) substitui "a" por "z" e exibe "zbrzczdzbrz" com ?. Em seguida, substitui três ocorrências de "a", começando pela segunda, por "q" e exibe "abrqcqdqbra".

```foxpro
STORE 'abracadabra' TO gcString
? STRTRAN(gcString, 'a', 'z')
? STRTRAN(gcString, 'a', 'q', 2, 3)
```

Exemplo com cadeia varbinary.

```foxpro
? STRTRAN(gcString, 0h61, 0h7A)
? STRTRAN(0h + gcString, 'a', 0h7A)         && This command shows parameters data type variability and returns varbinary string
? STRTRAN(0h1234567890, 0h5678, 0h876543)   && Returns 0h123487654390
```
