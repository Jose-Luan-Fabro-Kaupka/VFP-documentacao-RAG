# ADODB.Command já está aberto. (Erro 2081)

O Visual FoxPro exige que o State de objetos ADO Command seja igual a adStateClosed ao tentar passar um objeto ADO Command para o parâmetro Source dos métodos CursorFill.
