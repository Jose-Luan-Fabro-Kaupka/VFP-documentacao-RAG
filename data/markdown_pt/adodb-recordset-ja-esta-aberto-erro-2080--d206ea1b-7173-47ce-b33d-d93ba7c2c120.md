# ADODB.Recordset já está aberto. (Erro 2080)

O Visual FoxPro exige que um ADO Recordset esteja fechado quando ele está sendo adicionado a um objeto CursorAdapter. Isso ocorre porque o método CursorFill tenta abrir o ADO Recordset quando ele está sendo adicionado. Para usar um ADO Recordset que já está aberto, passe-o para o parâmetro Source do método CursorFill.
