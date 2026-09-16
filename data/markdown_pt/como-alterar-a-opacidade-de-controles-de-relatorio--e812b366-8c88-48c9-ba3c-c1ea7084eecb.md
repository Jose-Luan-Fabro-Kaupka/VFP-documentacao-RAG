# Como: alterar a opacidade de controles de relatório

Você pode alterar a opacidade dos controles de relatório Field, Label, Rectangle, Rounded Rectangle e Picture/OLE Bound. Quando um controle de relatório é opaco, os objetos que aparecem atrás do controle de relatório não ficam visíveis. Quando um controle de relatório é transparente, os objetos que aparecem atrás do controle de relatório ficam visíveis.

### Para alterar a opacidade de um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique no controle de relatório que deseja alterar.
- No menu Format, aponte para Backstyle e clique na configuração de opacidade desejada.

Você também pode alterar as configurações de opacidade clicando duas vezes no controle de relatório para abrir a caixa de diálogo de propriedades do controle de relatório. Clique na guia Style e, na área Backstyle, clique na configuração de opacidade desejada. Para obter mais informações, consulte Style Tab, Report Control Properties Dialog Box (Report Builder).

> **Observação:** Uma forma que usa Fill style 0 ("empty" ou "no fill") sempre será renderizada e aparecerá no designer como transparente, independentemente do modo Backstyle. Por outro lado, uma forma que usa Fill style 1 ("solid") sempre será renderizada e aparecerá no designer como opaca, independentemente do modo Backstyle. Para obter mais informações, consulte How to: Change Line Styles of Report Controls .

> **Observação:** Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable .
