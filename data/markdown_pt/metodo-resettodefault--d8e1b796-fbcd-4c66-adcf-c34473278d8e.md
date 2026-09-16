# Método ResetToDefault

Restaura uma propriedade, evento ou método à sua configuração padrão do Visual FoxPro. Disponível em tempo de execução e em tempo de design.

```foxpro
 [Form.]Object.ResetToDefault(cPropertyName | cEventName | cMethodName)
```

# Valor de retorno
 **cPropertyName**
Especifica o nome da propriedade a ser redefinida para a configuração padrão do Visual FoxPro.
**cEventName**
Especifica o nome do evento a ser redefinido. Todo o código definido pelo usuário no evento é excluído.
**cMethodName**
Especifica o nome do método a ser redefinido. Todo o código definido pelo usuário no método é excluído.

# Observações

Aplica-se a: controle CheckBox | classe Collection | objeto Column | controle ComboBox | controle CommandButton | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | objeto Cursor | classe CursorAdapter | objeto Custom | objeto DataEnvironment | controle EditBox | classe Exception (Visual FoxPro) | objeto Form | objeto FormSet | controle Grid | objeto Header | controle Image (Visual FoxPro) | controle Label (Visual FoxPro) | controle Line | controle ListBox | controle OLE Bound | controle OLE Container | controle OptionButton | controle OptionGroup | objeto Page | controle PageFrame | objeto ProjectHook | objeto Relation | objeto ReportListener | variável de sistema _SCREEN | controle Shape | objeto Session | controle Spinner | controle TextBox (Visual FoxPro) | controle Timer | objeto ToolBar

ResetToDefault retorna uma propriedade à configuração que tinha quando foi criada pela primeira vez. Por exemplo, se você alterou a fonte de um botão de comando, chamar este método para a legenda redefine a fonte para o padrão (Arial).

ResetToDefault remove todo o código definido pelo usuário de um evento ou método em tempo de design.

ResetToDefault não tem efeito em matrizes de membros, pois não há valor padrão em uma classe.

ResetToDefault não se aplica a métodos Access/Assign, pois estes estão mais intimamente ligados à propriedade associada e, portanto, são tratados de forma diferente dos métodos normais.
