# Comando UPDATE

Incluído para compatibilidade com versões anteriores. Use o Comando UPDATE - SQL em vez disso.

Atualiza a tabela aberta na área de trabalho selecionada atualmente com dados de outra tabela aberta em outra área de trabalho.

```foxpro
UPDATE ON field FROM file
	REPLACE field1 WITH expr1
	[, field2 WITH expr2 ...]
	[RANDOM]
```

# Observações

ON field

 Para usar UPDATE, a tabela atual e a tabela da qual você atualiza devem ter um campo comum. field especifica o campo comum que controla a atualização. A tabela atual deve estar indexada ou classificada em ordem ascendente no campo comum. O desempenho da atualização é melhorado se a tabela de atualização também estiver classificada ou indexada.

FROM file

 A tabela aberta na área de trabalho selecionada atualmente é atualizada com dados de uma tabela aberta em outra área de trabalho. Especifique o nome da tabela aberta na outra área de trabalho com file.

REPLACE field1 WITH expr1 ...

 Executar UPDATE substitui um campo (field1) na tabela atual por uma expressão de atualização (expr1). Você pode atualizar mais de um campo na tabela atual incluindo uma lista de campos (field2, field3 e assim por diante) e expressões de atualização correspondentes (expr2, expr3 e assim por diante).

 As expressões de atualização geralmente são os nomes de campos da tabela de atualização. Elas também podem ser expressões gerais ou constantes.

 Observe que para cada registro na tabela atual, pode haver vários registros correspondentes na tabela de atualização. Se houver vários registros correspondentes, o registro na tabela atual é atualizado por cada um dos registros correspondentes. Se a tabela atual contém registros de campo chave idênticos, apenas o primeiro dos registros correspondentes é atualizado.

RANDOM

 Você deve incluir a palavra-chave RANDOM se a tabela de atualização não estiver indexada ou classificada em ordem ascendente.

 Importante Um número incorreto de registros pode ser atualizado se a tabela de atualização não estiver indexada ou classificada em ordem ascendente e RANDOM não for incluído.
