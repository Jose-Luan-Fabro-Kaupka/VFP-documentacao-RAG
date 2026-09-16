# Propriedade RefreshCmd

Especifica o comando a usar para o Refresh de registro executado pelo método RecordRefresh. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.RefreshCmd[ = cCommand]
```

#### Parâmetros
 **cCommand**
Tipo de dados caractere. A tabela a seguir lista os valores possíveis de cCommand . cCommand Descrição Cadeia de caracteres ou expressão Especifica uma cadeia de comando válida para a fonte de dados especificada pelas propriedades RefreshCmdDataSourceType Property e RefreshCmdDataSource Property. Para fontes de dados ADO e ODBC, você pode especificar qualquer comando suportado pela fonte de dados e que retorne exatamente um registro. Para uma fonte de dados nativa do Visual FoxPro, o comando deve ser um comando SQL SELECT que retorne exatamente um registro. Os campos são correspondidos pela posição no cursor, excluindo campos especificados na propriedade RefreshIgnoreFieldList. Cadeia de caracteres vazia ("") O objeto CursorAdapter gera automaticamente um comando Refresh de registro. O comando gerado é baseado na fonte de dados e nas propriedades Tables, KeyFieldList, UpdateNameList e RefreshIgnoreFieldList do CursorAdapter. Se você incluir um comando, as propriedades Tables, KeyFieldList e UpdateNameList são ignoradas. Observação Um comando gerado automaticamente não inclui campos AUTOINC ou de chave, mesmo que não estejam incluídos na propriedade RefreshIgnoreFieldList.

# Observações

Aplica-se a: Classe CursorAdapter

O comando especificado é executado para cada registro de destino. Regras de validação para campos de destino não são executadas.

Nenhum campo é atualizado se ocorrer um erro durante o refresh do registro. Um erro é gerado se a conversão de dados de um campo de origem para o campo de destino não for suportada. Tentar atualizar um campo AUTOINC gerará um erro. A operação de refresh é cancelada se uma tentativa de atualizar índices falhar devido a chave não exclusiva ou por qualquer outro motivo.

Para Recordsets ADODB, as propriedades RefreshCmd, Tables, KeyFieldList e UpdateNameList do CursorAdapter são ignoradas, e nenhum erro é gerado se campos de chave não estiverem especificados.

Se o tipo de bloqueio do Recordset ADODB não for adLockBatchOptimistic ou adLockUnspecified, o CursorAdapter chama o Método Resync com o parâmetro ResyncValues definido como adResyncAllValues para atualizar o registro no Recordset antes que o registro no cursor seja atualizado.

Você pode definir esta propriedade no evento BeforeRecordRefresh.
