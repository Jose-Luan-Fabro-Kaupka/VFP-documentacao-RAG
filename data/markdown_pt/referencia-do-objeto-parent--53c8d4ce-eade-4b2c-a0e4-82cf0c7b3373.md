# Referência do objeto Parent

Referencia o objeto contêiner de um controle. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Control.Parent
```

# Observações

Aplica-se a: Controle CheckBox | Classe Collection | Objeto Column | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Classe CursorAdapter | Objeto Custom | Controle EditBox | Classe Exception (Visual FoxPro) | Objeto Form | Controle Grid | Objeto Header | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Objeto Project (Visual FoxPro) | Objeto ProjectHook | Objeto Separator | Objeto Session | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Controle Timer | Objeto ToolBar

Use a palavra-chave Parent para acessar as propriedades, métodos ou controles do objeto contêiner de um controle. Você também pode usar a referência do objeto Parent para acessar o objeto contêiner de uma página ou formulário.

A palavra-chave Parent é útil em uma aplicação na qual você passa controles como argumentos. Por exemplo, você pode passar uma variável de controle para um procedimento geral e usar a referência do objeto Parent para acessar seu objeto contêiner.

Você também pode usar a referência do objeto Parent para objetos em uma classe de controle que foram colocados em um formulário desconhecido.
