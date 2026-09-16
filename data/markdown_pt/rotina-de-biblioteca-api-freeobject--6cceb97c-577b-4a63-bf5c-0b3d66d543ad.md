# Rotina de biblioteca API _FreeObject( )

Libera um objeto do pool de dados da API do Visual FoxPro.

```foxpro
void _FreeObject(Value FAR *objct)
```

# Observações

Use _FreeObject( ) para liberar um objeto da tabela de objetos da API do Visual FoxPro.

### _FreeObject( ) é usado nos seguintes casos:

1. Se uma referência de objeto é retornada de qualquer função da API do Visual FoxPro (por exemplo, _Evaluate( ) ou _GetObjectProperty( )), você deve usar _FreeObject( ) para liberar o objeto quando não estiver mais usando-o.

2. Se você mantém uma referência a um objeto entre diferentes chamadas da API do Visual FoxPro, deve primeiro usar _ObjectReference( ) para incrementar a contagem do objeto. Quando não estiver mais usando o objeto, deve então usar _ObjectRelease( ) para decrementar a contagem do objeto e depois usar _FreeObject( ) para liberar o objeto.

Além das regras anteriores, você deve sempre limpar a estrutura Value que passa para qualquer função da API do Visual FoxPro que retorna um valor na estrutura Value passada. Por exemplo, você pode criar e chamar uma função que limpa a estrutura antes de chamar qualquer função que retorna um valor em sua estrutura. Você também pode criar e chamar uma função para limpar quaisquer referências de objeto ou handles não utilizados.

0 é retornado, a menos que ocorra um erro. Quando ocorre um erro, um número negativo representando um código de erro interno é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.
