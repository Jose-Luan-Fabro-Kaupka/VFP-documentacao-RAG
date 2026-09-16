# Classe Foundation Data Validation

Esta classe detecta conflitos de dados em dados em buffer.

| Categoria | Data Editing |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _datachecker |
| Classe base | Custom |
| Biblioteca de classes | _datanav.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\conflicts.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, precisa especificar os valores de propriedade apropriados. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| Método HandleRecord | Compara o valor atual, o valor antigo e o valor original em disco de cada campo, exibindo uma caixa de mensagem se uma alteração ou conflito for detectado. Sintaxe: HandleRecord(lnScope) Retorno: nReturn Argumentos: lnScope especifica o grau de validação: 0 = verificar conflitos 1 = verificar conflitos e verificar alterações. nReturn especifica a ação tomada: 0 = Sem alteração 1 = Alteração bem-sucedida 2 = Não foi possível fazer a alteração |
| Método String | Chamado pelo método HandleRecord, retorna um equivalente de caractere do valor passado. Retorna apenas uma notificação para campos memo. Sintaxe: String(luValue) Retorno: nenhum Argumentos: luValue especifica o valor a ser verificado. |
| Método VerifyChanges | Solicita ao usuário que salve todas as alterações feitas em uma tabela ou registro. Sintaxe: VerifyChanges( ) Retorno: nenhum Argumentos: nenhum |
| Método VerifyEachChange | Solicita ao usuário que confirme cada alteração feita. Sintaxe: VerifyEachChange( ) Retorno: nenhum Argumentos: nenhum |
| Método CheckcConflicts | Notifica o usuário quando os dados foram alterados após o início da edição do registro. Sintaxe: CheckcConflicts( ) Retorno: nenhum Argumentos: nenhum |
