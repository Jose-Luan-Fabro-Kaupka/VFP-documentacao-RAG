# Não é possível atualizar ADODB.Recordset porque o cursor FOX não possui uma coluna ADOBookmark. (Erro 2085)

O Visual FoxPro exige que um cursor esteja associado a um ADO Recordset, se for usado para atualizar um ADO Recordset.
 - Para verificar se um cursor está associado a um ADO Recordset, verifique sua propriedade SourceType usando a função CursorGetProp( ). Valores válidos para a propriedade SouceType são 4, 104 e 204.
