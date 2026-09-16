# Propriedade NoCpTrans

Especifica se os tipos de campo Character e Memo são criados como tipos de dados Character (Binary) ou Memo (Binary). Leitura/gravação. Há duas versões da sintaxe.

```foxpro
XMLAdapter.NoCpTrans [= lValue]
```

```foxpro
XMLField.NoCpTrans [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores para lValue. lValue Descrição False (.F.) Cria o campo como campo Character ou Memo normal. (Padrão) True (.T.) Cria o campo como campo Character (NoCpTrans) ou Memo (NoCpTrans).

# Observações

Aplica-se a: Classe XMLAdapter | Classe XMLField

Para obter mais informações sobre mapeamento de tipos de dados do Visual FoxPro e XSD, consulte Mapeamento de tipos de dados do Visual FoxPro e XML Schema.

Definir NoCpTrans no nível do XMLAdapter define os valores padrão de NoCpTrans para objetos XMLField que são criados e adicionados à coleção Fields pelos seguintes métodos do XMLAdapter:
 - LoadXML
- Attach
- AddTableSchema

Além disso, alterar NoCpTrans no nível do XMLAdapter afeta apenas o próximo conjunto de objetos XMLField criados, não os objetos XMLField existentes na coleção Fields. Portanto, para modificar a configuração de NoCpTrans para um objeto XMLField existente, altere o valor no nível do XMLField.
