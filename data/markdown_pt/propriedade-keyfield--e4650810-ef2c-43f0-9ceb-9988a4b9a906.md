# Propriedade Keyfield

Especifica se o campo é um campo chave.

Keyfield se aplica somente ao executar o método ApplyDiffgram do XMLTable. Você pode definir esta propriedade quando desejar; o Visual FoxPro não define esta propriedade.

```foxpro
XMLField.Keyfield [= lValue]
```

# Valor de retorno

Tipo de dados lógico. A tabela a seguir lista os valores para lValue.

| lValue | Descrição |
| --- | --- |
| False (.F.) | O campo não é um campo chave. (Padrão) |
| True (.T.) | O campo é um campo chave. |

# Observações

Aplica-se a: XMLField Class
