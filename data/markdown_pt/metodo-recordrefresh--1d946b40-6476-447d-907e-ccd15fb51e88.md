# Método RecordRefresh

Atualiza os valores atuais dos campos nos registros especificados.

```foxpro
CursorAdapter.RecordRefresh([nRecords],[ nRecordOffset])
```

#### Parâmetros
 **nRecords**
Número de registros consecutivos, em ordem física, a atualizar. É um inteiro maior ou igual a zero. Se for 1 ou omitido, somente o registro atual será atualizado; se for 0, nenhum campo será atualizado.
**nRecordOffset**
Número de registros anteriores ao atual em que a atualização começa. Pode ser maior, menor ou igual a zero. Se o atual for 10 e nRecordOffset for 4, começará no 6. Se for 0 ou omitido, começa no atual.

# Valor de retorno

Numeric. Retorna o número de registros atualizados ou zero se nenhum foi atualizado e não houve erros. Por exemplo, retorna zero se todos os registros de destino forem inserções armazenadas em buffer ou nRecords for zero. Em caso de falha, retorna um inteiro negativo igual ao valor negativo do número de registros atualizados com êxito menos 1.

# Observações

Aplica-se a: classe CursorAdapter

RecordRefresh atualiza os valores atuais dos campos dos registros de destino. Use CURVAL( ) para determiná-los.

As tabelas ou cursores devem estar abertos exclusivamente.

A operação não oferece suporte a inserções em buffer, que são ignoradas sem erro. Se houver alterações de tabela ou registro em buffer, elas serão preservadas e os valores atuais serão atualizados.

Se um registro não puder ser localizado em pelo menos uma tabela base, seus campos não serão atualizados e ele será marcado como DELETED. Os registros são processados um a um até atingir nRecords ou ocorrer falha. Uma chave de atualização não exclusiva gera erro.

A configuração FetchMemo de CursorAdapter é respeitada, exceto quando há índice em um campo Memo; nesse caso, ele sempre é obtido. Uma execução longa pode ser interrompida com ESC sem gerar erro.

Use AERROR( ) para determinar a causa de uma falha. ON ERROR e TRY...CATCH...FINALLY não podem determiná-la.

RecordRefresh integra-se a REFRESH( ). Quando REFRESH( ) é chamada para um cursor associado a CursorAdapter, RecordRefresh é chamado. Por compatibilidade, REFRESH( ) retorna zero se RecordRefresh falhar.

> **Observação:** RecordRefresh usa propriedades de CursorAdapter. No Visual FoxPro 8, REFRESH( ) sempre usa propriedades de cursor definidas por CURSORSETPROP( ) e CURSORGETPROP( ), independentemente da associação com CursorAdapter.
