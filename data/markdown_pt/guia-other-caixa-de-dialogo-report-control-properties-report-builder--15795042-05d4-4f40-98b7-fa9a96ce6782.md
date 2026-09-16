# Guia Other, caixa de diálogo Report Control Properties (Report Builder)

Permite adicionar comentários, dados do usuário, dicas de ferramenta e elementos de código que podem ser usados em tempo de execução nos controles de relatório do Report Designer ou Label Designer.
 - Como: adicionar comentários a controles de relatório
- Como: adicionar dados do usuário a controles de relatório
- Como: adicionar dicas de ferramenta a controles de relatório
 **Edit comment**
Abre a caixa de diálogo Comment para adicionar ou editar comentários do controle. Observação: os comentários são armazenados no campo memo COMMENTS da tabela de estrutura do relatório e não são usados pelo mecanismo de relatório por padrão. No entanto, o campo COMMENTS está disponível para subclasses de ReportListener.
**Edit user data**
Abre a caixa de diálogo User data para adicionar ou editar dados definidos pelo usuário para o controle. Observação: esses dados não ficam visíveis nem podem ser alterados ao modificar um layout no modo protegido. Eles são armazenados no campo memo USER da tabela de estrutura e não são usados pelo mecanismo por padrão. No entanto, o campo USER está disponível para subclasses de ReportListener.
**Edit tooltip**
Abre uma caixa de diálogo Tooltip para adicionar ou editar o texto da dica que aparecerá no layout ao apontar para o controle com o mouse.
**Edit settings**
Abre a caixa de diálogo Run-time extensions para adicionar ou editar recursos de código arbitrários no controle de relatório.
