# Como: preencher resultados de consulta em um controle de formulário

Se você deseja exibir os resultados da consulta em um formulário, pode usar uma tabela, matriz ou cursor para preencher uma grade, caixa de listagem ou caixa de combinação.

### Para preencher um controle de caixa de listagem ou caixa de combinação com uma tabela ou cursor
- No Form Designer, modifique o formulário que contém o controle que você deseja preencher.
- Defina a propriedade RowSourceType como 3 - SQL Statement .
- Na propriedade RowSource do controle, insira uma instrução SELECT - SQL que inclua uma cláusula INTO TABLE ou INTO CURSOR.

### Para preencher um controle de grade com uma tabela ou cursor
- No Form Designer, modifique o formulário que contém o controle que você deseja preencher.
- No evento Load do formulário, insira uma instrução SELECT - SQL que inclua uma cláusula INTO TABLE ou INTO CURSOR.
- Defina a propriedade RecordSource da grade com o nome da tabela ou cursor criado na Etapa 2.
- Defina a propriedade RecordSourceType da grade como 0 Table (para uma tabela) ou 1 Alias (para um cursor).
