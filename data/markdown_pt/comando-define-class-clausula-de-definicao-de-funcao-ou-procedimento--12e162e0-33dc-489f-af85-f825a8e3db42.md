# Comando DEFINE CLASS - Cláusula de definição de função ou procedimento

Define funções e procedimentos de métodos e eventos para a definição de classe.

```foxpro
[[PROTECTED | HIDDEN] FUNCTION | PROCEDURE Name[_ACCESS |_ASSIGN]
   ([cParamName | cArrayName[] [AS Type][@]]) [AS Type]
   [HELPSTRING cHelpString] | THIS_ACCESS(cMemberName) [NODEFAULT]
      cStatements
[ENDFUNC | ENDPROC]]
```

#### Parâmetros
 **[[PROTECTED | HIDDEN] FUNCTION | PROCEDURE Name [_ACCESS | _ASSIGN]**
Especifica eventos e métodos a criar para a definição de classe. Eventos e métodos são criados como funções ou procedimentos. Você pode criar uma função ou procedimento de evento para responder a um evento. Para obter mais informações, consulte User-Defined Procedures and Functions , FUNCTION Command e PROCEDURE Command . Observação Chamar funções e procedimentos de evento executa o código definido para essas funções e procedimentos e não chama o evento em si. Para obter mais informações sobre eventos no Visual FoxPro, consulte Understanding the Event Model . Você pode criar uma função ou procedimento de método, que atua no objeto criado com a definição de classe. Observação Você deve declarar cada método protegido em uma linha separada. Os sufixos _ACCESS ou _ASSIGN especificam a criação de um método Access ou Assign para uma propriedade com o mesmo nome. Por padrão, os métodos Access e Assign são protegidos, portanto você não pode acessar nem alterar um método Access ou Assign de fora da classe. Para obter mais informações, consulte Access and Assign Methods e How to: Create Access and Assign Methods . Observação Matrizes são passadas para métodos Access e Assign da mesma forma que procedimentos padrão do Visual FoxPro. Para obter mais informações, consulte Passing Data to Parameters .
**([ cParamName | cArrayName [] [AS Type ][@]]) [AS Type ]**
Especifica um ou mais parâmetros para passar argumentos ao método ou evento da classe ou especifica o nome de uma matriz usada para criar uma biblioteca de tipos. Observação Ao especificar uma matriz, você deve usar a notação de colchetes ([]). DEFINE CLASS não reconhece a notação de parênteses (()). Para parâmetros, a primeira cláusula AS Type especifica o tipo de dados do parâmetro. Para matrizes, a primeira cláusula AS Type especifica um tipo que deve ser um tipo de dados COM válido. Para obter mais informações, consulte a tabela na seção Observações. O tipo também pode ser uma referência a um ProgID de CoClass COM, como ADODB.RecordSet. Você pode especificar ProgIDs com ou sem aspas (""). Se você usar um ProgID de CoClass COM válido para uma cláusula AS Type, o Visual FoxPro o inclui na biblioteca de tipos. Por exemplo, a seguinte definição de método: PROCEDURE Test(oRS AS ADODB.Recordset @) AS ADODB.Recordset Cria uma entrada na biblioteca de tipos: Recordset Test([in, out] Recordset** oRS); Observação Para matrizes, você não pode especificar uma referência a um ProgID gerado pela biblioteca de tipos. Por exemplo, você não pode referenciar uma classe contida no mesmo servidor COM. Se você especificar uma matriz com um tipo para a primeira cláusula AS Type, o Visual FoxPro cria um SAFEARRAY com o tipo especificado. Se você especificar uma matriz sem um tipo para a primeira cláusula AS Type, o Visual FoxPro cria um SAFEARRAY de tipos de dados Variant. Se você especificar um tipo inválido, o Visual FoxPro usa o tipo Variant por padrão. Para obter mais informações sobre safe arrays, consulte a seção Observações. O sinal de arroba ( @ ) especifica que argumentos ou matrizes são passados para a função ou procedimento por referência. Observação Por padrão, os dados são passados para parâmetros em procedimentos definidos pelo usuário por referência e para funções definidas pelo usuário por valor. Para passar uma matriz inteira, você deve passá-la por referência. Para obter mais informações, consulte Passing Data to Parameters . Observação Você pode usar a primeira cláusula AS para implementar tipagem forte, disponibilizar a funcionalidade IntelliSense e para informações de definição de classe armazenadas em uma biblioteca de tipos (OLEPUBLIC). No entanto, o Visual FoxPro não impõe verificação de tipo durante a compilação ou execução do código, portanto você deve garantir o uso de tipos de dados válidos. Para matrizes, a tipagem forte é usada principalmente para criação de biblioteca de tipos e não é imposta em tempo de execução. Ao usar a cláusula cArrayName [] [AS Type ][@], você pode especificar tipagem forte para matrizes para que possam ser escritas corretamente como safe arrays em uma biblioteca de tipos. A tipagem estrita também é recomendada para uso com os métodos de interface especificados pela cláusula IMPLEMENTS. Para obter mais informações, consulte How to: Implement Strong Typing for Class, Object, and Variable Code . A segunda cláusula AS Type indica o tipo do valor de retorno da função. Observação Você não pode especificar matrizes como tipos de retorno. Por exemplo, embora o seguinte código seja válido, ele grava o tipo de retorno da biblioteca de tipos como VARIANT e não como SAFEARRAY: PROCEDURE GetWidgets() AS aWidgets[] ENDPROC Dica Se o método não retorna um valor, use AS VOID como valor de retorno. Isso é necessário para certas tecnologias, como Microsoft COM+ Services Queued Components. Se você deseja que parâmetros e seus tipos apareçam na biblioteca de tipos, deve usar a sintaxe de parâmetro inline em vez do comando LPARAMETERS para declarar os parâmetros, por exemplo: FUNCTION myMeth(parm1 AS Integer @, parm2 AS String) AS Integer ENDFUNC
**[HELPSTRING cHelpString ]**
Especifica uma cadeia de caracteres a adicionar à biblioteca de tipos como descrição da funcionalidade do método para exibição em um navegador de objetos ou IntelliSense.
**THIS_ACCESS( cMemberName )**
Especifica a criação de um procedimento ou função THIS_ACCESS para executar quando o valor de um membro do objeto é alterado ou consultado. Para obter mais informações, consulte Access and Assign Methods e How to: Create Access and Assign Methods .
**[NODEFAULT]**
Impede que o Visual FoxPro execute o processamento padrão de evento ou método para eventos e métodos do Visual FoxPro. Para obter mais informações, consulte NODEFAULT Command .
**cStatements**
Especifica o código a executar ao chamar a função ou procedimento para o evento ou método da classe. Dica Você pode especificar que funções e procedimentos de evento e método aceitem valores incluindo uma instrução PARAMETERS ou LPARAMETERS como a primeira linha executável da função ou procedimento. Para obter mais informações, consulte PARAMETERS Command e LPARAMETERS Command .
**[ENDFUNC | ENDPROC]]**
Indica o fim da função ou procedimento. Diferentemente da maioria das palavras-chave do Visual FoxPro, você não pode abreviar ENDFUNC e ENDPROC porque podem entrar em conflito com as palavras-chave ENDFOR e ENDPRINTJOB.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando DEFINE CLASS:

