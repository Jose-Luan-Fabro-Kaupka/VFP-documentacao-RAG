# How to: Add Code to a DBC Evento

Você pode adicionar código de procedimento a um evento DBC armazenando-o no arquivo de procedimentos armazenados do banco de dados ou em um arquivo de programa separado (.prg). Quando os eventos DBC são ativados para um banco de dados, o código do procedimento é executado.

### Para adicionar código a um evento DBC
- Abra o banco de dados no Database Designer.
- No menu Banco de dados, clique em Propriedades. A caixa de diálogo Propriedades do Banco de Dados é aberta. Se você ativou eventos DBC para o banco de dados, a caixa de seleção Arquivo de Eventos aparecerá disponível.
- Na lista Eventos, clique em an evento. Dica Para selecionar vários eventos, pressione e segure a tecla SHIFT enquanto clica no evento each.
- Escolha uma das seguintes opções: Para adicionar código ao arquivo de procedimento armazenado do banco de dados atual, clique em Editar código . -OR- Para adicionar código a um arquivo externo, clique na caixa de seleção Arquivo de eventos. Se nenhum arquivo for especificado, a caixa de diálogo Abrir será exibida para que você possa especificar um arquivo. Se um arquivo já tiver sido especificado, clique no botão de reticências (...) para exibir a caixa de diálogo Abrir. Cuidado Marcar a caixa de seleção Arquivo de Eventos altera a estrutura do banco de dados e torna o banco de dados não mais compatível com versões anteriores ao Visual FoxPro 7.0 ou ao Driver Visual FoxPro ODBC. Desmarcar a caixa de seleção Arquivo de Eventos torna o banco de dados compatível.

Uma janela de edição dos procedimentos armazenados ou arquivo externo é aberta com códigos de modelo de procedimento para o evento DBC.
