# Como: atualizar uma exibição um-para-muitos baseada em um valor de lista

Quando o usuário escolhe ir a um registro selecionando um valor em uma lista, você pode ter um relacionamento um-para-muitos que precisa refletir o ponteiro de registro alterado na tabela pai. Você pode implementar essa funcionalidade com tabelas locais e views locais ou remotas.

Para tabelas locais, se o RowSourceType da lista for 2 - Alias ou 6 - Fields e o RowSource for uma tabela local com um relacionamento definido no ambiente de dados do formulário, emita `THISFORM.Refresh` no evento InteractiveChange quando o usuário escolher um novo valor. O lado muitos do relacionamento um-para-muitos exibe automaticamente apenas os registros que correspondem à expressão da tabela pai envolvida na relação.

Para views, atualizar uma exibição um-para-muitos é um pouco diferente se o RowSource da caixa de lista for uma view local ou remota. O exemplo a seguir descreve a criação de um formulário com uma caixa de lista e uma grade. A caixa de lista exibe os valores do campo `cust_id` na tabela `TESTDATA!Customer`. A grade exibe os pedidos associados ao campo `cust_id` selecionado na caixa de lista.

Primeiro, nos Query and View Designers, crie uma view parametrizada para os pedidos. Quando você cria a view no View Designer, defina o critério de seleção para a chave estrangeira como uma variável. No exemplo a seguir, a variável é chamada `m.cCust_id`.
 View parametrizada usando uma variável

Então, quando você projeta o formulário, siga as etapas no procedimento a seguir. Observe que a view requer um valor para o parâmetro que não está disponível quando o formulário é carregado. Definindo a propriedade NoDataOnLoad do objeto cursor da view como true (.T.), você impede que a view seja executada até que a função REQUERY( ) seja chamada, momento em que o usuário teria selecionado um valor para a variável usada na view parametrizada.

### Para projetar uma lista um-para-muitos baseada em views locais ou remotas
- Adicione a tabela e a view parametrizada ao ambiente de dados.
- Na janela Properties do objeto cursor da view no Data Environment, defina a propriedade NoDataOnLoad como true (.T.).
- Defina a propriedade RowSourceType da caixa de lista como 6 — Fields e defina sua propriedade RowSource como o campo referenciado como chave estrangeira no parâmetro da view. No exemplo, você definiría a propriedade RowSource como customer.cust_id.
- Defina a propriedade RecordSource da grade como o nome da view que você criou anteriormente.
- No código do evento InteractiveChange da caixa de lista, armazene o valor da caixa de lista na variável e então reconsulte a view, como neste exemplo: m.cCust_id = THIS.Value *assumindo que o nome da view é orders_view =REQUERY("orders_view")

Para obter mais informações sobre views locais e remotas, consulte Creating Views.
