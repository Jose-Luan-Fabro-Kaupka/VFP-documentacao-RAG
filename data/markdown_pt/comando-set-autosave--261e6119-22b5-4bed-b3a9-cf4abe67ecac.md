# Comando SET AUTOSAVE

Determina se o Visual FoxPro descarrega os buffers de dados no disco ao sair de um READ ou retornar à janela Command.

```foxpro
SET AUTOSAVE ON | OFF
```

#### Parâmetros
 **ON**
Especifica que os buffers sejam descarregados no disco sempre que você sair de um READ ou retornar à janela Command.
**OFF**
Especifica que os buffers sejam descarregados somente se tiverem transcorrido cinco minutos desde a última descarga, e apenas ao sair de um READ ou retornar à janela Command. OFF é o padrão de SET AUTOSAVE.

# Observações

Descarregar os buffers pode reduzir a possibilidade de perda de dados se o computador ficar sem energia.

SET AUTOSAVE está limitado à sessão de dados atual.
