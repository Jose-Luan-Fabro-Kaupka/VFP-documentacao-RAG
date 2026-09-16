# Como: redefinir variáveis de relatório

Você pode especificar que uma variável de relatório seja redefinida para seu valor inicial na entrada de uma faixa de relatório específica. Por padrão, o Visual FoxPro redefine o valor de uma variável de relatório uma vez no início da execução de um relatório, deixando-a com o último valor avaliado quando a execução do relatório é concluída.

Você também pode usar as expressões On Entry e On Exit de uma faixa para definir o valor de uma variável de relatório.

### Para redefinir uma variável de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Variables . A caixa de diálogo Propriedades do relatório abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo Variáveis do relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Variáveis do relatório .
- Na caixa de diálogo Propriedades do relatório, clique na guia Variables se ela não estiver selecionada.
- Defina o valor de Reset value based on : Report para definir a variável para seu valor inicial antes do relatório começar a ser processado (padrão) Page para redefinir a variável de relatório para seu valor inicial quando a faixa Page Header começar a ser processada. Column para redefinir a variável para seu valor inicial quando a faixa Column Header começar a ser processada (disponível apenas em layouts de várias colunas). Group: <expr> para redefinir a variável para seu valor inicial quando a faixa Group Header começar a ser processada (disponível apenas quando um agrupamento de dados foi criado). Detail <n> para redefinir a variável para seu valor inicial quando um conjunto de faixas de detalhe começar a ser processado (disponível apenas em layouts com várias faixas de detalhe). Para obter mais informações sobre layouts com várias faixas de detalhe, consulte Trabalhando com tabelas relacionadas usando várias faixas de detalhe em relatórios .
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Variables, caixa de diálogo Propriedades do relatório (Report Builder).

### Para redefinir uma variável ao entrar ou sair de uma faixa
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Edit Bands .
- Na caixa de diálogo Edit Bands, clique na faixa de relatório desejada e depois em OK . A caixa de diálogo de propriedades da faixa de relatório abre. Dica Você também pode clicar duas vezes no separador de faixa no Report Designer ou Label Designer para abrir a caixa de diálogo de propriedades da faixa de relatório. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo da faixa de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Propriedades da faixa de relatório .
- Na caixa de diálogo de propriedades da faixa de relatório, clique na guia General se ela não estiver selecionada.
- Na área Run expression, digite uma expressão nas caixas On entry ou On exit que redefine a variável ao entrar ou sair da faixa. Um exemplo de tal expressão seria EXECSCRIPT("tVariable = 10") para atribuir à variável de relatório tVariable o valor numérico 10. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder .
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia General, caixa de diálogo Propriedades da faixa de relatório (Report Builder).
