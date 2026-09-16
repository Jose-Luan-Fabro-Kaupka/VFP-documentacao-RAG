# Comando DEFINE CLASS

Cria uma classe ou subclasse definida pelo usuário e especifica as propriedades, eventos e métodos da classe ou subclasse.

> **Cuidado:** Modificar propriedades somente leitura de classes base gera uma mensagem de erro.

A sintaxe completa das cláusulas principais de DEFINE CLASS aparece da seguinte forma:

```foxpro
DEFINE CLASS ClassName1 AS ParentClass [OF ClassLibrary] [OLEPUBLIC]
   [[PROTECTED | HIDDEN] PropertyName1, PropertyName2 ...]
   [[.]Object.]PropertyName = eExpression ...]
   [PEMName_COMATTRIB = nFlags | DIMENSION PEMName_COMATTRIB[numElements]
      [PEMName_COMATTRIB[1] = nFlags
              PEMName_COMATTRIB[2] = cHelpString
              PEMName_COMATTRIB[3] = cPropertyCapitalization
              PEMName_COMATTRIB[4] = cPropertyType
              PEMName_COMATTRIB[5] = nOptionalParams]]
   [ADD OBJECT [PROTECTED] ObjectName AS ClassName2 [NOINIT] [WITH cPropertylist]]
   [IMPLEMENTS cInterfaceName [EXCLUDE] IN TypeLib | TypeLibGUID | ProgID ]
   [[PROTECTED | HIDDEN] FUNCTION | PROCEDURE Name[_ACCESS |_ASSIGN]
      ([cParamName | cArrayName[] [AS Type][@]]) [AS Type]
      [HELPSTRING cHelpString] | THIS_ACCESS(cMemberName) [NODEFAULT]
            cStatements
   [ENDFUNC | ENDPROC]
ENDDEFINE
```

# Observações

O código a seguir mostra um resumo das cláusulas principais:

```foxpro
DEFINE CLASS Clause
   [Property_Definition_Clause]
   [PEMName_COMATTRIB Clause]
   [ADD OBJECT Clause]
   [IMPLEMENTS Clause]
   [Function_Procedure_Definition_Clause]
ENDDEFINE
```

As seções a seguir descrevem a sintaxe detalhada e os parâmetros de cada cláusula do comando DEFINE CLASS:
 - DEFINE CLASS Command - DEFINE CLASS Clause
- DEFINE CLASS Command - Property Definition Clause
- DEFINE CLASS Command - PEMName_COMATTRIB Clause
- DEFINE CLASS Command - ADD OBJECT Clause
- DEFINE CLASS Command - IMPLEMENTS Clause
- DEFINE CLASS Command - Function or Procedure Definition Clause

O código de classes definidas pelo usuário é armazenado em um arquivo de programa (.prg), semelhante a procedimentos.

> **Observação:** You cannot follow procedures in a .prg file with normal executable program code. Only class definitions, other procedures, and user-defined functions can follow the first DEFINE CLASS , PROCEDURE or FUNCTION statement in the file. Para obter mais informações, see User-Defined Procedures and Functions .

Você não pode colocar definições de classe criadas com DEFINE CLASS dentro de comandos de programação estruturada, por exemplo, IF ... ENDIF ou DO CASE ... ENDCASE, ou em loops, como DO WHILE ... ENDDO ou FOR ... ENDFOR.

Para instanciar, ou criar instâncias de, a classe que você definiu, use a função CREATEOBJECT( ). Você pode acessar propriedades públicas e chamar funções e procedimentos de método e evento fora da definição da classe conforme mostrado no exemplo a seguir:

```foxpro
myObject = CREATEOBJECT('MyClass')
myObject.myPropertyName =
myObject.myMethodName( argument1, argument2, ... )
myObject.myEventName
```

Protected or hidden properties, methods, and events have restricted access as defined by the PROTECTED and HIDDEN keywords. Para obter mais informações, see DEFINE CLASS Command - Property Definition Clause and DEFINE CLASS Command - Function or Procedure Definition Clause.

O Visual FoxPro converte valores de cláusula AS Type automaticamente quando outros servidores COM os usam. Quando você digita a cláusula AS no código, a funcionalidade IntelliSense no Visual FoxPro exibe as informações de tipo para servidores COM.

