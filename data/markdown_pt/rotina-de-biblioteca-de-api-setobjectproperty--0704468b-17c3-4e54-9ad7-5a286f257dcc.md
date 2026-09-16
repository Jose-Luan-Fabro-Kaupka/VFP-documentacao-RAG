# Rotina de biblioteca de API _SetObjectProperty( )

Define uma propriedade de um objeto.

```foxpro
int _SetObjectProperty(Value FAR *objct, char FAR *prop, Value FAR *val,
   int fAdd)
```

# Observações

O primeiro parâmetro *objct é uma referência de objeto; o segundo parâmetro *prop é o nome da propriedade a definir; o terceiro parâmetro *val é o novo valor da propriedade.

O último parâmetro fAdd é 0 ou um valor diferente de zero que especifica se a propriedade será adicionada ao objeto caso não exista. Se fAdd for um valor diferente de zero e a propriedade especificada não existir para o objeto, ela será adicionada ao objeto como uma propriedade definida pelo usuário e conterá o valor especificado com *val. Se fAdd for 0 e a propriedade especificada não existir para o objeto, ela não será adicionada ao objeto.

_SetObjectProperty( ) retorna 0 se for bem-sucedida; caso contrário, retorna o valor negativo do código de erro correspondente do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.
