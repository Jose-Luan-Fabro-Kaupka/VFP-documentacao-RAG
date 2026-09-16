# Propriedade OLEDropHasData

Especifica como uma operação de soltar é gerenciada. Disponível em tempo de execução e somente leitura em tempo de design.

```foxpro
Object.OLEDropHasData[= nDropEffect]
```

# Valor de retorno
 **nDropEffect**
Especifica como a operação de soltar é gerenciada. A tabela a seguir lista os valores de nDropEffect com uma descrição de cada um. nDropEffect Constante Foxpro.h Descrição –1 DROPHASDATA_VFPDETERMINE Padrão. O Visual FoxPro determina automaticamente se o DataObject contém dados em um formato que pode ser solto no destino de soltar. Se o DataObject contém dados em um formato adequado para o destino de soltar, os dados são soltos no destino de soltar. O Visual FoxPro manipula o ponteiro do mouse e a notificação da origem de arrastar. Se os dados não estiverem no formato adequado para o destino de soltar, o Visual FoxPro exibe o ponteiro do mouse No Drop, a operação de soltar é cancelada e a origem de arrastar é notificada de que a operação de soltar foi cancelada. 0 DROPHASDATA_NOTUSEFUL O DataObject não contém dados em um formato que pode ser solto no destino de soltar, e o ponteiro do mouse No Drop é exibido. 1 DROPHASDATA_USEFUL O DataObject contém dados em um formato que pode ser solto no destino de soltar.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | ProjectHook Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

OLEDropHasData é uma propriedade de destino de soltar e deve ser definida no evento OLEDragOver. Use GetFormat no evento OLEDragOver para determinar se o DataObject contém dados no formato adequado para o destino de soltar. Se os dados estiverem no formato adequado para o destino de soltar, defina OLEDropHasData como 1.
