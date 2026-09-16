# Como: personalizar consultas usando instruções SQL SELECT

Quando você cria uma consulta no Query Designer, o Visual FoxPro na verdade usa uma instrução SQL SELECT para recuperar as informações dos campos nas tabelas. Instruções SQL SELECT oferecem uma forma mais poderosa de manipular sua consulta e fornecem mais controle sobre os resultados da consulta e onde os resultados são armazenados. Para verificar sua consulta ou adicionar comentários, você pode exibir a instrução SQL SELECT na janela SQL e modificá-la para personalizar ainda mais sua consulta.

Quando você adiciona consultas à sua aplicação, pode usar instruções SQL SELECT para combinar uma variedade de fontes de dados, filtrar registros com mais precisão, manipular dados e classificar os resultados. Você pode usar instruções SQL SELECT com consultas criadas no Query Designer, views no View Designer ou em código para um evento ou procedure em um arquivo de programa (.prg). Para mais informações sobre onde você pode usar instruções SQL SELECT e o comando SQL SELECT, consulte Como: criar consultas (Visual FoxPro) e SELECT - SQL Command.

# Visualizando instruções SQL SELECT criadas por consultas

Você pode visualizar a instrução SQL que sua consulta constrói na janela SQL a qualquer momento enquanto cria sua consulta. Ao visualizar a instrução SQL criada pelo Query Designer, você pode verificar se a consulta está definida corretamente.

### Para visualizar a instrução SQL SELECT criada por uma consulta
- Crie sua consulta usando o Query Designer.
- No menu Query, escolha View SQL .

A janela SQL abre para exibir a instrução SQL SELECT que sua consulta criou. A primeira instrução é a instrução SQL SELECT. Por exemplo, você pode selecionar todos os registros da tabela `Customer` no banco de dados `TasTrade` onde o campo `country` contém o valor "Canada":

```foxpro
SELECT *;
   FROM tastrade!customer;
   WHERE Customer.country = Canada
```

O script para a instrução SQL SELECT que aparece na janela SQL é gerado automaticamente ao carregar ou modificar uma consulta no Query Designer.

Para executar a instrução SQL SELECT imediatamente, insira a instrução na janela Command. Se você quiser que cada cláusula apareça em uma linha separada na janela, termine cada linha, exceto a última, com ponto e vírgula (;) para que o Visual FoxPro processe o comando somente após a última linha.

Para incluir a instrução SELECT no código, copie a instrução SQL SELECT em um arquivo .prg.

# Editando instruções SQL SELECT na janela SQL

Na janela SQL, você pode editar a instrução SQL SELECT da consulta.

> **Observação:** O Query Designer analisa apenas a primeira instrução SQL SELECT na janela SQL, as cláusulas diretamente envolvidas com a instrução SELECT e o primeiro comentário que aparece na consulta. O Query Designer ignora todo o outro texto.

### Para editar a instrução SQL SELECT na janela SQL
- Crie ou abra uma consulta.
- Abra a janela SQL e edite a instrução SQL SELECT.

Você pode especificar um asterisco, table.* ou uma lista de campos delimitada por vírgulas para a instrução SELECT na janela SQL. Por exemplo, você pode especificar a instrução SQL como SELECT * FROM ou SELECT field1, field2, ... FROM. Suas preferências são preservadas durante o carregamento ou geração da consulta. Você também pode incluir o mesmo campo várias vezes na lista SELECT.

Para mais informações sobre o uso de sintaxe para o comando SQL SELECT, consulte SELECT - SQL Command.

# Carregando alterações de instrução SQL SELECT no Query Designer

Depois de editar a instrução SQL SELECT na janela SQL, você pode recarregar as alterações no Query Designer.

### Para atualizar a consulta no Query Designer
- Feche a janela SQL.

Você também pode atualizar a consulta clicando no Query Designer para trazê-lo para o primeiro plano.

Se o Query Designer não conseguir recarregar suas alterações depois que você faz alterações na janela View SQL, uma caixa de diálogo aparece e pergunta o seguinte:

"View/Query designer is unable to reload your changes. Would you like to rebuild content from the designer?"

Se você selecionar Yes, suas alterações são descartadas na janela SQL e o Visual FoxPro retorna você ao Query Designer. Se você selecionar No, o Visual FoxPro retorna você à janela SQL.

Para salvar uma instrução que não pode ser analisada, como uma chamada a uma stored procedure, selecione No e clique no botão Save na barra de ferramentas. O Visual FoxPro salva a consulta. Você também pode clicar no botão Save depois de inserir o comando na janela SQL para salvar a consulta. Você não precisa clicar na janela Query Designer, o que faz o Query Designer tentar carregar e analisar a consulta.
