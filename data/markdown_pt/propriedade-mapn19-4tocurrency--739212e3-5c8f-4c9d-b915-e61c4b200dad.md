# Propriedade MapN19_4ToCurrency

Especifica se o tipo XML xsd:decimal deve ser mapeado para o tipo de dados Currency do Visual FoxPro quando as facetas XML totalDigits e fractionDigits são 19 e 4, respectivamente. Você pode definir a propriedade MapN19_4ToCurrency para preservar a precisão. Leitura/gravação.

MapN_4ToCurrency se aplica apenas ao executar os métodos LoadXML e Attach, que recuperam XML de acordo com sua configuração.

```foxpro
XMLAdapter.MapN19_4ToCurrency [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores de lValue. lValue Descrição False (.F.) Não mapeia xsd:decimal para Currency. (Padrão) True (.T.) Mapeia xsd:decimal para Currency. As facetas XML totalDigits e fractionDigits devem ser 19 e 4, respectivamente.

# Observações

Aplica-se a: XMLAdapter Class

Por padrão, o Visual FoxPro mapeia xsd:decimal para Numeric. No entanto, você pode manter a precisão do tipo currency mapeando xsd:decimal para Currency em vez de Numeric. Por exemplo, campos currency do SQL Server são representados em XML como decimal 19,4 com 19 dígitos totais e 4 dígitos após o ponto decimal.

Para obter mais informações sobre mapeamento de tipos de dados Visual FoxPro e XSD, consulte Visual FoxPro and XML Schema Data Type Mapping.

# Exemplo

O exemplo a seguir mostra como o tipo de esquema XML simpleType, conforme definido, é mapeado para Currency no Visual FoxPro:

```foxpro
<xsd:simpleType>
   <xsd:restriction base="xsd:decimal">
   <xsd:totalDigits value="19"/>
   <xsd:fractionDigits value="4"/>
   </xsd:restriction>
   </xsd:simpleType>
```
