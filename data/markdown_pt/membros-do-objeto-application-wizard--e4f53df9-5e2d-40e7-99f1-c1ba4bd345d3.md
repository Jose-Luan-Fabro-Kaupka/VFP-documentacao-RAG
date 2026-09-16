# Membros do objeto Application Wizard

Quando um Application Wizard cria um novo projeto, ele gera automaticamente dois formulários para o novo aplicativo, um formulário Quick Start e um formulário About, subclassificados respectivamente dos formulários wzQuickStartForm e Wzaboutdialog na biblioteca Appwiz.vcx.

Os formulários subclassificados são contêineres para os seguintes objetos.
 Membros de Wzaboutdialog
| Objeto | Classe | Descrição |
| --- | --- | --- |
| cmdOK | CommandButton | Libera o formulário. |
 Membros de WzQuickStartForm
| Objeto | Classe | Descrição |
| --- | --- | --- |
| CmdClose | CommandButton | Fecha o formulário QuickStart. |
| CmdRun | CommandButton | Executa o formulário atualmente selecionado na list box. |
| LblForms | Label | Etiqueta de texto. |
| LstForms | List Box | Contém uma lista de todos os formulários definidos no aplicativo, gerada automaticamente no método Init da list box. Quando o usuário clica duas vezes no nome de um formulário, o formulário é executado. |
