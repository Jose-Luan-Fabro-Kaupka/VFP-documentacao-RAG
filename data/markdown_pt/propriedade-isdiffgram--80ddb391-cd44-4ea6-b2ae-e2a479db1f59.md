# Propriedade IsDiffGram

Indica se o objeto XMLAdapter está associado a um DiffGram do .NET. Leitura/gravação.

> **Observação:** Definir a propriedade IsDiffGram não altera de fato o documento XML associado.

```foxpro
XMLAdapter.IsDiffGram [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue. lValue Descrição False (.F.) O objeto XMLAdapter não é um DiffGram do .NET. (Padrão) True (.T.) O objeto XMLAdapter é um DiffGram do .NET.

# Observações

Aplica-se a: XMLAdapter Class

O XMLAdapter detecta se o XML importado é um DiffGram e define IsDiffGram. Ao criar e gerar XML a partir de tabelas e executar o método ToXML do XMLAdapter, o Visual FoxPro verifica IsDiffGram e cria XML consistente com essa configuração.
