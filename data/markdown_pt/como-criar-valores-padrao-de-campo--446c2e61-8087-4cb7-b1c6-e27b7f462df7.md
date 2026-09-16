# Como: criar valores padrão de campo

Você pode especificar valores padrão que os campos em tabelas de banco de dados contêm ao adicionar novos registros, independentemente de como os dados são inseridos. Esses valores padrão permanecem até serem substituídos por novos valores.

> **Observação:** Você pode especificar valores padrão para campos de qualquer tipo de dados, exceto campos General.

Você também pode visualizar o valor padrão do campo.

### Para especificar um valor padrão para um campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer .
- Na guia Fields, selecione o campo desejado.
- Na caixa Default value na área Field validation, digite o valor padrão desejado para o campo. Dica Coloque texto entre aspas ("") para campos de caractere.
- Clique em OK .

Para obter mais informações, consulte Fields Tab, Table Designer.

### Para especificar um valor padrão para um campo programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, inclua a cláusula DEFAULT.

-OU-
 - Para editar uma tabela existente, abra a tabela com o comando USE e depois use o comando SQL ALTER TABLE com a cláusula DEFAULT.

Para obter mais informações, consulte CREATE TABLE - SQL Command e ALTER TABLE - SQL Command.

Por exemplo, suponha que você deseja que sua aplicação limite a quantidade de mercadorias que um novo cliente pode pedir até que você possa concluir uma verificação de crédito e determinar o valor de crédito que deseja conceder a esse cliente. O código a seguir cria uma tabela de clientes com um campo de valor máximo de pedido com valor padrão de 1000:

```foxpro
CREATE TABLE Customer (Cust_ID C(6), Company C(40), Contact C(30), ;
   MaxOrdAmt Y(4) DEFAULT 1000)
```

Se a tabela existir, você pode adicionar um valor padrão para o campo:

```foxpro
ALTER TABLE Customer ALTER COLUMN MaxOrdAmt SET DEFAULT 1000
```

### Para visualizar o valor padrão de um campo em uma tabela de banco de dados
- Use a função DBGETPROP( ) para recuperar o valor da propriedade DefaultValue do campo.

Para obter mais informações, consulte DBGETPROP( ) Function.
