# Propriedade PreserveWhiteSpace

Preserva ou remove espaços em branco da saída XML. Leitura/gravação.

PreserveWhiteSpace se aplica somente ao executar os métodos LoadXML e ToXML do XMLAdapter, que respectivamente recuperam e criam XML consistente com essas configurações. PreserveWhiteSpace não se aplica a dados em uma seção CDATA.

```foxpro
XMLAdapter.PreserveWhiteSpace [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores para lValue. lValue Descrição False (.F.) Remove espaços em branco. (Padrão) True (.T.) Preserva espaços em branco.

# Observações

Aplica-se a: XMLAdapter Class
