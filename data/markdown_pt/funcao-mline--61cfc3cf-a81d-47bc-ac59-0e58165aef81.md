# Função MLINE( )

Retorna uma linha específica de um campo Memo como uma cadeia de caracteres.

> **Observação:** MLINE( ) é principalmente uma função de processamento de texto; portanto, os resultados do processamento de valores binários podem não ser os esperados. Por exemplo, MLINE( ) pode retornar resultados diferentes dependendo da configuração SET MEMOWIDTH. MLINE( ) pode interpretar valores binários como quebras de linha ou truncar valores binários inesperadamente. Recomenda-se usar a função ALINES( ) em vez disso para manipular valores binários.

```foxpro
MLINE(MemoFieldName, nLineNumber [, nNumberOfCharacters])
```

#### Parâmetros
 **MemoFieldName**
Especifica o nome do campo memo do qual MLINE( ) retorna uma linha. Se o campo memo estiver em uma tabela aberta em uma área de trabalho não atual, preceda o nome do campo memo com um ponto e o alias da tabela.
**nLineNumber**
Especifica o número da linha a retornar do campo memo. Se nLineNumber for negativo, 0 ou maior que o número de linhas no campo memo, MLINE( ) retorna uma cadeia de caracteres vazia. MLINE( ) remove quaisquer espaços à direita da linha especificada com nLineNumber .
**nNumberOfCharacters**
Especifica o número de caracteres desde o início do campo memo após os quais MLINE( ) retorna a linha especificada. A variável de sistema _MLINE é normalmente usada para nNumberOfCharacters . _MLINE é ajustada automaticamente cada vez que MLINE( ) é chamada. Em procedimentos recursivos que retornam linhas de campos memo grandes, você pode obter o melhor desempenho incluindo _MLINE como nNumberOfCharacters . Para obter mais informações, consulte Variável de Sistema _MLINE .

# Valor de retorno

Character ou Varbinary. MLINE( ) retorna uma cadeia de caracteres de uma linha específica em um campo Memo. Ao usar MLINE( ) com valores binários, como Varbinary e Blob, o valor de retorno tem o tipo Varbinary.

# Observações

O comprimento e o número das linhas em um campo memo são determinados pelo valor atual de SET MEMOWIDTH (o comprimento de linha padrão é 50 caracteres). Se um retorno de carro for encontrado, nenhum caractere adicional é retornado. A configuração atual de _WRAP determina como a linha do campo memo é exibida.

Ao pesquisar um campo memo por uma cadeia de caracteres, você pode usar ATLINE( ) ou ATCLINE( ) para retornar o número da linha em que a cadeia de caracteres é encontrada. Use esse número de linha em MLINE( ) para retornar o conteúdo da linha do campo memo.

# Exemplo

No exemplo a seguir, dois métodos são usados para retornar linhas de um campo memo. Dois loops usam MLINE( ) para retornar linhas do campo memo. Observe a melhoria de desempenho no segundo loop quando a variável de sistema _MLINE é usada em MLINE( ).

```foxpro
CLEAR
SET TALK OFF
SET MEMOWIDTH TO 50
CLOSE DATABASES
CREATE TABLE tmemo (name c(10), notes m)
APPEND BLANK                  && Add a record
WAIT WINDOW 'Filling memo field - takes several seconds' NOWAIT
*** Fill the memo field  ***
FOR gnOuterLoop = 1 TO 5         && loop 5 times
   FOR gnAlphabet = 65 TO 75   && letters A to H
      REPLACE notes WITH REPLICATE(CHR(gnAlphabet), 10) ;
         + CHR(13) ADDITIVE
   NEXT
NEXT
*** Display all lines from the memo field ***
STORE MEMLINES(notes) TO gnNumLines   && Number of lines in memo field
STORE SECONDS() TO gnBegin      && Beginning time
FOR gnCount = 1 TO gnNumLines   && Loop for # of lines in memo field
   ? MLINE(notes, gnCount)      && Display each line
NEXT
? STR(SECONDS() - gnBegin, 4, 2) + ' seconds'   && Total time
*** Preferable method using _MLINE in MLINE() ***
*** Display all lines from the memo field ***
WAIT 'Press a key to see the preferred method' WINDOW
CLEAR
STORE 0 TO _MLINE             && Reset _MLINE to zero
STORE SECONDS() TO gnBegin      && Beginning time
FOR count = 1 TO gnNumLines      && Loop for # of lines in memo field
   ? MLINE(notes, 1, _MLINE)      && Display each line
NEXT
? STR(SECONDS() - gnBegin, 4, 2) + ' seconds'   && Total time
SET TALK ON
CLOSE DATABASES
ERASE tmemo.dbf
ERASE tmemo.fpt
```
