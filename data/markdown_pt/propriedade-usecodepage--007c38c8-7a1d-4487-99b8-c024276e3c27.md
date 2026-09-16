# Propriedade UseCodePage

Especifica se o objeto XMLAdapter deve usar uma lógica especial para determinar qual página de código será usada na codificação ou decodificação de dados. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
XMLAdapter.UseCodePage = lValue
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. False (.F.) é o padrão; consulte a tabela abaixo para conhecer o efeito da configuração de UseCodePage como False (.F.) ou True (.T.).

# Observações

Aplica-se a: classe XMLAdapter

Quando a propriedade UseCodePage de XMLAdapter é True (.T.), o comportamento dos métodos ToCursor, ChangesToCursor e ApplyDiffgram muda da seguinte maneira:
 - XMLTable CodePage (ou XMLAdapter CodePage, se a página de código for zero) é usada como página de código do novo cursor, a menos que o parâmetro nCodePage seja passado.
- Quando um campo é preenchido, XMLField CodePage (ou a página de código do cursor, se for zero) é usada para decodificar dados Unicode. XMLField CodePage não precisa ser compatível com o Visual FoxPro. Por exemplo, a página de código 65001 pode ser usada para decodificar dados em UTF-8.

A tabela a seguir mostra como as configurações das propriedades UseCodePage, RespectCursorCP e UTF8Encoded afetam o método ToXML.

| RespectCursorCP | UTF8Encoded | UseCodePage=.F. | UseCodePage=.T. |
| --- | --- | --- | --- |
| False (.F.) | False (.F.) | A página de código Windows 1252 é usada como atributo de codificação do documento XML. Dados de caracteres são convertidos para a página de código padrão atual, exceto em campos marcados como NOCPTRANS. Dados Unicode são convertidos usando a página de código 1252. | Idêntico a UseCodePage = .F. |
| True (.T.) | False (.F.) | A página de código do cursor é usada como atributo de codificação do documento XML. Dados de caracteres não são convertidos; são usados os dados brutos da tabela. Dados Unicode são convertidos usando a página de código do cursor. | Idêntico a UseCodePage = .F. No entanto, será gerado um erro se XMLField CodePage for maior que zero e não corresponder à página de código do cursor. |
| False (.F.) | True (.T.) | A página de código UTF-8 é usada como atributo de codificação do documento XML. Dados de caracteres são convertidos para a página de código padrão atual, exceto em campos marcados como NOCPTRANS, e não ocorre conversão adicional para UTF-8. Dados Unicode são convertidos usando UTF-8. | Idêntico a UseCodePage = .F. |
| True (.T.) | True (.T.) | A página de código UTF-8 é usada como atributo de codificação do documento XML. Dados de caracteres são convertidos para a página de código padrão atual, exceto em campos marcados como NOCPTRANS. Esses campos são convertidos para UTF-8 usando a página de código especificada por SYS(3005) - Set Locale ID. Dados Unicode são convertidos usando UTF-8. | A página de código UTF-8 é usada como atributo de codificação do documento XML. Dados brutos de caracteres da tabela são convertidos para UTF-8 usando a página de código do cursor ou XMLField CodePage, se for maior que zero. Dados Unicode são convertidos usando UTF-8. |
