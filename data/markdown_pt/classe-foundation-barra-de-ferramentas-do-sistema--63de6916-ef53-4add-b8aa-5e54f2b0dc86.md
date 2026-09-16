# Classe Foundation Barra de Ferramentas do Sistema

Esta classe é uma classe gerenciadora que manipula e rastreia Barras de Ferramentas do Sistema para que você possa remover automaticamente as barras de ferramentas do sistema do Visual FoxPro em seu aplicativo e restaurá-las posteriormente. Esta classe é usada com a estrutura gerada pelo Assistente de Aplicativo.

| Categoria | Application |
| --- | --- |
| Catálogo Padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _systoolbars |
| Classe Base | Custom |
| Biblioteca de Classes | _app.vcx |
| Classe Pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\environ.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item da Galeria de Componentes, selecione Adicionar ao Projeto ou Adicionar ao Formulário. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos necessários.

Se lAutomatic for true (.T.), como em um aplicativo do tipo READEVENTS, a classe oculta automaticamente todas as barras de ferramentas do sistema existentes quando você a instancia. Ela então restaura automaticamente as barras de ferramentas do sistema ocultas quando sai do escopo.

Você também pode chamar os métodos HideSystemToolbars( ) e ShowSystemToolbars( ) manualmente.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| Propriedade lAutomatic | Oculta e restaura automaticamente as barras de ferramentas do sistema para o aplicativo. Padrão: .F. |
| Propriedade aSystemToolbars[1,0] | O array de barras de ferramentas do sistema. Padrão: .F. |
| Método Hidesystemtoolbars | Oculta manualmente as barras de ferramentas do sistema para o aplicativo. Sintaxe: Hidesystemtoolbars( ) Retorno: nenhum Argumentos: nenhum |
| Método Showsystemtoolbars | Exibe manualmente as barras de ferramentas do sistema para o aplicativo. Sintaxe: Showsystemtoolbars( ) Retorno: nenhum Argumentos: nenhum |
| Método Initializetoolbararray | Interno à classe. |
