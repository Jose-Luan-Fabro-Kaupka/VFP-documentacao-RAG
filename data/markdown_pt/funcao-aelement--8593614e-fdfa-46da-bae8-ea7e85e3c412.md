# Função AELEMENT( )

Retorna o número de um elemento de matriz a partir dos subscritos do elemento.

```foxpro
AELEMENT(ArrayName, nRowSubscript [, nColumnSubscript])
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz cujo número de elemento você deseja retornar.
**nRowSubscript**
Especifica o subscrito de linha. Se a matriz é unidimensional, AELEMENT( ) retorna identicamente nRowSubscript. Se você incluir apenas nRowSubscript e ele for maior que o número de linhas na matriz, o Visual FoxPro gera uma mensagem de erro.
**nColumnSubscript**
Especifica o subscrito de coluna. Se a matriz é bidimensional, inclua tanto nRowSubscript quanto nColumnSubscript.

# Valor de retorno

Numeric

# Observações

Você pode referenciar um elemento em uma matriz bidimensional de duas maneiras. O primeiro método usa dois subscritos para especificar a posição de linha e coluna do elemento na matriz, e o segundo método usa um número de elemento único. AELEMENT( ) retorna o número do elemento quando fornecido com os subscritos de linha e coluna de um elemento.

As funções do Visual FoxPro ADEL( ), ADIR( ), AFIELDS( ), AINS( ), ALEN( ), ASCAN( ), ASORT( ) e ASUBSCRIPT( ) podem manipular matrizes bidimensionais e exigem que os elementos sejam referenciados pelo seu número de elemento. AELEMENT( ) facilita a conversão de subscritos para um número de elemento para uso por essas funções. Os subscritos de linha e coluna correspondentes podem ser retornados de um número de elemento com ASUBSCRIPT( ).

O exemplo a seguir ilustra a criação de uma matriz com duas linhas e três colunas. DISPLAY MEMORY mostra o conteúdo dos elementos da matriz listados em ordem de número de elemento.

```foxpro
DIMENSION gaMyArray(2,3)
DISPLAY MEMORY LIKE gaMyArray
gaMyArray   Pub  A
  ( 1, 1)   L  .F. (element number 1)
  ( 1, 2)   L  .F. (element number 2)
  ( 1, 3)   L  .F. (element number 3)
  ( 2, 1)   L  .F. (element number 4)
  ( 2, 2)   L  .F. (element number 5)
  ( 2, 3)   L  .F. (element number 6)
```

Um elemento pode ser referenciado pelos seus subscritos ou pelo seu número de elemento. Os comandos `STORE 'INVOICE' TO gaMyArray(2, 1)` e `STORE 'INVOICE' TO gaMyArray(4)` armazenam a cadeia de caracteres INVOICE no mesmo elemento de matriz.

Em matrizes unidimensionais, um número de elemento é idêntico ao seu subscrito de linha único. Não é necessário usar AELEMENT( ) com matrizes unidimensionais.
