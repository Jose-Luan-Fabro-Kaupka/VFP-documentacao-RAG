# Classe Foundation Window Handler

Esta classe Window Handler de uso geral executa várias operações comuns de janela, como organizar janelas em cascata.

| Categoria | Application |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _windowhandler |
| Classe base | Custom |
| Biblioteca de classes | _ui.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\whandler.scx |

# Observações

Para usar, arraste a classe para um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Ao adicionar a classe a um projeto, você pode escolher entre adicionar a classe ou criar uma subclasse. Ao adicionar a classe a um formulário, o Visual FoxPro exibe o ícone no formulário para que você possa especificar os valores de propriedades apropriados e seus métodos disponíveis no Form Designer.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade IMDIWorkspaceColor | Contém a cor do Windows para a janela de frame de nível superior. Padrão: 0 |
| Método CascadeFormInstances | Organiza formulários em cascata. Sintaxe: CascadeFormInstances(tcFormName, tlOmitAutoCenteredForms, tnStartTop, tnStartLeft, tnStartColumn) Retorno: nenhum Argumentos: tcFormName especifica o formulário ou _screen no qual organizar os formulários em cascata. tlOmitAutoCenteredForms especifica se deve ignorar a organização em cascata para formulários autocentrados. tnStartTop especifica a coordenada superior inicial. tnStartLeft especifica a coordenada esquerda inicial. |
| Método GetCurrentTopFormRef | Retorna a janela de frame atual. Use principalmente para aplicações com formulários de nível superior. Sintaxe: GetCurrentTopFormReference( ) Retorno: loTopForm Argumentos: nenhum |
| IMDIWorkspaceColor_access( ) | Sintaxe: IMDIWorkspaceColor_access( ) Retorno: GetSysColor ( 12 ) Argumentos: nenhum |
| Método InvokeMenuItemInFrame | Use para invocar itens de menu em aplicações com formulários de nível superior para acessar determinadas caixas de diálogo do sistema, como a caixa de diálogo Find. Também use para implementar um item de menu em uma caixa de diálogo que não possui menu. Sintaxe: InvokeMenuItemInFrame(tcAction) Retorno: nenhum Argumentos: tcAction especifica a ação de navegação, como NEXT ou PREVIOUS. Você também pode usar as seguintes ações: UNDO, REDO, CUT, COPY, PASTE, CLEAR, SELECTALL, FIND, FINDAGAIN, REPLACE. |
| Método ShowCurrentTopForm | Interno à classe. |
| Método ShowWindowInFrame | Interno à classe. |
