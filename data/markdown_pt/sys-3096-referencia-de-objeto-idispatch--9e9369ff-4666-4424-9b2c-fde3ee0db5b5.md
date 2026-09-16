# SYS(3096) - Referência de objeto IDispatch

Retorna uma referência de objeto COM do Visual FoxPro para um ponteiro IDispatch.

```foxpro
SYS(3096, nPointer)
```

#### Parâmetros
 **nPointer**
Representa um ponteiro para um objeto COM como _VFP ou Excel.Application.

# Valor de retorno

Referência de objeto. SYS(3096) retorna uma referência de objeto COM do Visual FoxPro.

# Observações

Este ponteiro é fornecido para que desenvolvedores experientes que precisam determinar uma referência de objeto para uso em rotinas de API. O refcount para o objeto COM NÃO é alterado.
