# Comando REPLACE FROM ARRAY

Atualiza dados em campos com valores de uma matriz de variáveis.

```foxpro
REPLACE FROM ARRAY ArrayName [FIELDS FieldList] [Scope]
   [FOR lExpression1] [WHILE lExpression2] [NOOPTIMIZE]
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz cujos valores substituem os dados do campo.
**FIELDS FieldList**
Especifica que apenas os campos em FieldList sejam substituídos pelo conteúdo da matriz. Campos em áreas de trabalho não selecionadas devem ser precedidos pelo alias da tabela.
**Scope**
Especifica um intervalo de registros a serem substituídos pelo conteúdo da matriz. O escopo padrão para REPLACE FROM ARRAY é o registro atual (NEXT 1). Apenas os registros que estão dentro do intervalo são substituídos. A substituição ocorre até o final do escopo ou o final da matriz. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber e REST. Para obter mais informações sobre cláusulas de escopo, consulte Cláusulas de escopo .
**FOR lExpression1**
Especifica que os campos sejam substituídos apenas em registros para os quais lExpression1 avalia como true (.T.). Incluir FOR permite substituir registros condicionalmente, filtrando aqueles que você não deseja. A substituição ocorre em cada registro para o qual lExpression1 é true (.T.), ou até o final da matriz. Rushmore Query Optimization otimiza REPLACE FROM ARRAY FOR se lExpression1 for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte Comando SET OPTIMIZE e Usando Rushmore Query Optimization para acelerar o acesso a dados .
**WHILE lExpression2**
Especifica uma condição pela qual os campos em registros são substituídos pelo conteúdo da matriz enquanto a expressão lógica lExpression2 avalia como true (.T.).
**NOOPTIMIZE**
Impede a otimização Rushmore. Para obter mais informações, consulte Comando SET OPTIMIZE e Usando Rushmore Query Optimization para acelerar o acesso a dados .

# Observações

Campos memo e general são ignorados em REPLACE FROM ARRAY. Para importar dados para esses campos, use GATHER e APPEND GENERAL.

Começando com o primeiro elemento, os elementos da matriz substituem os campos correspondentes do registro. O primeiro elemento da matriz substitui o primeiro campo do registro, o segundo elemento da matriz substitui o segundo campo e assim por diante.

Se a matriz tiver menos elementos do que a tabela tem campos, os campos adicionais são ignorados. Se a matriz tiver mais elementos do que a tabela tem campos, os elementos adicionais da matriz são ignorados.

> **Observação:** Nenhuma substituição ocorre se o ponteiro de registro estiver no final do arquivo na área de trabalho atual e você especificar um campo em outra área de trabalho.
