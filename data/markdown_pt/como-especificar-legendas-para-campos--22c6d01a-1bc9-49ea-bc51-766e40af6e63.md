# Como: especificar legendas para campos

Para tabelas de banco de dados, você pode especificar e exibir uma legenda em vez do nome do campo no cabeçalho da coluna de uma janela ou grade de navegação. A legenda pode ser um texto ou uma expressão.

> **Observação:** As expressões não podem exceder 254 caracteres. Se a expressão exceder 254 caracteres, a legenda será padronizada com o nome do campo.

### Para especificar uma legenda para um campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer.
- Na aba Campos, selecione o campo desejado.
- Na caixa Legenda da área Exibir, digite o texto da legenda do campo. Dica Para especificar uma expressão para uma legenda de campo, inclua um sinal de igual (=) antes da sequência de caracteres da legenda.

Para obter mais informações, consulte Guia Campos, Designer de Tabela.

### Para especificar uma legenda para um campo programaticamente
- Use a função DBSETPROP( ) com a propriedade Caption field.

Para obter mais informações, consulte DBSETPROP( ) Função.

Por exemplo, o código a seguir especifica a legenda "Supplier_Fax" para um campo denominado Fax em uma tabela de fornecedores:

```foxpro
DBSETPROP('Supplier.Fax', 'Field', 'Caption', 'Supplier_Fax')
```
