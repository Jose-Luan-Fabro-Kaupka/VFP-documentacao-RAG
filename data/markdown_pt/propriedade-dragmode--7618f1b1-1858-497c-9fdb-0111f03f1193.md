# Propriedade DragMode

Especifica o modo de arrastar manual ou automático para uma operação de arrastar e soltar. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.DragMode[ = nMode]
```

# Valor de retorno
 **nMode**
As configurações da propriedade DragMode são: Configuração Descrição 0 (Padrão) Manual. Requer o uso do método Drag para iniciar o arrastar do controle de origem. 1 Automático. Clicar no controle de origem inicia automaticamente o arrastar.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro)

Quando DragMode está definido como 0 (Manual), o controle responde a eventos do mouse e o método Drag deve ser usado para iniciar operações de arrastar.

Quando DragMode está definido como 1 (Automático), o controle não responde a eventos do mouse e as operações de arrastar começam automaticamente quando o usuário pressiona e mantém o botão primário (esquerdo) do mouse sobre o controle.

Soltar o botão do mouse enquanto o ponteiro do mouse está sobre um controle de destino ou formulário durante uma operação de arrastar gera um evento DragDrop para o objeto de destino e encerra a operação de arrastar. Arrastar também pode disparar um evento DragOver.

> **Observação:** Enquanto um controle está sendo arrastado, ele não recebe outros eventos de mouse ou teclado iniciados pelo usuário (KeyPress, MouseDown, MouseMove ou MouseUp).
