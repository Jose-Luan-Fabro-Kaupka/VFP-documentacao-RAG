# Função GETPEM( )

Retorna o valor atual de uma propriedade ou o código de programa de um evento ou método em tempo de design.

```foxpro
GETPEM(oObjectName | cClassName, cProperty | cEvent | cMethod)
```

#### Parâmetros
 **oObjectName**
Especifica o objeto para o qual um valor de propriedade ou código de programa de evento ou método é retornado. oObjectName pode ser qualquer expressão que avalie para um objeto, como uma referência de objeto, uma variável de memória de objeto ou um elemento de matriz de objetos.
**cClassName**
Especifica a classe para a qual um valor de propriedade ou código de programa de evento ou método é retornado.
**cProperty**
Especifica a propriedade cujo valor é retornado.
**cEvent**
Especifica o evento para o qual o código de programa é retornado.
**cMethod**
Especifica o método para o qual o código de programa é retornado.

# Valor de retorno

Character, Currency, Date, DateTime, Numeric ou Logical

# Observações

No Visual FoxPro 6.0 e posterior, usar GETPEM( ) para retornar código de método é suportado apenas durante uma sessão interativa do Visual FoxPro. No entanto, você pode obter código de método de um objeto usando sua propriedade Class, como no código a seguir:

```foxpro
LOCAL oObject, lcCode
oObject = NEWOBJECT("_form", HOME()+"ffc\_base.vcx")
lcCode = GETPEM(oObject.class, "Release")
```
