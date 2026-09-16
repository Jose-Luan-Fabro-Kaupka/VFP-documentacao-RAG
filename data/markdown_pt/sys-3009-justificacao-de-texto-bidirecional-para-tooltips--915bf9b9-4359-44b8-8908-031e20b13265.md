# SYS(3009) - Justificação de texto bidirecional para ToolTips

Habilita ou desabilita a justificação de texto bidirecional para ToolTips.

```foxpro
SYS(3009 [, 0 | 1])
```

#### Parâmetros
 **0**
(Padrão) Desabilita a justificação de texto bidirecional para ToolTips. O texto em ToolTips é justificado da esquerda para a direita.
**1**
Habilita a justificação de texto bidirecional para ToolTips. O texto em ToolTips é justificado da direita para a esquerda.

# Valor de retorno

Character. Se as opções 0 ou 1 forem omitidas, SYS(3009) retorna a configuração atual de justificação de texto bidirecional.

# Observações

SYS(3009) afeta a justificação de texto dos ToolTips para todos os controles e campos memo em uma sessão interativa ou de tempo de execução do Visual FoxPro.
