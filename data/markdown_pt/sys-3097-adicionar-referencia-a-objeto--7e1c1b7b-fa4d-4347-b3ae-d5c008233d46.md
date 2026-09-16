# SYS(3097) - Adicionar referência a objeto

Executa uma chamada IDispatch AddRef em um objeto COM.

```foxpro
SYS(3097, oObject)
```

#### Parâmetros
 **oObject**
Referência de objeto ao objeto COM. Observação Esta função é fornecida para desenvolvedores experientes. Contagens de referência inválidas de objetos COM podem causar problemas, como objetos que não são liberados corretamente ou chamadas a objetos que não existem mais.

# Valor de retorno

Numérico. Retorna o Refcount atual após adicionar uma nova referência de objeto.
