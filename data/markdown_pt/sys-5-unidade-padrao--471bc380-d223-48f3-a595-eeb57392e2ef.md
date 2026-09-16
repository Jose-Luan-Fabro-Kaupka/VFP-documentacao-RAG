# SYS(5) - Unidade Padrão

Retorna a unidade padrão atual do Visual FoxPro.

```foxpro
SYS(5)
```

# Valor de retorno

Character

# Observações

Esta função retorna a unidade padrão atual do Visual FoxPro. Use SET DEFAULT ou CD para especificar uma unidade padrão.

# Exemplo

```foxpro
CD "C:\\Program Files"
?SYS(5)
SET DEFAULT TO C:
?SYS(5)
```
