# Função STREXTRACT( )

Recupera uma cadeia de caracteres entre dois delimitadores.

```foxpro
STREXTRACT(cSearchExpression, cBeginDelim [, cEndDelim [, nOccurrence
[, nFlag]]])
```

#### Parâmetros
 **cSearchExpression**
Especifica a cadeia de caracteres a pesquisar.
**cBeginDelim**
Especifica o caractere que delimita o início de cSearchExpression.
**cEndDelim**
Especifica o caractere que delimita o fim de cSearchExpression.
**nOccurrence**
Especifica em qual ocorrência de cBeginDelim em cSearchExpression iniciar a extração.
**nFlag**
Especifica o tipo de controles colocados na pesquisa. O número que você especifica em nFlag fornece um valor de bit que determina opções de acordo com a tabela a seguir: Valor de bit (aditivo) Descrição 0 1 Pesquisa sem distinção de maiúsculas e minúsculas 1 2 Delimitador final não obrigatório. Especifica que uma pesquisa que não encontra ocorrência de cEndDelim retorna o conteúdo de cSearchExpression a partir da localização de cBeginDelim. 2 4 Inclui os delimitadores na expressão retornada.

# Retorno

Character ou Varbinary.

 O tipo de dados Result é derivado do tipo de dados do primeiro parâmetro.

# Observações

O padrão é uma pesquisa com distinção de maiúsculas e minúsculas na qual os delimitadores devem ser encontrados (sem valor nFlag).

Se cBeginDelim for uma cadeia de caracteres vazia, a pesquisa é conduzida desde o início de cSearchExpression até a primeira ocorrência de cEndDelim. Se cEndDelim for uma cadeia de caracteres vazia, STREXTRACT( ) retorna uma cadeia de caracteres de nOccurrence de cBeginDelim até o fim de cSearchExpression.

# Exemplo

```foxpro
CLEAR
SET PATH TO (HOME(2) + 'Data\')   &&Set path to the customer table
USE customer && any table
?cursortoxml(0,"x",1,0,2)   && Produce variable "x" that has XML of  first 2 records of table
?x         && show the XML
xmlproc(x,0)      && Parse the XML
PROCEDURE xmlproc(x as String, nLev as Integer)   as void
   LOCAL cTagName, cContents, mterm
   DO WHILE .t.
      cTagName = STREXTRACT(x,"<",">")
      IF LEN(cTagName) = 0   && no tag found
         ??' ',x   && print out raw string as contents
         EXIT
      ENDIF
      IF RIGHT(cTagName,1) = '/'   && like "<region/>"
         cTagName = LEFT(cTagName, LEN(cTagName)-1)
         cContents=""
         mterm = "<"+cTagName+"/>"   && "<region/>"
      ELSE
         mterm = "</"+cTagName+">"   && "</region>"
         cContents = STREXTRACT(x,"<"+cTagName+">", mterm,1,2)
      ENDIF
      ?REPLICATE("  ",nLev),nLev+1,PADR(cTagName,20)
      xmlproc(cContents, nLev+1)
      x = STREXTRACT(x, mterm)   && get the rest of the xml
   ENDDO
```
