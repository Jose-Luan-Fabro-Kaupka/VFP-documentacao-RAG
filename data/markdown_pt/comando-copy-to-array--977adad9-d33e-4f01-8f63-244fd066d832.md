# Comando COPY TO ARRAY

Copia dados da tabela atualmente selecionada para uma matriz.

```foxpro
COPY TO ARRAY ArrayName
   [FIELDS FieldList | FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton]
   [Scope] [FOR lExpression1] [WHILE lExpression2] [NOOPTIMIZE]
```

#### Parâmetros
 **ArrayName**
Especifica a matriz para a qual os dados da tabela são copiados.
**FIELDS FieldList**
Especifica que apenas os campos especificados em FieldList são copiados para a matriz. Se você omitir FIELDS FieldList, todos os campos são copiados para a matriz se a matriz tiver colunas suficientes.
**FIELDS LIKE Skeleton**
Especifica que os campos que correspondem ao esqueleto de campo Skeleton são copiados para a matriz.
**FIELDS EXCEPT Skeleton**
Especifica que todos os campos, exceto os que correspondem ao esqueleto de campo Skeleton, são copiados para a matriz.
**Scope**
Especifica um intervalo de registros copiados para a matriz. Apenas os registros dentro do intervalo são copiados. As cláusulas de escopo são: ALL, NEXT nRecords, RECORD nRecordNumber e REST. Para obter mais informações sobre cláusulas de escopo, consulte o tópico online Cláusulas de escopo.
**FOR lExpression1**
Especifica que apenas os registros que satisfazem a condição lógica lExpression1 são copiados para a matriz. Para copiar registros condicionalmente para a matriz, inclua a cláusula FOR para filtrar registros indesejados.
**WHILE lExpression2**
Especifica uma condição em que os registros são copiados para a matriz enquanto a expressão lógica lExpression2 é avaliada como True (.T.).
**NOOPTIMIZE**
Desabilita a otimização de consulta Rushmore de COPY TO ARRAY. Para obter mais informações, consulte Comando SET OPTIMIZE e Usar otimização de consulta Rushmore para acelerar o acesso a dados.

# Observações

Rushmore otimiza uma consulta COPY TO ARRAY que inclui FOR lExpression1 se lExpression1 for uma expressão otimizável. Para obter o melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter informações sobre expressões otimizáveis pelo Rushmore, consulte Comando SET OPTIMIZE e Usar otimização de consulta Rushmore para acelerar o acesso a dados.

COPY TO ARRAY e SCATTER são semelhantes. COPY TO ARRAY copia vários registros para uma matriz, enquanto SCATTER copia apenas um registro para uma matriz ou um conjunto de variáveis de memória. Tanto COPY TO ARRAY quanto SCATTER criam uma nova matriz se não existir uma matriz com o nome especificado.

Para copiar um único registro para uma matriz, você pode especificar uma matriz unidimensional. A matriz unidimensional especificada deve ter o mesmo número de elementos que campos na tabela, não contando campos memo. Campos Memo e Blob são ignorados em COPY TO ARRAY.

Se você especificar uma matriz unidimensional, o primeiro campo de um registro é armazenado no primeiro elemento da matriz, o segundo campo é armazenado no segundo elemento da matriz, e assim por diante. Se a matriz unidimensional tiver mais elementos que a tabela tem campos, os elementos restantes permanecem inalterados. Se a matriz tiver menos elementos que a tabela tem campos, os campos restantes são ignorados.

Para copiar vários registros ou uma tabela inteira para uma matriz, especifique uma matriz bidimensional. O número de linhas na matriz é o número de registros que a matriz pode armazenar, e o número de colunas na matriz é o número de campos que a matriz pode armazenar.

Cada registro é armazenado em uma linha da matriz, e cada campo do registro é armazenado em uma coluna da matriz. Para cada registro, o primeiro campo é armazenado na primeira coluna da matriz, o segundo campo é armazenado na segunda coluna da matriz, e assim por diante. Se a matriz tiver mais colunas que a tabela tem campos, as colunas restantes não são alteradas. Se a matriz tiver menos colunas que a tabela tem campos, os campos restantes não são armazenados na matriz.

Cada linha sucessiva na matriz é preenchida com o conteúdo do próximo registro na tabela. Se a matriz tiver mais linhas que a tabela tem registros, as linhas restantes não são alteradas. Se a matriz tiver menos linhas que a tabela tem registros, os registros restantes não são armazenados na matriz.

Dados podem ser copiados de matrizes para novos registros de tabela com APPEND FROM ARRAY. Dados também podem ser copiados de uma matriz ou de um conjunto de variáveis de memória para registros em uma tabela com GATHER.

O esqueleto de campo Skeleton suporta curingas. Por exemplo, para especificar que todos os campos que começam com as letras A e P são copiados para a matriz, use o seguinte:

```foxpro
COPY TO ARRAY aMyArray FIELDS LIKE A*,P*
```

A cláusula LIKE pode ser combinada com a cláusula EXCEPT:

```foxpro
COPY TO ARRAY aMyArray FIELDS LIKE A*,P* EXCEPT PARTNO*
```

Ativar o autoincremento não tem efeito no comando COPY TO ARRAY. Apenas os valores dos registros são copiados para a matriz.

# Exemplo

No exemplo a seguir, a tabela `Customer` é aberta. Uma matriz bidimensional é então criada e os três primeiros registros de `Customer` são copiados para a matriz. DISPLAY MEMORY mostra os dados armazenados na matriz.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer  && Opens Customer table.
DIMENSION gaTemp(3,10)
COPY NEXT 3 TO ARRAY gaTemp
DISPLAY MEMORY LIKE gaTemp
```
