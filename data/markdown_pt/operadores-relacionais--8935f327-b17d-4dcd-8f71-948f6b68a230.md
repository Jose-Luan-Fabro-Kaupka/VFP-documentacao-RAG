# Operadores relacionais

Operadores relacionais funcionam com todos os tipos de dados e retornam um valor lógico. A tabela a seguir lista os operadores relacionais.
 Operadores relacionais
| Operador | Ação | Código |
| --- | --- | --- |
| < | Menor que | ? 23 < 54 |
| > | Maior que | ? 1 > 2 |
| = | Igual a | ? cVar1 = cVar |
| <>, #, != | Diferente de | ? .T. <> .F. |
| <= | Menor ou igual a | ? {^1998/02/16} <= {^1998/02/16} |
| >= | Maior ou igual a | ? 32 >= nHisAge |
| == | Comparação de cadeia de caracteres | ? status == "Open" |

O operador == pode ser usado quando uma comparação exata de cadeias de caracteres é necessária. Se duas expressões de caracteres são comparadas com o operador ==, as expressões em ambos os lados do operador == devem conter exatamente os mesmos caracteres, incluindo espaços em branco, para serem consideradas iguais. A configuração SET EXACT é ignorada quando cadeias de caracteres são comparadas usando ==. Consulte SET EXACT para obter mais informações sobre o uso do operador == para comparar cadeias de caracteres.

Você também pode usar o operador igual a (=) para determinar se duas referências de objeto referem-se ao mesmo objeto. O exemplo a seguir demonstra um uso simples:

```foxpro
CLEAR ALL
X = CREATEOBJECT('Form')
Y = CREATEOBJECT('Form')
? X = Y  && Displays false (.F.)
Z = X
? X = Z  && Displays true (.T.)
```
