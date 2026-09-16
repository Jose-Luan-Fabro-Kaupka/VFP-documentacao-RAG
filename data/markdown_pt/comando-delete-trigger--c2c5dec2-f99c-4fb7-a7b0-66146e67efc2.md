# Comando DELETE TRIGGER

Remove um trigger Delete, Insert ou Update de uma tabela do banco de dados atual.

```foxpro
DELETE TRIGGER ON TableName FOR DELETE | INSERT | UPDATE
```

#### Parâmetros
 **TableName**
Especifica o nome da tabela da qual o trigger será excluído.
**FOR DELETE | INSERT | UPDATE**
Especifica o trigger a excluir. Inclua FOR DELETE para remover o trigger Delete, FOR INSERT para remover o trigger Insert e FOR UPDATE para remover o trigger Update.

# Observações

Use CREATE TRIGGER para criar um trigger Delete, Insert ou Update para uma tabela.

# Exemplo

O exemplo a seguir cria um trigger Update, que impede que valores maiores que 50 sejam inseridos no campo `maxordamt` da tabela `customer`. DISPLAY DATABASE é usado para exibir o trigger Update. DELETE TRIGGER é então usado para remover o trigger Update, e DISPLAY DATABASE é executado novamente para verificar a remoção do trigger Update.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')  && Open testdata database
USE CUSTOMER  && Open customer table
CREATE TRIGGER ON customer FOR UPDATE AS maxordamt <= 50
CLEAR
DISPLAY DATABASE
DELETE TRIGGER ON customer FOR UPDATE
DISPLAY DATABASE
```
