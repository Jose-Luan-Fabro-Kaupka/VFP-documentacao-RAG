# Passar dados para parâmetros em outras linguagens de programação

Você pode comparar como a passagem de dados difere entre o Visual FoxPro e outras linguagens.

A tabela a seguir compara a passagem de dados para parâmetros por referência entre o Visual FoxPro e outras linguagens.

| Visual FoxPro | BASIC |
| --- | --- |
| =ABC(@X) –OR– DO ABC WITH X | ABC X |

| Pascal | C/C++ |
| --- | --- |
| procedure ABC var x:integer); | ABC(&VAR); |

A tabela a seguir compara a passagem de dados para parâmetros por valor entre o Visual FoxPro e outras linguagens.

| Visual FoxPro | BASIC |
| --- | --- |
| =ABC(X) | ABC ByVal X |

| Pascal | C/C++ |
| --- | --- |
| procedure ABC (x:integer); | ABC(X); |
