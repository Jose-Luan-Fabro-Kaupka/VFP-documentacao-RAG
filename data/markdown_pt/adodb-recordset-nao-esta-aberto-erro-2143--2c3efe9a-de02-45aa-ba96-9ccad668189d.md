# ADODB.Recordset não está aberto. (Erro 2143)

O Visual FoxPro exige que um Recordset ADO esteja aberto quando ele é passado ao parâmetro Source dos métodos CursorFill.
 - Certifique-se de que o Recordset ADO foi aberto corretamente e que o State do Recordset ADO está definido como adStateOpen (1).
