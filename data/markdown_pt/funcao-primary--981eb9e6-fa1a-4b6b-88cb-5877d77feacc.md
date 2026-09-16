# Função PRIMARY( )

Retorna true (.T.) se uma tag de índice é uma tag de índice primário; caso contrário, retorna false (.F.).

```foxpro
PRIMARY([nIndexNumber] [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
Especifica o número da tag de índice para a qual PRIMARY( ) retorna o status primário. PRIMARY( ) retorna o status primário na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de tags de índice compostas estruturais e compostas independentes.
 - Status primário de cada tag no índice composto estrutural (se houver) é retornado primeiro. O status primário é retornado para as tags na ordem em que as tags são criadas no índice estrutural.
- Status primário de cada tag em quaisquer índices compostos independentes abertos é retornado em seguida. O status primário é retornado para as tags na ordem em que as tags são criadas nos índices compostos independentes. Se você omitir nIndexNumber, PRIMARY( ) verifica a tag de índice mestre controladora para ver se é uma tag de índice primário. Se não houver tag de índice mestre controladora, PRIMARY( ) retorna false (.F.).
 **nWorkArea**
Especifica a área de trabalho da tag de índice especificada com nIndexNumber.
**cTableAlias**
Especifica a área de trabalho da tag de índice especificada com nIndexNumber. Se você omitir nWorkArea e cTableAlias, PRIMARY( ) verifica a tag de índice na área de trabalho atualmente selecionada para ver se é uma tag de índice primário.

# Valor de retorno

Logical

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados. FOR ... ENDFOR é usado para criar um loop no qual o status primário de cada tag de índice no índice estrutural de `customer` é verificado. O nome de cada tag de índice estrutural é exibido com seu status primário.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'Data\')   && Sets path to database
OPEN DATABASE testdata  && Open testdata database
USE Customer     && Open customer table
FOR nCount = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(nCount))  && Checks for tags in the
   ? TAG(nCount)  && Display tag name
   ? PRIMARY(nCount)     && Display primary status
   ELSE
      EXIT  && Exit the loop when no more tags are found
   ENDIF
ENDFOR
```
