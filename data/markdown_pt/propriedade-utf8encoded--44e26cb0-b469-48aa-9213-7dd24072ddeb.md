# Propriedade UTF8Encoded

Especifica se a codificação deve ser definida como Unicode Transformation Format-8 (UTF-8). UTF8Encoded funciona em conjunto com a propriedade RespectCursorCP.

UTF8Encoded se aplica somente ao executar o método ToXML do XMLAdapter, que cria XML consistente com sua configuração.

```foxpro
XMLAdapter.UTF8Encoded [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) Não define a codificação como UTF-8. (Padrão) True (.T.) Define a codificação como UTF-8.

# Observações

Aplica-se a: XMLAdapter Class

A codificação padrão para XML é UTF-8, enquanto para o Visual FoxPro a codificação padrão é Windows-1252. Quando você deseja enviar dados para XML, pode preservar a codificação UTF-8 definindo a codificação como UTF-8 e instruindo o Visual FoxPro a traduzir caracteres de byte duplo para a sequência de codificação UTF-8 adequada.

Se você tem um grupo de caracteres representando texto coreano ou chinês, pode converter esses caracteres para conjuntos de caracteres de byte duplo (DBCS) para visualizá-los no Visual FoxPro. Você pode então reconverter para UTF-8 ao transmiti-los pela Web como XML para que outros sistemas possam exibir corretamente os dados.

Por exemplo, a tabela a seguir descreve como RespectCursorCP e UTF8Encoded interagem entre si.

| RespectCursorCP | UTF8Encoded | Conversão realizada |
| --- | --- | --- |
| False | False | Windows-1252 (Padrão) |
| True | False | Define o atributo de codificação de saída para a página de código do cursor. |
| False | True | Define o atributo de codificação de saída como UTF-8. Nenhuma tradução de caractere ocorre. |
| True | True | Define o atributo de codificação de saída como UTF-8. Traduz dados de caractere para UTF-8. |
| True | False | Define o atributo de codificação de saída para a página de código do cursor. |
