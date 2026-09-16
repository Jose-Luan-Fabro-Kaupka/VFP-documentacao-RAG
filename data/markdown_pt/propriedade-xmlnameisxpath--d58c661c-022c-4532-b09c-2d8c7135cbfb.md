# Propriedade XMLNameIsXPath

Especifica se a propriedade XMLName contém uma expressão XPath. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
XMLTable.XMLNameIsXPath = [lValue]
```

# Valor da propriedade/Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue. lValue Descrição False (.F.) (Padrão) A propriedade XMLName não contém expressões XPath. True (.T.) A propriedade XMLName contém uma expressão XPath.

# Observações

Aplica-se a: XMLAdapter Class | XMLTable Class | XMLField Class

Se você alterar a propriedade de True (.T.) para False (.F.), pode ocorrer um erro se o valor da propriedade XMLName Property contiver caracteres de espaço em branco.

Para obter mais informações sobre expressões XPath, consulte a XPath Reference no Microsoft Core XML Services 4.0 (MSXML4) SDK na biblioteca MSDN em http://msdn.microsoft.com/library.
