# Como: adicionar comentários a views

Você pode adicionar comentários às views que criar. Os comentários que você adiciona a uma view são armazenados no arquivo de banco de dados (.dbc) que contém a view.

### Para adicionar um comentário a uma view
- Abra a view no View Designer.
- No menu Query, clique em Comments.
- Na caixa Comment, digite os comentários que deseja adicionar à view.
- Quando terminar, clique em OK.

Você pode ver os comentários de uma view abrindo a janela SQL. Para obter mais informações, consulte How to: View and Edit SQL Statements for Views.

### Para editar comentários de uma view
- Abra a view no View Designer.
- Abra a janela SQL da view.
- Na janela SQL, edite a chamada da função DBSETPROP( ) que contém a propriedade Comment da view.
- Quando terminar, feche a janela SQL.

Para obter mais informações, consulte How to: View and Edit SQL Statements for Views.

### Para adicionar ou editar um comentário em uma view programaticamente
- Use a função DBSETPROP( ) com a propriedade Comment da view.

Para obter mais informações, consulte DBSETPROP( ) Function.
