# Evento AfterRecordRefresh

Ocorre imediatamente após a execução do método RecordRefresh.

```foxpro
PROCEDURE Object.AfterRecordRefresh
LPARAMETERS nRecords, nRecordOffset, nRefreshed
```

#### Parâmetros
 **nRecords**
O número de registros a atualizar passado ao método RecordRefresh.
**nRecordOffset**
O deslocamento de registro passado ao método RecordRefresh.
**nRefreshed**
O valor de retorno do método RecordRefresh.

# Observações

Aplica-se a: CursorAdapter Class

Consulte o método RecordRefresh para obter informações adicionais sobre os parâmetros nRecords e nRecordOffset e o valor de retorno do método RecordRefresh passado ao parâmetro nRefreshed.

> **Observação:** Este evento ocorre apenas uma vez após a execução do método RecordRefresh, não cada vez que uma atualização de registro é tentada.

Você pode incluir a função AERROR( ) neste evento para determinar a causa de erros (se houver) gerados pelo método RecordRefresh.
