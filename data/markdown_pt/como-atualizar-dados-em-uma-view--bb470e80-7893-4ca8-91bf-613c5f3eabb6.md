# Como: atualizar dados em uma view

Para atualizar dados em uma view, certifique-se de que as opções e propriedades que controlam atualizações para views estão definidas para que a view possa ser atualizada. Para obter mais informações, consulte Preparando para atualizar views.

> **Observação:** As propriedades padrão da view podem fornecer todas as informações necessárias para que sua view possa ser atualizada.

### Para visualizar opções de atualização de uma view
- Abra a view no View Designer e clique na guia Update Criteria. A guia Update Criteria exibe as configurações de atualização da view.

Para obter mais informações, consulte Como: editar views e Guia Update Criteria, View Designer.

### Para definir propriedades de atualização de uma view
- Use o comando DISPLAY DATABASE para exibir as configurações de propriedade atuais da view.
- Use a função DBSETPROP( ) para modificar as configurações de propriedade da view.

Para obter mais informações, consulte Função DBSETPROP( ).

Quando você usa DBSETPROP( ) para definir propriedades em uma view antes de usar a view, as configurações são armazenadas no banco de dados e usadas automaticamente sempre que você ativa a view. Uma vez que a view está ativa, você pode usar a função CURSORSETPROP( ) para alterar configurações de propriedade na view ativa. Configurações de propriedade definidas em uma view ativa com CURSORSETPROP( ) não são salvas quando você fecha a view.

O exemplo a seguir lista as etapas que você seguirá para especificar as cinco propriedades de atualização de view programaticamente:
 - Defina a propriedade Tables com pelo menos um nome de tabela. Por exemplo, se você tem uma view baseada na tabela customer chamada cust_view, pode definir o nome da tabela com a seguinte função: DBSETPROP('cust_view','View','Tables','customer') Dica Se uma tabela aparece como qualificador na propriedade UpdateName, mas não está incluída na lista padrão da propriedade Tables, a tabela pode não ter um campo de chave primária especificado. Torne a tabela atualizável adicionando o campo que você considera ser um campo de chave à lista da propriedade KeyField e depois adicione a tabela à lista da propriedade Tables.
- Defina a propriedade KeyField com um ou mais nomes de campo Visual FoxPro locais que juntos definem uma chave exclusiva para a tabela de atualização. Usando o mesmo exemplo, você pode tornar cust_id o campo de chave usando o seguinte código: DBSETPROP('cust_view.cust_id','Field','KeyField',.T.) Cuidado Certifique-se de que o(s) campo(s) de chave que você especifica definem uma chave exclusiva tanto na tabela base que deseja atualizar quanto na view.
- Mapeie os campos da view para seus campos de tabela base com a propriedade UpdateName. Esta propriedade é particularmente útil quando sua view é baseada em uma junção de duas tabelas com um nome de campo comum, ou quando os campos são aliased na view. Para atualizar a tabela base desejada, você mapeia o nome do campo da view Visual FoxPro para o campo e nome da tabela base. DBSETPROP('cust_view.cust_id','Field','UpdateName',; 'customer.cust_id') Dica Para evitar criar campos sinônimo em sua view, você pode qualificar nomes de campo na instrução SQL usada para construir sua view. Em seguida, use a propriedade UpdateName do Visual FoxPro da view para mapear cada campo qualificado para o nome correto de tabela e campo base.
- Especifique o escopo dos campos que deseja atualizar com a propriedade Updatable. Você deve especificar apenas os campos também especificados com a propriedade UpdateName. DBSETPROP('cust_view.cust_id','Field','Updatable', .T.)
- Defina a propriedade SendUpdates como True (.T.). A propriedade SendUpdates controla se cria e envia atualizações para as tabelas e campos que podem ser atualizados. DBSETPROP('cust_view','View','SendUpdates',.T.)
