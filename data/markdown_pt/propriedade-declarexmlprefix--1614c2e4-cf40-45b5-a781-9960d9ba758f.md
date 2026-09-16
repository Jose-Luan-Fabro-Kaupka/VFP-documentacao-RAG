# Propriedade DeclareXMLPrefix

Especifica se o objeto XMLAdapter declara um XMLPrefix para o objeto envolvido na análise. Leitura/gravação em tempo de design e execução.

```foxpro
XMLAdapter.DeclareXMLPrefix = lValue
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. Valores: False (.F.) (padrão), uma propriedade de prefixo de namespace XML não é declarada; True (.T.), um XMLPrefix é declarado para o objeto.

# Observações

Aplica-se a: classe XMLTable | classe XMLTable

Se quiser que XMLAdapter declare prefixos para os objetos envolvidos na análise, defina DeclareXMLPrefix além de XMLNamespace e XMLPrefix. Se RespectNesting for True (.T.), os seguintes objetos participarão da análise: XMLAdapter, o objeto XMLTable de destino e seus ancestrais.

Se XMLNamespace ou XMLPrefix estiver vazio, DeclareXMLPrefix será ignorada.

Se quiser declarar um namespace para todas as operações de análise, especifique XMLNamespace com XMLPrefix em SelectionNamespaces.
