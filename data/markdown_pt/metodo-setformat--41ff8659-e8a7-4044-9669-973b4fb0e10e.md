# Método SetFormat

Coloca um formato de dados no objeto OLE DataObject. Disponível apenas em tempo de execução.

Você pode chamar o método SetFormat nos eventos OLEStartDrag e OLESetData.

```foxpro
oDataObject.SetFormat(nFormat | cFormat)
```

#### Parâmetros
 **nFormat | cFormat**
Especifica o formato dos dados colocados no objeto DataObject. Você também pode criar seu próprio formato especificando uma cadeia de caracteres exclusiva para cFormat. A tabela a seguir lista valores para alguns formatos de dados comuns com uma descrição de cada formato. Formato de dados* nFormat | cFormat Descrição CF_TEXT 1 Formato de texto. CF_OEMTEXT 7 Formato de texto contendo caracteres no conjunto de caracteres OEM. CF_UNICODETEXT 13 Formato de texto Unicode. Observação Disponível apenas para versões do Visual FoxPro em execução no Windows NT 4.0 ou posterior. CF_FILES ou CF_HDROP 15 Um handle que identifica uma lista de arquivos, como um conjunto de arquivos arrastados do Windows Explorer. CFSTR_OLEVARIANTARRAY "OLE Variant Array" Uma matriz. Vários valores podem ser transferidos em uma única operação de arrastar e soltar com este formato. Por exemplo, este formato pode ser usado para arrastar um conjunto de itens em uma list box para outra list box. CFSTR_OLEVARIANT "OLE Variant" Uma variant. Todos os tipos de dados no Visual FoxPro são representados como variants. Este formato pode ser usado para arrastar e soltar dados do Visual FoxPro sem perder o tipo de dados. CFSTR_VFPSOURCEOBJECT "VFP Source Object" Uma referência ao objeto de origem de arrastar do Visual FoxPro. * Definido em FOXPRO.H.

# Observações

Aplica-se a: DataObject Object

Você pode colocar um formato de dados no objeto DataObject antes de colocar os dados correspondentes no objeto DataObject. Se você colocar um formato de dados no objeto DataObject sem dados correspondentes e invocar o método GetData no evento OLEDragDrop, o evento OLESetData é executado para a origem de arrastar. A origem de arrastar pode então colocar os dados no DataObject com o método SetData no evento OLESetData.

> **Dica:** Ao usar formatos de dados que não são nativamente suportados pelo Visual FoxPro ou ao usar um grande número de formatos, você pode melhorar o desempenho de arrastar e soltar OLE colocando apenas os formatos de dados no objeto DataObject quando uma grande quantidade de dados é colocada no objeto DataObject.
