# Propriedade RefreshTimeStamp

Especifica se os campos incluídos na propriedade TimestampFieldList são atualizados automaticamente quando um comando Insert ou Update é executado. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.RefreshTimestamp[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes valores lógicos: Setting Description True (.T.) Habilita a atualização automática dos campos incluídos na propriedade TimestampFieldList. False (.F.) (Padrão) Desabilita a atualização automática dos campos incluídos na propriedade TimestampFieldList.

# Observações

Aplica-se a: classe CursorAdapter

Definir a propriedade RefreshTimestamp como True (.T.) é idêntico a incluir os campos de timestamp no final da propriedade InsertCmdRefreshFieldList e da propriedade UpdateCmdRefreshFieldList.
