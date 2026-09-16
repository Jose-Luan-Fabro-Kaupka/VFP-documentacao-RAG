# Foundation Class Cross Tab

Esta classe usa o mecanismo do Assistente de tabela cruzada para gerar um relatório de tabela cruzada quando colocada em um formulário.

| Categoria | Automação |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Automation |
| Classe | _xtab |
| Classe base | Custom |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\Automate.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário em um ambiente de dados, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de lDisplayNulls, lTotalRows, nTotalOption e lBrowseAfter. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cOutfile | O nome do arquivo de saída. Padrão: xtabquery |
| Propriedade lCursorOnly | Especifica se a fonte de dados de entrada é cursor. Padrão: .T. |
| Propriedade lCloseTable | Especifica se deve fechar a fonte de dados de origem após a geração da tabela cruzada. Padrão: .T. |
| Propriedade lShowThem | Especifica se deve mostrar o termômetro durante a geração da tabela cruzada. Padrão: .T. |
| Propriedade nRowField | Especifica a posição do campo na fonte de dados das linhas da tabela cruzada. Padrão: 1 |
| Propriedade nColField | Especifica a posição do campo na fonte de dados das colunas da tabela cruzada. Padrão: 2 |
| Propriedade nDataField | Especifica a posição do campo na fonte de dados dos dados da tabela cruzada. Padrão: 3 |
| Propriedade lTotalRows | Especifica se deve totalizar linhas na saída da tabela cruzada. Padrão: .F. |
| Propriedade nTotalOption | Especifica a opção de totalização a executar: 0 = soma 1 = contagem 2 = % do total. Padrão: 0 |
| Propriedade lDisplayNulls | Especifica se deve exibir valores nulos na saída da tabela cruzada. Padrão: .F. |
| Propriedade lBrowseAfter | Especifica se deve abrir uma janela Browse na saída da tabela cruzada. Padrão: .T. |
| Método RunXtab | Gera uma tabela cruzada. Sintaxe: RunXtab( ) Retorno: nenhum Argumentos: nenhum |
