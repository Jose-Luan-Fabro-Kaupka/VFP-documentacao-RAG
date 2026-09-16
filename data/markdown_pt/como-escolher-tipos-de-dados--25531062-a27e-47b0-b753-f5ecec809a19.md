# Como: escolher tipos de dados

Depois de especificar o nome de um campo, você pode escolher o tipo de dado que ele pode armazenar.

### Para escolher um tipo de dado para um campo
- Abra a tabela no Table Designer.
- Na guia Fields, selecione o campo desejado.
- Na lista Type, selecione um tipo de dado para o campo. Dica Se o campo for do tipo Numeric ou Float, defina o número de casas decimais na coluna Decimal. Se um campo inteiro contiver valores incrementados automaticamente, será necessário especificar os valores seguinte e de incremento. Para obter mais informações, consulte Como: definir valores de campo com incremento automático.

Para obter mais informações, consulte Guia Fields, Table Designer.

### Para escolher programaticamente um tipo de dado para um campo
- Ao criar a tabela com o comando SQL CREATE TABLE, especifique o tipo de dado do campo.

-OU-
 - Para editar uma tabela existente, abra-a com o comando USE e use o comando SQL ALTER TABLE.

Para obter mais informações, consulte Comando CREATE TABLE - SQL ou Comando ALTER TABLE - SQL.

Por exemplo, o código a seguir cria e abre uma tabela chamada Customer com três campos, Cust_ID, Company e Contact, usando o comando CREATE TABLE:

```foxpro
CREATE TABLE Customer (Cust_ID C(6), Company C(40), Contact C(30))
```

No exemplo, `C(6)` indica que o campo contém dados Character e tem largura de 6 caracteres.
