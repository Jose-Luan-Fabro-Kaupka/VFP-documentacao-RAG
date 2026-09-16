# Como: adicionar legendas em tempo de design a controles Field

Para controles de relatório Field, você pode atribuir uma legenda em tempo de design que aparece no layout do Report Designer no lugar da expressão de campo regular.

As legendas em tempo de design são visíveis apenas no designer quando a sessão de design foi iniciada usando a palavra-chave PROTECTED. Para sessões de design normais, a expressão de campo é exibida no controle de campo.

Esta legenda em tempo de design é uma cadeia de caracteres literal, armazenada na coluna NAME do arquivo de origem do layout de relatório (.frx ou .lbx). O aplicativo padrão do report builder, ReportBuilder.app, expõe esta propriedade para Fields na guia Protection. Para obter mais informações, consulte Guia Protection, caixa de diálogo Report Control Properties (Report Builder).

### Para definir uma legenda em tempo de design em um controle de relatório Field
- Abra o layout de relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle desejado ou clique com o botão direito nele e selecione Properties no menu de contexto. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou uma caixa de diálogo diferente pode ser exibida. Não há forma de definir uma legenda em tempo de design usando a caixa de diálogo nativa do controle de relatório. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Protection.
- Digite uma cadeia de caracteres na caixa de texto Design-time caption. Por exemplo, para um controle de campo com uma expressão de DATETIME(), você pode digitar uma amostra da saída como "13 July 1996 14:25." Observação Legendas em tempo de design não são expressões. Você deve digitar uma série literal de caracteres. Não as envolva com aspas, a menos que deseje que as aspas apareçam no designer como parte da legenda visível.
- Quando terminar, clique em OK.
