# Rotina de biblioteca de API _ObjectReference( )

Incrementa a contagem de referências de um objeto.

```foxpro
int _ObjectReference(Value FAR *objct)
```

# Observações

CLEAR MEMORY ou CLEAR ALL libera um objeto de API da memória.

0 é retornado, a menos que ocorra um erro. Quando ocorre um erro, um número negativo representando um código de erro interno é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.
