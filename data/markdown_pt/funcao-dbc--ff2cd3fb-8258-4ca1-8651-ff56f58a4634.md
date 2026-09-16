# Função DBC( )

Retorna o nome e o caminho do banco de dados atual.

```foxpro
DBC()
```

# Valor de retorno

Character

# Observações

DBC( ) retorna a cadeia de caracteres vazia se não houver banco de dados atual.

Use SET DATABASE para especificar o banco de dados atual.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa DBC( ) para exibir informações sobre o banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')  && Opens the DBC.
CLEAR
? DBC()  && Displays the path and name of the database
```
