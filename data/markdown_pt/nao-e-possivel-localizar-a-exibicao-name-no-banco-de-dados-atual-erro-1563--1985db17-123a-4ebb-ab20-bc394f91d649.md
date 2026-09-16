# Não é possível localizar a exibição "name" no banco de dados atual (Erro 1563)

O nome especificado não é o nome de uma exibição no banco de dados atual. Verifique se o nome inserido está correto e se o banco de dados atual é o banco de dados necessário. Use o comando DISPLAY VIEWS ou o comando LIST VIEWS para confirmar os nomes das exibições existentes no banco de dados.

Se o nome da exibição estiver na lista, o índice .dbc poderá estar corrompido.

### Para recriar o índice
- Feche o banco de dados.
- Exclua o arquivo de índice (database_name.DCX).
- Reabra o banco de dados.
- Recrie o índice.
