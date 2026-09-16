# Propriedade XMLSchemaLocation

Especifica informações de esquema.

XMLSchemaLocation se aplica apenas ao executar os seguintes métodos XMLAdapter:
 - LoadXML
- Attach
- ToXML

```foxpro
XMLAdapter.XMLSchemaLocation [= cValue]
```

# Valor de retorno

Tipo de dados Character. A tabela a seguir lista os valores de cValue.

| cValue | Descrição |
| --- | --- |
| "1" | LoadXML processa esquema inline ou externo, se referenciado no documento XML. ToXML gera esquema inline. (Padrão) |
| " schema location " | LoadXML processa esquema inline ou externo, se referenciado e acessível no documento XML. Caso contrário, o Visual FoxPro tenta carregar o esquema do " schema location " especificado. ToXML gera esquema externo no local especificado. |
| "" (Vazio) | LoadXML não: Processa nenhum esquema durante o carregamento. Altera a coleção Tables. Define a propriedade IsDiffGram. ToXML não gera nenhum esquema. |

# Observações

Aplica-se a: Classe XMLAdapter
