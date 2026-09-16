# SYS(2333) - Suporte a interface dupla ActiveX

Habilita ou desabilita o suporte a interface dupla ActiveX (VTABLE binding).

```foxpro
SYS(2333 [, 0 | 1 | 2])
```

#### Parâmetros
 **0**
Desabilita o suporte a interface dupla ActiveX. Se 0 ou 1 for omitido, o suporte a interface dupla ActiveX é desabilitado. 0 é o padrão de inicialização para o Visual FoxPro 6.0 ou posterior.
**1**
Habilita o suporte a interface dupla ActiveX. 1 é o padrão de inicialização para o Visual FoxPro 5.0.
**2**
Retorna a configuração atual de SYS(2333) (0 ou 1).

# Valor de retorno

Character

# Observações

A interface dupla (VTABLE binding) do controle ActiveX é uma otimização suportada pelo Visual FoxPro. Se um controle ActiveX não usar a interface dupla, você pode desabilitar a otimização ao usar esse controle.

Se um controle ActiveX não funcionar corretamente quando o controle é instanciado, execute SYS(2333) ou SYS(2333, 0) antes que o controle seja instanciado para desabilitar o suporte a interface dupla para o controle. Depois que o controle tiver sido instanciado, execute SYS(2333, 1) para habilitar o suporte a interface dupla ActiveX para quaisquer controles instanciados posteriormente.
