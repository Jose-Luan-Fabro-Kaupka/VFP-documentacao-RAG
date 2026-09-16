# Comparação de cadeias de caracteres e valores no Visual FoxPro

O Visual FoxPro possui dois operadores relacionais que testam igualdade: o operador de sinal de igual (=) e o operador de sinal de igual duplo (==). Você pode usar o operador = para realizar uma comparação entre dois valores do mesmo tipo e ele é adequado para comparar dados dos tipos Character, Numeric, Date e Logical. No entanto, ao comparar expressões de caractere com o operador =, os resultados podem não ser exatamente os esperados.

As expressões de caractere são comparadas caractere por caractere da esquerda para a direita até que uma das expressões não seja igual à outra ou até o final da expressão à direita do operador = ser atingido, conforme especificado pela configuração do comando SET EXACT como OFF, ou até os finais de ambas as expressões serem atingidos, conforme especificado pela configuração do comando SET EXACT como ON.

Você pode usar o operador == para realizar uma comparação exata de dados de caractere ou binários. Se você comparar duas expressões de caractere ou binárias usando o operador ==, as expressões em ambos os lados do operador == devem conter precisamente os mesmos caracteres ou bytes, incluindo espaços ou bytes zero (0), respectivamente, para serem consideradas iguais. A configuração SET EXACT é ignorada quando cadeias de caracteres ou expressões binárias são comparadas usando o operador ==. Para obter mais informações, consulte Operadores relacionais.

A tabela a seguir mostra como a escolha do operador e a configuração SET EXACT afetam as comparações.

> **Observação:** Um sublinhado representa um espaço em branco.

| Comparação | = com SET EXACT OFF | = com SET EXACT ON | == com SET EXACT ON ou OFF |
| --- | --- | --- | --- |
| "abc" = "abc" | Correspondência | Correspondência | Correspondência |
| "ab" = "abc" | Sem correspondência | Sem correspondência | Sem correspondência |
| "abc" = "ab" | Correspondência | Sem correspondência | Sem correspondência |
| "abc" = "ab_" | Sem correspondência | Sem correspondência | Sem correspondência |
| "ab" = "ab_" | Sem correspondência | Correspondência | Sem correspondência |
| "ab_" = "ab" | Correspondência | Correspondência | Sem correspondência |
| "" = "ab" | Sem correspondência | Sem correspondência | Sem correspondência |
| "ab" = "" | Correspondência | Sem correspondência | Sem correspondência |
| "__" = "" | Correspondência | Correspondência | Sem correspondência |
| "" = "___" | Sem correspondência | Correspondência | Sem correspondência |
| TRIM("___") = "" | Correspondência | Correspondência | Correspondência |
| "" = TRIM("___") | Correspondência | Correspondência | Correspondência |

Ao trabalhar com instruções SQL como o comando SELECT - SQL, a configuração SET ANSI pode afetar os resultados se você usar o operador =.
