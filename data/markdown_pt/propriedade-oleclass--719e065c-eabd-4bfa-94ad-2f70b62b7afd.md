# Propriedade OLEClass

Retorna o ID de classe nomeado de um objeto OLE. Somente leitura em tempo de design e em tempo de execução para um objeto existente, mas pode ser definida para um objeto quando ele é criado.

```foxpro
Control.OLEClass[ = cName]
```

# Valor de retorno
 **cName**
O ID de classe nomeado do objeto. Este é o nome registrado do aplicativo que foi usado para criar o objeto ou que será invocado se o objeto for ativado.

# Observações

Aplica-se a: OLE Bound Control | OLE Container Control

Você define a propriedade OLEClass de um objeto contêiner OLE usando a caixa de diálogo Insert Object quando adiciona inicialmente um contêiner OLE a um formulário, ou em código ao criar um objeto OLE como parte de uma definição de classe. Esta propriedade também é definida quando você cria objetos OLE usando o comando APPEND GENERAL.

A propriedade OLEClass de um objeto especifica o aplicativo usado para criar ou editar o objeto OLE. Para especificar o conteúdo real do objeto, defina sua propriedade DocumentFile Property.

# Exemplo

O exemplo a seguir adiciona um controle OLE Container a um formulário e usa as propriedades OLEClass e DocumentFile para especificar o Microsoft Excel como servidor de Automation e uma planilha do Excel como o arquivo a editar.

```foxpro
Define class myForm as form
 add object oleXLSheet1 as oleXLSheet
EndDefine
Define class oleXLSheet as OLECONTROL
 oleclass = "Excel.Sheet"
 documentfile="C:\msoffice\Excel\mysheet.xls"
 oletypeallowed = 1  && Embedded
EndDefine
```
