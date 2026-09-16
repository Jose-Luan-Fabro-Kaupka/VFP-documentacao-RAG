# Evento AfterCursorUpdate

Ocorre imediatamente após todos os eventos intermediários AfterUpdate, AfterDelete ou AfterInsert terem ocorrido e antes que a função TABLEUPDATE( ) retorne.

```foxpro
PROCEDURE Object.AfterCursorUpdate
LPARAMETERS nRows, lTableUpdateResult, cErrorArray
```

#### Parâmetros
 **nRows**
Especifica a configuração do parâmetro nRows de uma operação da função TABLEUPDATE( ).
**lTableUpdateResult**
Especifica o valor retornado por uma operação TABLEUPDATE( ).
**cErrorArray**
Contém o conteúdo do parâmetro cErrorArray de uma operação TABLEUPDATE( ). O Visual FoxPro preenche esta matriz a partir de TABLEUPDATE( ) apenas nas circunstâncias descritas pela descrição de cErrorArray na função TABLEUPDATE( ).

# Observações

Aplica-se a: Classe CursorAdapter

AfterCursorUpdate ocorre uma vez ao término do processo de atualização. Se várias linhas estão sendo atualizadas, os eventos AfterUpdate, AfterInsert e AfterDelete ocorrem para cada linha atualizada, conforme apropriado.

Você pode chamar a função AERROR( ) para recuperar erros de fontes de dados upstream.

No Visual FoxPro 9.0, o registro de destino é mantido atual em um ADODB.Recordset durante o evento AfterCursorUpdate.
