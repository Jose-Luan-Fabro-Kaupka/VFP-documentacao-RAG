# Função CREATEOBJECT( )

Cria um objeto a partir de uma definição de classe ou de um aplicativo habilitado para Automation.

```foxpro
CREATEOBJECT(cClassName [, eParameter1, eParameter2, ...])
```

#### Parâmetros
 **ClassName**
Especifica a classe ou objeto OLE a partir do qual o novo objeto é criado. O Visual FoxPro busca a classe ou objeto OLE na seguinte ordem: Visual FoxPro base classes Classes in the current program Classes in .vcx class libraries opened with SET CLASSLIB Classes in procedure files opened with SET PROCEDURE Classes in the Visual FoxPro program execution chain The OLE registry if SET OLEOBJECT is ON OLE objects are created using the following syntax for ClassName : ApplicationName.Class For example, to create a Microsoft Excel worksheet (which supports Automation), you can use the following syntax: x = CREATEOBJECT('Excel.Sheet') When this code is run, Microsoft Excel is started (if not already running), and a new worksheet is created. A class library can have an alias. To specify an object in a class library with an alias, include the class library alias followed by a period and the object name. Note that ClassName cannot be the Visual FoxPro OLE Container control base class.
**eParameter1 , eParameter2, ...**
Esses parâmetros opcionais são usados para passar valores ao procedimento do evento Init da classe. O evento Init é executado quando você emite CREATEOBJECT( ) e permite inicializar o objeto.

# Valor de retorno

Object

# Observações

Use CREATEOBJECT( ) para criar um objeto a partir de uma definição de classe ou de um aplicativo que suporta Automation, e atribua uma referência ao objeto a uma variável de sistema ou elemento de matriz.

Antes de poder criar um objeto a partir de uma classe definida pelo usuário, a classe definida pelo usuário deve primeiro ser criada com DEFINE CLASS, ou deve estar disponível em uma biblioteca de classes visuais .vcx aberta com SET CLASSLIB.

Use = ou STORE para atribuir uma referência ao objeto a uma variável de sistema ou elemento de matriz. Se um objeto atribuído a uma variável de sistema ou elemento de matriz for liberado, a variável de sistema ou elemento de matriz contém o valor nulo. Use RELEASE para remover a variável de sistema ou elemento de matriz da memória.

# Exemplo

O exemplo a seguir usa DEFINE CLASS e CREATEOBJECT( ) para criar duas classes personalizadas chamadas FormChild e FormGrandChild a partir da classe base Form do Visual FoxPro. ACLASS( ) é usada para criar uma matriz chamada `gaNewarray` contendo os nomes das classes, que são então exibidos.

```foxpro
CLEAR
* Verify current class library setting
cCurClassLib=SET("CLASSLIB")
IF LEN(ALLTRIM(cCurClassLib))=0
   cCurClassLib="None"
ENDIF
WAIT WINDOW "Current class library is: " + cCurClassLib + CHR(13);
   + "Press any key to continue..."
frmMyForm = CREATEOBJECT("FormGrandChild")
* Create an array
FOR nCount = 1 TO ACLASS(gaNewarray, frmMyForm)
   ? gaNewarray(nCount)  && Display the names of the classes
ENDFOR
RELEASE frmMyForm
* Create FormChild from FORM baseclass
DEFINE CLASS FormChild AS FORM
ENDDEFINE
* Create FormGrandChild from user-defined FormChild class
DEFINE CLASS FormGrandChild AS FormChild
ENDDEFINE
```
