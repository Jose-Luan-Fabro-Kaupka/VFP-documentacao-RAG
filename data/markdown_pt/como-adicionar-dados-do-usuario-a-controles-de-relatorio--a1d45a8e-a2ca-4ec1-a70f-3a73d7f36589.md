# Como: adicionar dados do usuário a controles de relatório

Você pode adicionar dados definidos pelo usuário a um controle de relatório. Dados definidos pelo usuário aparecem no campo USER da tabela de estrutura do relatório (.frx ou .lbx) e não aparecem na saída renderizada.

Você pode usar o conteúdo do campo USER em métodos de um objeto Reportlistener ao executar um relatório ou etiqueta no modo object-assisted. Para obter mais informações, consulte Understanding Visual FoxPro Object-Assisted Reporting.

### Para adicionar dados definidos pelo usuário a um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, dê um clique duplo no controle de relatório ao qual deseja adicionar dados do usuário. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não está definida para o Report Builder padrão ou está definida para um construtor de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable . Observação A caixa de diálogo que aparece quando não há construtor de relatório definido não inclui a capacidade de editar os dados definidos pelo usuário.
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Other se ela não estiver selecionada.
- Na área User data, clique em Edit user data . A caixa de diálogo de dados do usuário da banda de relatório é aberta.
- Na caixa de diálogo de dados do usuário, digite os dados definidos pelo usuário que deseja para o controle de relatório.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Other Tab, Report Control Properties Dialog Box (Report Builder).
