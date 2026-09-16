# Caixa de diálogo Propriedades de edição

Esta caixa de diálogo permite definir opções de edição para a janela de edição atual ou definir opções de cor e fonte para todas as sessões de edição.

Esta caixa de diálogo aparece quando você escolhe Properties no menu de atalho de qualquer janela de edição ou quando você clica em Properties no menu Edit.

# Comportamento

As opções nesta área afetam apenas a janela de edição atual.
 **Drag-and-drop editing**
Habilita edição de texto por arrastar e soltar para manipular texto com o mouse.
**Wordwrap**
Quebra linhas de texto dentro da janela. Wordwrap está disponível apenas quando a coloração de sintaxe está definida como OFF. Para obter mais informações, consulte Guia Editor, Caixa de diálogo Options .
**Automatic indent**
Recua automaticamente o texto de acordo com a indentação da primeira linha. Isso não afeta como o texto é salvo.
**Embedded hyperlinks**
Permite especificar se hiperlinks podem ser incluídos no tipo de arquivo selecionado.

# Aparência

Permite controlar o tamanho, estilo, cor e outras características do texto.
 **Alignment**
Especifica alinhamento à esquerda, centralizado ou à direita do texto.
**Font**
Altera a fonte na janela de edição. Clique no botão de reticências (...) para abrir a caixa de diálogo Font.
**Show line/column position**
Habilita a exibição do número da linha e da posição da coluna na barra de status. O número da linha não é exibido se wordwrap estiver habilitado.
**Syntax coloring**
Alterna se as cores são exibidas para elementos de sintaxe. Você só pode selecionar se wordwrap estiver definido como OFF. Para obter mais informações, consulte Guia Editor, Caixa de diálogo Options .
**Display white space**
Especifica se espaços, tabulações e parágrafos aparecem como caracteres no editor atualmente ativo. Esta opção está disponível quando você trabalha no editor de texto. Marcadores de parágrafo (line feeds) aparecem apenas se a opção wordwrap estiver habilitada. Para exibir espaço em branco, clique em View White Space no menu Format. Observação A opção View White Space não é suportada em plataformas de conjunto de caracteres de byte duplo (DBCS).

# Opções de salvamento

Permite gerenciar características de arquivos salvos. As opções de salvamento disponíveis dependem do tipo de arquivo que você abre.
 **Make backup copy**
Especifica que o Visual FoxPro crie uma cópia de backup cada vez que você salvar um arquivo. A cópia de backup é salva com o nome do arquivo e uma extensão .bak na sua pasta Visual FoxPro Projects.
**Save with line feeds**
Salva o arquivo com line feeds que foram inseridos nele. Se esta caixa não estiver selecionada, os line feeds são removidos quando o arquivo é salvo. Para obter mais informações, consulte Propriedade AddLineFeeds .
**Save with end-of-file marker**
Coloca um caractere CTRL+Z no final de um arquivo quando o arquivo é salvo. Este caractere extra, quando salvo com o arquivo, ajuda a resolver a diferença entre atividade de edição normal e atividade MODIFY MEMO. Para obter mais informações, consulte Comando MODIFY MEMO .
**Compile before saving (Program editor)**
Especifica que o Visual FoxPro compile automaticamente o programa e verifique erros de sintaxe quando o arquivo é salvo.
**Save preferences**
Determina se as configurações de um arquivo aberto e todas as outras janelas desse mesmo tipo são salvas para a próxima vez que forem abertas. Se Save preferences não estiver selecionado, as preferências são salvas apenas para a janela aberta individual.
**Apply to method code (Form or Class Designer)**
Especifica as configurações atuais como padrão para todos os métodos de formulário ou classe.
**Apply to menu code (Menu Designer)**
Especifica as configurações atuais como padrão para todos os procedimentos de menu.
**Apply to .PRG or .TXT files (Program or text editor)**
Especifica as configurações atuais como padrão para arquivos .prg ou .txt.
**Apply to memos (Memo field editor)**
Especifica as configurações atuais como padrão para campos memo.

# Indentação

Permite especificar o tamanho e o comportamento de espaços e tabulações.
 **Tab size**
Especifica a largura, em caracteres, de uma tabulação para o tipo de arquivo atualmente selecionado. O intervalo é de 1 a 50. O valor padrão é 4.
**Indent size**
Especifica a largura, em caracteres, de uma indentação de parágrafo para o tipo de arquivo atualmente selecionado. Se for diferente do tamanho da tabulação, tabulações e/ou espaços extras são usados para criar o valor especificado. O intervalo é de 1 a 50. O valor padrão é 4.
**Insert spaces**
Especifica que espaços sejam inseridos pela tecla tab para o tipo de arquivo atualmente selecionado. O valor padrão é 4.
**Keep tabs**
Especifica que tabulações sejam inseridas pela tecla tab para o tipo de arquivo atualmente selecionado (padrão).

# Informações do arquivo (Editor de programa ou texto)

Permite especificar as características do sistema de arquivos salvos.
 **File Name**
Especifica o nome e o diretório do programa ou arquivo de texto que está sendo editado.
**Size**
Especifica o tamanho do programa ou arquivo de texto que está sendo editado.
**Last Saved**
A data e hora em que o programa ou arquivo de texto foi salvo pela última vez no disco.
