# Função ASUBSCRIPT( )

Retorna o subscrito de linha ou coluna de um elemento a partir do número do elemento.

```foxpro
ASUBSCRIPT(ArrayName, nElementNumber, nSubscript)
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array.
**nElementNumber**
Especifica o número do elemento.
**nSubscript**
Determina se o subscrito de linha ou coluna é retornado. Se o array é unidimensional, inclua o número do elemento em nElementNumber e 1 em nSubscript. ASUBSCRIPT( ) retorna identicamente nElementNumber. Se o array é bidimensional, inclua tanto o número do elemento nElementNumber quanto um valor de 1 ou 2 em nSubscript. Especificar 1 em nSubscript retorna o subscrito de linha do elemento, e especificar 2 retorna o subscrito de coluna. Para obter mais informações sobre como referenciar elementos em um array, consulte DIMENSION.

# Valor de retorno

Numérico

# Observações

Você pode referenciar elementos em arrays variáveis bidimensionais de duas maneiras. O primeiro método usa dois subscritos para especificar a posição de linha e coluna do elemento no array. O segundo método usa um número de elemento. Use ASUBSCRIPT( ) para obter o subscrito de linha ou coluna de um elemento a partir do número do elemento.

No exemplo a seguir, um array com duas linhas e três colunas é criado. DISPLAY MEMORY mostra o conteúdo dos elementos do array listados na ordem do número do elemento.

```foxpro
DIMENSION gaMyArray(2,3)
DISPLAY MEMORY LIKE gaMyArray
GAMYARRAY  Pub  A
  ( 1, 1)   L  .F. (element number 1)
  ( 1, 2)   L  .F. (element number 2)
  ( 1, 3)   L  .F. (element number 3)
  ( 2, 1)   L  .F. (element number 4)
  ( 2, 2)   L  .F. (element number 5)
  ( 2, 3)   L  .F. (element number 6)
```

Cada um destes comandos armazena a cadeia de caracteres INVOICE no mesmo elemento do array:

```foxpro
STORE 'INVOICE' TO gaMyArray(2, 1)
STORE 'INVOICE' TO gaMyArray(4)
```

Em arrays unidimensionais, o número de um elemento é idêntico ao seu único subscrito de linha. Não é necessário usar ASUBSCRIPT( ) com arrays unidimensionais.
