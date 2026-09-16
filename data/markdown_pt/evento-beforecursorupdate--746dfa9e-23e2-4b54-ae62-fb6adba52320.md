# Evento BeforeCursorUpdate

Ocorre imediatamente antes da execução da função TABLEUPDATE( ).

```foxpro
PROCEDURE Object.BeforeCursorUpdate
LPARAMETERS nRows, lForce
```

#### Parâmetros
 **nRows**
Especifica a configuração do parâmetro nRows da função TABLEUPDATE( ).
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE( ).

# Observações

Aplica-se a: CursorAdapter Class

BeforeCursorUpdate ocorre uma vez no início do processo de atualização. Se várias linhas estão sendo atualizadas, os eventos BeforeUpdate, BeforeInsert e BeforeDelete ocorrem para cada linha atualizada, conforme apropriado.

Se o código em BeforeCursorUpdate retornar False (.F.), nenhuma operação de atualização, inserção ou exclusão ocorre.
