# Criação de interfaces de documento único e múltiplo

O Visual FoxPro permite criar dois tipos de aplicativos:
 - Aplicativos de interface de documento múltiplo (MDI) consistem em uma única janela principal, e as janelas do aplicativo estão contidas dentro ou flutuam sobre a janela principal. O Visual FoxPro é principalmente um aplicativo MDI, com a janela Command, janelas de edição e janelas de designer contidas na janela principal do Visual FoxPro.
- Aplicativos de interface de documento único (SDI) consistem em uma ou mais janelas independentes, cada uma das quais aparece separadamente na área de trabalho do Windows. O Microsoft Exchange é um exemplo de aplicativo SDI, no qual cada mensagem que você abre aparece em sua própria janela independente.

Um aplicativo consistindo em uma única janela geralmente é um aplicativo SDI, mas alguns aplicativos misturam elementos SDI e MDI. Por exemplo, o Visual FoxPro exibe seu depurador como um aplicativo SDI, que por sua vez contém janelas MDI próprias.

Para suportar ambos os tipos de interfaces, o Visual FoxPro permite criar vários tipos de formulários:
 - Child form . Um formulário contido em outra janela, usado na criação de aplicativos MDI. Formulários filhos não podem ser movidos fora dos limites de seu formulário pai (o formulário principal) e, quando minimizados, aparecem na parte inferior de seu formulário pai. Se seu formulário pai for minimizado, eles são minimizados junto com ele.
- Floating form . Um formulário que pertence a um formulário pai (principal), mas não está contido nele. Em vez disso, formulários flutuantes podem ser movidos para qualquer lugar na tela. Eles não podem ser movidos para trás de sua janela pai. Se minimizados, um formulário flutuante aparece na parte inferior da área de trabalho. Se seu formulário pai for minimizado, formulários flutuantes são minimizados junto com ele. Formulários flutuantes também são usados na criação de aplicativos MDI.
- Top-level form . Um formulário independente sem formulário pai, usado para criar um aplicativo SDI ou para servir como pai de outros formulários filhos em um aplicativo MDI. Formulários de nível superior operam no mesmo nível que outros aplicativos Windows e podem aparecer na frente ou atrás deles. Eles aparecem na barra de tarefas do Windows.
 Formulários filho, flutuantes e de nível superior
