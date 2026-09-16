# Guia Other, Caixa de diálogo Propriedades de faixa de relatório (Report Builder)

Permite adicionar comentários e dados de usuário para uma faixa de relatório no Report Designer ou Label Designer.
 - Como: adicionar comentários a faixas de relatório
- Como: adicionar dados de usuário a faixas de relatório
 **Editar comentário**
Abre uma caixa de diálogo Comment para que você possa adicionar ou editar comentários para a faixa de relatório. Observação Os comentários são armazenados no campo memo COMMENTS da tabela de estrutura do relatório e não são usados pelo mecanismo de relatório por padrão. No entanto, o campo COMMENTS está disponível para uso por subclasses de ReportListener.
**Editar dados de usuário**
Abre uma caixa de diálogo User data para que você possa adicionar ou editar dados definidos pelo usuário para a faixa de relatório. Observação Os dados de usuário não são visíveis e não podem ser alterados ao modificar um layout de relatório no modo protegido. Observação Os dados de usuário são armazenados no campo memo USER da tabela de estrutura do relatório e não são usados pelo mecanismo de relatório por padrão. No entanto, o campo USER está disponível para uso por subclasses de ReportListener.
