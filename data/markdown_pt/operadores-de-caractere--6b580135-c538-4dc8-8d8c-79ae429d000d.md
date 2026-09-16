# Operadores de caractere

Você pode unir e comparar dados de caractere usando os operadores de caractere +, - e $. A tabela a seguir lista os operadores de expressão de caractere em ordem de precedência.
 Operadores de caractere
| Operador | Ação | Código |
| --- | --- | --- |
| + | Concatenação. Une duas cadeias de caracteres, uma cadeia de caracteres e um campo, ou uma cadeia de caracteres e uma variável. | ? 'Good ' + 'morning' |
| - | Concatenação. Remove espaços em branco à direita do elemento que precede o operador e então une dois elementos. | ? customer.first - customer.last |
| $ | Comparação. Busca uma expressão de caractere dentro de outra. | ? 'father' $ 'grandfather' ? 'Main' $ customer.address |
