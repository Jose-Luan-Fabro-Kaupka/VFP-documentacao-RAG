# Comando PACK DATABASE

Remove do banco de dados atual os registros marcados para exclusão.

```foxpro
PACK DATABASE
```

# Observações

Um banco de dados contém registros marcados para exclusão depois que uma tabela ou exibição é removida do banco de dados ou quando a estrutura de uma tabela do banco de dados é modificada.

O banco de dados deve ser aberto exclusivamente, e nenhuma tabela ou exibição do banco de dados pode estar aberta.

# Exemplo

No exemplo a seguir, PACK DATABASE é usado para compactar o banco de dados `testdata`, removendo os registros marcados para exclusão.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'data\')     && Sets path to database
OPEN DATABASE testdata  && Open the database
PACK DATABASE && Pack the current database
```
