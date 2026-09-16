# Comando SET NOTIFY

Habilita ou desabilita a exibição de determinadas mensagens do sistema. Os seguintes são exemplos de mensagens do sistema afetadas por SET NOTIFY:
 - "Expression is valid" na caixa de diálogo Expression Builder
- "Do Canceled", que aparece quando a execução do programa é cancelada

```foxpro
SET NOTIFY [CURSOR] ON | OFF
```

#### Parâmetros
 **CURSOR**
Especifica se mensagens relacionadas a dados devem aparecer na barra de status.
**ON**
Habilita a exibição de determinadas mensagens do sistema. (Padrão)
**OFF**
Desabilita a exibição de determinadas mensagens do sistema.

# Observações

As mensagens do sistema são exibidas na barra de status gráfica, e não na barra de status baseada em caracteres, na parte inferior da janela principal do Visual FoxPro.

Quando SET NOTIFY CURSOR está definido como OFF, o Visual FoxPro suprime todas as mensagens relacionadas a dados de serem exibidas na barra de status. Essas mensagens incluem alias, fonte de dados, ponteiro de registro, contagem de registros e status de exclusivo/registro desbloqueado.

A configuração de SET NOTIFY CURSOR não afeta SET NOTIFY.

Você pode usar SET("NOTIFY",1) para retornar o valor atual de SET NOTIFY CURSOR.

SET NOTIFY desabilita a exibição de mensagens que aparecem mesmo se SET TALK estiver OFF.
