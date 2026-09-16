# Comando RENAME VIEW

Renomeia uma view SQL no banco de dados atual.

```foxpro
RENAME VIEW ViewName1 TO ViewName2
```

#### Parâmetros
 **ViewName1**
Especifica o nome da view SQL a ser renomeada.
**ViewName2**
Especifica o novo nome da view SQL.

# Observações

O banco de dados que contém a view SQL deve ser aberto de forma exclusiva e deve ser o banco de dados atual antes que a view SQL possa ser renomeada. Para abrir um banco de dados para uso exclusivo, inclua EXCLUSIVE em OPEN DATABASE.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata`. CREATE SQL VIEW é usado para criar uma view SQL local chamada `myview,` que é criada a partir de uma instrução SELECT - SQL que seleciona todos os registros da tabela `customer`. RENAME VIEW é usado para alterar o nome da view de `myview` para `yourview`.

O View Designer é exibido, permitindo modificar a view SQL recém-renomeada. Após o View Designer ser fechado, a view SQL é apagada.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CREATE SQL VIEW myview AS SELECT * FROM customer  && Create the view
RENAME VIEW myview TO yourview  && Change the view name
MODIFY VIEW yourview  && Open the View designer
DELETE VIEW yourview  && Delete the view
```
