# Rotina de biblioteca API _GetObjectProperty( )

Retorna um valor de propriedade para um objeto.

```foxpro
int _GetObjectProperty(Value FAR *retval, Value FAR *objct,
   char FAR *prop)
```

# Observações

O objeto para o qual retornar uma propriedade é especificado com *objct, e a propriedade a retornar é especificada com *prop.

O valor retornado é colocado na estrutura de valor *retval.

> **Observação:** Você deve sempre preencher a estrutura *retval com 0 antes de chamar _GetObjectProperty().

_GetObjectProperty( ) retorna 0 se for bem-sucedido; caso contrário, o valor negativo do código de erro correspondente do Visual FoxPro é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.
