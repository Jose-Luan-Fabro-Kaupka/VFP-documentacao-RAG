# Acoplando formulários

Você pode acoplar formulários da mesma maneira que acopla barras de ferramentas. Entretanto, ao contrário das barras de ferramentas acopladas, os formulários acoplados são redimensionados para preencher a área de acoplamento do item ao qual estão acoplados, mas somente as dimensões afetadas são alteradas. Por exemplo, se você acoplar um formulário à borda direita do objeto de destino, a largura do formulário não será alterada.

Você pode acoplar por vínculo ou por guia formulários definidos pelo usuário dentro das janelas da IDE do Visual FoxPro. Um formulário é acoplado por vínculo a outro quando eles compartilham um contêiner. Um formulário é acoplado por guia a outro quando exibem guias nas quais você pode clicar para exibir cada formulário. Enquanto o formulário estiver acoplado, os controles nele ainda poderão receber o foco. Quando um formulário é acoplado à borda da janela principal do Visual FoxPro, sua barra de título é exibida com metade da altura.

> **Observação:** Ao contrário das janelas do Visual FoxPro, o Visual FoxPro não salva as configurações de acoplamento ao fechar um formulário definido pelo usuário. Você precisa fornecer código para executar essa tarefa.

Ao acoplar um formulário, o Visual FoxPro chama o evento Resize do formulário. Para obter mais informações, consulte Evento Resize.

Quando a propriedade Visible de um formulário é definida como .F. (False), o Visual FoxPro desacopla automaticamente o formulário e o oculta. Quando a propriedade Visible do formulário é definida como .T. (True), o Visual FoxPro tenta acoplá-lo no local original, se possível. Para obter mais informações, consulte Propriedade Visible (Visual FoxPro).

Você pode usar as seguintes funções, propriedades, métodos e eventos para recuperar o estado de acoplamento do formulário ou escrever código para eventos de acoplamento:
 - Função ADOCKSTATE( )
- Evento AfterDock
- Evento BeforeDock
- Método Dock
- Propriedade Dockable
- Propriedade Docked
- Método GetDockState
- Evento UnDock
