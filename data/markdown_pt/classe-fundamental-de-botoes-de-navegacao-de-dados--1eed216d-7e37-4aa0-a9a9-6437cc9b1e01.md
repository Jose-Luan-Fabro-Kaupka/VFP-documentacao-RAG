# Classe fundamental de botões de navegação de dados

Esta classe é um conjunto de botões de navegação que inclui Top, Next, Prev e Bottom. Ela também contém a classe DataChecker para verificar conflitos durante a navegação entre registros.

| Categoria | Navegação de dados |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Navigation |
| Classe | _datanavbtns |
| Classe base | Container |
| Biblioteca de classes | _datanav.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Forms\single.scx |

# Observações

Para usar a classe, solte-a em um projeto ou formulário de um ambiente de dados ou, no menu de atalho do item da Galeria de Componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Ao adicionar a classe a um formulário, forneça objetos de entrada e saída. Ao soltá-la em um projeto, você pode optar por adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar as classes fundamentais do Visual FoxPro para obter mais informações.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| cSkipTable property | A tabela na qual o ponteiro deve ser movido. Padrão: "" |
| lEnableDisableOnInit property | Especifica se os botões de navegação são habilitados quando carregados pela primeira vez. Padrão: .T. |
| RecordPointerMoved method | Chamado sempre que o ponteiro de registro é movido, fornecendo um novo evento para a classe. Sintaxe: RecordPointerMoved( ) Retorno: nenhum. Argumentos: nenhum. |
| EnableDisableButtons method | Habilita ou desabilita botões conforme a posição do ponteiro de registro. Sintaxe: EnableDisableButtons( ) Retorno: nenhum. Argumentos: nenhum. |
| BeforeRecordPointerMoved method | Chamado antes de mover o ponteiro de registro para determinar se a tabela contém registros. Sintaxe: BeforeRecordPointerMoved( ) Retorno: nenhum. Argumentos: nenhum. |
