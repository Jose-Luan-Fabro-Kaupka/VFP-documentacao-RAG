# Classe base Shell Execute

Esta classe permite iniciar uma aplicação ou documento com sua aplicação associada a partir da aplicação atual.

| Categoria | Utilitário do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _shellexecute |
| Biblioteca de classes | _environ.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\Buttons.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método ShellExecute | Tenta executar o arquivo tcFileName no diretório tcWorkDir. Sintaxe: ShellExecute(tcFileName, tcWorkDir, tcOperation) Retorno: nSuccess Argumentos: tcFileName especifica o arquivo a ser executado. tcWorkDir especifica o caminho para o arquivo a ser executado. tcOperation especifica a operação a ser executada. nSuccess especifica a falha ou o sucesso da tentativa de execução usando um dos seguintes valores: 2 = Associação inválida (por exemplo, URL inválida) 29 = Falha ao carregar a aplicação 30 = Aplicação ocupada 31 = Sem associação de aplicação Valores acima de 32 representam sucesso e retornam um identificador de instância para a aplicação em execução. |
