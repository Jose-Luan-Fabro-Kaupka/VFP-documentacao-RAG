# Janela Task List Manager

Permite acompanhar tarefas. Para personalizar o Task List Manager, consulte Personalizando o Task List Manager.

O Task List Manager aparece quando você clica em Task List no menu Tools. Você também pode acessar o Task List Manager usando a variável de sistema _TASKLIST, que referencia Tasklist.app por padrão. Você pode modificar esta referência na guia File Locations na caixa de diálogo Options. Para obter mais informações, consulte Variável de sistema _TASKLIST ou Guia File Locations, Caixa de diálogo Options.

A lista de tarefas é armazenada como uma tabela no arquivo FoxTask.dbf. Você pode especificar um arquivo diferente usando a variável de sistema _FOXTASK. Para obter mais informações, consulte Variável de sistema _FoxTask.

# Indicadores visuais da lista de tarefas

O Task List Manager indica informações importantes por meio de indicadores visuais:

| Indicador visual | Descrição |
| --- | --- |
| Texto vermelho | Indica que a Due Date já passou. |
| Texto preto | Indica que a Due Date ainda não chegou. |
| Texto azul | Indica que hoje é a Due Date. |
| Texto em negrito | Indica que a tarefa ainda não foi Read. |
| Texto tachado | Indica que a tarefa foi Completed. |
| Seta vermelha para cima | Indica uma tarefa de Priority alta. |
| Seta azul para baixo | Indica uma tarefa de Priority baixa. |
| Ícone com seta | Indica uma tarefa Shortcut. |
| Ícone com pessoa/tarefa | Indica uma tarefa User-Defined ou Other. |

# Campos de tarefa

O Task List Manager inclui os seguintes campos:

| Nome do campo | Descrição | Exibido inicialmente | Removível | Editável por Shortcut | Editável pelo usuário |
| --- | --- | --- | --- | --- | --- |
| Priority | Lista suspensa mostrando a prioridade da tarefa. | X | X | X | |
| Task Completed | Caixa de seleção indicando se a tarefa está completa. | X | X | X | |
| Task Type | Representação visual do tipo de tarefa (ícone). Internamente, os tipos são representados pelos seguintes valores no campo Foxtask Type: Observação S - Shortcut Observação U – User-Defined Observação O – Other | X | | | |
| Contents | Descrição da tarefa. | X | X | | |
| File Name | Nome do arquivo contendo o Shortcut ou associado à tarefa. | X | X | X | |
| Due Date | Data em que a tarefa está programada para ser concluída. | X | X | X | X |
| Class | Nome da classe contendo o Shortcut ou associação da tarefa. | X | X | | |
| Line | Número da linha do Shortcut ou associação da tarefa. | X | X | | |
| Method | Nome do método contendo o Shortcut ou associação da tarefa. | X | X | | |
| Timestamp | Carimbo de data/hora numérico quando a tarefa foi adicionada pela primeira vez. | X | | | |
| Custom | Você pode adicionar campos personalizados para tarefas. | X | X | X | |
 **Caixa de diálogo Tasklist Options**
Exibe opções para adicionar, remover e navegar em campos personalizados no Task List Manager. Você também pode editar a estrutura da tabela e limpar a tabela Task List. A caixa de diálogo Tasklist Options aparece quando você clica com o botão direito no Task List Manager e clica em Options. Botão New Cria uma nova tabela e exibe o Table Designer para que você possa adicionar novos campos personalizados e seus tipos de dados. Não modifique o campo UniqueID inicial na definição da tabela. Observação A guia Fields na caixa de diálogo Task Properties trata todos os campos personalizados como tipo Character e não executa nenhuma validação de tipo. Botão Edit Structure Permite editar a estrutura da tabela de colunas definidas pelo usuário. Botão Clear Remove a associação da tabela de campos personalizados do Task List. A tabela e seu conteúdo permanecem intactos para que possam ser restaurados posteriormente, se necessário. Botão Browse Permite selecionar uma tabela de campos personalizados existente para configurar uma associação à tabela principal FoxTask.dbf. Observação Quando uma tabela de campos personalizados foi criada, ela não pode ser alterada diretamente do Task List Manager. Você deve fazer isso manualmente no Visual FoxPro usando o Table Designer. Clean Up FoxTask Limpa e compacta a tabela subjacente Task List.
