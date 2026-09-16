# Propriedade UpdateGramSchemaLocation

Especifica o nome e a localização do esquema de mapeamento passados para a função XMLUPDATEGRAM( ). Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** UpdateGramSchemaLocation se aplica somente quando CursorAdapter DataSourceType é "XML". Quando especificado, UpdateGramSchemaLocation é passado para o parâmetro SchemaLocation em XMLUPDATEGRAM( ). O Visual FoxPro não oferece suporte à criação de esquemas de mapeamento; portanto, você deve fornecer um.

```foxpro
CursorAdapter.UpdateGramSchemaLocation [= cName]
```

# Valor de retorno
 **cName**
Tipo de dados Character. O parâmetro cName especifica um nome e localização de esquema de mapeamento, e o valor padrão é uma cadeia de caracteres vazia ("").

# Observações

Aplica-se a: Classe CursorAdapter
