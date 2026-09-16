# Como: criar valores padrão para campos de exibição

Assim como nos campos de tabela, você pode especificar valores padrão para campos de exibição. Esses valores padrão são armazenados no banco de dados e ficam disponíveis quando você usa a exibição.

> **Observação:** O Visual FoxPro não compara os valores padrão criados localmente com os valores padrão armazenados na fonte de dados remota. Você deve criar valores padrão aceitáveis para a fonte de dados.

### Para especificar um valor padrão para um campo de exibição
- Abra a exibição no View Designer e clique na guia Fields.
- Na guia Fields, selecione um campo e clique em Properties.
- A caixa de diálogo View Field Properties será aberta.
- Na caixa Default value da área Field Validation, digite o valor padrão do campo.
- Ao terminar, clique em OK.

Para obter mais informações, consulte Guia Fields, designers de consultas e exibições e Caixa de diálogo View Field Properties.

### Para especificar programaticamente um valor padrão para um campo de exibição
- Use a função DBSETPROP( ) com a propriedade de campo DefaultValue para exibições.

Para obter mais informações, consulte Função DBSETPROP( ).

Por exemplo, talvez você queira que seu aplicativo limite a quantidade de mercadorias que um novo cliente pode solicitar até que haja tempo para concluir uma verificação de crédito e determinar o limite que será concedido. O exemplo a seguir cria um campo `maxordamt` com o valor padrão 1000:

```foxpro
OPEN DATABASE testdata
USE VIEW customer_view
?DBSETPROP ('Customer_view.maxordamt', 'Field', 'DefaultValue', 1000)
```

Você também pode usar valores padrão para preencher automaticamente algumas linhas para o usuário. Por exemplo, pode adicionar um controle Grid a um formulário de entrada de pedidos baseado em uma exibição remota de uma tabela de itens de pedido. O campo order_id é o campo-chave que mapeia cada linha do Grid para sua correspondente na tabela remota de itens de pedido. Como o ID do pedido de cada linha da grade será o mesmo para um pedido, você pode usar um valor padrão para reduzir a digitação, preenchendo automaticamente o campo `order_id`.

> **Dica:** Se uma das regras de negócio do aplicativo exigir que um campo contenha uma entrada, fornecer um valor padrão ajuda a garantir que determinada regra de campo ou de registro não seja violada.
