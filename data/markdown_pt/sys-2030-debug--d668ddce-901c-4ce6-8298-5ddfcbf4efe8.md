# SYS(2030) - Debug

Habilita ou desabilita recursos de depuração no código de usuário de componentes do sistema.

```foxpro
SYS(2030[, 0 | 1])
```

#### Parâmetros
 **0**
Desabilita os recursos de depuração.
**1**
Habilita recursos de depuração para que você possa depurar código de componentes do sistema.

# Retorna

Numérico. Valor da configuração atual.

# Observações

A partir do Visual FoxPro 7, sempre que o código de usuário executa diretamente um componente do sistema, como _GENMENU ou _BROWSER, certos recursos de depuração (profiling, dohistory, breakpoints e single step) são desabilitados. SYS(2030, 1) permite executar o depurador neste tipo de código de usuário desabilitando o comportamento padrão e, depois, reabilitando o comportamento após a depuração emitindo SYS(2030, 0).
