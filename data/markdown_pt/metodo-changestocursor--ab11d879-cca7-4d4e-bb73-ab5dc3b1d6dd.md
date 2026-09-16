# Método ChangesToCursor

Cria um cursor com buffer de tabela e o preenche com alterações, que vêm do DiffGram associado.

> **Observação:** ChangesToCursor é suportado apenas para objetos XMLTable na coleção Tables do XMLAdapter. ChangesToCursor ignora objetos XMLField quando a propriedade Alias do XMLField está vazia.

```foxpro
XMLTable.ChangesToCursor( [ cAlias [, lIncludeUnchangedData [, nCodePage ]]] )
```

#### Parâmetros
 **cAlias**
Especifica o nome do alias para o cursor a ser criado. O valor de cAlias assume como padrão a propriedade XMLTableAlias, inclusive quando cAlias é uma cadeia de caracteres vazia ("").
**lIncludeUnchangedData**
Especifica se deve incluir dados inalterados no cursor criado. A tabela a seguir lista os valores para lIncludeUnchangedData . lIncludeUnchangedData Descrição False (.F.) (Padrão) Não incluir dados inalterados no cursor criado. True (.T.) Incluir dados inalterados no cursor criado.
**nCodePage**
Inteiro maior que zero (0) especificando um code page. O valor padrão é zero (0).

# Observações

Aplica-se a: XMLTable Class

Ao mapear campos binários para tipos de dados Character, o Visual FoxPro preenche qualquer espaço em branco restante com caracteres 0x00 (CHR(0) ou zeros) após a decodificação.

O parâmetro nCodePage deve existir na lista de code pages suportados. Se nCodePage for zero (0) e a propriedade UseCodePage for False (.F.), o code page padrão atual é usado. Para obter mais informações, consulte Code Pages Supported by Visual FoxPro e a propriedade UseCodePage.

Se a propriedade RespectNesting do XMLAdapter for True (.T.), o nó para um registro inalterado deve ser um filho imediato do nó da tabela externa. Se a tabela não estiver aninhada, o nó deve ser um filho imediato do nó XMLAdapter.

O método ChangesToCursor falha se a propriedade XMLNameIsXPath for True (.T.) porque não suporta expressões XPath.