A tabela a seguir mostra as informações de tipo de dados que são exibidas.

| Tipo definido VFP | Conversão COM Typelib | IntelliSense exibe |
| --- | --- | --- |
| Array | SAFEARRAY(type) | Array |
| BinaryMemo | VARIANT | — |
| Boolean | VARIANT_BOOL | Logical |
| Byte | unsigned char | Number |
| Character * | BSTR | String |
| Currency * | CURRENCY | Currency |
| Date | DATE | Date |
| DateTime | DATE | Date |
| Decimal * | wchar_t | Number |
| Double | double | Number |
| Float | VARIANT | — |
| Integer | long | Number |
| Logical | VARIANT_BOOL | Logical |
| Long | long | Number |
| Memo | VARIANT | — |
| Number | double | Number |
| Object | IDispatch* | Object |
| Short | long | Number |
| Single * | single | Number |
| String | BSTR | String |
| Variant | VARIANT | — |
| Void | void | VOID |

You can view code for Access and Assign methods in the Trace window of the Debugger window. However, you cannot execute Access and Assign methods from the Watch and Local windows of the Debugger window. Para obter mais informações, see Access and Assign Methods, Trace Window, and Debugger Window.

Um safe array é uma matriz unidimensional ou multidimensional de um único tipo de dados, que pode ser do tipo VARIANT, permitindo criar matrizes de tipos mistos. O safe array armazena seu limite inferior, que não precisa ser zero, e seu tamanho. Safe arrays permitem bloqueio e desbloqueio para que você possa ter certeza de que o ponteiro recebido para os dados é válido.

# Exemplos

### Exemplo 1

O exemplo a seguir cria uma classe chamada MyForm da classe base Form e cria uma propriedade protected chamada Version. A classe também contém outra propriedade chamada Caption, que não é protected. A definição da classe inicializa os valores padrão de Version e Caption para as cadeias de caracteres "1.0" e "My Form", respectivamente.

```foxpro
DEFINE CLASS MyForm AS Form
   PROTECTED Version
   Version = "1.0"
   Caption = "My Form"
ENDDEFINE
```

### Exemplo 2

O exemplo a seguir cria o formulário frmOLETest de uma classe base Form e usa o método AddObject para adicionar um objeto chamado OCXTest baseado na classe BlueOLEControl criada por DEFINE CLASS e especifica a classe OLE para o controle ActiveX Listview. A palavra-chave .Object é usada para especificar um valor para a propriedade BackColor do controle antes de ser criado.

```foxpro
PUBLIC frmOLETest
frmOLETest = CREATEOBJECT('Form')
frmOLETest.Visible = .T.
frmOLETest.AddObject('OCXTest', 'BlueOLEControl', 'MSComctlLib.ListViewCtrl')
frmOLETest.OCXTest.View = 2
frmOLETest.OCXTest.ListItems.Add(1,'one','Item One')
frmOLETest.OCXTest.ListItems.Add(2,'two','Item Two')
DEFINE CLASS BlueOLEControl AS OLEControl
   * Set property for Outline ActiveX control.
   .Object.Backcolor = 16776960

   * Set properties for the OLE Container control.
   Visible = .T.
   Height = 100
   Width = 200
ENDDEFINE
```

Para obter mais informações, see AddObject Method.

### Exemplo 3

O exemplo a seguir demonstra como definir uma matriz de atributos de biblioteca de tipos usando a cláusula DIMENSION PEMName_COMATTRIB:

```foxpro
#INCLUDE foxpro.h
DEFINE CLASS myOLEClass AS Custom OLEPUBLIC
   MyProperty = 5.2
   * Set COM attributes for MyProperty.
   DIMENSION MyProperty_COMATTRIB[4]
   myProperty_COMATTRIB[1] = COMATTRIB_READONLY
   myProperty_COMATTRIB[2] = "Help text displayed in object browser"
   myProperty_COMATTRIB[3] = "MyProperty"  && Proper capitalization.
   myProperty_COMATTRIB[4] = "Float"        && Data type
ENDDEFINE
```

