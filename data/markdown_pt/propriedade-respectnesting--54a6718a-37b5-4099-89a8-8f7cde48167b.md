# Propriedade RespectNesting

Especifica se o método ToXML deve aninhar tabelas com base na configuração da propriedade NestedInto e se o aninhamento deve ser respeitado durante a análise XML.

```foxpro
XMLAdapter.RespectNesting = [lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) Especifica que o método ToXML ignora a configuração da propriedade NestedInto. True (.T.) Especifica que o método ToXML aninha tabelas com base na propriedade NestedInto.

# Observações

Aplica-se a: XMLAdapter Class

Quando esta propriedade está definida como False (.F.), o comportamento do XMLAdapter é o mesmo que no Visual FoxPro 8.0. No entanto, quando RespectNesting está definido como True (.T.), o comportamento do Visual FoxPro 9.0 difere da seguinte forma:
 - Ao carregar um esquema .NET Dataset, o método LoadXML define as propriedades NestedInto, NextSiblingTable e FirstNestedTable para todos os objetos XMLTables com base nas informações de aninhamento do esquema.
- Os métodos ToCursor e ChangesToCursor (quando apenas registros inalterados são carregados) usam a seguinte lógica de análise: Se uma tabela está aninhada, seu nó deve ser um filho imediato do nó da tabela externa. Se uma tabela não está aninhada, seu nó deve ser um filho imediato do nó do XMLAdapter.
- Se o esquema é gerado, o método ToXML respeita as informações de aninhamento e gera esquema com aninhamento apropriado.
- Se o XML é gerado no modo diffgram + changes-only, um erro é gerado porque o formato aninhado não é suportado para esse modo.
- O método ToXML aninha os dados de forma apropriada. O aninhamento é feito com base nas informações de aninhamento e no relacionamento definido do cursor externo para o cursor aninhado. Observe que um relacionamento direto é necessário.
