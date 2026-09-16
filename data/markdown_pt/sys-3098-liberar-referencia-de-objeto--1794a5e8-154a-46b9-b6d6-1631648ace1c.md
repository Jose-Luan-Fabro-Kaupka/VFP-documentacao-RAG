# SYS(3098) - Liberar referência de objeto

Executa uma chamada IDispatch Release em um objeto COM.

```foxpro
SYS(3098, oObject)
```

#### Parâmetros
 **oObject**
Referência de objeto para objeto COM. Observação Esta função é fornecida para desenvolvedores experientes. Contagens de referência de objetos COM inválidas podem causar problemas como objetos não liberados corretamente ou chamadas a objetos que não existem mais.

# Retorna

Numeric. Retorna o Refcount atual após liberar uma referência de objeto.