No entanto, se você deseja definir apenas o elemento nFlags, não precisa criar uma matriz:

```foxpro
#INCLUDE foxpro.h
DEFINE CLASS myOLEClass AS Custom OLEPUBLIC
   MyProperty = "Test"
   * Set the only the nFlags attribute for MyProperty.
   myProperty_COMATTRIB = COMATTRIB_READONLY
ENDDEFINE
```

# Exemplo 4

O exemplo a seguir cria uma classe chamada MyForm da classe base Form e adiciona um command button da classe base CommandButton e uma check box da classe base CheckBox:

```foxpro
DEFINE CLASS MyForm AS Form
   ADD OBJECT cmdButton1 AS CommandButton
   ADD OBJECT chkBox1 AS CheckBox
ENDDEFINE
```

Como outro exemplo, o código a seguir cria uma classe chamada MyForm, adiciona um command button e uma check box à classe e especifica valores para as propriedades Caption do command button e da check box.

```foxpro
DEFINE CLASS MyForm AS Form
   ADD OBJECT cmdButton1 AS CommandButton WITH Caption = "Yes"
   ADD OBJECT chkBox1 AS CheckBox WITH Caption = "Click Me"
ENDDEFINE
```

### Exemplo 5

O exemplo a seguir cria uma classe chamada MyPublisherClass como uma classe Custom, usa a palavra-chave OLEPUBLIC para especificar que clientes Automation podem acessar a classe quando incluída em um servidor Automation, usa a cláusula IMPLEMENTS para herdar a definição de classe da definição de classe Publisher na biblioteca de tipos MyBookStore.dll e inclui o método ShowPrice da interface Publisher.

```foxpro
DEFINE CLASS MyPublisherClass AS Custom OLEPUBLIC
   IMPLEMENTS Publisher IN "MyBookStore.dll"
   PROCEDURE Publisher_ShowPrice(cGetID AS Long) AS Short
   ENDPROC
ENDDEFINE
```

### Exemplo 6

O exemplo a seguir cria uma classe chamada MyForm da classe base Form e contém um procedimento para uma definição de evento Click. O formulário criado da classe contém um método Click que exibe uma caixa de diálogo quando você clica no formulário.

```foxpro
DEFINE CLASS MyForm AS Form
   PROCEDURE Click
      = MESSAGEBOX('MyForm has been clicked!')
   ENDPROC
ENDDEFINE
```

Como outro exemplo, o código a seguir contém um procedimento para um dos objetos adicionados à classe. Este procedimento de evento substitui o evento Click padrão do command button:

```foxpro
DEFINE CLASS MyForm AS Form
   ADD OBJECT MyButton AS CommandButton
   ADD OBJECT chkBox1 AS CheckBox
   PROCEDURE MyButton.Click
      = MESSAGEBOX('This is my click event procedure')
   ENDPROC
ENDDEFINE
```

### Exemplo 7

O exemplo a seguir mostra como você pode especificar tipagem forte usando a cláusula PROCEDURE cArrayName[] [AS Type][@][AS Type] para que matrizes possam ser corretamente escritas como safe arrays em uma biblioteca de tipos:

```foxpro
DEFINE CLASS mySession AS Session OLEPUBLIC
    PROCEDURE GetWidgets1(aWidgets[])
    ENDPROC
    PROCEDURE GetWidgets2(aWidgets[] AS Integer)
    ENDPROC
    PROCEDURE GetWidgets3(aWidgets[] AS Integer @)
    ENDPROC
    PROCEDURE GetRS(oRS[] AS ADODB.Recordset @)
    ENDPROC
ENDDEFINE
```

Como outro exemplo, o código a seguir demonstra como você pode especificar tipagem complexa forte definindo um tipo baseado em uma classe COM:

```foxpro
DEFINE CLASS mySession AS Session OLEPUBLIC
   PROCEDURE GetRS() AS ADODB.Recordset
      x=CREATEOBJECT("ADODB.Recordset")
      RETURN X
   ENDPROC
   PROCEDURE SetRS(oRS AS ADODB.Recordset @)
      oRS=CREATEOBJECT("ADODB.Recordset")
   ENDPROC
ENDDEFINE
```
