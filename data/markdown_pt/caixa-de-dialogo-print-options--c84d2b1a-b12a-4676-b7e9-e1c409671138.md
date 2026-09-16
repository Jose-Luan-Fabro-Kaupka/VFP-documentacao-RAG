# Caixa de diálogo Print Options

Permite especificar opções para imprimir arquivos ou o conteúdo da janela Command ou da Área de Transferência.

Esta caixa de diálogo aparece quando você seleciona Options na caixa de diálogo Print. Para obter mais informações, consulte a caixa de diálogo Print (Visual FoxPro).

# Print What

Especifica o tipo e o arquivo a imprimir.
 **Type**
Especifica o tipo de arquivo a imprimir. Cuidado A opção ASCII File ignora o driver da impressora e envia o conteúdo do arquivo selecionado diretamente para a impressora. Certifique-se de que o arquivo contém comandos de impressora válidos. Enviar comandos de impressora inválidos ao dispositivo de impressão pode causar falha na impressora e exigir uma reinicialização.
**File**
Especifica o caminho e o nome do arquivo que deseja imprimir. Para procurar e selecionar um arquivo, clique no botão de reticências (...) para abrir a caixa de diálogo Print File. Para obter mais informações, consulte a caixa de diálogo Print File.

# Print Options

Especifica opções de saída para o arquivo.
 **Line numbers**
Imprime números de linha na margem esquerda. Esta opção está disponível para imprimir o conteúdo da janela Command e da Área de Transferência.
**Page eject before**
Avança a impressora para o topo da próxima página antes de imprimir o arquivo.
**Page eject after**
Avança a impressora para o topo da próxima página após imprimir o arquivo. Esta opção não está disponível para relatórios e etiquetas.
**Restore environment**
Ao executar relatórios do FoxPro versão 2.x, garante que as configurações do ambiente de dados previamente salvas com o relatório sejam usadas para executar o relatório. Esta opção não se aplica a relatórios do Visual FoxPro porque eles usam seus próprios ambientes de dados.
**Options**
Exibe a caixa de diálogo Report and Label Print Options para selecionar registros que deseja imprimir de um relatório ou etiqueta. Disponível somente ao imprimir relatórios e etiquetas. Para obter mais informações, consulte a caixa de diálogo Report and Label Print Options.
