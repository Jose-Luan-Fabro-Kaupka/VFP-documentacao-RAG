# Função DBUSED( )

Retorna true (.T.) se o banco de dados especificado estiver aberto.

```foxpro
DBUSED(cDatabaseName)
```

#### Parâmetros
 **cDatabaseName**
Especifica o nome do banco de dados para o qual DBUSED( ) retorna um valor lógico indicando se o banco de dados está aberto ou não.

# Valor de retorno

Lógico

# Observações

DBUSED( ) retorna true (.T.) se o banco de dados especificado estiver aberto; caso contrário, retorna false (.F.).

# Exemplo

O exemplo a seguir abre o banco de dados TESTDATA e usa DBUSED( ) para determinar se os bancos de dados TESTDATA e TEST estão abertos.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CLEAR
? 'Testdata database open? '
?? DBUSED('testdata')     && Displays .T.
? 'Test database open? '
?? DBUSED('test')     && Displays .F.
```
