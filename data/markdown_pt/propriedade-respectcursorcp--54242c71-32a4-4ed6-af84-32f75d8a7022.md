# Propriedade RespectCursorCP

Especifica se a página de código do cursor deve ser levada em consideração.

> **Observação:** A propriedade UTF8Encoded funciona em conjunto com a configuração de RespectCursorCP quando UTF8Encoded é True (.T.).

RespectCursorCP se aplica somente ao executar o método ToXML do XMLAdapter, que cria XML consistente com sua configuração.

Para obter mais informações sobre como páginas de código mapeiam para atributos de codificação XML, consulte Função CURSORTOXML( ).

```foxpro
XMLAdapter.RespectCursorCP [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores para lValue. lValue Descrição False (.F.) Cria XML com codificação Windows-1252 padrão. (Padrão) True (.T.) Define a codificação para a página de código do cursor.

# Observações

Aplica-se a: Classe XMLAdapter

Por exemplo, a tabela a seguir descreve como RespectCursorCP e UTF8Encoded interagem entre si.

| RespectCursorCP | UTF8Encoded | Conversão realizada |
| --- | --- | --- |
| False | False | Windows-1252 (Padrão) |
| True | False | Define o atributo de codificação de saída para a página de código do cursor. |
| False | True | Define o atributo de codificação de saída para UTF-8. Nenhuma tradução de caracteres ocorre. |
| True | True | Define o atributo de codificação de saída para UTF-8. Traduz dados de caracteres para UTF-8. |
| True | False | Define o atributo de codificação de saída para a página de código do cursor. |
