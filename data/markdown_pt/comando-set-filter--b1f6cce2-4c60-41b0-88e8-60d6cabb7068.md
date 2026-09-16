# Comando SET FILTER

Especifica que os registros na tabela atual devem atender a certas condições para serem acessíveis.

```foxpro
SET FILTER TO [lExpression] [IN nWorkArea | cTableAlias]
```

#### Parâmetros
 **lExpression**
Especifica a condição que os registros devem satisfazer. Se a tabela atual estiver indexada em um campo ou campos especificados em lExpression, a tecnologia Rushmore Query Optimization pode otimizar consultas baseadas no campo ou campos.
**IN nWorkArea | cTableAlias**
Especifica a área de trabalho ou o alias de tabela afetado pelo comando SET FILTER. Use esta cláusula para especificar uma área de trabalho ou uma tabela fora da área de trabalho atual.

# Observações

Você pode definir um filtro separado para cada tabela aberta. Na maioria dos casos, depois de emitir SET FILTER, você pode recuperar apenas os registros na tabela que satisfazem a condição especificada pela expressão lógica lExpression. Quando a cláusula de escopo aplicada referencia registros em termos relativos, todos os comandos que permitem uma cláusula de escopo respeitarão a condição SET FILTER. No entanto, qualquer comando que use um escopo declarado ou implícito de RECORD nRecordNumber, incluindo GOTO, REPLACE e outros, não respeitará o filtro. Esses comandos sempre atuam no registro especificado, se o registro existir. Isso é verdade mesmo se o filtro excluir esse registro. Observe, no entanto, que o comando GOTO TOP/BOTTOM respeita a condição de filtro.

A condição especificada por SET FILTER não é avaliada até que o ponteiro de registro seja movido na tabela.

Quando você emite SET FILTER TO sem usar lExpression, desativará o filtro para a tabela atual.

SELECT – SQL não respeita a condição de filtro atual.

> **Observação:** Quando você usa SET FILTER para filtrar dados em uma grade, use o comando SET KEY para aumentar o desempenho da grade.

Quando você emite um comando SET FILTER, o Visual FoxPro converte internamente a expressão de filtro para um formato preferido. Se sua expressão de filtro original incluir comandos abreviados (por exemplo, UPPE em vez de UPPER), os valores de retorno de SET("FILTER") e FILTER( ) não corresponderão exatamente à sua expressão de filtro original. Você pode usar NORMALIZE( ) com a expressão de filtro. Isso a retornará em um formato que corresponde à saída de SET("FILTER") e FILTER( )."
