# OLEDropMode Propriedade

Especifica como um destino de descarte gerencia operações de descarte OLE. Disponível em tempo de design e tempo de execução.

```foxpro
Object.OLEDropMode[= nValue]
```

# Valor de retorno
 **nValue**
Especifica como o objeto the de controle or manipula as operações de eliminação OLE. A tabela a seguir lista as configurações para nValue . nValue Constante Foxpro.h Descrição 0 DROP_DISABLED Desativado (padrão). Os dados não podem ser descartados no objeto de controle the or e nenhum evento de destino de descarte ocorre. O ponteiro do mouse No Drop é exibido quando o ponteiro do mouse é posicionado sobre o objeto de controle the or. Definir OLEDropMode como 0 fornece compatibilidade com versões anteriores (sem suporte para drop OLE) para aplicativos existentes. 1 DROP_ENABLED Habilitado. O Visual FoxPro permite a eliminação de dados no objeto de controle the or e ocorrem eventos de destino de eliminação. 2 DROP_PASSTOCONTAINER Passe para o contêiner. O objeto The de controle or se comporta como se estivesse desativado para operações de descarte OLE e os dados são descartados no contêiner para o objeto the de controle or. A propriedade OLEDropMode do contêiner deve ser definida como 1 ou 2 para aceitar os dados. O ponteiro do mouse No Drop é exibido se a propriedade OLEDropMode do contêiner estiver definida como 0.

# Observações
Aplica-se a: CheckBox Controle | ComboBox Controle | CommandButton Controle | CommandGroup Controle | Container Objeto | Control Objeto (Visual FoxPro) | EditBox Controle | Form Objeto | Grid Controle | Image Controle (Visual FoxPro) | Label Controle (Visual FoxPro) | Line Controle | ListBox Controle | OptionButton Controle | OptionGroup Controle | Page Objeto | PageFrame Controle | ProjectHook Objeto | Shape Controle | Spinner Controle | TextBox Controle (Visual FoxPro) | ToolBar Objeto

OLEDropMode é uma propriedade drop target. Se a propriedade DropMode para o objeto a de controle or estiver definida como 0 – Desativado, o objeto the de controle or não poderá atuar como uma fonte de descarte OLE. Isso fornece compatibilidade com versões anteriores para suporte anterior de arrastar e soltar em versões anteriores do Visual FoxPro.

Se a propriedade Enabled do objeto a de controle or estiver definida como falsa (.F.), você não poderá eliminar dados no objeto the de controle or. Para operações de soltar, o ponteiro do mouse Sem Soltar é exibido quando a propriedade Enabled do objeto de controle a or é definida como falsa (.F.).
