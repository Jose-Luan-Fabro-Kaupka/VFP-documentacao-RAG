# Como: visualizar e editar instruções SQL para views

Quando você cria uma view no View Designer, o Visual FoxPro constrói uma instrução SQL SELECT para recuperar as informações dos campos nas tabelas. Você pode ver e editar a instrução SQL SELECT que o Visual FoxPro constrói e as propriedades definidas para a view na janela SQL. Quaisquer alterações que você fizer na janela SQL são preservadas durante o carregamento ou a geração da view.

### Para exibir a definição da view
- Abra a view no View Designer.
- No menu Query, clique em View SQL.

A janela SQL da view abre e exibe a instrução SQL SELECT gerada automaticamente para a view e as propriedades da view. Para obter mais informações, consulte SELECT - SQL Command e a função DBSETPROP( ).

Por exemplo, suponha que você crie uma view no View Designer usando o banco de dados de amostra Northwind e selecione todos os registros na tabela Customers onde o campo Country contém o valor "Canada". A instrução SQL SELECT a seguir aparece na janela SQL quando você a abre:

```foxpro
SELECT *;
   FROM Northwind!Customers ;
   WHERE Customers.Country = "Canada"
```

Você também pode incluir a instrução SQL SELECT em código copiando a instrução SQL SELECT da janela SQL para um arquivo de programa (.prg). Você também pode executar a instrução SQL SELECT imediatamente copiando a instrução e executando-a na janela Command.

> **Dica:** Se você desejar processar a instrução somente depois de digitar a última linha, digite cada cláusula em uma linha separada na janela e termine cada linha, exceto a última, com um ponto e vírgula (;).

### Para editar a definição da view
- Na janela SQL, edite a instrução SQL SELECT ou as propriedades da view.
- Para atualizar o View Designer, feche a janela SQL ou clique no View Designer para torná-lo a janela ativa.

O View Designer é atualizado com as alterações que você fez na definição da view.

> **Observação:** Se o View Designer não puder recarregar suas alterações depois que você fizer alterações na janela View SQL, uma caixa de diálogo aparece com o seguinte prompt:

"View/Query designer is unable to reload your changes. Would you like to rebuild content from the designer?"

Clicar em Yes descarta suas alterações na janela SQL e retorna você ao View Designer. Clicar em No retorna você à janela SQL.

> **Dica:** Para salvar uma instrução que não pode ser analisada, como uma chamada a um stored procedure, clique em No e depois em Save na barra de ferramentas padrão. O Visual FoxPro salva a consulta. Você pode salvar a consulta clicando em Save na barra de ferramentas padrão depois de digitar o comando na janela SQL. Você não precisa clicar na janela View Designer, o que faz o View Designer tentar carregar e analisar a consulta.
