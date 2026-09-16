# O cursor "name" está associado a outro objeto CursorAdapter. (Erro 2112)

O Visual FoxPro não permite que um cursor seja associado a um objeto CursorAdapter se ele já estiver associado a outro objeto CursorAdapter.
 - Para verificar se um cursor já está associado a um CursorAdapter, verifique sua propriedade SourceType usando a função CursorGetProp( ).
