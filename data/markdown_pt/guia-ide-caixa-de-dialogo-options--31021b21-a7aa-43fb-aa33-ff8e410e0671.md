# Guia IDE, caixa de diálogo Options

Contém opções para os editores do Visual FoxPro.

# Specify file/window

Permite especificar quais tipos de arquivo são afetados pelas configurações feitas nesta guia.
 **Type:**
Permite especificar os editores ou os tipos de arquivos para os quais você está definindo condições de edição padrão.
**Extensions:**
Especifica as extensões de arquivo do tipo de arquivos selecionado.
**Override individual settings**
Permite substituir temporariamente as configurações padrão do FoxUser.

# Indentation

Permite especificar o tamanho e o comportamento de espaços e tabulações.
 **Tab size**
Especifica a largura, em caracteres, de uma tabulação para o tipo de arquivo selecionado no momento. O intervalo é de 1 a 50. O valor padrão é 4.
**Indent size**
Especifica a largura, em caracteres, de um recuo de parágrafo para o tipo de arquivo selecionado no momento. Se for diferente do tamanho da tabulação, tabulações e/ou espaços extras são usados para criar o valor especificado. O intervalo é de 1 a 50. O valor padrão é 4.
**Insert spaces**
Especifica que espaços sejam inseridos pela tecla Tab para o tipo de arquivo selecionado no momento. O valor padrão é 4.
**Keep tabs**
Especifica que tabulações sejam inseridas pela tecla Tab para o tipo de arquivo selecionado no momento (padrão).

# Save options

Permite especificar como os arquivos do tipo selecionado são salvos.
 **Make backup**
Para alguns tipos de arquivo, especifica se um arquivo de backup é criado sempre que você salva um arquivo desse tipo.
**Save with line feeds**
Especifica que o tipo de arquivo atual seja salvo com os caracteres de retorno e avanço de linha CHR(13)+CHR(10).
**Save with end-of-file marker**
Especifica que o tipo de arquivo atual seja salvo com CTRL+Z no final do arquivo.
**Compile before saving**
Especifica que uma compilação seja tentada antes que o tipo de arquivo atual seja salvo.

# Appearance and behavior

Permite especificar como o texto aparece no tipo de arquivo selecionado.
 **Alignment:**
Especifica se o tipo de arquivo atual é formatado à esquerda, centralizado ou à direita.
**Font:**
Especifica a fonte, o estilo, o tamanho e o script do tipo de arquivo atual.
**Use font script**
Especifica que o script de fonte atual seja usado globalmente em todo o Visual FoxPro. Se esta caixa de seleção não estiver marcada, o Visual FoxPro usa o script de fonte padrão do Windows.
**Drag-and-drop editing**
Especifica se arquivos subsequentes do tipo de arquivo selecionado fornecem comportamento de arrastar e soltar. Para desabilitar arrastar e soltar, você também deve selecionar a caixa de seleção override individual settings. Essas seleções, uma vez aplicadas, funcionam em todos os arquivos dos tipos de arquivo selecionados abertos posteriormente.
**Automatic indent**
Permite especificar que um recuo seja automaticamente mantido em linhas subsequentes a uma linha recuada.
**Show line/column position**
Permite exibir, na linha de status da janela principal, o número da linha e da coluna do cursor em campos Memo.
**Word wrap**
Para alguns tipos de arquivo, permite especificar se as palavras quebram para a próxima linha no limite da janela do editor.
**Syntax coloring**
Permite especificar se a coloração de sintaxe está disponível para o tipo de arquivo selecionado. Você pode gerenciar parâmetros de cor de sintaxe na guia Editor, caixa de diálogo Options.
**Embedded hyperlinks**
Permite especificar se hiperlinks podem ser incluídos no tipo de arquivo selecionado. Atributos de não visitado, visitado e hover estão disponíveis se você tiver o Internet Explorer instalado.
**Display white space**
Permite especificar se espaços, tabulações, parágrafos e outros marcadores de não caractere são exibidos nos editores para o tipo de arquivo selecionado.

# Apply button

Salva as configurações pendentes para o tipo de arquivo selecionado no momento.

# Reset All button

Restaura os padrões do Visual FoxPro para o tipo de arquivo selecionado. Para restaurar todas as configurações de tipo, você deve usar a lista Specify file/window e clicar em Reset All para cada tipo de arquivo na lista.
