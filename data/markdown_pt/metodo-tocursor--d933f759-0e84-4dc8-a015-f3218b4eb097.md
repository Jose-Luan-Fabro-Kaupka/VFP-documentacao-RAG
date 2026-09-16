# Método ToCursor

Cria um cursor especificado por XMLTable com os campos descritos pela coleção Fields de XMLTable e o carrega com dados do documento XML referenciado.

O método ToCursor é suportado apenas para objetos XMLTable na coleção Tables de XMLAdapter.

```foxpro
XMLTable.ToCursor( [ lAppend [, cAlias [, nCodePage ]]] )
```

#### Parâmetros
 **lAppend**
Especifica se deve anexar dados ou registros a um cursor existente especificado pelo parâmetro cAlias. A tabela a seguir lista os valores para lAppend . lAppend Descrição False (.F.) (Padrão) Não adiciona campos a um cursor existente. True. (.T.) Adiciona campos a um cursor existente.
**cAlias**
Especifica o alias para o cursor de destino. O valor de cAlias assume por padrão a propriedade XMLTableAlias, inclusive quando cAlias é uma cadeia de caracteres vazia ("").
**nCodePage**
Especifica uma página de código. O valor padrão é zero (0).

# Observações

Aplica-se a: classe XMLTable

Se a propriedade Alias de XMLField estiver vazia, o método ToCursor de XMLTable ignora objetos XMLField e cria um cursor que não inclui nenhum campo especificado por esses objetos XMLField.

O parâmetro nCodePage deve existir na lista de páginas de código suportadas. Se nCodePage é zero (0) e a propriedade UseCodePage é False (.F), a página de código padrão atual é usada. Para obter mais informações, consulte Páginas de código suportadas pelo Visual FoxPro e a Propriedade UseCodePage.

Quando você usa ToCursor para anexar dados, o Visual FoxPro adiciona uma linha vazia se nenhum nome de objeto XMLField corresponder a qualquer coluna do cursor.

Ao mapear campos binários para tipos de dados Character, o Visual FoxPro preenche qualquer espaço em branco restante com caracteres 0x00 (CHR(0) ou zeros) após a decodificação.

Se a propriedade RespectNesting de XMLAdapter é True (.T.), o nó deve ser um filho imediato do nó da tabela externa. Se a tabela não estiver aninhada, o nó deve ser um filho imediato do nó de XMLAdapter.

O método ToCursor falha se a propriedade XMLAdapter.XMLNameIsXPath é True (.T.) e XMLAdapter.IsDiffgram é True (.T.).
