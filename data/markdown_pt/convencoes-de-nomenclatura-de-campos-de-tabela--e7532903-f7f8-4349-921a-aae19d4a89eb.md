# Convenções de nomenclatura de campos de tabela

Ao nomear campos em tabelas, use o formato a seguir.

```foxpro
TableAlias.PrefixFieldName
```

#### Parâmetros
 **TableAlias**
Especifica o nome ou alias de uma tabela.
**Prefix**
Indica o tipo de dados de um campo de tabela. A tabela a seguir lista os prefixos sugeridos para Prefix . Prefix Description c Character y Currency d Date t DateTime b Double f Float g General i Integer l Logical m Memo n Numeric q Varbinary v Varchar , Varchar (Binary) w Blob
**FieldName**
Especifica o nome do campo.

# Exemplo

O exemplo a seguir ilustra como a letra "c" indica que o campo LastName da tabela Customer tem tipo Character:

```foxpro
Customer.cLastName
```
