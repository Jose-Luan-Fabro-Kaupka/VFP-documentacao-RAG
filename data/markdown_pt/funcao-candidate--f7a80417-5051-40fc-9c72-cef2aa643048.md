# Função CANDIDATE( )

Retorna true (.T.) se uma tag de índice for uma tag de índice candidata; caso contrário, retorna false (.F.).

```foxpro
CANDIDATE([nIndexNumber] [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
Especifica o número da tag de índice para a qual CANDIDATE( ) retorna o status de candidato. CANDIDATE( ) retorna o status de candidato na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de tags de índice composto estrutural e composto independente: o status de candidato de cada tag no índice composto estrutural (se houver) é retornado primeiro. O status de candidato é retornado para as tags na ordem em que foram criadas no índice estrutural. O status de candidato de cada tag em quaisquer índices compostos independentes abertos é retornado por último. O status de candidato é retornado para as tags na ordem em que foram criadas nos índices compostos independentes. Se você omitir nIndexNumber, CANDIDATE( ) verifica a tag de índice controladora mestre para ver se é uma tag de índice candidata. Se não houver tag de índice controladora mestre, CANDIDATE( ) retorna false (.F.).
**nWorkArea**
Especifica a área de trabalho da tag de índice especificada com nIndexNumber.
**cTableAlias**
Especifica a área de trabalho da tag de índice especificada com nIndexNumber. Se você omitir nWorkArea e cTableAlias, CANDIDATE( ) verifica a tag de índice na área de trabalho selecionada atualmente para ver se é uma tag de índice candidata.

# Valor de retorno

Logical

# Observações

Uma tag de índice candidata é uma tag de índice que pode se tornar a tag de índice primária porque não contém valores nulos ou duplicados.

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. FOR ... ENDFOR é usado para criar um loop no qual o status de candidato de cada tag de índice no índice estrutural de `customer` é verificado. O nome de cada tag de índice estrutural é exibido com seu status de candidato.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer     && Open customer table
FOR nCount = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(nCount))  && Checks for tags in the index
   ? TAG(nCount)  && Display tag name
   ? CANDIDATE(nCount)  && Display candidate status
   ELSE
      EXIT  && Exit the loop when no more tags are found
   ENDIF
ENDFOR
```
