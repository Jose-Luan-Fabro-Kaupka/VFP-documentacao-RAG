# Método GetFormat

Determina se dados em um formato especificado estão disponíveis no DataObject de arrastar e soltar OLE. Disponível somente em tempo de execução.

```foxpro
oDataObject.GetFormat(nFormat | cFormat)
```

#### Parâmetros
 **nFormat | cFormat**
Especifica o formato dos dados a recuperar. A tabela a seguir lista alguns dos formatos com uma descrição de cada formato. Para obter mais informações sobre os formatos de dados disponíveis, consulte a documentação do Visual C++ na Microsoft Developer Network. Você também pode criar seu próprio formato especificando uma cadeia de caracteres exclusiva para cFormat . Formato de dados* nFormat | cFormat Descrição CF_TEXT 1 Formato de texto. CF_OEMTEXT 7 Formato de texto contendo caracteres no conjunto de caracteres OEM. CF_UNICODETEXT 13 Formato de texto Unicode. Observação Disponível somente para versões do Visual FoxPro executadas no Windows NT 4.0 ou posterior. CF_FILES ou CF_HDROP 15 Um identificador que identifica uma lista de arquivos, como um conjunto de arquivos arrastados do Windows Explorer. CFSTR_OLEVARIANTARRAY "OLE Variant Array" Uma matriz. Vários valores podem ser transferidos em uma única operação de arrastar e soltar com este formato. Por exemplo, este formato pode ser usado para arrastar um conjunto de itens em uma caixa de listagem para outra caixa de listagem. CFSTR_OLEVARIANT "OLE Variant" Uma variante. Todos os tipos de dados no Visual FoxPro são representados como variantes. Este formato pode ser usado para arrastar e soltar dados do Visual FoxPro sem perder o tipo de dados. CFSTR_VFPSOURCEOBJECT "VFP Source Object" Uma referência ao objeto de origem de arrastar do Visual FoxPro. * Definido em FOXPRO.H.

# Observações

Aplica-se a: DataObject Object

O método GetFormat retorna true (.T.) se o DataObject contém dados no formato que você especificar com nFormat ou cFormat; caso contrário, retorna false (.F.).
