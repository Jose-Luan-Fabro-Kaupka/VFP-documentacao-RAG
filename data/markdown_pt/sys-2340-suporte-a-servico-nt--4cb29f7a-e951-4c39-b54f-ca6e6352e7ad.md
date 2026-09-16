# SYS(2340) - Suporte a serviço NT

Desabilita ou habilita o suporte a serviço NT.

```foxpro
SYS(2340 [,0 | 1 ])
```

#### Parâmetros
 **0**
Desabilita o suporte a serviço NT (padrão).
**1**
Habilita o suporte a serviço NT.

# Valor de retorno

Caractere

# Observações

Esta função intercepta mensagens de logoff do Windows (WM_QUERYENDSESSION e WM_ENDSESSION) para o Visual FoxPro e especifica se deve manter instâncias do COM Server do Visual FoxPro em execução ou encerrá-las. Um aplicativo Visual FoxPro será encerrado quando o usuário atual fizer logoff do Windows. Se o aplicativo é um Windows Service, esse serviço será encerrado. Habilitar o suporte a serviço NT permitirá que aplicativos Visual FoxPro continuem mesmo se o usuário atual fizer logoff do Windows.