```foxpro
DEFINE CLASS Clause
   [Property_Definition_Clause]
   [PEMName_COMATTRIB Clause]
   [ADD OBJECT Clause]
   [IMPLEMENTS Clause]
   [Function_Procedure_Definition_Clause]
ENDDEFINE
```

Para obter mais informações e a sintaxe completa, consulte DEFINE CLASS Command. Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS, consulte os seguintes tópicos:
 - DEFINE CLASS Clause
- Property Definition Clause
- PEMName_COMATTRIB Clause
- ADD OBJECT Clause
- IMPLEMENTS Clause

# Exemplos

### Exemplo 1

O exemplo a seguir cria uma classe chamada MyForm a partir da classe base Form e contém um procedimento para uma definição de evento Click. O formulário criado a partir da classe contém um método Click que exibe uma caixa de diálogo quando você clica no formulário.

```foxpro
DEFINE CLASS MyForm AS Form
   PROCEDURE Click
      = MESSAGEBOX('MyForm has been clicked!')
   ENDPROC
ENDDEFINE
```

### Exemplo 2

O exemplo a seguir mostra como você pode especificar tipagem forte usando a cláusula PROCEDURE cArrayName[] [AS Type ][@][AS Type] para que matrizes possam ser escritas corretamente como safe arrays em uma biblioteca de tipos:

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
   REFERENCE "ADODB.Recordset"
   PROCEDURE GetRS() AS ADODB.Recordset
      x=CREATEOBJECT("ADODB.Recordset")
      RETURN X
   ENDPROC
   PROCEDURE SetRS(oRS AS ADODB.Recordset @)
      oRS=CREATEOBJECT("ADODB.Recordset")
   ENDPROC
ENDDEFINE
```
