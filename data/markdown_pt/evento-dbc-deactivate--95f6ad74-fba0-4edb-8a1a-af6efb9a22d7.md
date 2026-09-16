# Evento dbc_Deactivate

Ocorre quando um banco de dados deixa de estar ativo. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_Deactivate(cDatabaseName)
```

```foxpro
PROCEDURE dbc_Deactivate
LPARAMETERS cDatabaseName
```

#### Parâmetros
 **cDatabaseName**
Especifica o nome do banco de dados sendo desativado.

# Observações

Você pode ter muitos bancos de dados abertos ao mesmo tempo, mas apenas um pode estar ativo por vez. Várias situações podem desativar um banco de dados. Para desativar explicitamente um banco de dados sem ativar outro banco de dados, use o comando SET DATABASE TO sem argumentos.

Se vários bancos de dados (com DBC Events ativados) estiverem abertos, quando um for desativado, o método dbc_Deactivate nesse banco de dados é executado.

Se você colocar código DBC Events em um arquivo de programa, o código se aplica a qualquer banco de dados que especifique esse arquivo de programa como seu arquivo de eventos. Nesse código de programa, use o parâmetro cDatabaseName para determinar qual banco de dados chamou o evento. Dessa forma, você pode usar um bloco de código de método para determinar o banco de dados desativado e aplicar código apropriado a esse banco de dados.

Retorne .F. deste procedimento para impedir que o banco de dados seja desativado. Como fechar um banco de dados o desativa implicitamente, isso também impedirá que o banco de dados seja fechado.

# Exemplo

```foxpro
PROCEDURE dbc_Deactivate ;
         (cDatabaseName)
? '     cDatabaseName = ' + TRANSFORM(cDatabaseName) + ' - ' ;
                      + TYPE('cDatabaseName')+' /end/ '
ENDPROC
```
