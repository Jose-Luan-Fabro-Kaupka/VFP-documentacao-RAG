# Método AddTableSchema

Adiciona um novo objeto XMLTable à coleção Tables de XMLAdapter e os objetos XMLField necessários à coleção Fields de XMLTable, com base no alias de tabela especificado.

Os seguintes parâmetros devem ser convertidos em Unicode antes de serem passados como parâmetros para AddTableSchema:
 - cXMLName
- cXMLNamespace
- cXMLPrefix

Você pode usar a função STRCONV( ) para realizar essa conversão.

```foxpro
XMLAdapter.AddTableSchema(cAlias [, lElementBased [, cXMLName
   [, cXMLNamespace [, cXMLPrefix [, lWrapMemoInCDATA
   [, lWrapCharacterInCDATA[, lAutoNest]]]]]]])
```

#### Parâmetros
 **cAlias**
Especifica o alias da tabela ou do cursor do Visual FoxPro a ser usado como modelo de esquema.
**lElementBased**
Especifica o estilo do XML. O valor padrão de lElementBased é verdadeiro (.T.).
**cXMLName**
Especifica o nome a ser usado para a tabela no XML e deve ser convertido em Unicode antes de ser passado como parâmetro. O valor padrão do parâmetro cXMLName é o valor do parâmetro cAlias. A conversão em Unicode é realizada automaticamente.
**cXMLNamespace**
Especifica o namespace XML a ser usado, que deve ser convertido em Unicode antes de ser passado como parâmetro. O valor padrão é uma cadeia de caracteres vazia ("").
**cXMLPrefix**
Especifica o prefixo XML a ser usado, que deve ser convertido em Unicode antes de ser passado como parâmetro. O valor padrão é uma cadeia de caracteres vazia ("").
**lWrapMemoInCDATA**
Especifica se campos Memo devem ser envolvidos em seções CDATA. O valor padrão é especificado pela propriedade WrapMemoInCDATA do objeto XMLAdapter.
**lWrapCharacterInCDATA**
Especifica se campos Character devem ser envolvidos em seções CDATA. O valor padrão é especificado pela propriedade WrapCharInCDATA do objeto XMLAdapter.
**lAutoNest**
Especifica se as tabelas adicionadas à coleção Tables de XMLAdapter são aninhadas automaticamente. O valor padrão é especificado pela propriedade RespectNesting do objeto XMLAdapter.

# Observações

Aplica-se a: classe XMLAdapter

As seguintes configurações de propriedade afetam a execução do método AddTableSchema:
 - DisableEncode
- NoCpTrans
- WrapCharInCDATA
- WrapMemoInCDATA

Se lAutoNest estiver definido como verdadeiro (.T.), o aninhamento dos objetos XMLTable na coleção Tables de XMLAdapter ocorrerá depois que o novo objeto XMLTable for adicionado. O relacionamento especificado com o comando SET RELATION e a propriedade Alias de XMLTable determinam o esquema de aninhamento.
 - Tabelas pai: o primeiro objeto XMLTable com um valor da propriedade Alias que corresponda ao Alias de um cursor pai em qualquer relacionamento com a nova tabela torna-se o objeto XMLTable pai da nova tabela, e o novo objeto XMLTable torna-se o último objeto aninhado.
- Tabelas aninhadas: quaisquer objetos XMLTable com um alias correspondente ao alias de um cursor filho em qualquer relacionamento a partir da nova tabela tornam-se objetos XMLTable aninhados no novo objeto XMLTable, a menos que já estejam aninhados.
