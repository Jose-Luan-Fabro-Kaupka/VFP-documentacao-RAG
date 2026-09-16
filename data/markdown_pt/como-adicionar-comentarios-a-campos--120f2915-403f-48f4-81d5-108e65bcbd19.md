# Como: adicionar comentários a campos

Você pode adicionar descrições aos campos de uma tabela de banco de dados para facilitar sua compreensão e atualização. Quando você seleciona um campo de uma tabela de banco de dados no Project Manager, o texto do comentário é exibido na área Description da janela Project Manager.

### Para adicionar um comentário a um campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer.
- Na guia Fields, selecione o campo desejado.
- Na caixa Field comment do campo, digite o texto da descrição.
- Clique em OK.

Para obter mais informações, consulte Table Designer (Visual FoxPro).

### Para adicionar programaticamente um comentário a um campo
- Use a função DBSETPROP( ) para definir a propriedade Comment do campo.

Para obter mais informações, consulte Função DBSETPROP( ).

Por exemplo, suponha que você queira adicionar uma descrição a um campo de preço unitário em uma tabela que contém itens de um pedido. O código a seguir atribui o texto "Current retail price per unit" ao campo:

```foxpro
?DBSETPROP('OrdItems.Price', 'Field', 'Comment', ;
   'Current retail price per unit')
```
