# Conflito de atualização. Algumas das suas alterações no lote de registros atual foram confirmadas (Erro 1595)

O texto completo desta mensagem de erro é:

Update conflict. Some of your changes in the current row batch were committed. Use TABLEUPDATE( ) with the lForce parameter to commit the update or the manual transaction to roll back the update (Error 1595)

A atualização de várias tabelas não foi incluída em uma transação remota e falhou.
 - Algumas das tabelas envolvidas na atualização podem ter sido confirmadas nas tabelas remotas base. Force a atualização para o registro atual ou para o lote de registros atual ou reverta a transação manual remota na conexão atual. Para obter mais informações, consulte TABLEUPDATE( ) Function .
