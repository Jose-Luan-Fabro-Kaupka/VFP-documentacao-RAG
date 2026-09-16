# Classe Foundation Object State

Esta classe determina o estado de um objeto. Ela salva e/ou restaura configurações de propriedades de objetos automaticamente ou explicitamente.

| Categoria | Aplicativo |
| --- | --- |
| Catálogo Padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _objectstate |
| Classe Base | Custom |
| Biblioteca de Classes | _app.vcx |
| Classe Pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\environ.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, forneça quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para Usar Classes Foundation do Visual FoxPro para obter mais informações sobre o uso de classes foundation.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| propriedade aProperties[1,3] | A matriz para salvar/restaurar propriedades de oObject . Padrão: .F. |
| propriedade lAutomatic | Especifica se as propriedades de oObject são salvas e restauradas. Se este atributo for true (.T.), o objeto _ObjectState restaurará todos os atributos que você salvou para seu objeto de destino quando o objeto _ObjectState for destruído. Padrão: .F. |
| oObject | Referência ao objeto de destino cujo estado está sendo salvo. Padrão: .NULL. |
| método Restore | Restaura o valor de uma propriedade para oObject se o valor foi alterado. Se tcWhichProperty não for passado, todas as propriedades salvas de oObject são restauradas. Este método é chamado sem argumento no evento _ObjectState.Destroy( ) quando _ObjectState.lAutomatic é true (.T.). Sintaxe: Restore(tcWhichProperty) Retorno: tcSave Argumentos: tcWhichProperty especifica a propriedade a ser restaurada. tcSave especifica o valor a ser restaurado. |
| método Save | Salva o valor atual de uma propriedade para oObject. Você pode usar isso em vez do argumento tlSave do método Set. Sintaxe: Save(tcProperty, tcTypeValue) Retorno: nenhum Argumentos: tcProperty especifica a propriedade sendo acessada. tcTypeValue especifica o valor sendo salvo para tcProperty . |
| método Set | Define uma propriedade para um novo valor para oObject . Sintaxe: Set(tcProperty, tvValue, tlSave) Retorno: nenhum Argumentos: tcProperty especifica a propriedade a definir. tvValue especifica o valor para o qual tcProperty deve ser definido. tlSave especifica se o valor atual é retido para restauração posterior. |
