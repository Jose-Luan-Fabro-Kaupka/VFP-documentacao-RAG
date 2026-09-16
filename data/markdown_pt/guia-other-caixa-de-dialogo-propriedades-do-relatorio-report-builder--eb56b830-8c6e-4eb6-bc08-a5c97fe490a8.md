# Guia Other, Caixa de diálogo Propriedades do relatório (Report Builder)

Permite adicionar comentários, dados do usuário e elementos de código que você pode usar em tempo de execução de relatórios no Report Designer ou Label Designer.

A caixa de diálogo Propriedades do relatório aparece quando você clica em Properties no menu Report ou no menu de atalho de um relatório.
 **Edit comment**
Abre a caixa de diálogo Comment. Isso permite adicionar ou editar comentários para o relatório. Observação O sistema armazena os comentários no campo memo COMMENTS da tabela de estrutura do relatório. Por padrão, o mecanismo de relatório não os utiliza. No entanto, subclasses de ReportListener podem usar o campo COMMENTS.
**Edit user data**
Abre a caixa de diálogo User data. Isso permite adicionar ou editar dados definidos pelo usuário para o relatório. Observação Os dados do usuário não são visíveis e não podem ser alterados quando você modifica um layout de relatório no modo protegido. Observação O sistema armazena os dados do usuário no campo memo USER da tabela de estrutura do relatório. Por padrão, o mecanismo de relatório não os utiliza. No entanto, subclasses de ReportListener podem usar o campo USER.
**Edit settings**
Abre uma caixa de diálogo Run-time extensions. Isso permite adicionar ou editar recursos de código arbitrários ao controle de relatório. Comentários no bloco de código de extensões em tempo de execução explicam como usar extensões em tempo de execução.
