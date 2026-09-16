# Classe básica Shortcut Menu

Quando colocada em um projeto ou formulário, esta classe cria dinamicamente menus de atalho pop-up.

| Categoria | Menus |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Menus |
| Classe | _shortcutmenu |
| Classe base | Custom |
| Biblioteca de classes | _menu.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\newmenu.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes básicas.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cOnSelection | Especifica a rotina de seleção da barra de menus. Padrão: "" |
| propriedade cMenu | Especifica o nome do menu de atalho. Padrão: "" |
| método DeactivateMenu | Desativa o menu de atalho existente. Sintaxe: DeactivateMenu( ) Retorno: nenhum Argumentos: nenhum |
| método ActivateMenu | Ativa o menu de atalho existente. Sintaxe: ActivateMenu(tcParentMenu) Retorno: nenhum Argumentos: tcParentMenu especifica o nome do menu do qual o atalho é ativado. |
| método ClearMenu | Libera o menu de atalho existente. Sintaxe: ClearMenu( ) Retorno: nenhum Argumentos: nenhum |
| método NewMenu | Cria um novo pop-up de menu para o menu de atalho. Sintaxe: NewMenu( ) Retorno: nenhum Argumentos: nenhum |
| método AddMenubar | Adiciona uma nova barra de menus ao menu de atalho. Sintaxe: AddMember(tcPrompt, tcOnSelection, tcClauses, tnElementNumber, tlMark, tlDisabled, tlBold) Retorno: nenhum Argumentos: tcPrompt especifica a etiqueta do item. tcOnSelection especifica a ação executada ao selecionar o item. tcClauses especifica qualquer cláusula de comando para o item. tnElementNumber especifica a localização do elemento na matriz. tlMark especifica se deve usar o caractere de marca padrão. tlDisabled especifica se o item de menu está desabilitado. tlBold especifica se o item está em negrito. |
| método AddMenuSeparator | Adiciona um separador ao menu de atalho. Sintaxe: AddMenuSeparator(tnElementNumber) Retorno: nenhum Argumentos: tnElementNumber especifica a posição que o separador ocupa no menu. |
| método ShowMenu | Exibe o menu de atalho existente. Sintaxe: ShowMenu( ) Retorno: nenhum Argumentos: nenhum |
| método SetMenu | Libera o menu de atalho atual para criar um novo. Sintaxe: SetMenu(toObject) Retorno: nenhum Argumentos: toObject especifica o nome do novo menu de atalho. |
| propriedade aMenu[1,0] | Interno à classe. |
