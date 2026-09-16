# Como: atribuir metadados estruturados a controles de relatório

O aplicativo Report Builder padrão permite atribuir metadados estruturados a controles de relatório e faixas de layout individuais.

O XML de metadados dos elementos do relatório é armazenado no campo STYLE da tabela de estrutura do relatório (.frx ou .lbx). Para obter mais informações, consulte Noções básicas e extensão da estrutura de relatórios.

> **Observação:** Os documentos XML de metadados de relatório são instâncias do esquema XML Memberdata (.xsd) do Visual FoxPro, que também especifica o formato de documentos de metadados para extensibilidade de classes e propriedades. Para ver o esquema Memberdata completo, consulte Extensibilidade de MemberData.

ReportBuilder.App permite editar diretamente o texto completo do elemento XML memberdata de um controle de relatório. Ele também expõe dois atributos de metadados de relatório para edição conveniente:
 - O atributo Run-time extensions pode armazenar um script executável.
- O atributo Execute When pode especificar uma expressão que o código de método de ReportListener pode avaliar para executar condicionalmente.

Assim como não usa diretamente o conteúdo do campo User Data, o mecanismo de relatório não referencia diretamente os metadados XML. Você pode usar esses metadados em métodos personalizados de um objeto ReportListener ao executar um relatório ou layout de rótulo no modo assistido por objeto. Para obter mais informações, consulte Noções básicas sobre relatórios assistidos por objeto no Visual FoxPro. Também é possível criar extensões do Report Builder que usem os metadados durante sessões de design. Para obter mais informações, consulte Extensões XML MemberData de relatório.

### Para atribuir os atributos de metadados Run-time extensions e Execute When a um controle de relatório
- Abra o relatório ou rótulo no designer apropriado.
- No designer, clique duas vezes no controle ao qual deseja adicionar dados do usuário. A caixa de diálogo Propriedades do controle é aberta. Observação: se a variável de sistema _REPORTBUILDER não estiver definida como o Report Builder padrão ou usar um builder de terceiros, será exibida a caixa de diálogo Controle de Relatório ou outra caixa. A caixa exibida quando nenhum report builder está definido não permite editar metadados.
- Na caixa Propriedades do Controle de Relatório, clique na guia Other, caso não esteja selecionada.
- Na área Run-time extensions, clique em Edit settings. A caixa de diálogo Run-time extensions da faixa é aberta.
- Na caixa de edição Run-time extensions, digite o script ou os dados da extensão. Na caixa de expressão Execute When, informe um valor ou expressão que classes ReportListener personalizadas possam usar em tempo de execução.
- Ao terminar, clique em OK.

Para obter mais informações, consulte Guia Other, caixa de diálogo Propriedades do Controle de Relatório (Report Builder).

### Para editar diretamente o XML de metadados
- Abra o relatório ou rótulo no designer apropriado.
- No designer, clique duas vezes no controle ao qual deseja adicionar dados do usuário. A caixa de diálogo Propriedades é aberta. Se _REPORTBUILDER não estiver configurado com o Report Builder padrão, poderá ser exibida outra caixa de diálogo. O Report Builder padrão também permite especificar uma caixa diferente para editar o XML de metadados. A caixa exibida sem um report builder não permite essa edição.
- Na caixa de propriedades do controle, clique na guia Other, caso não esteja selecionada.
- Na área Run-time extensions, clique em Edit settings.
- Na caixa Run-time extensions, clique em Edit XML. A caixa Metadata XML é aberta. Se ainda não houver metadados atribuídos ao controle, ReportBuilder insere um modelo XML vazio na caixa de edição.
- Informe valores para os atributos de metadados.
- Ao terminar, clique em OK.
- Para obter mais informações sobre o formato XML de metadados de relatório compatível, consulte o esquema XML em Extensibilidade de MemberData.
