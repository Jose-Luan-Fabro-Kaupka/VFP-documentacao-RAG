# SYS(102) - Configuração de impressora

Incluído para compatibilidade com versões anteriores. Use SET("PRINTER") em vez disso.

```foxpro
SYS(102)
```

# Valores de retorno

Character

# Exemplo

```foxpro
IF SYS(102) != 'OFF'
   SET PRINTER OFF
ENDIF
```
