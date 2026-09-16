# Propriedade FetchMemoCmdList

Especifica os comandos a serem usados para a busca de campos Memo executada pelo método DelayedMemoFetch. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.FetchMemoCmdList[ = cCommands]
```

#### Parâmetros
 **cCommands**
Tipo de dados Character. cCommands é uma lista separada por vírgulas de pares de nomes de campos Memo e comandos de busca de campos Memo correspondentes. O comando de busca deve estar entre colchetes angulares (< >). Certifique-se de que não haja espaço em branco entre o colchete angular direito (>) e a vírgula em vários pares de nome de campo Memo e comando de busca. O exemplo a seguir demonstra o formato adequado para dois pares de nomes de campos Memo e comandos de busca de campos Memo correspondentes: oCA.FetchMemoCmdList=; "memofield1 <SELECT memofield1 FROM MyCAMemoFetch WHERE field3=?EVALUATE(this.RefreshAlias +'.field3')>, ; Memofield2 <SELECT memofield2 FROM MyCAMemoFetch WHERE field3=?EVALUATE(this.RefreshAlias +'.field3')>" Você pode especificar qualquer comando suportado pela fonte de dados e que retorne exatamente um registro. Se um comando para o campo Memo de destino não for especificado na propriedade FetchMemoCmdList, o CursorAdapter tenta gerar o comando. O comando gerado é baseado na fonte de dados e nas propriedades Tables, KeyFieldList e UpdateNameList do CursorAdapter. Um erro é gerado se o Visual FoxPro não conseguir gerar um comando apropriado.

# Observações

Aplica-se a: Classe CursorAdapter

Apenas o primeiro conjunto de resultados é usado pelo método DelayedMemoFetch.

Um erro é gerado se a conversão de dados de um campo de origem para o campo de destino não for suportada. Regras de validação para campos de destino não são executadas. Se um registro de destino não puder ser localizado, a implementação nativa do Visual FoxPro DelayedMemoFetch marca o registro de destino como DELETED e gera um erro.

Para Recordsets ADODB, a propriedade FetchMemoCmdList é ignorada. As propriedades Tables, KeyFieldList e UpdateNameList do CursorAdapter também são ignoradas, e nenhum erro é gerado se os campos-chave não estiverem especificados. Os campos são atualizados usando os valores atuais dos campos no Recordset.

Se o tipo de bloqueio do Recordset ADODB não for adLockBatchOptimistic ou adLockUnspecified, o CursorAdapter chama o método Resync com o parâmetro ResyncValues definido como adResyncAllValues para atualizar o registro antes que o valor do campo seja recuperado.
