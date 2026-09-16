# Excluindo arquivos modificáveis das compilações

Seu projeto de aplicativo provavelmente contém arquivos, como tabelas, que os usuários precisam modificar. No entanto, quando você compila um aplicativo a partir de um projeto Visual FoxPro, os arquivos do projeto são reunidos em um único arquivo de aplicativo, e os arquivos do projeto designados como included tornam-se somente leitura.

Para arquivos que os usuários precisam modificar, você deve adicioná-los ao projeto, mas excluí-los do processo de compilação. Arquivos excluídos permanecem parte do seu aplicativo, de modo que o Visual FoxPro continua a rastreá-los como parte do seu projeto. No entanto, arquivos excluídos não são compilados no arquivo de aplicativo, para que os usuários possam modificá-los.

Geralmente, você deve incluir arquivos executáveis, como formulários, relatórios, consultas, menus e programas, e todos os outros arquivos que os usuários não precisam atualizar. Você deve excluir arquivos de dados, bibliotecas ActiveX control (.ocx), bibliotecas de vínculo dinâmico Visual FoxPro (.fll) e bibliotecas de vínculo dinâmico Windows (.dll). Por padrão, tabelas são excluídas porque se presume que os usuários alteram tabelas em um aplicativo.

> **Observação:** Você não pode incluir arquivos de aplicativo (.app) em um projeto. Você não pode excluir arquivos designados como arquivos principais. Para obter mais informações sobre arquivos principais, consulte How to: Set the Starting Point .

No entanto, você deve incluir ou excluir arquivos conforme os requisitos do seu aplicativo. Por exemplo, você pode incluir uma tabela que contém informações sensíveis do sistema ou informações somente leitura para protegê-la de alterações inadvertidas. Por outro lado, se seu aplicativo permite que os usuários alterem um relatório, você pode excluir o relatório.
