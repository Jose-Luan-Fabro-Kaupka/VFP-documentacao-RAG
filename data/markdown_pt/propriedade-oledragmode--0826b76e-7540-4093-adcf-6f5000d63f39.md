# Propriedade OLEDragMode

Especifica como uma operação de arrastar é iniciada. Disponível em tempo de design e de execução.

```foxpro
Object.OLEDragMode[= nValue]
```

# Valor de retorno
 **nValue**
Especifica como o controle ou objeto trata operações de arrastar OLE. A lista a seguir apresenta as configurações de nValue. Configuração Descrição 0 Manual (Padrão). O Visual FoxPro não inicia a operação de arrastar OLE quando você tenta arrastar dados. Você deve chamar o método OLEDrag para iniciar a operação. Definir OLEDragMode como 0 oferece compatibilidade com versões anteriores (sem suporte para arrastar OLE) às aplicações existentes, caso você não inclua código adicional para a operação. 1 Automatic O Visual FoxPro inicia automaticamente uma operação de arrastar quando você tenta arrastar dados.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

OLEDragMode é uma propriedade da origem da operação de arrastar. Se a propriedade DragMode de um controle ou objeto estiver definida como 1 – Automatic, o controle ou objeto não poderá atuar como uma origem de arrastar OLE. Isso oferece compatibilidade com o suporte anterior a operações de arrastar e soltar em versões anteriores do Visual FoxPro.

Observe que a propriedade OLEDragMode é somente leitura para o controle Grid.
