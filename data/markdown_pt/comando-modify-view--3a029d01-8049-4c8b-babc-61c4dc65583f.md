# Comando MODIFY VIEW

Exibe o View Designer, permitindo modificar uma exibição SQL existente.

```foxpro
MODIFY VIEW ViewName [REMOTE][NOWAIT]
```

#### Parâmetros
 **ViewName**
Especifica o nome da exibição a ser modificada.
**REMOTE**
Especifica que a exibição é uma exibição remota que usa tabelas remotas. Se você omitir REMOTE, pode modificar uma exibição usando tabelas locais.
**NOWAIT**
Continua a execução do programa após o View Designer ser aberto. O programa não aguarda o fechamento do View Designer, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY VIEW ... NOWAIT. Sem a cláusula NOWAIT, MODIFY VIEW abre o View Designer e a execução do programa é pausada até você fechar o Designer.

# Observações

Exibições SQL são criadas com CREATE SQL VIEW.
