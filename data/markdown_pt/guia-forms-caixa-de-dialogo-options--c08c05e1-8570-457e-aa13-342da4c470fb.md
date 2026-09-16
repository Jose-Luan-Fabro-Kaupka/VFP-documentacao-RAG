# Guia Forms, caixa de diálogo Options

Contém opções para o Form Designer.

Quando você escolhe Set As Default, que aparece em cada guia da caixa de diálogo, o Visual FoxPro salva as configurações de opção no registro (banco de dados de registro do sistema Windows).

> **Observação:** Se uma instância do Form Designer já estiver aberta quando você alterar configurações na guia Forms da caixa de diálogo Options, o Form Designer não reflete as alterações até que você feche essa instância e a reabra.

# Grid
 **Grid lines**
Especifica que o Form Designer exibe linhas de grade para ajudar a alinhar controles. Observação Estas são configurações padrão somente para novos formulários. As configurações de formulários existentes são salvas no arquivo de recursos.
**Snap to grid**
Especifica que, ao desenhar novos controles, suas bordas se alinham com as linhas de grade mais próximas. Observação Estas são configurações padrão somente para novos formulários. As configurações de formulários existentes são salvas no arquivo de recursos.
**Horizontal spacing (pixels)**
Especifica a largura do espaço entre linhas de grade horizontais. A largura é baseada na opção Scale units na guia Forms. Observação Estas são configurações padrão somente para novos formulários. As configurações de formulários existentes são salvas no arquivo de recursos.
**Vertical spacing (pixels)**
Especifica a altura do espaço entre linhas de grade verticais. A altura é baseada na opção Scale Units na guia Forms. Observação Estas são configurações padrão somente para novos formulários. As configurações de formulários existentes são salvas no arquivo de recursos.
**Show position**
Especifica se a posição e as dimensões do objeto são exibidas na barra de status.
**Tab ordering**
Especifica como definir a ordem de tabulação em um formulário. Para ordenar controles clicando neles, escolha Interactive. Para ordenar controles usando a caixa de diálogo Tab Order, escolha By List. Observação Especifica como o botão Set Tab Order na barra de ferramentas do Form Designer define a ordem.
**Scale units**
Especifica Pixels ou Foxels, o que define o modo de escala padrão para o Form Designer e o Class Designer.
**Maximum design area**
Especifica o tamanho máximo do formulário em tempo de design. A configuração padrão é None, o que impede que o formulário apareça cortado dentro do Form Designer. Você não pode dimensionar um formulário maior que a resolução especificada. É uma boa ideia especificar a menor resolução que seus usuários desejarão para que todos os usuários possam ver seus formulários.

# Template classes

Especifica uma biblioteca de classes e classe nas quais basear seus novos formulários e form sets. O padrão é que o Visual FoxPro use sua classe base.
 **Form set**
Exibe a caixa de diálogo Form Set Template, na qual você seleciona um modelo de form set.
**Form**
Exibe a caixa de diálogo Form Template, na qual você seleciona um modelo de formulário.
**Builder lock**
Especifica que builders são exibidos automaticamente no Form Designer quando você cria um controle que tem um builder registrado para ele.
**Prompt to save changes before running form**
Especifica que, ao executar um formulário a partir do Form Designer, você é solicitado a salvar alterações no formulário feitas desde a última vez que o salvou. Se você desmarcar esta opção, o Form Designer salva alterações automaticamente antes de executar o formulário.
