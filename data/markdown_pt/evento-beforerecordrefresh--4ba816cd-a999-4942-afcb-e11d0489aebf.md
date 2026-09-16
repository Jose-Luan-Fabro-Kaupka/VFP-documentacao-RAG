# Evento BeforeRecordRefresh

Ocorre imediatamente antes da execução do método RecordRefresh.

```foxpro
PROCEDURE Object.BeforeRecordRefresh
LPARAMETERS nRecords, nRecordOffset
```

#### Parâmetros
 **nRecords**
Especifica o número de registros consecutivos (em ordem física) a atualizar. Este parâmetro é passado ao método RecordRefresh.
**nRecordOffset**
Especifica o número de registros antes do registro atual onde a atualização começa. Este parâmetro é passado ao método RecordRefresh.

# Observações

Aplica-se a: Classe CursorAdapter

Os parâmetros nRecords e nRecordOffset são passados ao método RecordRefresh. Consulte o Método RecordRefresh para obter informações adicionais sobre os parâmetros nRecords e nRecordOffset.

Se o evento BeforeRecordRefresh falhar ou não retornar um valor lógico true (.T.), o método RecordRefresh não é executado e o evento AfterRecordRefresh não ocorre.
