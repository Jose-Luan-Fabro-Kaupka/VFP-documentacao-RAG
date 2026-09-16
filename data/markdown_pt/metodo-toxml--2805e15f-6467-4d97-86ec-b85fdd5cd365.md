# Método ToXML

Gera XML em um arquivo ou variável de memória.

```foxpro
XMLAdapter.ToXML( cXMLDocument [, cSchemaLocation [, lFile [, lIncludeBefore [, lChangesOnly ]]]] )
```

#### Parâmetros
 **cXMLDocument**
Especifica o arquivo ou o nome da variável de memória para o documento XML.
**cSchemaLocation**
Especifica o local de uma referência a um esquema externo. O valor padrão de cSchemaLocation é vazio (""). Se cSchemaLocation estiver vazio e um esquema externo foi gerado, o valor de XMLAdapterXMLSchemaLocation é usado como referência ao esquema externo.
**lFile**
Especifica se cXMLDocument é um arquivo. O valor padrão de lFile é False (.F.).
**lIncludeBefore**
Especifica se a seção diffgr:before deve ser incluída no DiffGram. A seção diffgr:before contém a versão original de uma linha. O valor padrão de lIncludeBefore é False (.F.). Se lIncludeBefore for True (.T.), o Visual FoxPro filtra registros excluídos, independentemente da configuração de filtro atual, como SET FILTER TO NOT DELETED( ) e SET DELETED ON ou OFF . Todos os registros excluídos no buffer da tabela são inseridos na seção diffgr:before, mas não possuem linha correspondente no bloco DataInstance do DiffGram. Embora você possa querer ocultar linhas excluídas usando um filtro, o DiffGram indica quais linhas foram excluídas para que a fonte de dados possa ser atualizada corretamente. O Visual FoxPro ignora lIncludeBefore se a propriedade IsDiffGram do XMLAdapter for False (.F.).
**lChangesOnly**
Especifica se o XML deve conter apenas alterações. O Visual FoxPro ignora lChangesOnly se a propriedade IsDiffGram do XMLAdapter for False (.F.) ou se lIncludeBefore for False (.F.).

# Observações

Aplica-se a: Classe XMLAdapter

Se a propriedade Alias do XMLTable estiver vazia, nenhum elemento XML é gerado para esse objeto XMLTable; no entanto, a tabela é incluída no esquema se um for gerado.

Para campos de caractere, o Visual FoxPro preenche qualquer espaço restante no campo com espaço em branco (0x20). Quando ToXML mapeia campos de caractere para campos binários e realiza codificação, ToXML codifica o espaço em branco à direita independentemente do valor da propriedade PreserveWhiteSpace do XMLAdapter.

As seguintes configurações de propriedade do XMLAdapter afetam como ToXML é executado:
 - Propriedade ForceCloseTag
- Propriedade FormattedOutput
- Propriedade PreserveWhiteSpace
- Propriedade RespectCursorCP
- Propriedade RespectNesting
- Propriedade UseCodePage
- Propriedade UTF8Encoded
- Propriedade XMLNameIsXPath
- Propriedade XMLSchemaLocation

XML aninhado Quando a propriedade RespectNesting do XMLAdapter é True (.T.) e uma relação entre as tabelas é especificada, ToXML gera XML aninhado. O aninhamento não é suportado se o parâmetro IChangesOnly estiver definido como True (.T.).

Codificação XML Quando a propriedade RespectCursorCP do XMLAdapter é True (.T.), UTF8Encoded do XMLAdapter é False (.F.) e dois ou mais aliases de tabela são referenciados na coleção Tables, essas tabelas devem usar a mesma página de código. Se você também definir a propriedade UseCodePage, os resultados gerados por ToXML variam. Consulte a propriedade UseCodePage para uma tabela que mostra os resultados.

Condições de overflow numérico Um objeto XMLAdapter não carrega XML contendo condições de overflow numérico do tipo Visual FoxPro, por exemplo, `*****.**`, no lugar de um valor Numeric ou Integer. O analisador Microsoft XML Core Services (MSXML) causa um erro semelhante ao seguinte:

```foxpro
Error 2110 (XML Error): XML Error: XML Parse error: The value of '***' is invalid according to its data type.
The element: 'myfield' has an invalid value according to its data type.
Line 7, Position 17.
   <myfield>***</myfield>
```

Se a propriedade XMLNameIsXpath for True (.T.) para o objeto XMLAdapter ou XMLTable e a propriedade XMLName não estiver vazia, ToXML falha. ToXML ignora objetos XMLField que usam expressões XPath.
