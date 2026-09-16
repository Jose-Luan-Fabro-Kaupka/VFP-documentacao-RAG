# Função ASCAN( )

Pesquisa um array por um elemento que contém os mesmos dados e tipo de dados que uma expressão.

```foxpro
ASCAN(ArrayName, eExpression [, nStartElement [, nElementsSearched [, nSearchColumn [, nFlags ]]]])
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array a pesquisar.
**eExpression**
Especifica a expressão geral a pesquisar.
**nStartElement**
Especifica o número do elemento no qual a pesquisa começa. O número do elemento que você especifica é incluído na pesquisa. Se você omitir nStartElement ou passar um valor negativo em seu lugar, todo o array é pesquisado por padrão.
**nElementsSearched**
Especifica o número de elementos que são pesquisados. Se você omitir nStartElement e nElementsSearched ou passar um valor negativo em seu lugar, a pesquisa começa com o primeiro elemento do array e continua até o último elemento do array se você não especificar nSearchColumn. Observação Você pode referenciar um elemento em um array variável bidimensional de uma de duas maneiras. O primeiro método usa dois subscritos para especificar a posição de linha e coluna do elemento no array; o outro método usa um número de elemento. Esta função e outras que manipulam arrays bidimensionais requerem números de elemento (nStartElement e nElementsSearched). Use AELEMENT( ) para retornar o número do elemento a partir de subscritos de linha e coluna em um array bidimensional.
**nSearchColumn**
Especifica a coluna do array a pesquisar. Isso é frequentemente útil em arrays criados por funções como AFIELDS( ). Você pode usar 0 ou um número negativo para nSearchColumn para impor uma pesquisa de todo o array. Se você usar um valor maior que 0 para nSearchColumn, ASCAN( ) trata a coluna especificada como um array unidimensional, usando cada linha de dados como um elemento na pesquisa. Por exemplo, o exemplo a seguir pesquisa apenas o terceiro e quarto elementos da coluna 2 em vez de todo o array. ? ASCAN(abc,"M",3,2,2) O Visual FoxPro gera um erro se nSearchColumn for um número maior que o número de colunas disponíveis. Dicas Se o parâmetro nSearchColumn for usado, os parâmetros nStartElement e nElementsSearched não podem ser omitidos. Use –1 como valor de substituição. ? ASCAN(abc,"HELLO",-1,-1,2,15) && Search the whole column 2 of two-dimensional array
 **nFlags**
Especifica critérios de pesquisa adicionais a aplicar à função de varredura. Varreduras padrão diferenciam maiúsculas de minúsculas. O número que você especifica em nFlags fornece um valor de bit que determina a configuração de diferenciação de maiúsculas/minúsculas ou exatidão de uma varredura conforme a tabela a seguir: NFlag Bit Descrição 0 0000 Comportamento existente no Visual FoxPro 6 ou anterior 1 0001 Sem diferenciação de maiúsculas/minúsculas 2 0010 Comportamento atual existente na versão anterior do Visual FoxPro 3 0011 Sem diferenciação de maiúsculas/minúsculas 4 0100 Exact OFF 5 0101 Sem diferenciação de maiúsculas/minúsculas; Exact OFF 6 0110 Exact ON 7 0111 Sem diferenciação de maiúsculas/minúsculas; Exact ON 8 1000 Retornar número da linha 9 1001 Sem diferenciação de maiúsculas/minúsculas; retornar número da linha 10 1010 Retornar número da linha 11 1011 Sem diferenciação de maiúsculas/minúsculas; retornar número da linha 12 1100 Retornar número da linha; Exact OFF 13 1101 Sem diferenciação de maiúsculas/minúsculas; Retornar número da linha; Exact OFF 14 1110 Retornar número da linha; Exact ON 15 1111 Sem diferenciação de maiúsculas/minúsculas; Retornar número da linha; Exact ON

Os valores de bit são os seguintes:

| Bit | Descrição |
| --- | --- |
| 0 | Bit de sem diferenciação de maiúsculas/minúsculas |
| 1 | Bit Exactness ON (efetivo somente se o bit 2 estiver definido) |
| 2 | Bit de substituição da configuração Exact do sistema |
| 3 | Retornar número da linha se array 2D |

nFlags aplica-se somente à função ASCAN( ) e não afeta as configurações de SET EXACT.

# Valor de retorno

Numeric

# Observações

Se uma correspondência for encontrada, ASCAN( ) retorna o número do elemento que contém a expressão. Se uma correspondência não puder ser encontrada, ASCAN( ) retorna 0.

Os critérios para uma correspondência bem-sucedida de dados de caracteres são determinados pela configuração do SET EXACT do sistema se nFlag com bit 2 não estiver definido. Se SET EXACT estiver ON, um elemento deve corresponder à expressão de pesquisa caractere por caractere e ter o mesmo comprimento. Se SET EXACT estiver OFF, e um elemento e a expressão de pesquisa corresponderem até o final da expressão ser atingido, a correspondência é bem-sucedida. Para obter mais informações sobre critérios de correspondência para cadeias de caracteres, consulte a tabela de comparação de cadeias de caracteres no tópico Comando SET EXACT.

No Visual FoxPro 6.0, os parâmetros nStartElement e nElementsSearched são opcionais. nStartElement deve ser > 0 enquanto nElementsSearched pode ser qualquer valor. Para acomodar o parâmetro nSearchColumn, você precisará ignorar esses parâmetros passando um valor de -1.

Os parâmetros nStartElement e nElementsSearched assumem significado especial se o valor de nSearchColumn for maior que 0. No Visual FoxPro 6.0, eles são sempre referenciados a todo o array. A partir do Visual FoxPro 7.0, se um nSearchColumn positivo for passado, os valores de nStartElement e nElementsSearched são referenciados ao array unidimensional único representado por nSearchColumn. Por exemplo, o seguinte pesquisaria apenas o terceiro e quarto elementos da coluna 2, e não todo o array:

```foxpro
? ASCAN(abc,"M",3,2,2)
```

# Exemplo

O exemplo a seguir cria e preenche um array com nomes de empresas e usa ASCAN( ) para pesquisar um nome de empresa específico. Se o nome da empresa for encontrado, ele é removido do array.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer     && Open customer table
SELECT company FROM customer ;
   WHERE country = 'UK' ;
   INTO ARRAY gaCompanies
gnCount = _TALLY
gcName = 'Seven Seas Imports'
CLEAR
DISPLAY MEMORY LIKE gaCompanies*
gnPos = ASCAN(gaCompanies, gcName) && Search for company
IF gnPos != 0
   *** Company found, remove it from the array ***
   = ADEL(gaCompanies, gnPos)
   gnCount = gnCount - 1
ENDIF
DISPLAY MEMORY LIKE gaCompanies
```
