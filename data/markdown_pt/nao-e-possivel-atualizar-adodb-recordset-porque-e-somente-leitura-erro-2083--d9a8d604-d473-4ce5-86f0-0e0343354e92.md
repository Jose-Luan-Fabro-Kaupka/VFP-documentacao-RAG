# Não é possível atualizar ADODB.Recordset porque é somente leitura. (Erro 2083)

Ocorre quando o Recordset ADO fornecido está em uma configuração não atualizável e é definido como a origem de dados.
 - Certifique-se de que o Recordset ADO está configurado para suportar atualizações. O Recordset ADO deve normalmente ter sua propriedade CursorType como adOpenKeyset, adOpenDynamic ou adOpenStatic, e sua propriedade CursorLocation deve normalmente ser adUseClient.
