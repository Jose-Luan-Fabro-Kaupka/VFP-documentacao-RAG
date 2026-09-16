# Caixa de diálogo Coverage Profiler Statistics

Exibe informações resumidas do arquivo .log atual e fornece acesso a informações de projeto, texto de origem e arquivos ignorados.

# Statistics

Exibe informações resumidas sobre o arquivo selecionado no painel Source List. O conteúdo desta área depende do tipo de arquivo selecionado. A caixa de diálogo exibe estatísticas apenas sobre linhas nos casos de arquivos de banco de dados (.dbc) ou de programa (.prg). No caso de tipos de arquivo como .frx, .lbx, .scx e .vcx, que contêm classes, a caixa de diálogo exibe informações sobre linhas e sobre classes. Os detalhes que compõem essas informações são exibidos no painel Source Code como informações de modo Coverage ou Profile.

# View Details
 **Statistics by Project**
Permite selecionar um arquivo de projeto e gerar um relatório detalhado e resumido sobre a cobertura do projeto.
**Source Text Log**
Exibe o arquivo de log atual no editor do Visual FoxPro.
**Source Files Skipped**
Abre uma janela Browse no cursor SkippedFiles. Este cursor contém nomes de arquivos para os quais o Coverage Profiler não fornece informações. Esses arquivos podem ser arquivos para os quais você não tem código não compilado, arquivos que o Coverage Profiler não conseguiu localizar ou código-fonte do Coverage Profiler.
