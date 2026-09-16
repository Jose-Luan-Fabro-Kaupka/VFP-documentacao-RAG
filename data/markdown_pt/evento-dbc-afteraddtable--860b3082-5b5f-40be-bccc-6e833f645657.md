# Evento dbc_AfterAddTable

Ocorre depois que uma tabela é adicionada a um banco de dados ativo. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterAddTable(cTableName, cLongTableName)
```

```foxpro
PROCEDURE dbc_AfterAddTable
LPARAMETERS cTableName, cLongTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela sendo adicionada ao banco de dados.
**cLongTableName**
Especifica o nome longo da tabela sendo adicionada ao banco de dados.

# Observações

Você pode adicionar código de método ao evento dbc_AfterAddTable para executar funções como atualizar seu dicionário de dados ou enviar um e-mail ao administrador do banco de dados.

Este evento não ocorre quando você cria uma tabela no banco de dados.

# Exemplo

```foxpro
PROCEDURE dbc_AfterAddTable ;
         (cTableName, ;
          cLongTableName)
? '     cTableName     = ' + TRANSFORM(cTableName)     + ' - ' ;
                       + TYPE('cTableName ')
? '     cLongTableName = ' + TRANSFORM(cLongTableName) + ' - ' ;
                       + TYPE('cLongTableName ')+' /end/ '
ENDPROC
```
