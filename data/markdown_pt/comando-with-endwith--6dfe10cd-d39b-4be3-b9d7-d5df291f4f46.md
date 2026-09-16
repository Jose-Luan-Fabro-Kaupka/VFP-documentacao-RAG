# Comando WITH ... ENDWITH

Especifica várias propriedades para um objeto.

```foxpro
WITH ObjectName [AS <Type> [OF <Class Library>]]
   [.cStatements]
ENDWITH
```

#### Parâmetros
 **ObjectName**
Especifica o nome do objeto. ObjectName pode ser o nome do objeto ou uma referência ao objeto.
**Type**
Uma classe base, nome de classe ou biblioteca de tipos. (Somente para Intellisense)
**Class Library**
Biblioteca de classes contendo a classe base, nome de classe ou biblioteca de tipos especificada com Type . (Somente para Intellisense.)
**.cStatements**
cStatements pode consistir em qualquer número de comandos Microsoft Visual FoxPro usados para especificar propriedades para ObjectName . Coloque um ponto antes de cStatement para indicar que é uma propriedade de ObjectName .

# Observações

WITH ... ENDWITH fornece uma maneira conveniente de especificar várias propriedades para um único objeto. Observe que você também pode executar métodos de dentro de uma estrutura WITH ... ENDWITH.

# Exemplo

O exemplo a seguir cria uma classe personalizada chamada Employee. Depois que a classe Employee foi criada com CREATEOBJECT( ), WITH ... ENDWITH é usado para definir várias propriedades para a classe. Os valores das propriedades são então exibidos.

```foxpro
moemployee = CREATEOBJECT('employee')
WITH moemployee
   .First_Name = 'John'
   .Last_Name = 'Smith'
   .Address = '16 Maple Lane'
   .HireDate = {^1998-02-16}
ENDWITH
CLEAR
? moemployee.First_Name + ' '
?? moemployee.Last_Name
? moemployee.Address
? moemployee.HireDate
DEFINE CLASS employee AS CUSTOM
      First_Name = SPACE(20)
      Last_Name = SPACE(20)
      Address = SPACE(30)
      HireDate = {  -  -  }
ENDDEFINE
```
