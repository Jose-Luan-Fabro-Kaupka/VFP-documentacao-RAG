# Como: excluir tabelas

Você pode remover tabelas ou excluí-las permanentemente do disco quando não precisar mais delas. Para obter informações sobre remover e excluir tabelas de banco de dados, consulte How to: Remove a Table from a Database.

> **Observação:** Se você excluir uma tabela que tenha arquivos associados, como um arquivo memo (.fpt) ou arquivos de índice (.cdx ou .idx), certifique-se de excluir esses arquivos.

### Para remover ou excluir uma free table
- Abra o projeto no Project Manager .
- No Project Manager , expanda o nó Data e depois o nó Free Tables.
- No nó Free Tables, clique na tabela desejada e depois em Remove . Uma caixa de diálogo de confirmação é exibida para que você possa escolher remover ou excluir a tabela.
- Na caixa de diálogo de confirmação, escolha uma das seguintes opções Para remover a tabela do projeto, clique em Remove . -OU- Para excluir a tabela permanentemente do disco, clique em Delete .

Para obter mais informações, consulte Project Manager Window.

### Para excluir uma free table programaticamente
- Feche a tabela com o comando CLOSE e a palavra-chave TABLES.
- Exclua o arquivo usando o comando DELETE FILE ou o comando ERASE.

Para obter mais informações, consulte DELETE FILE Command e ERASE Command.
