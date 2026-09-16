# Como: adicionar contêineres do Visual FoxPro

Além de form-sets e formulários, o Visual FoxPro fornece quatro classes de contêiner base:
 - CommandGroup Control
- Grid Control
- OptionGroup Control
- PageFrame Control

### Para adicionar objetos contêiner a um formulário
- Na barra de ferramentas Form Controls, selecione o botão do objeto contêiner desejado (grupo de botões, grade, grupo de botões de opção ou page frame) e arraste-o para dimensionar no formulário.

Quando você adiciona um grupo de botões de comando ou um grupo de botões de opção a um formulário no Form Designer, o grupo contém dois botões por padrão. Quando você adiciona um page frame a um formulário, o page frame contém duas páginas por padrão. Você pode adicionar mais botões ou páginas definindo a ButtonCount Property ou a PageCount Property para o número desejado.

Quando você adiciona uma grade a um formulário, a propriedade ColumnCount Property (Visual FoxPro) é definida como – 1 por padrão, o que indica AutoFill. Em tempo de execução, a grade exibirá tantas colunas quanto houver campos na tabela RowSource. Se você não quiser AutoFill, pode especificar o número de colunas definindo a propriedade ColumnCount da grade.

Para mais informações sobre esses objetos contêiner, consulte Understanding Container and Control Objects e Using Controls.
