# Comando DELETE VIEW

Exclui uma view SQL do banco de dados atual.

```foxpro
DELETE VIEW ViewName
```

#### Parâmetros
 **ViewName**
Especifica o nome da view excluída do banco de dados atual.

# Observações

Use CREATE SQL VIEW para criar uma view SQL e adicioná-la ao banco de dados atual. Se uma view SQL estiver aberta e depois for excluída, os cursores que contêm os resultados da view SQL não são fechados.

DELETE VIEW requer uso exclusivo do banco de dados. Para abrir um banco de dados para uso exclusivo, inclua EXCLUSIVE em OPEN DATABASE.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata`. CREATE SQL VIEW é usado para criar uma view SQL local chamada `myview`. O View Designer é exibido, permitindo que você especifique tabelas e condições para a view SQL. Depois de salvar a view SQL, DISPLAY DATABASE é usado para exibir informações sobre a view SQL. DELETE VIEW é então usado para excluir a view SQL local chamada `myview`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CREATE SQL VIEW myview
CLEAR
DISPLAY DATABASE
DELETE VIEW myview
```
