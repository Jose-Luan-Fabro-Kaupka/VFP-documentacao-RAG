# Rotina de biblioteca de API _ObjectRelease( )

Decrementa a contagem de referências de um objeto.

```foxpro
int _ObjectRelease(Value FAR *objct)
```

# Observações

0 é retornado, a menos que ocorra um erro. Quando ocorre um erro, um número negativo representando um código de erro interno é retornado.
