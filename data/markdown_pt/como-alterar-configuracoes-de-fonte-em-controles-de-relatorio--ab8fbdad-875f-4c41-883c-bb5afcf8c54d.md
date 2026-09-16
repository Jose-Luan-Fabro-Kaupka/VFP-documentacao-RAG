# Como: alterar configurações de fonte em controles de relatório

Você pode alterar as configurações de fonte em controles Field e Label. É possível alterar a configuração de fonte em um controle existente ou a configuração de fonte padrão para novos controles.

> **Observação:** Ao definir a fonte padrão, a configuração se aplica apenas a novos controles Field e Label que você adicionar ao layout da página. Para alterar a fonte e o tamanho de controles Field e Label existentes, selecione os controles desejados e altere a fonte no menu Format.

Para obter mais informações sobre como definir a fonte padrão para o layout da página e novos controles de relatório, consulte Como: alterar configurações de página para relatórios.

### Para alterar a fonte de um controle de relatório Field ou Label existente
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique no controle de relatório Field ou Label que deseja alterar.
- No menu Format, clique em Font .
- Na caixa de diálogo Font, selecione o estilo e o tamanho de fonte desejados e clique em OK . Importante Os controles de expressão de campo e de etiqueta de texto são criados inicialmente sem um script de fonte específico. Selecionar uma fonte não padrão usando o menu Format conforme descrito acima armazenará a configuração Font Script selecionada no layout do relatório. O mecanismo de relatório consultará essa configuração ao renderizar o controle de relatório. Veja abaixo como redefinir a configuração de script de fonte para "use system default".

Para obter mais informações, consulte Caixa de diálogo Font.

Você também pode alterar as configurações de fonte clicando duas vezes no controle de relatório para abrir a caixa de diálogo de propriedades do controle de relatório. Clique na guia Style e, na área Font, clique no botão de reticências (…) para abrir a caixa de diálogo Font. Para obter mais informações, consulte Guia Style, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

> **Observação:** Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou outra caixa de diálogo pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .

### Para definir a especificação Font Script de um controle de relatório Field ou Label para usar o padrão do sistema
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório Field ou Label que deseja alterar ou clique com o botão direito e selecione Properties . A caixa de diálogo de propriedades do controle de relatório é aberta.
- Selecione a guia Style.
- Desmarque a caixa de seleção Use Font Script.
- Clique em OK .

Para obter mais informações, consulte Guia Style, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

> **Observação:** Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou outra caixa de diálogo pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
