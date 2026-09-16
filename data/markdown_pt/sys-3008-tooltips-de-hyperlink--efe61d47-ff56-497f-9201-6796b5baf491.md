# SYS(3008) - Tooltips de hyperlink

Habilita ou desabilita tooltips de hyperlink.

```foxpro
SYS(3008 [, 0 | 1]
```

#### Parâmetros

| Parâmetro | Descrição |
| --- | --- |
| 0 | Desabilita tooltips de hyperlink. |
| 1 | (Padrão) Habilita tooltips de hyperlink. |

# Observações

Emita SYS(3008) sem parâmetro para retornar sua configuração atual. SYS(3008) afeta todos os tooltips de hyperlink no Visual FoxPro, incluindo editores abertos com MODIFY COMMAND Command, MODIFY FILE Command e MODIFY MEMO Command e o EditBox Control.

SYS(3008) não afeta a biblioteca de classes foundation _Hyperlink incluída com o Visual FoxPro.
