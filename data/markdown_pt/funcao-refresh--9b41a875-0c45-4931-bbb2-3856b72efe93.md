# Função REFRESH( )

Atualiza dados em uma view SQL remota ou local atualizável, ou cursor CursorAdapter.

```foxpro
REFRESH([nRecords [, nRecordOffset]] [, cTableAlias | nWorkArea])
```

#### Parâmetros
 **nRecords**
Especifica o número de registros a atualizar. Se nRecords é 1 ou você omite nRecords , somente o registro atual é atualizado. Se nRecords é 0, nenhum registro é atualizado.
**nRecordOffset**
Especifica o número de registros antes do registro atual onde a atualização começa. Por exemplo, se o registro atual é o registro 10 e nRecordOffset é 4, a atualização de registros começa com o registro 6. Se nRecordOffset é 0 ou você omite nRecordOffset , a atualização começa com o registro atual.
**cTableAlias**
Especifica o alias do cursor associado a uma view SQL remota ou local, ou a um cursor CursorAdapter onde os registros são atualizados.
**nWorkArea**
Especifica a área de trabalho do cursor onde os registros são atualizados. Se você omitir nWorkArea e cTableAlias , os registros são atualizados na área de trabalho atualmente selecionada.

# Valor de retorno

Numérico. REFRESH( ) retorna o número de registros atualizados.

# Observações

Os registros são atualizados com dados das tabelas que definem a view SQL ou CursorAdapter. A menos que especificado, os registros são atualizados na view SQL ou cursor CursorAdapter aberto na área de trabalho atualmente selecionada.

> **Observação:** REFRESH( ) não atualiza o conteúdo de registros em buffer; no entanto, valores de campo que são acessíveis para o registro através da função CURVAL( ) são atualizados. Para obter mais informações, consulte Função CURVAL( ) .

> **Cuidado:** Os registros devem ter chaves primárias exclusivas. Se uma chave para um registro não pode ser localizada na tabela base, o registro correspondente na view SQL ou CursorAdapter é marcado para exclusão.

> **Dica:** Chamar a função REFRESH( ) pode resultar em um impacto significativo no desempenho porque a função reexecuta a consulta na qual a view é baseada. Portanto, não chame esta função mais do que o necessário.
