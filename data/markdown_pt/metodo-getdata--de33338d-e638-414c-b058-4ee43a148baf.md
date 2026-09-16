# Método GetData

Recupera dados do objeto DataObject de arrastar e soltar OLE. Disponível somente em tempo de execução.

```foxpro
oDataObject.GetData(nFormat | cFormat [, @ArrayName])
```

#### Parâmetros
 **nFormat | cFormat**
Especifica o formato dos dados a recuperar. A tabela a seguir lista os valores de cada formato de dados e uma descrição de cada formato. O DataObject oferece suporte automaticamente aos seguintes formatos (mais formatos estão disponíveis, mas podem exigir programação adicional para uso). Para obter mais informações sobre os formatos de dados disponíveis, consulte a documentação do Visual C++® no Microsoft Developer Network. Formato de dados* nFormat | cFormat Descrição CF_TEXT 1 Formato de texto. CF_OEMTEXT 7 Formato de texto contendo caracteres no conjunto de caracteres OEM. CF_UNICODETEXT 13 Formato de texto Unicode Observação Disponível somente para versões do Visual FoxPro em execução no Windows NT 4.0 ou posterior. CF_FILES ou CF_HDROP 15 Um identificador que representa uma lista de arquivos, como um conjunto de arquivos arrastados do Windows Explorer. CF_LOCALE 16 Um identificador para o identificador de localidade associado ao texto na área de transferência. CFSTR_OLEVARIANTARRAY "OLE Variant Array" Um array do Visual FoxPro. Vários valores podem ser transferidos em uma única operação de arrastar e soltar com este formato. Por exemplo, este formato pode ser usado para arrastar um conjunto de itens em uma caixa de listagem para outra caixa de listagem. CFSTR_OLEVARIANT "OLE Variant" Uma variante do Visual FoxPro. Todos os tipos de dados no Visual FoxPro são representados como variantes. Este formato pode ser usado para arrastar e soltar dados do Visual FoxPro sem perder o tipo de dados. CFSTR_VFPSOURCEOBJECT "VFP Source Object" Uma referência a um objeto do Visual FoxPro. * Definido em FOXPRO.H.
**@ArrayName**
Especifica o nome do array no qual os dados são armazenados quando os dados podem conter vários valores. Os únicos formatos de dados nos quais os dados podem conter vários valores são CF_FILES, CF_HDROP e CFSTR_OLEVARIANTARRAY. Por exemplo, você pode arrastar um conjunto de arquivos do Windows Explorer para uma caixa de listagem do Visual FoxPro. Use o método GetData no evento OLEDragDrop da caixa de listagem para colocar os nomes dos arquivos em um array e, em seguida, use o método AddItem em um loop FOR ... ENDFOR para adicionar o conteúdo do array à caixa de listagem. O array deve existir antes de você especificar seu nome no método GetData. Se o array existir e não for grande o suficiente para conter os dados, o Visual FoxPro aumenta automaticamente o tamanho do array. Se o array for maior do que o necessário, o Visual FoxPro trunca o array.

# Observações

Aplica-se a: objeto DataObject

O valor retornado pelo método GetData é determinado pelo formato dos dados especificado com nFormat ou cFormat. False (.F.) é retornado se o DataObject não contiver dados no formato que você especificar com nFormat ou cFormat. True (.T.) é retornado quando os dados estão em um formato de vários valores, como CF_FILES, CF_HDROP ou CFSTR_OLEVARIANTARRAY. Os dados no DataObject são retornados quando os dados estão em um formato de valor único, como CF_TEXT, CFSTR_OLEVARIANT ou CFSTR_VFPSOURCEOBJECT.

O evento OLESetData para uma origem de arrastar é acionado se o formato de dados que você especificar com nFormat ou cFormat existir, mas não houver dados no DataObject para esse formato. (O método SetFormat pode ser usado para especificar um formato de dados antes que os dados correspondentes sejam colocados no DataObject com o método SetData.)
