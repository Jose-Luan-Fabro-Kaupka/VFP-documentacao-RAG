# Foundation Class Conflict Catcher

Esta classe fornece uma caixa de diálogo que exibe linhas conflitantes encontradas durante sessões de edição sob buffering otimista. Os valores original, atual e novo são apresentados para resolução. Você pode usar esta classe com buffering de linha ou de tabela.

| Categoria | Data Query |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _conflicts |
| Classe base | Form |
| Biblioteca de classes | _dataquery.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\Conflicts.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Se você escolher Criar um novo formulário da classe selecionada, o Visual FoxPro exibe a caixa de diálogo Abrir para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer. Você precisa executar SET MULTILOCKS ON e habilitar buffering.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade CursorAlias | Especifica o alias a verificar para conflitos. Padrão: "" |
| Propriedade lAutoCheck | Especifica se a verificação começa na inicialização. Padrão: .T. |
| Método StartCheck | Verifica conflitos nos dados em buffer do alias. Sintaxe: StartCheck( ) Retorno: nenhum Argumentos: nenhum |
| Propriedade ConflictAlias | Interna à classe. |
| Propriedade lRowConflict | Interna à classe. |
| Propriedade aConflicts[1,0] | Interna à classe. |
| Método NextConflict | Interna à classe. |
| Método CheckSource | Interna à classe. |
| Método Alert | Interna à classe. |
