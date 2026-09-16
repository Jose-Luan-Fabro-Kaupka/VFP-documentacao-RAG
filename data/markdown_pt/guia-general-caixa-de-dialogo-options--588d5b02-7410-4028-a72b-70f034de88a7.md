# Guia General, caixa de diálogo Options

Contém opções de som, programação, entrada de dados e outras opções no Visual FoxPro.

Quando você escolhe Set As Default — que aparece em cada guia da caixa de diálogo — o Visual FoxPro salva todas as opções em todas as guias.

# Som de aviso
 **Off**
Desativa o som de erro. Corresponde ao comando SET BELL .
**Default**
Define o som de erro como o padrão do sistema. Corresponde ao comando SET BELL .
**Play**
Define o som de erro como um arquivo .wav. Digite o nome do arquivo na caixa ou clique no botão de diálogo para selecionar um arquivo .wav existente. Corresponde ao comando SET BELL .

# Programação
 **Cancel programs on Escape**
Especifica que você pode cancelar um programa em execução pressionando a tecla ESC. Corresponde ao comando SET ESCAPE .
**Log compilation errors**
Especifica que o Visual FoxPro registra erros de compilação em um arquivo com o mesmo nome do arquivo do projeto, mas com extensão .err. Corresponde ao comando SET LOGERRORS .
**SET DEVELOPMENT**
Especifica que o Visual FoxPro recompila um programa antes de executá-lo se o código objeto for mais antigo que o código-fonte. Corresponde ao comando SET DEVELOPMENT .
**dBASE compatibility**
Especifica compatibilidade com as linguagens FoxBASE+ e dBASE. Corresponde ao comando SET COMPATIBLE .
**Use Visual FoxPro color palette**
Especifica que o Visual FoxPro aplica a paleta de cores padrão a todos os bitmaps e objetos OLE, o que evita deslocamento de paleta quando várias imagens são exibidas ao mesmo tempo. Corresponde ao comando SET PALETTE .
**Confirm file replacement**
Especifica que o Visual FoxPro solicita verificação quando você está prestes a substituir arquivos existentes por novos. Corresponde ao comando SET SAFETY .
**Browse IME control**
Especifica que o Visual FoxPro exibe um Input Method Editor quando você navega para uma caixa de texto na janela Browse. Esta configuração não tem efeito se você não estiver trabalhando em um ambiente de conjuntos de caracteres de byte duplo (DBCS). Corresponde ao comando SET BROWSEIME .

# Entrada de dados
 **Navigation keys**
Especifica se deve usar teclas de navegação compatíveis com Windows ou MS-DOS para tarefas como mover entre controles em formulários. Corresponde ao comando SET KEYCOMP .
**Fill new records with current values**
Especifica que o Visual FoxPro copia automaticamente valores do registro atual para um novo registro que você está inserindo ou anexando. Corresponde ao comando SET CARRY .
**Enter or tab to exit fields**
Especifica que você deseja sair de caixas de texto somente pressionando ENTER ou TAB. Caso contrário, você pode sair de caixas de texto digitando além do último caractere na caixa de texto. Corresponde ao comando SET CONFIRM .

# Conformidade com o ano 2000
 **Strict Date Level**
Especifica se datas ambíguas e constantes DateTime geram erros. Corresponde ao comando SET STRICTDATE .
