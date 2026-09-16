# Propriedade Width

Especifica a largura de um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Object.]Width[ = nWidth]
```

# Valor de retorno
 **nWidth**
Especifica a largura de um objeto.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Custom Object | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

Use as propriedades Height, Width, Left e Top para operações ou cálculos baseados na área total de um objeto, como dimensionar ou mover o objeto.

Para formulários e controles, os valores desta propriedade mudam conforme o objeto é dimensionado pelo usuário ou em código. As configurações máximas desta propriedade para todos os objetos dependem do sistema.

Para formulários, a propriedade Width especifica a largura externa do formulário, excluindo as bordas. Se a propriedade ScrollBars estiver definida para habilitar barras de rolagem, Width não inclui o espaço ocupado pela barra de rolagem quando ela aparece. No Visual FoxPro, a largura máxima de um formulário foi aumentada para aproximadamente 32.000 pixels.

Para controles, a propriedade Width é medida a partir do centro da borda do controle, de modo que controles com larguras de borda diferentes se alinhem corretamente.

> **Observação:** A propriedade Width é somente leitura quando se aplica a um controle contido em um objeto Column.

A propriedade Width é determinada na unidade de medida especificada pela configuração da propriedade ScaleMode.
