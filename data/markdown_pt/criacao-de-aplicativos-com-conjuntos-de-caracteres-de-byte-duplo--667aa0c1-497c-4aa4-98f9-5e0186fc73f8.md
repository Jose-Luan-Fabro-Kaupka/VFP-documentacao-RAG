# Criação de aplicativos com conjuntos de caracteres de byte duplo

O Visual FoxPro suporta conjuntos de caracteres de byte duplo (DBCS) — conjuntos de caracteres que requerem mais de um byte para representar um caractere. Alguns exemplos de idiomas que requerem um conjunto de caracteres de byte duplo são chinês simplificado, chinês tradicional e coreano.

O suporte a DBCS do Visual FoxPro permite que você crie aplicativos internacionais. Por exemplo, você pode criar um aplicativo coreano com uma versão dos EUA do Visual FoxPro se estiver executando a versão coreana do Windows. As funções DBCS do Visual FoxPro operam corretamente no conjunto de caracteres coreano e a sequência de ordenação coreana é suportada.

> **Observação:** O Visual FoxPro fornece funções de programação especiais para uso com cadeias de caracteres em ambientes DBCS.

# Usando caracteres DBCS ao nomear objetos

O Visual FoxPro permite que você use caracteres DBCS ao nomear elementos de seus aplicativos. Como no Visual FoxPro em geral, os elementos podem:
 - Ter até 254 bytes de comprimento com a combinação de caracteres de byte duplo e caracteres simples. Por exemplo, se você usar apenas caracteres de byte duplo, o nome que está criando pode ter somente 127 caracteres.
- Começar com uma letra, número, sublinhado ou combinação de byte inicial-final.
- Contener apenas letras, números, sublinhados ou caracteres DBCS.

Essas regras se aplicam a variáveis, objetos (janelas, menus e assim por diante), nomes de funções e procedimentos, nomes de classes e subclasses, aliases e constantes. Você também pode usar caracteres de byte duplo para nomes de arquivo. Para evitar a possibilidade de que caracteres no nome do arquivo sejam inadvertidamente tratados como delimitadores, é mais seguro sempre colocar o nome do arquivo entre aspas.

> **Observação:** Os limites de comprimento do Visual FoxPro são expressos usando caracteres de byte simples. Usar caracteres de byte duplo em nomes de campo, expressões de índice, nomes de variáveis, nomes de janelas e assim por diante efetivamente reduz o comprimento do nome. Por exemplo, um nome de campo pode ter até 10 bytes em uma tabela livre, então um nome de campo pode consistir em 10 caracteres de byte simples, mas apenas 5 caracteres de byte duplo. Para obter mais informações sobre capacidades do sistema do Visual FoxPro, consulte System Capacities .

# Ordenando dados DBCS

Para ajudá-lo a ordenar informações em ambientes DBCS, o Visual FoxPro suporta sequências de ordenação para chinês simplificado, chinês tradicional, japonês e coreano. Sequências de ordenação permitem que você ordene corretamente campos de caractere em tabelas para cada idioma.

A tabela a seguir lista as opções de sequência de ordenação do Visual FoxPro e o idioma correspondente.

| Opções | Idioma |
| --- | --- |
| JAPANESE | Japonês |
| KOREAN | Coreano |
| PINYIN | Chinês simplificado |
| STROKE | Chinês simplificado e tradicional |

Para obter mais informações, consulte How to: Specify a Sort Order.
