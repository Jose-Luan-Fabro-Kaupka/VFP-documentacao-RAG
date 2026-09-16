# Como: definir o alinhamento do conteúdo de controles de relatório

Você pode alterar o alinhamento do texto em controles Field e Label. Alterar o alinhamento nesses controles afeta apenas seu conteúdo e não afeta o alinhamento do controle no layout da página. Você também pode centralizar o conteúdo de campos General, especificados por controles de relatório Picture/OLE Bound, dentro de suas molduras.

### Para alterar o alinhamento de saída em um controle Field ou Label
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique no controle de relatório Field ou Label que deseja alterar.
- No menu Format, aponte para Text Alignment e clique no alinhamento desejado.

Você também pode alterar o alinhamento em um controle Field dependendo do tipo de dados que especifica para o controle na guia Format na caixa de diálogo Field Properties. Para obter mais informações, consulte Format Tab, Report Control Properties Dialog Box (Report Builder).

> **Observação:** Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo de controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Expression Dialog Box.

# Centralizando conteúdo de campos General em molduras

Ao especificar campos General em controles de relatório Picture/OLE Bound, o conteúdo em campos General pode variar em forma e tamanho das molduras que os contêm. Quando a moldura é maior que seu conteúdo, o conteúdo no campo General aparece ancorado no canto superior esquerdo da moldura. Você pode centralizar o conteúdo de campos General horizontalmente dentro de suas molduras.

### Para centralizar um campo General em sua moldura
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório Picture/OLE Bound. A caixa de diálogo Picture/OLE Bound Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo de controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Picture Dialog Box.
- Na caixa de diálogo Picture/OLE Bound Properties, clique na guia General se ela não estiver selecionada.
- Na guia General, clique em Center general field horizontally in frame.
- Quando terminar, clique em OK. Ao gerar saída para o relatório, o conteúdo do campo General aparece centralizado dentro da moldura.

Para obter mais informações, consulte General Tab, Report Control Properties Dialog Box (Report Builder).
