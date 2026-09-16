# Como: Implementar digitação forte for Código de classe, objeto e variável

Para obter controle more sobre seu código, tornar a codificação mais fácil e menos vulnerável a erros e disponibilizar a funcionalidade IntelliSense para objetos visuais, referências de classe, controles ActiveX, servidores COM e elementos de código definidos pelo usuário, use digitação forte. Bibliotecas de tipos OLEPUBLIC também usam tipagem forte.

> **Observação:** Visual FoxPro não é uma linguagem fortemente tipada e não requer que você declare variáveis ​​com tipos de dados específicos. O Visual FoxPro não impõe digitação forte em tempo de design ou de execução.

Para obter mais informações, consulte Suporte ao IntelliSense no Visual FoxPro.

### Para implementar digitação forte
- Para objetos, parâmetros de método e valores, use a cláusula AS no comando DEFINE CLASS.

-OR-
 - For declarações de parâmetros e variáveis, use a cláusula AS nos seguintes comandos: FUNCTION Comando LOCAL Comando LPARAMETERS Comando PARAMETERS Comando PROCEDURE Comando PUBLIC Comando

Quando você usa a cláusula AS no código, o IntelliSense exibe uma lista suspensa de tipos disponíveis, incluindo tipos das seguintes fontes:
 - Classes base de objetos visuais FoxPro.
- Tipos de dados do Visual FoxPro.

O exemplo a seguir usa a cláusula AS no comando DEFINE CLASS para implementar digitação forte para a classe OLEPUBLIC personalizada e o método the MyMethod:

```foxpro
DEFINE CLASS MyClass1 AS Custom OLEPUBLIC
   FUNCTION MyMethod (MyParam1 AS integer, MyParam2 AS string) AS integer
      RETURN MyParam1
   ENDFUNCTION
ENDDEFINE
```

O exemplo a seguir usa a cláusula AS nos comandos LOCAL, PUBLIC, LPARAMETERS, PARAMETERS e FUNCTION para implementar digitação forte:

```foxpro
LOCAL oExcel AS "excel.application"
oExcel = CREATEOBJECT("excel.application")
oExcel.   && Displays a list of members.
PUBLIC ARRAY MyArray[2] AS _form OF ffc\_base
LPARAMETERS MyParam1 AS String OF _Base.vcx
PARAMETERS MyParam1 AS Custom OF MyBase.vcx
FUNCTION MyFunction AS Custom
```
