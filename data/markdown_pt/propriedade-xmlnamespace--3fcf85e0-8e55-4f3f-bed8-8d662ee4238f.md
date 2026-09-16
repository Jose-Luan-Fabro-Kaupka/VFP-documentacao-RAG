# Propriedade XMLNamespace

Contém o seguinte para os objetos especificados:

XMLAdapter: XMLNamespace contém o XML Namespace ao qual XMLAdapter XMLName pertence, se houver. Leitura/gravação.

XMLTable: XMLNamespace contém o XML Namespace ao qual XMLTable XMLName pertence. Se estiver vazio, a propriedade Namespace do XMLAdapter é usada em vez disso. Leitura/gravação.

> **Observação:** Somente os métodos ToCursor , ChangesToCursor e ApplyDiffgram do XMLTable usam o XMLTable XMLNameSpace . O XMLField XMLName deve pertencer ao mesmo namespace que XMLTable XMLName .

```foxpro
Object.XMLNamespace
```

# Valor de retorno

Tipo de dados caractere. XMLNamespace contém uma cadeia de caracteres Unicode ou está vazio ("") quando não preenchido.

> **Observação:** Antes de atribuir um valor de cadeia de caracteres a XMLNamespace , você deve converter o valor para Unicode. Você pode usar a função STRCONV( ) para atender a esse requisito.

# Observações

Aplica-se a: XMLAdapter Class | XMLTable Class

> **Observação:** O Visual FoxPro desconsidera a propriedade XMLTable XMLNamespace ao executar o método ToXML do XMLAdapter. Em vez disso, insere XMLTable XMLName e XMLField XMLName no XMLAdapter XMLNamespace .
