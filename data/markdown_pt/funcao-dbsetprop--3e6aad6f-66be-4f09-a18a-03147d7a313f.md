# Função DBSETPROP( )

Define uma propriedade para o banco de dados atual ou para campos, conexões nomeadas, tabelas ou exibições no banco de dados atual.

```foxpro
DBSETPROP(cName, cType, cProperty, ePropertyValue)
```

#### Parâmetros
 **cName**
Especifica o nome do banco de dados aberto atual ou do campo, conexão nomeada, tabela ou exibição no banco de dados aberto atual para o qual DBGETPROP( ) retorna informações. Para definir uma propriedade para um campo em uma tabela ou exibição, prefixe o nome do campo com o nome da tabela ou exibição que contém o campo. Por exemplo, para definir uma propriedade para o campo custid na tabela customer, especifique o seguinte para cName : customer.custid
**cType**
Especifica se cName é o banco de dados atual ou um campo, conexão nomeada, tabela ou exibição no banco de dados atual. A tabela a seguir lista os valores que você pode especificar para cType : cType Description CONNECTION cName é uma conexão nomeada no banco de dados atual. DATABASE cName é o banco de dados atual. FIELD cName é um campo no banco de dados atual. TABLE cName é uma tabela no banco de dados atual. VIEW cName é uma exibição no banco de dados atual.
**cProperty**
Especifica o nome da propriedade a ser definida. Se uma propriedade for somente leitura, seu valor não pode ser alterado com DBSETPROP( ) . Se você tentar definir uma propriedade somente leitura, o Visual FoxPro gera uma mensagem de erro. Para obter mais informações sobre as propriedades que você pode especificar com cProperty , incluindo seus tipos de dados, consulte DBGETPROP( ) .
**ePropertyValue**
Especifica o valor ao qual cProperty será definido. ePropertyValue deve ser do mesmo tipo de dados do tipo de dados da propriedade. Cuidado O Visual FoxPro não verifica se o valor que você especifica é válido para a propriedade. Assim, é possível definir uma propriedade com um valor inválido usando DBSETPROP( ) . Por exemplo, DBSETPROP( ) pode ser usado para definir uma expressão de regra de campo para uma expressão que não é válida para o campo, e o Visual FoxPro não gerará um erro. Para evitar um erro ao definir a propriedade Tables de uma exibição, prefixe ePropertyValue com a designação do banco de dados na sintaxe a seguir:

```foxpro
         <databaseName>!ePropertyValue
```

# Valor de retorno

Tipo de dados lógico. DBSETPROP( ) retorna True (.T.) se o Visual FoxPro definir com sucesso a propriedade que você especificar. O Visual FoxPro gera um erro se a propriedade que você especificar não puder ser definida.

# Observações

Para obter mais informações sobre como recuperar valores de propriedade atuais, consulte DBGETPROP( ) Function.

# Exemplo

O exemplo a seguir usa DBSETPROP( ) para especificar um comentário para o campo `cust_id` na tabela `customer`. DBGETPROP( ) é usado para exibir o comentário.

```foxpro
CLOSE DATABASES
CLEAR
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer     && Open customer table
= DBSETPROP("customer.cust_id", "Field", "Comment", ;
  "Property has been set by DBSETPROP.")  && New field comments
cRESULTS = DBGETPROP("customer.cust_id", "Field", "Comment")
WAIT WINDOW "Cust_id field comments: "+ cRESULTS  && Display comments
```
