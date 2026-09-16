# Caixa de Diálogo Look Up Reference

Fornece uma forma de pesquisar ocorrências de uma referência de código em um projeto, pasta ou subpasta específica. Você pode filtrar sua pesquisa por tipo de arquivo.

A caixa de diálogo Look Up Reference aparece apenas no modo de design quando você seleciona Code References no menu Tools. Você também pode selecionar Look Up Reference ao clicar com o botão direito dentro da janela de edição de programas ou abrir a caixa de diálogo Look Up Reference programaticamente pela primeira vez usando o seguinte código:

```foxpro
DO(_FOXREF)
```

Para obter mais informações sobre como chamar a variável de sistema _FOXREF, consulte Variável de Sistema _FOXREF.
 **Look for**
Especifica a expressão de pesquisa de destino. O Visual FoxPro preenche a caixa Look for com a expressão selecionada na janela Editing. A caixa Look for contém quaisquer expressões selecionadas recentemente ou pesquisadas anteriormente. Quando você seleciona a caixa de seleção Use regular expressions, um botão de seta ao lado da caixa Look for torna-se disponível. Selecionar a caixa de seleção Use regular expressions permite pesquisas com caracteres curinga. Para obter mais informações, consulte "Use regular expressions" neste tópico.
**Scope**
Especifica o intervalo da pesquisa e contém as seguintes opções: Folder Pesquisar a pasta atual e, opcionalmente, subpastas. Project Pesquisar o conjunto de arquivos no projeto selecionado. Apenas projetos abertos aparecem na lista drop-down.
**Look in**
Especifica a pasta atual e contém uma lista drop-down com o histórico de pastas selecionadas anteriormente quando Folder está selecionado na caixa Scope. Para selecionar uma pasta diferente, clique no botão de reticências (...) para abrir a caixa de diálogo Select Directory. A caixa Look in não está disponível quando Project está selecionado na caixa Scope.
**Search subfolders**
Inclui subpastas da pasta selecionada em sua pesquisa. A caixa de seleção Search subfolders está disponível apenas quando Folder está selecionado na caixa Scope.
**Limit search to project home directory and subfolders**
Inclui apenas os arquivos no projeto que estão localizados dentro da pasta inicial do projeto e subpastas. Arquivos compartilhados são excluídos. Esta caixa de seleção está disponível apenas quando Project está selecionado na caixa Scope.
**Overwrite prior results**
Controla se os resultados de uma pesquisa anterior são incluídos ou substituídos na nova pesquisa. Esta opção funciona de forma semelhante a selecionar Clear All Results no menu de contexto na janela Code References para substituir todo o conteúdo no painel Search. A caixa de seleção Overwrite prior results está disponível quando o escopo Folder ou Project está selecionado.
**File Types**
Especifica um conjunto de tipos de arquivo para limitar sua pesquisa. Os tipos de arquivo são separados por vírgulas. O valor mais recente usado em uma pesquisa é usado na próxima pesquisa. Você pode adicionar tipos de arquivo personalizados usando o arquivo FoxRefAddin.dbf. A tabela FoxRefAddin permite extensões de tipo de arquivo específicas que são excluídas ao fazer uma pesquisa de nome de arquivo curinga (*.*). A tabela a seguir lista todos os tipos de arquivo do Visual FoxPro que são suportados e como as pesquisas em um tipo de arquivo são conduzidas. Extensão de arquivo Comportamento .cdx Pesquisar expressões de índice. Selecionar esta extensão requer que uma tabela esteja aberta para encontrar a expressão. .dbc Pesquisar stored procedures, fonte de remote view, conexões e outros dados .dbc, excluindo arquivos .dbf e estruturas. .dbf Pesquisar nomes de campos e quaisquer metadados de arquivo .dbc estendidos, como expressões de trigger, mas não o conteúdo da tabela. O Visual FoxPro pode precisar abrir ou fechar tabelas temporariamente se você selecionar esta extensão. .frx, .lbx Pesquisar expressões de relatório e label, valores de label e data environment. .mnx Pesquisar nomes de menu e código associado. .prg Pesquisar arquivos de programa e exibir o número da linha para a referência, se encontrada. .scx Pesquisar todo o código de método, data environment e valores de propriedade não padrão. .vcx Pesquisar todo o código de método e valores de propriedade não padrão. Outros tipos de arquivo Tratar expressões de pesquisa como texto estrito. A tabela a seguir lista grupos de tipos de arquivo padrão que aparecem na lista drop-down na caixa File Types. Tipos de arquivo Extensões de arquivo All Files *.* Common *.scx, *.vcx, *.prg, *.frx, *.lbx, *.mnx, *.dbc, *.qpr, *.h All Source *.scx, *.vcx, *.prg, *.frx, *.lbx, *.mnx, *.dbc, *.dbf, *.cdx, *.qpr, *.h Forms and Classes *.scx, *.vcx, *.prg Reports and Labels *.frx, *.lbx Menus *.mnx Programs *.prg, *.h, *.qpr, *.mpr Data Structures *.dbc, *.dbf, *.cdx Text *.txt, *.xml, *.xsl, *.html, *.log, *.asp, *.aspx Observação O grupo de tipos de arquivo de origem Common inclui apenas arquivos .dbc como opção de fonte de dados por padrão. O comportamento padrão é pesquisar apenas stored procedures. Você pode alterar este comportamento clicando no botão Options na caixa de diálogo Look Up Reference.
**Options**
Abre a caixa de diálogo Options para definir opções adicionais para sua pesquisa. Para obter mais informações, consulte Caixa de Diálogo Look Up Reference, Caixa de Diálogo Options .

# Grupo Options

A caixa de grupo Options inclui opções adicionais que você pode especificar para personalizar sua pesquisa.
 **Match case**
Especifica se sua pesquisa é sensível a maiúsculas e minúsculas.
**Match whole word**
Especifica se sua pesquisa deve corresponder a palavras inteiras exatamente.
**Use regular expressions**
Permite pesquisas com caracteres curinga. Selecionar a caixa de seleção Use regular expressions habilita o botão de seta ao lado da caixa Look for. Clicar no botão de seta abre um menu do qual você pode selecionar um tipo de expressão regular para inserir na caixa Look for. Para obter mais informações sobre expressões regulares, consulte Expressões Regulares e Operadores .
**Comments**
Especifica se deve incluir comentários de código em sua pesquisa. Comentários começam com um asterisco (*), duplo e comercial (&&) ou palavra-chave NOTE. A lista drop-down Comments inclui as seguintes opções: Include Comments Incluir comentários em sua pesquisa. Ignore Comments Ignorar comentários em sua pesquisa. Comments Only Pesquisar apenas comentários.
