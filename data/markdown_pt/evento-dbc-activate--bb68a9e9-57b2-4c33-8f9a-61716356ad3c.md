# Evento dbc_Activate

Ocorre quando um banco de dados se torna ativo. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_Activate(cDatabaseName)
```

```foxpro
PROCEDURE dbc_Activate
LPARAMETERS cDatabaseName
```

#### Parâmetros
 **cDatabaseName**
Especifica o nome do banco de dados sendo ativado.

# Observações

Você pode ter muitos bancos de dados abertos ao mesmo tempo, mas apenas um pode estar ativo por vez. Um banco de dados pode se tornar ativo em várias circunstâncias. Para ativar explicitamente um banco de dados, use o comando SET DATABASE TO. Se vários bancos de dados (com DBC Events ativado) estão abertos, o método dbc_Activate é executado apenas no banco de dados ativo.

Se você colocar código de DBC Events em um arquivo de programa, o código se aplica a qualquer banco de dados que especifique esse arquivo de programa como seu arquivo de eventos. Neste caso, o código de método de eventos DBC pode afetar vários bancos de dados ao mesmo tempo. Quando você usa eventos DBC dessa maneira, use o parâmetro cDatabaseName no código do evento para especificar qual banco de dados está sendo ativado. Assim você pode usar um bloco de código de método para determinar o banco de dados ativado e depois aplicar código apropriado para esse banco de dados.

Retorne False (.F.) deste procedimento para impedir que o banco de dados seja ativado.

O Visual FoxPro ignorará um retorno de False (.F.) deste evento durante o tempo de design.

# Exemplo

```foxpro
PROCEDURE dbc_Activate ;
         (cDatabaseName)
? '     cDatabaseName  = ' + TRANSFORM(cDatabaseName) + ' - ' ;
                       + TYPE('cDatabaseName ')+' /end/ '
ENDPROC
```
