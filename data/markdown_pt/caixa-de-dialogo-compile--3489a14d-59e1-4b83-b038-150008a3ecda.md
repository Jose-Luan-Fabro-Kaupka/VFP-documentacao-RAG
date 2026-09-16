# Caixa de diálogo Compile

Permite compilar arquivos de programa, menu ou consulta.

> **Observação:** Se você tem um programa aberto na janela Edit, o comando Compile compila o programa atual sem exibir nenhuma opção.

Esta caixa de diálogo aparece quando você escolhe Compile no menu Program.
 **File name**
Exibe arquivos que você pode selecionar para compilar. Para compilar arquivos, selecione o nome do arquivo na lista e escolha Compile, ou clique duas vezes no nome do arquivo. Para escolher vários arquivos, pressione e mantenha pressionada a tecla CTRL enquanto seleciona nomes de arquivo. Os arquivos exibidos são aqueles no diretório atual que correspondem ao tipo especificado na caixa List files of type.
**Directories**
Exibe o diretório atual. Você pode selecionar um diretório diferente que contenha os arquivos que deseja compilar.
**Drives**
Exibe a unidade atual. Você pode selecionar uma unidade de disco rígido diferente que contenha os arquivos que deseja compilar.
**List files of type**
Lista os tipos de arquivo disponíveis com Program (.prg) como padrão. Se você atribuiu aos seus programas, formulários, menus ou consultas uma extensão diferente do padrão do Visual FoxPro, pode vê-los escolhendo All Files.
**Compile**
Compila os arquivos selecionados.
**Select All**
Seleciona todos os arquivos na caixa File name para compilação.
**Deselect All**
Limpa a seleção de todos os arquivos na caixa File name.
**More**
Expande a caixa de diálogo Compile para que você possa especificar outras opções.

# Opções
 **Encrypt compiled files**
Codifica arquivos compilados para impedir que programas de descompilação reconstruam o código-fonte.
**Include debugging information**
Especifica se incluir informações de depuração com o arquivo compilado. Se esta caixa de seleção não estiver marcada, você não pode visualizar a execução do programa na janela Trace do Debugger. Esta caixa de seleção corresponde à palavra-chave NODEBUG no comando COMPILE.
**Compile updated files only**
Compila apenas os arquivos selecionados que são novos ou foram atualizados desde a última vez que foram compilados.

# Localização de mensagens de erro
 **.ERR File**
Armazena mensagens de erro para cada arquivo selecionado em um arquivo de erro (.err) separado com o mesmo nome base do arquivo original. O arquivo .err é armazenado no mesmo diretório do arquivo de origem. Se você não marcar esta caixa, as mensagens de erro para todos os arquivos selecionados são armazenadas juntas em um arquivo que você especifica na caixa File.
**Append**
Adiciona mensagens de erro para cada arquivo selecionado a um arquivo de log existente. Esta caixa de seleção é habilitada se você desmarcar a caixa de seleção .err File.
**File**
Armazena mensagens de erro para todos os arquivos selecionados em um arquivo de log. Digite o nome do arquivo de log na caixa ou escolha o botão de diálogo para localizar e especificar um arquivo de log existente. Esta caixa de texto é habilitada se você desmarcar a caixa de seleção .err File.

# Localização de arquivos compilados
 **Directory**
Especifica um caminho para armazenar arquivos de saída compilados. Digite o caminho na caixa ou escolha o botão de reticências (...) para navegar e selecionar um diretório e nome de arquivo.
