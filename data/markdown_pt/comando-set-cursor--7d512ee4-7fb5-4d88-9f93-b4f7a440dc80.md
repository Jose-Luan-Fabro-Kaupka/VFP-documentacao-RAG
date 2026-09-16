# Comando SET CURSOR

Determina se o ponto de inserção é exibido quando o Visual FoxPro aguarda entrada.

```foxpro
SET CURSOR ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Faz com que o ponto de inserção seja exibido durante um @ ... GET, @ ... EDIT, WAIT ou INKEY( ) pendente.
**OFF**
Impede que o ponto de inserção seja exibido durante um @ ... GET, @ ... EDIT, WAIT ou INKEY( ) pendente.

# Observações

SET CURSOR, semelhante a SYS(2002), permite ligar ou desligar o ponto de inserção.
