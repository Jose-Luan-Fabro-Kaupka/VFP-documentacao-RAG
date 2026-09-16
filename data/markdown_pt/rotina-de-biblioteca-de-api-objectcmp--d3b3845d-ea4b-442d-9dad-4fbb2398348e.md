# Rotina de biblioteca de API _ObjectCmp( )

Compara as propriedades de dois objetos e retorna 0 se suas propriedades e valores de propriedade são idênticos.

```foxpro
int _ObjectCmp(Value FAR *objct1, Value FAR *objct2)
```

# Observações

0 é retornado se os objetos têm propriedades e valores de propriedade idênticos. -1 é retornado se um objeto tem uma propriedade que o outro objeto não tem, ou se os objetos têm propriedades idênticas, mas os valores de uma ou mais propriedades diferem.

Se ocorrer um erro (por exemplo, se você omitir um dos objetos), o valor negativo do código de erro correspondente do Visual FoxPro é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.
