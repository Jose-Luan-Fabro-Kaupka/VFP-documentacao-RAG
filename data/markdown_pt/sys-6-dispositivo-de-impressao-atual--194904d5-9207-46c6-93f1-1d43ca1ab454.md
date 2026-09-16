# SYS(6) — Dispositivo de impressão atual

Retorna o dispositivo de impressão atual.

```foxpro
SYS(6)
```

# Valor de retorno

Character

# Observações

Esta função retorna a configuração atual de SET PRINTER TO.

# Exemplo

```foxpro
? SYS(6)
SET PRINTER TO output.txt
? SYS(6)
```
