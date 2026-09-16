# Este elemento de matriz foi definido como um objeto e não pode ser redefinido na definição da classe (Erro 1780)

Depois que você definiu um elemento de matriz como membro de objeto em uma definição de classe, ele não pode ser redefinido.

Por exemplo, o código a seguir causaria este erro:

```foxpro
DEFINE CLASS test AS form
   DIME a[1]
   ADD OBJECT a[1] AS commandbutton
   a[1] = 10
ENDDEFINE
```
