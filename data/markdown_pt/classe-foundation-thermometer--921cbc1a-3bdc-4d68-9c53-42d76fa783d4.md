# Classe Foundation Thermometer

Esta classe, quando colocada em um formulário, fornece uma classe de termômetro padrão.

| Categoria | Interface do usuário |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Dialogs |
| Classe | _thermometer |
| Classe base | Form |
| Biblioteca de classes | _therm.vcx |
| Classe pai | _thermometer |
| Amostra | ...\Samples\Solution\Ffc\therm.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho Item da Galeria de Componentes, selecione Add to Project. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Se você escolher Create a new form from the selected class, o Visual FoxPro exibe a caixa de diálogo Abrir para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer. Você precisa especificar valores de propriedade apropriados no método Update.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cCurrentTask | Especifica a tarefa atual. Padrão: "" |
| propriedade iBasis | Especifica a base para calcular a porcentagem. Padrão: 0 |
| propriedade iPercentage | Especifica a porcentagem de conclusão na qual a exibição é atualizada. Padrão: 0 |
| propriedade iProgress | Especifica a quantidade concluída ( iPercentage ). Padrão: 0 |
| método Complete | Exibe termômetro 100% completo. Sintaxe: Complete(m.cTask) Retorno: nenhum Argumentos: m.cTask especifica o que exibir quando o progresso estiver completo. |
| método Update | Atualiza o termômetro. Sintaxe: Update(iProgress, cTask) Retorno: nenhum Argumentos: iProgress especifica o incremento de progresso. cTask especifica a mensagem a ser exibida. |
| propriedade cThermRef | Interno à classe. |
| propriedade ShpThermBarMaxWidth | Interno à classe. |
