# Método ApplyDiffgram

Aplica um DiffGram a tabelas locais do Visual FoxPro.

```foxpro
XMLTable.ApplyDiffgram( [ cAlias [, oCursorAdapter [, lPreserveChanges [, nCodePage ]]]] )
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor de destino. O valor de cAlias assume como padrão a propriedade XMLTableAlias, inclusive quando cAlias é uma cadeia de caracteres vazia ("").
**oCursorAdapter**
Especifica um objeto CursorAdapter preexistente. ApplyDiffgram anexa o cursor com buffer de tabela temporário contendo alterações ao objeto CursorAdapter especificado. ApplyDiffgram também aplica quaisquer atualizações, como registros modificados, inseridos ou excluídos, à tabela base definida para o objeto CursorAdapter ou ao cursor correspondente à propriedade Alias do objeto XMLTable. Se você não fornecer um valor para oCursorAdapter , ApplyDiffgram trata automaticamente as atualizações na tabela base. Observação Você pode atualizar a fonte de dados remota usando o método ApplyDiffgram, desde que o CursorAdapter esteja configurado para esse fim.
**lPreserveChanges**
Especifica se deve manter o cursor, com alterações, anexado ao objeto CursorAdapter e quaisquer alterações nas propriedades do objeto CursorAdapter intactas quando você fornece um objeto CursorAdapter personalizado e ApplyDiffgram falha. A tabela a seguir descreve os valores para lPreserveChanges . lPreserveChanges Descrição True (.T.) (Padrão) Manter o cursor, com alterações, anexado ao cursor adapter e as alterações nas propriedades do cursor adapter intactas. False (.F.) Desanexar o cursor, com alterações, e reverter quaisquer alterações feitas nas propriedades do cursor adapter.
**nCodePage**
Especifica um code page. O valor padrão é zero (0).

# Observações

Aplica-se a: XMLTable Class

ApplyDiffgram é suportado apenas para objetos XMLTable na coleção Tables do XMLAdapter. ApplyDiffgram ignora objetos XMLField quando a propriedade Alias do XMLField está vazia.

O Visual FoxPro verifica a propriedade Keyfield do XMLField ao executar ApplyDiffgram.

> **Dica:** Quando você usa atualização automática, deve definir as propriedades XMLField Keyfield apropriadas na coleção Fields como True (.T.) para melhorar o desempenho de atualização.

O Visual FoxPro altera as propriedades de um CursorAdapter personalizado da seguinte forma:
 - Se a propriedade Tables estiver vazia, o Visual FoxPro a define como a tabela especificada pelo parâmetro cAlias.
- O Visual FoxPro define a propriedade SendUpdates como True (.T.).
- Se a propriedade DataSource estiver vazia, o Visual FoxPro a define como "Native".
- Se a propriedade KeyFieldList estiver vazia, o Visual FoxPro adiciona campos-chave somente se especificados. Caso contrário, o Visual FoxPro adiciona todos os campos.
- Se KeyFieldList for modificado, o Visual FoxPro define a propriedade WhereType como Key Fields (DB_KEY ou 1).
- Se a propriedade UpdatableFieldList estiver vazia, o Visual FoxPro adiciona todos os campos.
- Se a propriedade UpdateNameList estiver vazia, o Visual FoxPro adiciona todos os campos e usa a tabela especificada pelo parâmetro cAlias como tabela base.

Após aplicar o DiffGram, o Visual FoxPro restaura todos os valores de propriedade listados aos seus estados anteriores.

O parâmetro nCodePage deve existir na lista de code pages suportados. Se nCodePage for zero (0) e a propriedade UseCodePage for False (.F.), o code page padrão atual é usado. Para obter mais informações, consulte Code Pages Supported by Visual FoxPro e a propriedade UseCodePage.

O método ApplyDiffgram falha se expressões XPath são usadas para objetos XMLAdapter ou XMLTable.
