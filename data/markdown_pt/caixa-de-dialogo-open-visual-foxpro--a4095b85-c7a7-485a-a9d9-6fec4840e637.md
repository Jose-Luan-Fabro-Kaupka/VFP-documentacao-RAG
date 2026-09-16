# Caixa de diálogo Open (Visual FoxPro)

Usada para abrir um arquivo existente ou criar um novo arquivo. Esta caixa de diálogo aparece quando você seleciona Open no menu File.

Projetos abertos anteriormente aparecem na parte inferior do menu File. Você pode abrir um projeto aberto anteriormente escolhendo seu nome na parte inferior do menu File.

> **Observação:** Arquivos criados com o comando Open não são adicionados a um projeto.

A função GETFILE( ) corresponde à caixa de diálogo Open. Por exemplo, esta caixa de diálogo aparece quando você digita `? GETFILE( )` na janela Command.

# Atalho

CTRL+O
 **Look in**
Exibe uma lista suspensa de locais onde você pode procurar seu arquivo. Nos sistemas operacionais Windows 2000 e Windows XP, a barra Places no lado esquerdo da caixa de diálogo exibe locais comuns, como My Documents e Desktop. Clique em um desses ícones para fazer o local correspondente aparecer na lista suspensa.
**File name**
Exibe o nome do arquivo atualmente selecionado ou permite especificar o arquivo que você deseja abrir.
**Class Library**
Especifica o nome da biblioteca de classes. Esta caixa aparece somente ao abrir uma biblioteca de classes ou ao usar AGETCLASS( ) ou MODIFY CLASS .
**Files of type**
Exibe uma lista de tipos de arquivo. Você pode selecionar um tipo de arquivo na lista suspensa para exibir somente arquivos de um tipo específico. As seguintes extensões não são mais usadas nesta versão do Visual FoxPro: .lbl, .fpc, .cat e .frm.
**Class Name**
Exibe classes armazenadas na biblioteca de classes exibida na caixa Class Name. Esta lista aparece somente ao abrir uma biblioteca de classes ou ao usar AGETCLASS( ) ou MODIFY CLASS .
**Open as read-only**
Especifica que o arquivo que você abre pode ser visualizado, mas não modificado.
**Environment**
Salva todas as configurações de ambiente com o arquivo e abre o ambiente associado quando você abre o arquivo. Observação A caixa de seleção Environment aparece somente em versões anteriores ao Visual FoxPro 8.0. Esta opção está disponível quando você escolhe Form, Label ou Report na lista List Files of Type e é marcada por padrão. Para abrir um formulário, etiqueta ou relatório sem abrir um ambiente associado, desmarque a caixa de seleção.
**Open exclusive**
Especifica que você pode usar uma tabela (.dbf) ou um arquivo de banco de dados (.dbc) de forma exclusiva, de modo que nenhum outro usuário possa abrir o arquivo. Esta opção está disponível somente ao abrir uma tabela. Corresponde ao comando USE.
**Code Page**
Exibe a caixa de diálogo Code Page para que você possa especificar a página de código necessária para visualizar o arquivo corretamente. Este comando se aplica somente a arquivos de texto, como programas (.prg), consultas (.qpr) e texto (.txt).
**Preview**
Especifica que você pode visualizar arquivos gráficos quando eles são selecionados na lista de arquivos. Esta caixa de seleção aparece somente quando você pode abrir ou selecionar um arquivo gráfico. Por exemplo, esta caixa de seleção aparece na caixa de diálogo Open quando você adiciona um controle Image a um formulário e clica duas vezes na propriedade Picture na janela Properties. Observação A caixa de seleção Preview aparece somente ao executar o Visual FoxPro em sistemas operacionais anteriores ao Windows 2000. Você pode visualizar imagens no Windows 2000 e posteriores clicando no ícone View Menu perto do topo da caixa de diálogo e depois em Thumbnails.
