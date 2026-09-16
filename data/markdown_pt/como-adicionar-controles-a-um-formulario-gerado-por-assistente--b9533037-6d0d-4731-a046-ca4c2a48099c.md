# Como: adicionar controles a um formulário gerado por assistente

Se você criar um formulário com um dos assistentes de formulário e depois quiser adicionar controles a ele, pode corresponder ao estilo dos controles existentes usando os controles na biblioteca de controles do assistente, Wizstyle.vcx.

Quando você abre a biblioteca de controles do assistente, controles no estilo do assistente (como `chiselfield`, `embossedmemo` e assim por diante) estão disponíveis na barra de ferramentas Form Controls. Para descobrir qual controle usar, selecione um controle existente e observe sua classe e biblioteca de classes. Por exemplo, um campo padrão do assistente estaria na classe `Standardfield`, encontrada em Wizstyle.vcx.

> **Dica:** Use ToolTips na barra de ferramentas Form Controls para ajudá-lo a identificar nomes de classe.

### Para corresponder controles em um formulário gerado por assistente
- No Form Designer , abra o formulário.
- Na barra de ferramentas Form Controls, escolha o botão View Classes e escolha Add .
- Na caixa de diálogo Open, localize Wizstyle.vcx no subdiretório Wizards e escolha OK .
- Na barra de ferramentas Form Controls, selecione o controle que corresponde a um controle existente no formulário e arraste no formulário para adicioná-lo. Observação Se você mover um formulário para um novo diretório ou outro sistema, deve mover a biblioteca de controles associada ao formulário junto com ele.
