# SYS(2339) - Chamar CoFreeUnusedLibraries quando o objeto COM é liberado

Define ou retorna se o Visual FoxPro chama a função do sistema operacional CoFreeUnusedLibraries quando um objeto COM é liberado.

```foxpro
SYS(2339 [, 0 | 1 ])
```

#### Parâmetros
 **0**
Especifica que CoFreeUnusedLibraries não é chamada (padrão).
**1**
Especifica que CoFreeUnusedLibraries é chamada.

# Valor de retorno

Character

# Observações

Se você tiver problemas para liberar um servidor COM mesmo que todas as referências sejam liberadas, talvez precise alterar esta configuração. Você também pode usar o comando DECLARE - DLL para chamar CoFreeUnusedLIbraries diretamente.
