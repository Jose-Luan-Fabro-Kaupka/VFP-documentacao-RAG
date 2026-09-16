# Expressões regulares e operadores

Expressões regulares são conjuntos de símbolos que você pode usar para criar pesquisas para encontrar e substituir padrões de texto. Expressões regulares fornecem uma forma concisa e flexível de especificar critérios de pesquisa e filtro mais complexos contra uma seleção de texto do que a pesquisa por padrão de caractere curinga disponível na caixa de diálogo Find.

A tabela a seguir descreve o comportamento dos operadores de expressão regular em uma consulta.

| Operador | Comportamento |
| --- | --- |
| . | Corresponde a qualquer caractere único, exceto o caractere de nova linha (\n). |
| * | Corresponde ao caractere precedente zero ou mais vezes. Você também pode usar um ponto de interrogação (?). Exemplo "zo*" corresponde a "z" ou "zoo". A expressão "a?ve?" corresponde a "ve" em "never". |
| + | Corresponde ao caractere precedente uma ou mais vezes. Exemplo "zo+" corresponde a "zoo", mas não a "z". |
| ^ | Corresponde ao início da cadeia de entrada. |
| $ | Corresponde ao final da cadeia de entrada. |
| [ xyz ] | Corresponde a qualquer caractere no conjunto. Os colchetes de abertura e fechamento são obrigatórios. Exemplo "[abc]" corresponde ao "a" em "plain". |
| [^ xyz ] | Corresponde a qualquer caractere que não esteja no conjunto. Os colchetes de abertura e fechamento são obrigatórios. Exemplo "[^abc]" corresponde ao "p" em "plain". |
| [ a - z ] | Corresponde a qualquer caractere no intervalo especificado. Exemplo "[a-z]" corresponde a qualquer caractere alfabético minúsculo no intervalo de "a" a "z". |
| [^ a - z ] | Corresponde a qualquer caractere que não esteja no intervalo especificado. Exemplo "[^m-z]" corresponde a qualquer caractere que não esteja no intervalo de "m" a "z". |
| \ | Marca o próximo caractere como caractere especial, como caractere de escape, ou como literal. Exemplo "\\" corresponde a "\", e "\(" corresponde a "(". |
| ( pattern ) | Corresponde a um grupo de padrão. Os parênteses de abertura e fechamento são obrigatórios. Exemplo "(tress)" corresponde a "mattress", mas não a "mattres". Para corresponder a caracteres de parênteses, use "\(" ou "\)". |
| x | y | Corresponde a x ou y . Exemplo "z|wood" corresponde a "z" ou "wood". A expressão "(z|w)ood" corresponde a "zood" ou "wood". |
| { m } | Corresponde ao caractere precedente exatamente m vezes, onde m é não negativo. As chaves de abertura e fechamento são obrigatórias. Exemplo "o{2}" não corresponde ao "o" em "Bob", mas corresponde aos dois primeiros o's em "food" ou "foooood". |
| { m ,} | Corresponde ao caractere precedente pelo menos m vezes, onde m é não negativo. Exemplo "o{2,}" não corresponde ao "o" em "Bob", mas corresponde a todos os o's em "fooooood". Além disso, a expressão "o{1,}" é equivalente a "o+", e "o{0,}" é equivalente a "o*". |
| { m , n } | Corresponde ao caractere precedente pelo menos m e no máximo n vezes, onde m e n são não negativos. Exemplo "o{1,3}" corresponde aos três primeiros o's em "foooooood". Além disso, a expressão "o{0,1}" é equivalente a "o?". |
| Todo o resto | Corresponde a si mesmo. |

As regras a seguir se aplicam quando você usa operadores de expressão regular:
 - Você pode colocar expressões regulares entre aspas correspondentes (" "). Você deve colocar expressões regulares entre aspas se a expressão contiver um espaço ou um parêntese de fechamento ()).

A classe Foundation Regular Expressions fornece acesso a rotinas para usar expressões regulares em seus aplicativos. Para obter mais informações, consulte Regular Expressions Foundation Class.

O Visual FoxPro fornece um exemplo de expressões regulares que você pode usar para determinar como incorporar pesquisa de texto com expressões regulares em seu aplicativo. Para obter mais informações, consulte Search Text Using Regular Expressions Sample.

Você pode consultar a MSDN para detalhes gerais sobre expressões regulares e correspondência de propriedades de padrão.
