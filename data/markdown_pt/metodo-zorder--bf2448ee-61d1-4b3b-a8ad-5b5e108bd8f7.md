# Método ZOrder

Posiciona um formulário ou controle especificado na frente ou atrás na ordem z dentro de seu nível gráfico. Posiciona um controle contido pelo objeto ToolBar na frente ou atrás da matriz de controles que determina a ordem em que os controles aparecem na barra de ferramentas.

```foxpro
 [Object.]ZOrder([nOrder])
```

# Valor de retorno
 **nOrder**
Especifica um inteiro que indica a posição do objeto em relação a outros objetos. Se você omitir nOrder, a configuração é 0. Configuração Descrição 0 (Padrão) O objeto é posicionado na frente da ordem z. 1 O objeto é posicionado atrás na ordem z.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

Existem duas camadas gráficas associadas a objetos. A camada de fundo é o espaço de desenho, onde aparecem os resultados dos métodos gráficos, e a camada da frente é a camada de objetos. O conteúdo de uma camada cobre o conteúdo da camada atrás. O método ZOrder organiza objetos apenas dentro da camada em que o objeto aparece.

> **Observação:** Para um objeto Page, o método ZOrder não afeta a configuração da propriedade PageOrder. ZOrder determina apenas qual Page está no topo e ativa.

Para obter mais informações sobre o uso de controles, consulte Usando controles.
