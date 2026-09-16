# Comandos CLOSE

Fecha vários tipos de arquivo.

```foxpro
CLOSE [ALL | ALTERNATE | DATABASES [ALL] | DEBUGGER | FORMAT | INDEXES
   | PROCEDURE | TABLES [ALL]]
```

#### Parâmetros
 **ALL**
Fecha todos os bancos de dados, tabelas e índices abertos na sessão de dados atual e em qualquer sessão de dados inativa e seleciona a área de trabalho 1. CLOSE ALL também fecha quaisquer arquivos abertos com as funções de arquivo de baixo nível FCREATE( ) e FOPEN( ), e quaisquer arquivos de procedimento abertos com SET PROCEDURE. CLOSE ALL não fecha um arquivo aberto com SET PRINT. CLOSE ALL também fecha o seguinte: Form Designer Project Manager Label Designer Report Designer Query Designer CLOSE ALL não fecha estes: Command window Debug window Help Trace window
**CLOSE ALTERNATE**
Fecha um arquivo alternativo aberto com SET ALTERNATE.
**CLOSE DATABASES [ALL]**
Fecha o banco de dados atual na sessão de dados atual e suas tabelas. Se não houver banco de dados atual, todas as tabelas livres, índices e arquivos de formato abertos em todas as áreas de trabalho na sessão de dados atual são fechados, e a área de trabalho 1 é selecionada. Observação Usar CLOSE DATABASES na janela Command não fecha um banco de dados se o banco de dados foi aberto no Project Manager expandindo seu nó ou quando um formulário está em execução em sua própria sessão de dados. Nessas circunstâncias, o banco de dados permanece aberto até que o Project Manager feche o banco de dados ou até que o formulário que usa o banco de dados seja fechado. A palavra-chave ALL especifica fechar os seguintes itens na sessão de dados atual e em todas as sessões de dados inativas e que a área de trabalho 1 é selecionada: Todos os bancos de dados abertos e suas tabelas, exceto bancos de dados atualmente selecionados em outras sessões de dados ou bancos de dados e suas tabelas que estão abertos em outras sessões de dados. Todas as tabelas livres abertas. Todos os índices e arquivos de formato em todas as áreas de trabalho.
**CLOSE DEBUGGER**
Fecha o depurador do Visual FoxPro.
**CLOSE FORMAT**
Fecha um arquivo de formato na área de trabalho atual aberto com SET FORMAT.
**CLOSE INDEXES**
Fecha todos os arquivos de índice abertos (tanto arquivos .idx de entrada única quanto arquivos .cdx compostos independentes) na área de trabalho atual. Um índice composto estrutural (um arquivo .cdx aberto automaticamente com a tabela) não é fechado.
**CLOSE PROCEDURE**
Fecha um arquivo de procedimento aberto com SET PROCEDURE.
**CLOSE TABLES [ALL]**
Fecha todas as tabelas no banco de dados atualmente selecionado. CLOSE TABLES fecha todas as tabelas livres em todas as áreas de trabalho se um banco de dados não estiver aberto. Inclua ALL para fechar todas as tabelas em todos os bancos de dados e todas as tabelas livres. Todos os bancos de dados permanecem abertos. CLOSE TABLES não deve ser emitido quando uma transação está em andamento; o Visual FoxPro gerará uma mensagem de erro.
