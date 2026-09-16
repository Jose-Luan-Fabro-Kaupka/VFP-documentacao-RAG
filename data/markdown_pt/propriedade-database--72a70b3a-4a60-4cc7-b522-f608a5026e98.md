# Propriedade Database

Especifica o caminho para o banco de dados que contém a tabela ou view associada a um cursor ou CursorAdapter. Somente leitura em tempo de design; leitura/gravação em tempo de execução.

> **Observação:** Quando você acessa um cursor regular usando a função CURSORSETPROP(), a propriedade Database é somente leitura em tempo de execução.

```foxpro
DataEnvironment.Cursor.Database [ = cPath ]
```

# Valor de retorno
 **cPath**
Especifica o caminho completo para o arquivo de banco de dados (.dbc).

# Observações

Aplica-se a: Cursor Object

Se o cursor é baseado em uma tabela livre, Database contém uma cadeia de caracteres vazia ("").
