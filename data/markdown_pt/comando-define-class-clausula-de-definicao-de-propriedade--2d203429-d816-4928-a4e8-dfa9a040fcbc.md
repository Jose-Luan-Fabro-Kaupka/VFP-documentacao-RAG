# Comando DEFINE CLASS - Cláusula de definição de propriedade

Define propriedades e seus valores para a definição de classe.

```foxpro
[[PROTECTED | HIDDEN] PropertyName1, PropertyName2 ...]
[[.]Object.]PropertyName = eExpression ...]
```

#### Parâmetros
 **[PROTECTED | HIDDEN] PropertyName1, PropertyName2 ... ]**
Especifica uma ou mais propriedades de classe a criar. Propriedades são atributos nomeados da classe e definem características e comportamentos para a classe. Use vírgulas para separar cada propriedade ou declare cada propriedade em uma linha separada. Observação Todas as definições de propriedade devem aparecer antes das definições de função ou procedimento. A palavra-chave PROTECTED impede acesso e alterações nas propriedades especificadas de fora da definição de classe. Métodos e eventos na definição de classe ou subclasse podem acessar propriedades protegidas. A palavra-chave HIDDEN impede acesso e alterações nas propriedades especificadas de fora da definição de classe. No entanto, somente métodos e eventos na definição de classe, não subclasses, podem acessar propriedades ocultas. Dica Você pode criar subclasses com métodos Access e Assign se não incluir a palavra-chave HIDDEN.
**[[.]Object.] PropertyName = eExpression ... ]**
Atribui valores padrão às propriedades de classe. Usar .Object. indica que o Visual FoxPro deve aplicar o valor a uma propriedade de controle ActiveX ao criá-lo. Para obter mais informações, consulte a seção Exemplos.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando DEFINE CLASS :

```foxpro
DEFINE CLASS Clause
   [Property_Definition_Clause]
   [PEMName_COMATTRIB Clause]
   [ADD OBJECT Clause]
   [IMPLEMENTS Clause]
   [Function_Procedure_Definition_Clause]
ENDDEFINE
```

Para obter mais informações e a sintaxe completa, consulte o comando DEFINE CLASS . Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS , consulte os seguintes tópicos:
 - Cláusula DEFINE CLASS
- Cláusula PEMName_COMATTRIB
- Cláusula ADD OBJECT
- Cláusula IMPLEMENTS
- Cláusula de definição de função ou procedimento

# Exemplo

O exemplo a seguir cria o formulário frmOLETest a partir de uma classe base Form e usa o método AddObject para adicionar um objeto chamado OCXTest baseado na classe BlueOLEControl criada por DEFINE CLASS e especifica a classe OLE para o controle ActiveX Listview. A palavra-chave .Object é usada para especificar um valor para a propriedade BackColor do controle antes de ele ser criado.

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

Para obter mais informações, consulte o método AddObject .
