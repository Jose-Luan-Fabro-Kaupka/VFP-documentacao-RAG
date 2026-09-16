# Como: criar relações persistentes entre tabelas

Você pode criar relações persistentes entre tabelas de banco de dados baseadas em uma expressão simples ou complexa ou em seus índices. Essas relações são armazenadas no arquivo de banco de dados (.dbc). O tipo de tag de índice ou chave determina o tipo de relação persistente que você pode criar. Por exemplo, em uma relação um-para-muitos entre duas tabelas, você deve usar uma tag de índice ou chave primária ou candidata em uma tabela para o lado "um" na relação e uma tag de índice ou chave regular na outra tabela para o lado "muitos" na relação.

Antes de criar uma relação persistente, você precisa executar as seguintes etapas:
 - Determine qual tabela contém os registros primários e qual tabela contém os registros relacionados.
- Na tabela com os registros primários, adicione um campo inteiro e depois adicione um índice primário no novo campo.
- Na tabela com os registros relacionados, adicione um campo que corresponda à chave de índice primário na tabela de registros primários e depois adicione um índice regular nesse novo campo. Observação Use a mesma expressão para ambos os índices. Por exemplo, se você usar uma função na expressão no campo de chave primária, precisa usar a mesma função na expressão no campo de chave estrangeira.

Para obter mais informações, consulte Identifying Relationships and Working with Table Indexes.

### Para criar uma relação persistente entre tabelas
- Abra o banco de dados no Database Designer .
- No Database Designer , arraste o nome do índice da tabela que deseja relacionar para o nome do índice na tabela relacionada.

Uma linha representando a relação persistente entre as duas tabelas aparece no Database Designer.

Para obter mais informações, consulte Database Designer (Visual FoxPro).

### Para criar uma relação persistente entre tabelas programaticamente
- Use os comandos CREATE TABLE ou ALTER TABLE com a cláusula FOREIGN KEY.

Para obter mais informações, consulte CREATE TABLE - SQL Command e ALTER TABLE - SQL Command.

Por exemplo, o código a seguir usa o comando SQL ALTER TABLE e as tabelas Customer e Orders para criar uma relação persistente um-para-muitos, onde um cliente tem muitos pedidos, baseada na chave de índice primário, `Cust_ID`, na tabela Customer e uma nova chave estrangeira, `cust_id`, na tabela Orders:

```foxpro
ALTER TABLE Orders;
   ADD FOREIGN KEY Cust_ID TAG ;
      Cust_Id REFERENCES Customer
```
