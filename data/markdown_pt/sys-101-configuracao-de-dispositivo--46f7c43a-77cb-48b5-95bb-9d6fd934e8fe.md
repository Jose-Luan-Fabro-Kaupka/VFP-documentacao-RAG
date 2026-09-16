# SYS(101) - Configuração de dispositivo

Incluído para compatibilidade retroativa. Use SET("DEVICE") em vez disso.

```foxpro
SYS(101)
```

# Valores de retorno

Caractere

# Exemplo

```foxpro
IF SYS(101) != 'SCREEN'
   SET DEVICE TO SCREEN
ENDIF
```
