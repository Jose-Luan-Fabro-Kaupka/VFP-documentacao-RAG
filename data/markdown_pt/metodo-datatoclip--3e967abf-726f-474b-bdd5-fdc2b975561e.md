# Método DataToClip

Copia um conjunto de registros como texto para a Área de transferência.

```foxpro
ApplicationObject.DataToClip([nWorkArea | cTableAlias]
   [, nRecords] [, nClipFormat])
```

# Valor de retorno
 **nWorkArea**
Especifica o número da área de trabalho da tabela para a qual os registros são copiados para a Área de transferência. Se você omitir cTableAlias e nWorkArea , os registros são copiados para a Área de transferência da tabela aberta na área de trabalho atual.
**cTableAlias**
Especifica o alias da tabela para a qual os registros são copiados para a Área de transferência.
**nRecords**
Especifica o número de registros copiados para a Área de transferência. Se nRecords for maior que o número de registros restantes na tabela, todos os registros restantes são copiados para a Área de transferência. Se nRecords e nClipFormat forem omitidos, o registro atual e todos os registros restantes são copiados para a Área de transferência.
**nClipFormat**
Especifica como os campos são delimitados. As configurações para nClipFormat são: nClipFormat Description 1 (Padrão) Campos delimitados com espaços 3 Campos delimitados com tabulações Se nClipFormat for omitido, os campos são delimitados com espaços.

# Observações

Aplica-se a: Application Object | _VFP System Variable

Os nomes dos campos aparecem como a primeira linha do texto copiado para a Área de transferência, seguidos por uma linha separada para cada registro.
