# Guia Data Environment, Caixa de Diálogo Report Properties (Report Builder)

Permite especificar configurações de ambiente de dados e sessão de dados para o relatório ou etiqueta.

Esta guia é pré-selecionada quando você escolhe Load data environment no menu Report.
 - How to: Load Data Environments for Reports
- How to: Specify a Report's Data Session

# Load data environment

Especifica opções para carregar um ambiente de dados para o relatório ou etiqueta.
 **Copy from another report file**
Especifica substituir o ambiente de dados atual do layout por uma cópia do ambiente de dados de outro arquivo de relatório (.frx) ou etiqueta (.lbx).
**Link to a DataEnvironment class**
Especifica vincular a uma classe DataEnvironment em um arquivo de biblioteca de classes visual (.vcx) ou biblioteca de classes programática (.prg).
**Select**
Exibe a caixa de diálogo Open para que você possa selecionar um relatório, etiqueta ou arquivo de biblioteca de classes visual contendo o ambiente de dados que deseja usar.
**Class**
Exibe a classe DataEnvironment escolhida.
**Class Library / Source**
Exibe a biblioteca de classes visual (.vcx) ou o arquivo de programa (.prg) contendo a classe DataEnvironment, ou o arquivo de relatório (.frx) ou etiqueta (.lbx) de origem do qual o ambiente de dados foi carregado.
**Report uses a private data session**
Especifica que o report engine deve usar uma sessão de dados exclusiva ao executar o relatório. As únicas tabelas disponíveis serão as do Data Environment do relatório ou abertas explicitamente no código de método.
