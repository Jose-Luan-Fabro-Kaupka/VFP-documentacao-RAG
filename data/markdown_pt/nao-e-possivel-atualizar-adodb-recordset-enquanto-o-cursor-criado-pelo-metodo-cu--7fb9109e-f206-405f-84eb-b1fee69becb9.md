# Não é possível atualizar ADODB.Recordset enquanto o cursor, criado pelo método CursorAdapter.CursorFill, não estiver anexado a um objeto CursorAdapter. (Erro 2082)

O Visual FoxPro requer que um cursor, criado a partir de um Recordset ADO usando o método CursorFill, esteja anexado a um objeto CursorAdapter antes de poder ser atualizado.
 - Para atualizar o cursor, reanexe o cursor ao objeto CursorAdapter.
