# Método WriteMethod

Grava o texto especificado no método especificado. Disponível somente em tempo de design.

```foxpro
Control.WriteMethod(cMethodName, cMethodText [,lCreateMethod [, nVisibility [, cDescription]]])
```

#### Parâmetros
 **cMethodName**
Especifica o nome do método no qual gravar o texto especificado.
**cMethodText**
Especifica o texto a gravar nos métodos especificados.
**lCreateMethod**
Especifica se o método é criado quando ele ainda não existe. Como este método é útil somente em tempo de design, você deve salvar o formulário ou a classe antes que as alterações possam ter efeito.
**nVisibility**
Especifica a visibilidade do novo método. nVisibility Visibilidade 1 Public 2 Protected 3 Hidden
**cDescription**
Especifica uma descrição para o novo método. A descrição do método é limitada a 255 caracteres.

# Observações

Aplica-se a: Controle CheckBox | Classe Collection | Objeto Column | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Custom | Controle EditBox | Classe Exception (Visual FoxPro) | Objeto Form | Objeto FormSet | Controle Grid | Objeto Header | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Objeto ReportListener | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Controle Timer | Objeto ToolBar
