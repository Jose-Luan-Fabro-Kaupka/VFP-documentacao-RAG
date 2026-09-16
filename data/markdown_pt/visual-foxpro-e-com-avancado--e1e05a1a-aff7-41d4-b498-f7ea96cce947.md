# Visual FoxPro e COM avançado

Você pode aproveitar os recursos COM no Visual FoxPro implementando interfaces e event binding. Versões anteriores do Visual FoxPro forneciam suporte a early binding para servidores COM, mas apenas late binding como cliente. O Visual FoxPro agora contém suporte para clientes com early binding. Este tópico discute o funcionamento interno de early binding versus late binding tanto para cliente quanto para servidor, bem como desempenho COM e como tornar objetos COM mais descobríveis.

# Visão geral

O COM foi desenvolvido para tornar possível que aplicativos fossem tratados como objetos, que podem chamar uns aos outros. As relações entre objetos podem assumir muitas formas. A forma mais simples é um objeto cliente, que chama um objeto servidor. Exemplos de interações de objetos mais complexas do que esse cenário cliente-servidor incluem objetos peer-to-peer, que se chamam mutuamente.

Se os objetos não têm conhecimento prévio uns dos outros, deve haver alguma forma para os objetos descreverem como outro pode chamar a si mesmo. Interfaces de eventos são exemplos de objetos que descrevem essas interfaces de callback. São interfaces que não são implementadas pelo desenvolvedor do objeto de software, mas são implementadas por um cliente desse objeto. Controles Microsoft ActiveX são um exemplo de objetos COM com interfaces muito sofisticadas. Essas interfaces (tanto no controle quanto no host) tornam possível que o controle atue como um controle nativo em um site host. O site host pode implementar a interface de eventos do controle. Essa combinação pode ser muito poderosa nas mãos do desenvolvedor.

Este tópico começa com um servidor COM muito simples do Microsoft Visual FoxPro e mostra como ele é útil. Em seguida, aborda Type Libraries, como você pode lê-las para descobrir como um objeto COM se expõe ao mundo, e desempenho e tratamento de erros. Por fim, fala sobre o que é uma interface e sobre implementar interfaces.

Outra dimensão de objetos se chamando uns aos outros é como eles se chamam. O Visual FoxPro 6.0 tornou possível que clientes com early binding e late binding chamassem servidores do Visual FoxPro 6.0, mas o Visual FoxPro 6.0 só podia chamar servidores usando late binding. A versão atual do Visual FoxPro inclui a capacidade de chamadas de cliente com early binding.

# Criando um servidor COM simples do Visual FoxPro

Você cria um arquivo PRG, que será chamado MYCLASS.PRG, com o seguinte código:

```foxpro
*This entirely self-contained program will build a COM server
* called "myserver.myclass"
* It will unregister a prior instance, if any
IF PROGRAM() != "MYCLASS"
   ?"this file MUST BE NAMED 'myclass.prg'"
   return
ENDIF
IF FILE("myclass.dll")
   DECLARE integer DllUnregisterServer IN myclass.dll
   DllUnregisterServer()
   CLEAR DLLS
ENDIF
BUILD PROJECT myserver FROM myclass
BUILD DLL myserver from myserver recomp
*now test this COM server:
ox = CreateObject("myserver.myclass")    && create the server object
ox.mydocmd("USE home(1)+'samples\data\customer'")    && use a table
?ox.myeval("RECCOUNT()")    && get the record count
DEFINE CLASS myclass AS session OLEPUBLIC
   PROCEDURE MyDoCmd(cCmd as String) as Variant ;
         helpstring "Execute a VFP cmd"
      &cCmd    && just execute parm as if it were a fox command
   FUNCTION MyEval(cExpr as String) ;
         helpstring "Evaluate a VFP expression"
      RETURN &cExpr    && evaluate parm as if it were a fox expr
   FUNCTION Error(nError, cMethod, nLine)
      COMreturnerror(cMethod+'  err#='+str(nError,5)+;
         '  line='+str(nline,6)+' '+message(),_VFP.ServerName)
      && this line is never executed
ENDDEFINE
```

Um programa com essa estrutura constrói servidores COM e não polui o registro. Observe que o código antes da definição da classe é executado apenas em tempo de compilação. Construir um servidor COM registra-o automaticamente no registro. Reconstruir o servidor automaticamente cancela o registro primeiro. No entanto, as informações para cancelar o registro são armazenadas no arquivo PJX. Se o PJX for excluído e reconstruído, as entradas do registro não são removidas quando um novo PJX é construído.

Agora, você construiu seu primeiro servidor. Construir um servidor no Visual FoxPro também constrói uma Type Library e registra informações no registro do sistema, incluindo o ProgId, a Type Library e a localização do arquivo. O processo de compilação cria um arquivo chamado myserver.vbr, que mostra quais chaves do registro são alteradas para registrar o servidor corretamente.

Observe que você está usando a classe base SESSION que foi nova no Visual FoxPro 6.0 SP3. É uma classe base muito leve que é não visual e tem apenas a propriedade DataSession para tornar possíveis sessões de dados separadas. Ao construir servidores COM, a classe base FORM também tem uma propriedade DataSession, mas tem muitas outras propriedades irrelevantes para um servidor COM. Além disso, essas propriedades são, por padrão, gravadas na Type Library, a menos que você as marque todas como protected ou hidden.

# Type Libraries

Uma Type Library é um arquivo que pode ser autônomo ou incorporado como recurso dentro de um EXE ou DLL. É um método independente de linguagem para publicar as interfaces, propriedades e métodos de um objeto COM. Pode conter help strings, IDs de contexto de Help, nomes de parâmetros e nomes de membros (de propriedades e métodos). Se não estiver incorporada dentro de um EXE ou DLL, as extensões de arquivo típicas são TLB ou OLB.

As Type Libraries geradas pelo Visual FoxPro 6.0 contêm os nomes de métodos e parâmetros dos métodos OLE Public. Se houver uma descrição no Description da classe no VCX, então essa descrição é colocada na Type Library como help string.

Você pode visualizar uma Type Library usando várias ferramentas. Por exemplo, use o Object Browser no Microsoft Excel ou Microsoft Word, o Class Browser no Visual FoxPro ou o OLE Viewer no Visual C++ para visualizar uma Type Library. Você pode ver que Type Libraries podem conter modelos de objetos inteiros do aplicativo servidor e podem ser bastante extensas.

Quando uma ferramenta está visualizando uma Type Library, o servidor não pode ser reconstruído, porque a Type Library não pode ser reescrita. Além disso, se um cliente tem o servidor instanciado, ele não pode ser reconstruído. Usar uma cópia da DLL ou EXE compilada é uma forma de evitar esse problema.

### Lendo uma Type Library

Uma ferramenta de leitura de Type Library (TLBINF32.DLL) acompanha o Microsoft Visual Studio. É uma ferramenta destinada ao uso por vários produtos, portanto foi escrita como um servidor COM. Aqui está um código de exemplo para ler a Type Library do servidor de exemplo criado anteriormente.

```foxpro
clear
PUBLIC otlb
otli=NEWOBJECT('tli.tliapplication')
otlb=otli.TypeLibInfoFromFile("myserver.dll")
*otlb=otli.TypeLibInfoFromFile("tlbinf32.dll")
*otlb=otli.TypeLibInfoFromFile("c:\program files\microsoft office\office\excel9.olb")
?"CoClasses:"
FOR each oCoClass in otlb.CoClasses
   ?"  ",oCoClass.name
   *now each interface associated with this CoClass
   for each oInterface in oCoClass.Interfaces
      ?"     ",oInterface.name
   endfor
endfor
?
?"Interfaces"
FOR each oInterface in otlb.Interfaces
   ?"  ",oInterface.name
ENDFOR
?
?"Interface Members for 1st interface"
FOR each oMember IN otlb.Interfaces(1).Members
   ?"  ", oMember.name
   FOR each oParm in oMember.Parameters
      ?"             ",oParm.name
   ENDFOR
ENDFOR
```

Este código primeiro cria uma instância da ferramenta de leitura TLB e então invoca o método TypeLibInfoFromFile para carregar uma Type Library. Os itens dentro da biblioteca são representados como várias coleções, que podem ser manipuladas com bastante facilidade no Visual FoxPro usando a construção FOR EACH.

A coleção Interface é uma coleção de interfaces descritas na Type Library. Essas interfaces podem ser aquelas implementadas pelo servidor ou podem ser interfaces que devem ser implementadas por um cliente, por exemplo, no caso de Events.

A coleção CoClass descreve os objetos COM que podem ser criados por um cliente. A interface padrão implementada pelo CoClass é mostrada, junto com uma interface Event Source opcional.

Outras interfaces além da padrão do CoClass e da interface Event podem ser descritas. A forma pela qual um cliente obtém essas outras interfaces pode ser por meio de uma chamada de método. Por exemplo, uma interface ICell pode ser retornada de um método chamado GetCell.

Constantes também podem ser definidas na Type Library. Por exemplo, para obter as constantes, como xlMaximized, da Type Library do Excel, explore a coleção otlb.Constants.

Uma forma de aprender a usar a ferramenta TLBINF32.DLL é usá-la em si mesma. Isso mostrará as propriedades, métodos, parâmetros e assim por diante que são úteis.

# Desempenho

Desempenho significa muitas coisas para muitas pessoas. No contexto de software e objetos COM, desempenho significa obter resultados mais rapidamente. COM trata de fazer módulos de software se comunicarem uns com os outros. Portanto, melhorar as comunicações COM alcançará maior desempenho.

Por exemplo, considere o seguinte código:

```foxpro
ox=CreateObject("excel.application")
start = seconds()
ox.workbooks.add
SET EXCLUSIVE OFF
USE HOME()+'samples\data\customer'
ox.visible=1
FOR i= 1 TO RECCOUNT()
   FOR J = 1 TO FCOUNT()
      ox.Activesheet.cells(i,j).value = EVAL(FIELD(j))
   NEXT
   SKIP
NEXT
ox.Workbooks(1).Close(0)   && close workbook, discarding changes
ox=0   && release Excel
?seconds() - start
```

Ele preenche uma planilha do Excel com os valores de uma tabela. Este código leva cerca de 30 segundos para executar para 92 registros na máquina do autor.

Ao tentar melhorar o desempenho, você deve ter em mente exatamente o que está acontecendo e tentar descobrir onde estão os gargalos.

Tornar a planilha visível apenas depois de preenchida, em vez de antes, reduz um pouco o tempo. Fazer o Excel não maximizado torna um pouco mais rápido.

Observe que a maior parte do tempo é gasto executando a única linha de código que atribui o valor à célula. Você pode remover todas as chamadas COM alterando esta linha para

```foxpro
      oa= EVAL(FIELD(j))
```

Isso obviamente altera a intenção do código, mas faz o loop duplo levar apenas um segundo. Isso indica que 29 segundos estavam sendo gastos na parte ox.Activesheet.cells da linha.

Analisando esta linha mais a fundo, o Visual FoxPro avalia ox.Activesheet, e o resultado é colocado em um valor temporário. Então, esse valor temporário é desreferenciado para obter a coleção cells. Cada "." na expressão resulta em um valor temporário obtido e então desreferenciado para obter um novo valor.

Cada uma dessas desreferências do operador ponto "." é na verdade uma chamada de método COM de ida e volta ao Excel, invocando um método do Excel que retorna um valor. Primeiro, o método IApplication.ActiveSheet é invocado, que retorna ao Visual FoxPro uma referência temporária à planilha ativa. Então, a interface desse objeto é usada para obter a coleção cells. Então, a coleção é desreferenciada usando os índices da célula como parâmetros para obter uma referência de objeto a uma única célula. Então, a propriedade value dessa célula recebe um novo valor (outra ida e volta COM). Isso totaliza quatro idas e voltas.

Obter uma referência de objeto a ox.Activesheet antes do loop duplo aninhado e usar essa referência em cache em vez disso resultou em cerca de 50 por cento de melhoria.

```foxpro
oa = ox.Activesheet    && get an object reference
FOR i= 1 TO RECCOUNT()
   FOR J = 1 TO FCOUNT()
      oa.cells(i,j).value = EVAL(FIELD(j))
   NEXT
   SKIP
NEXT
```

Como o Activesheet é invariante de loop em relação ao loop duplo, você pode obter uma referência de objeto a ele antes do loop e armazená-la em cache em uma variável. Isso remove uma ida e volta, tornando o total três.

O número de idas e voltas diminuiu em 25 por cento, mas a diminuição de tempo foi de 50 por cento. A remoção do número de idas e voltas não resultará em uma diminuição proporcional no tempo total. A sobrecarga de criar e liberar várias variáveis temporárias, a fração do tempo gasto realmente no servidor executando o código e outros fatores não são lineares.

> **Observação:** O código anterior não precisa usar Activesheet de forma alguma. A coleção cells também é encontrada a partir da interface Iapplication. Foi usada aqui apenas para fins de ilustração.

# Usando Visual Basic como cliente

Você pode usar o Visual Basic como cliente para realizar a mesma tarefa.

Para usar o Visual Basic como cliente
 - Inicie o Excel.
- No menu Tools, aponte para Macro .
- Clique em Macros e nomeie como t .
- Clique em Create .
- No menu Tools, clique em References e adicione a Type Library myserver às referências. Isso torna possível que as informações da Type Library myserver sejam usadas na macro.
- Cole o seguinte código: Sub t() Dim ox As New myserver.myclass ox.mydocmd ("SET EXCLUSIVE OFF") ox.mydocmd ("USE C:\Program Files\Microsoft Visual FoxPro VersionNumber \Samples\Data\Customer") n = ox.MyEval("reccount()") nflds = ox.MyEval("fcount()") nsecs = ox.MyEval("seconds()") For i = 1 To n For j = 1 To nflds cc = "evaluate(field(" & j & "))" Application.Sheets(1).Cells(i, j).Value = ox.MyEval(cc) Next ox.mydocmd ("skip") Next MsgBox (ox.MyEval("seconds()") - nsecs) End Sub

# Tratamento de erros

O tratamento de erros é muito importante em servidores COM, e particularmente em servidores DLL. Se o cliente invocasse um método no servidor que causasse algum tipo de erro, como File Not Found ou Access Denied, não seria bom que o servidor exibisse uma caixa de mensagem indicando o erro. O desenvolvedor deve usar o método Error da classe OLE Public para tratar esses erros de forma adequada. Uma nova função no Visual FoxPro 6.0, chamada COMReturnError, fará com que um objeto COM Error seja criado e retornado ao cliente COM. Ela recebe dois parâmetros: o Source e o Description. Você pode colocar quaisquer cadeias de caracteres que desejar nesses parâmetros. Este método de exemplo pode ser colado diretamente no exemplo myserver anterior.

```foxpro
FUNCTION Error(nError, cMethod, nLine)
   COMreturnerror(cMethod+'  err#='+str(nError,5)+'  line='+str(nline,6)+'
      '+message(),_VFP.ServerName)
   && this line is never executed
```

Você pode invocar este método de erro chamando o método MyDocmd com um comando inválido:

```foxpro
ox = CreateObject("myserver.myclass")    && create the server object
?ox.mydocmd("illegal command")    && causes an Error to occur
```

O erro que ocorre no servidor é capturado pelo método MyClass::Error, que então faz o servidor abortar o processamento e retornar o objeto COM Error com o Source e o Description preenchidos.

```foxpro
?aerror(myarray)
list memo like myarray
MYARRAY     Pub    A
   (   1,   1)     N  1429        (      1429.00000000)
   (   1,   2)     C  "OLE IDispatch exception code 0 from mydocmd
                      err#=   16  line=     2 Unrecognized command v
                      erb.: c:\fox\test\myserver.exe.."
   (   1,   3)     C  "c:\fox\test\myserver.exe"
   (   1,   4)     C  "mydocmd  err#=   16  line=     2 Unrecognized
                       command verb."
   (   1,   5)     C  ""
   (   1,   6)     N  0           (         0.00000000)
   (   1,   7)     N  0           (         0.00000000)
```

# Interfaces

Operacionalmente, uma interface COM pode ser pensada como um ponteiro para uma tabela de endereços de função. Esta tabela é às vezes chamada vtable, ou tabela de funções virtuais. A definição da interface inclui o número de entradas na tabela, a associação entre o nome do método e o índice da tabela, e as assinaturas de função de cada chamada de método. A assinatura consiste no número de parâmetros, nos tipos dos parâmetros e no valor de retorno.

Todas as interfaces COM herdam de IUnknown. Isso significa que as três primeiras entradas na vtable de cada interface COM são definidas como os endereços da implementação do servidor de IUnkown::QueryInterface, IUnkown::AddRef e IUnkown::Release.

Quando uma interface herda de outra interface, tudo o que isso significa é que a vtable da interface consiste nas vtables das interfaces herdadas primeiro.

Interfaces duais são interfaces COM que herdam da interface IDispatch. A interface IDispatch tem apenas quatro métodos: GetTypeInfoCount, GetTypeInfo, GetIDsOfNames e Invoke. Assim, as primeiras sete interfaces são bem definidas em uma interface IDispatch e em qualquer outra interface que herda de IDispatch.

Para Myserver.dll criado anteriormente, a interface dual IMyClass ficaria assim:

```foxpro
   IMyClass
      QueryInterface(QI params)  (from IUnknown)
      Addref                     (from IUnknown)
      Release                    (from IUnknown)
      GetTypeInfoCount()         (from IDispatch)
      GetTypeInfo()              (from IDispatch)
      GetIDsOfNames()            (from IDispatch)
      Invoke()                   (from IDispatch)
      MyDoCmd(cCmd)              (from IMyClass)
      MyEval(cExpr)              (from IMyClass)
```

Suponha que o cliente deseja fazer uma chamada ao método Activesheet da interface dual IApplication no servidor. A chamada real pode ser feita de duas formas: early binding e late binding. Early binding é às vezes chamado VTtable binding, porque significa apenas que o cliente chama o servidor diretamente encontrando o endereço de Activesheet na vtable diretamente. Este endereço de função é uma entrada na vtable e será maior que sete. Este índice de endereço de função é codificado no cliente na compilação do cliente e é conhecido como early binding. Se versões subsequentes do servidor alterassem a ordem da vtable, então as chamadas de cliente com early binding seriam errôneas.

Chamadas com late binding passam pela interface IDispatch. O cliente chama IDispatch::GetIDsOfNames com a cadeia de caracteres Activesheet para obter o ID de função dessa função. (Este ID de função então pode ser armazenado em cache pelo cliente para chamadas subsequentes.) O cliente então empacota todos os parâmetros de Activesheet em uma única estrutura DISPPARAMS, e a função IDispatch::Invoke é chamada com o ID de função e os DISPPARAMS como parâmetros. A implementação de IDispatch::Invoke no lado do servidor desempacota a estrutura DISPPARAMS, faz a chamada real a Activesheet, obtém o valor de retorno e passa de volta ao cliente.

Como o late binding não codifica o índice de função das chamadas de método, os clientes não precisam saber em tempo de compilação qual é o índice de função dos métodos e ainda funcionarão, mesmo se uma nova versão do servidor reorganizar a ordem da vtable ou alterar as assinaturas dos métodos. No entanto, o empacotamento de parâmetros no lado do cliente e o desempacotamento no lado do servidor adicionam tempo de execução às chamadas de método que não existe com chamadas de early binding.

### Implementando interfaces

Implementar uma interface significa que você examina as propriedades, eventos e métodos de um objeto e cria um novo objeto que tem exatamente as mesmas propriedades, eventos e métodos. Isso inclui quaisquer parâmetros, tipos de parâmetros e valores de retorno. Em outras palavras, se um objeto sabe como chamar outro objeto usando uma interface específica, então também sabe como chamar qualquer objeto que implemente essa interface específica.

Implementar uma interface promete ao cliente que cada método nessa interface pode ser chamado. Isso significa que se houver um método chamado `Sample(parm1 as int, parm2 as string, parm3 as variant @) as int`, então essa assinatura de método idêntica deve ser encontrada no objeto.

No seguinte exemplo ADO, por exemplo, se um parâmetro for removido da assinatura do método, executar o código produz esta mensagem:

> **Observação:** Class can not be instantiated because Member 'RECORDSETEVENTS_WillChangeField' has wrong # of parameters

Da mesma forma, remover um método produz outra mensagem de erro.

Como mencionado anteriormente, as interfaces são descritas em Type Libraries para todos verem. O Visual FoxPro Object Browser (no menu Tools) torna possível inspecionar type libraries. Se você arrastar uma interface dele para um PRG que está aberto no editor do Visual FoxPro, então o object browser gerará as assinaturas de método necessárias para implementar essa interface.

# Event Binding

A capacidade de implementar interfaces torna possíveis algumas capacidades interessantes com o Microsoft Office. Este exemplo implementa os eventos para Microsoft Outlook, Excel e Word. Como você pode ver pelos nomes dos métodos, cada aplicativo Office fornece interfaces diferentes. O novo comando EventBinding na versão atual do Visual FoxPro torna possível para o desenvolvedor vincular uma classe Visual FoxPro que implementa uma interface ao objeto COM que é a fonte e o publicador de eventos.

Este modelo de eventos é chamado eventos fortemente acoplados. O cliente e o servidor devem ter conhecimento íntimo uns dos outros, e há uma correspondência um-para-um entre os objetos. Um novo modelo de interação de eventos de objetos é chamado eventos fracamente acoplados, no qual um objeto pode publicar eventos e outro objeto pode assinar esses eventos.

```foxpro
CLEAR
CLEAR all
PUBLIC ox as Excel.Application, ;
   ow as word.application, ;
   oOutlook as Outlook.Application
oOutlookEvents= NEWOBJECT('OutlookEvents')
oOutlook = NEWOBJECT("Outlook.Application")
oOutlookEvents.oo = oOutlook
? "Outlook",EVENTHANDLER( oOutlook, oOutlookEvents)
oWordEvents = NEWOBJECT("WordEvents")
ow = NEWOBJECT("word.application")
oWordEvents.ow = ow
?"Word",EVENTHANDLER(ow,oWordEvents)
ow.visible = .t.
ow.Activate
ow.Documents.Add
oExcelEvents = NEWOBJECT("ExcelEvents")
oex = NEWOBJECT("excel.application")
oex.Workbooks.Add
?"Excel",EVENTHANDLER(oex, oExcelEvents)
oex.visible = .t.
_screen.WindowState= 1
DEFINE CLASS OutlookEvents AS SESSION OLEPUBLIC
   IMPLEMENTS ApplicationEvents IN Outlook.Application
   oo = .null.
   PROCEDURE ApplicationEvents_ItemSend(ITEM AS VARIANT, ;
         CANCEL AS LOGICAL) AS VOID
      ?PROGRAM()
      m.item.Body=STRTRAN(m.item.Body,"good","bad") + ;
         CHR(13)+CHR(10)+TRANSFORM(DATETIME())+" Fox was here!"
*      if Recipients fails, it could be outlook security
*      m.item.Recipients.Add("someone@example.com")
   PROCEDURE ApplicationEvents_NewMail() AS VOID
      ?PROGRAM()
   PROCEDURE ApplicationEvents_Reminder(ITEM AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE ApplicationEvents_OptionsPagesAdd(PAGES AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE ApplicationEvents_Startup() AS VOID
      ?PROGRAM()
   PROCEDURE ApplicationEvents_Quit() AS VOID
      ?PROGRAM()
   PROCEDURE destroy
      ?PROGRAM()
      IF !ISNULL(this.oo)
         ?EVENTHANDLER(this.oo,this,.t.)
      ENDIF
ENDDEFINE
DEFINE CLASS WordEvents as Custom
   implements applicationevents2 in "word.application"
   ow = .null.
   PROCEDURE applicationevents2_startup()
      ?PROGRAM()
   PROCEDURE applicationevents2_quit
      ?PROGRAM()
   procedure applicationevents2_DocumentBeforeClose(Cancel,Doc)
      ?PROGRAM()
   procedure DocumentBeforeClose(Cancel,Doc)
      ?PROGRAM()
   procedure applicationevents2_DocumentBeforePrint(Cancel,Doc)
      ?PROGRAM()
   procedure applicationevents2_DocumentBeforeSave(Doc,SaveAsUI,Cancel)
      ?PROGRAM()
   procedure applicationevents2_DocumentChange
      ?PROGRAM()
   procedure applicationevents2_DocumentOpen(Doc)
      ?PROGRAM()
   procedure applicationevents2_NewDocument(Doc)
      ?PROGRAM()
   procedure applicationevents2_WindowActivate(Doc,Wn)
      ?PROGRAM()
   procedure applicationevents2_WindowBeforeDoubleClick(Sel,Cancel)
      ?PROGRAM()
   procedure applicationevents2_WindowBeforeRightClick(Sel,Cancel)
      ?PROGRAM()
   procedure applicationevents2_WindowDeactivate(Doc,Wn)
      ?PROGRAM()
   procedure applicationevents2_WindowSelectionChange(Sel)
      ?PROGRAM(),sel.text
      IF sel.start < sel.end
          sel.InsertAfter("Fox!")
*!*         mtmp = sel.text
*!*         sel.text=STRTRAN(mtmp,"good","Great!")
      endif
   PROCEDURE destroy
       ?PROGRAM()
       IF !ISNULL(this.ow)
         ?EVENTHANDLER(this.ow,this,.t.)
      ENDIF
ENDDEFINE
DEFINE CLASS ExcelEvents AS session OLEPUBLIC
   IMPLEMENTS AppEvents IN "excel.application"
   PROCEDURE AppEvents_NewWorkbook(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetSelectionChange(Sh AS VARIANT, ;
         Target AS VARIANT) AS VOID
      LOCAL mtmp,mcell
      mcell = m.target.Cells(1,1)
      IF !ISNULL(mcell)
         mtmp = m.target.Cells(1,1).Value
         ?PROGRAM(),VARTYPE(mtmp)
         DO case
         case ISNULL(mtmp)
   *         m.target.Cells(1,1).Value  = "Fox is great"
         CASE VARTYPE(mtmp)='C'
            m.target.Cells(1,1).Value = ;
               STRTRAN(mtmp,"good","great!")
         CASE VARTYPE(mtmp)='N'
            m.target.Cells(1,1).Value = mtmp + 1
         ENDCASE
      ENDIF
   PROCEDURE AppEvents_SheetBeforeDoubleClick(Sh AS VARIANT, ;
         Target AS VARIANT, Cancel AS LOGICAL) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetBeforeRightClick(Sh AS VARIANT, ;
         Target AS VARIANT, Cancel AS LOGICAL) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetActivate(Sh AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetDeactivate(Sh AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetCalculate(Sh AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetChange(Sh AS VARIANT, Target AS VARIANT) AS
         VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookOpen(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookActivate(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookDeactivate(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookBeforeClose(Wb AS VARIANT, ;
         Cancel AS LOGICAL) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookBeforeSave(Wb AS VARIANT, ;
         SaveAsUI AS LOGICAL, Cancel AS LOGICAL) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookBeforePrint(Wb AS VARIANT, ;
         Cancel AS LOGICAL) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookNewSheet(Wb AS VARIANT, ;
         Sh AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookAddinInstall(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookAddinUninstall(Wb AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WindowResize(Wb AS VARIANT, Wn AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WindowActivate(Wb AS VARIANT, Wn AS VARIANT) AS
         VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WindowDeactivate(Wb AS VARIANT, Wn AS VARIANT) AS
         VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetFollowHyperlink(Sh AS VARIANT, ;
         Target AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_SheetPivotTableUpdate(Sh AS VARIANT, ;
         Target AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookPivotTableCloseConnection(Sh AS VARIANT, ;
         Target AS VARIANT) AS VOID
      ?PROGRAM()
   PROCEDURE AppEvents_WorkbookPivotTableOpenConnection(Sh AS VARIANT, ;
         Target AS VARIANT) AS VOID
      ?PROGRAM()
ENDDEFINE
```

Aqui está um exemplo de implementação de interfaces de eventos ADO. Neste caso, o usuário não está interagindo com um aplicativo, causando eventos a ocorrer, como nos exemplos Office anteriores. Aqui, o usuário está chamando ADO diretamente usando chamadas de método, e ADO está chamando de volta ao cliente usando sua interface de eventos.

```foxpro
clear
CLEAR all
local ox as adodb.recordset
local oc as ADODB.Connection
oe = NEWOBJECT("myclass")
oe2 = NEWOBJECT("myclass")
oc=NEWOBJECT("adodb.connection")
connstr = "Driver={Microsoft Visual FoxPro Driver};UID=;PWD=;SourceDB=" + ;
   HOME(1)+"samples\data\testdata.dbc" + ;
    ";SourceType=DBC;Exclusive=No;BackgroundFetch=No;Collate=Machine;"
*
oc.ConnectionString= connstr
oc.Open
ox = oc.Execute("select * from customer")
* Now enable event handling
?EVENTHANDLER(ox,oe)
?EVENTHANDLER(ox,oe2)
?
?PADR(ox.Fields(0).Value,20)
?EVENTHANDLER(ox,oe2,.f.) && Turn off 2nd obj event handling
ox.MoveNext
?PADR(ox.Fields(0).Value,20)
ox.MoveNext
CLEAR all
retu
for i = 0 to ox.Fields.Count-1
*   ?PADR(ox.Fields(i).Name,20)
*   ?ox.Fields[i].value
endfor
DEFINE CLASS myclass AS session
   implements RecordsetEvents IN "adodb.recordset"
*  implements RecordsetEvents IN ;
*"C:\PROGRAM FILES\COMMON FILES\SYSTEM\ADO\MSADO15.DLL"
   PROCEDURE Recordsetevents_WillChangeField(cFields AS Number @, ;
         Fields AS VARIANT @, adStatus AS VARIANT @, ;
         pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_FieldChangeComplete(;
         cFields AS Number @, ;
         Fields AS VARIANT @, pError AS VARIANT @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_WillChangeRecord(adReason AS VARIANT @, ;
         cRecords AS Number @, adStatus AS VARIANT @, ;
         pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_RecordChangeComplete(adReason AS VARIANT @, ;
         cRecords AS Number @, pError AS VARIANT @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_WillChangeRecordset(adReason AS VARIANT @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
      ?adreason,adstatus,precordset.recordcount
   PROCEDURE Recordsetevents_RecordsetChangeComplete(;
         adReason AS VARIANT @, ;
         pError AS VARIANT @, adStatus AS VARIANT @, ;
         pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_WillMove(adReason AS VARIANT @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_MoveComplete(adReason AS VARIANT @, ;
         pError AS VARIANT @, adStatus AS VARIANT @, ;
         pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_EndOfRecordset(fMoreData AS LOGICAL @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_FetchProgress(Progress AS Number @, ;
         MaxProgress AS Number @, adStatus AS VARIANT @, ;
         pRecordset AS VARIANT @) AS Void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
   PROCEDURE Recordsetevents_FetchComplete(pError AS VARIANT @, ;
         adStatus AS VARIANT @, pRecordset AS VARIANT @) AS void
      ? " "+program() + ' ' + TRANSFORM(DATETIME())
ENDDEFINE
```

# Usando Smart Tags do Office XP

O Office XP inclui uma nova capacidade chamada Smart Tags. Enquanto uma trabalhadora do conhecimento típica em uma empresa trabalha, ela pode usar vários aplicativos de computador e usar assuntos semelhantes em cada um. Por exemplo, a empresa pode ter uma lista de clientes, e ela pode precisar enviar e-mail, criar documentos ou planilhas, ou até visualizar páginas Web sobre clientes. Suponha que neste instante ela está escrevendo uma mensagem de e-mail sobre o cliente ALFKI, e precisa saber o número de telefone ou limite de crédito do cliente. Normalmente, isso significa iniciar ou alternar para outro aplicativo, que mantém essas informações, fazer uma pesquisa por ALFKI e transferir os dados para o e-mail.

A tecnologia Smart Tags é uma forma pela qual vários aplicativos podem reconhecer cadeias de caracteres (tags) dentro de texto e, opcionalmente, fornecer ao usuário uma forma de invocar um menu diretamente sobre essa tag que pode fornecer informações úteis ou executar tarefas úteis. Um smart tag em ALFKI pode não apenas oferecer o limite de crédito e o endereço, mas também pode oferecer a opção de ir ao site Web do cliente, adicionar a um log de transações, iniciar outro aplicativo ou até discar o telefone. O usuário pode até digitar ALFKI temporariamente em qualquer aplicativo que esteja usando atualmente, pesquisar informações e então excluir essa cadeia de caracteres no aplicativo.

O seguinte é um exemplo da tecnologia Smart Tags que reconhece os IDs de cliente na tabela de clientes de exemplo. Os verbos de ação do Smart Tag compõem os campos da tabela, mais um para visitar o site Web do cliente. Se o aplicativo é Word, o verbo para o campo insere esse campo no documento Word. Para Excel, o valor do campo é inserido na coluna adjacente, e a largura dessa coluna é ajustada. Para Internet Explorer, uma caixa de mensagem é exibida (observe que, embora seja uma DLL do Visual FoxPro, MessageBox pode ser chamado usando Declare DLL).

Um Smart Tag só precisa registrar seu ProgID no registro nos locais apropriados. O Smart Tag SDK (disponível no site da Microsoft) fornece mais detalhes sobre Smart Tags.

Um Smart Tag deve implementar duas interfaces: ISmartTagRecognizer e ISmartTagAction. A primeira examina uma cadeia de caracteres e chama de volta em um objeto analisado se uma tag é reconhecida. A segunda interface descreve as ações possíveis e realmente executa as ações.

> **Observação:** Se você tiver algum aplicativo Office aberto, ele terá uma instância da sua DLL aberta. Você não poderá modificar a DLL até fechar o aplicativo Office.

O método Logit grava em um arquivo de log, que é uma técnica útil para aprender como as interfaces funcionam e para depurar qualquer código. Usar um editor que atualiza automaticamente um arquivo modificado externamente para exibir o log é útil.

```foxpro
CLEAR ALL
clear
SET excl off
?PROGRAM()
*Smart tags in Office XP. Just change the DATAPATH,STAGPATH if necessary
IF PROGRAM() != "STAG"
   ?"this file MUST BE NAMED 'stag.prg'"
ENDIF
#define STNAME  "MynameSpaceURI#MyLocalName"
#define DATAPATH HOME(1)+"samples\data\"
#define STAGPATH "C:\Program Files\Common Files\Microsoft Shared\Smart Tag\mstag.tlb"
IF .t.
   IF FILE("stag.dll")
      DECLARE integer DllUnregisterServer IN stag.dll
      DllUnregisterServer()
      CLEAR DLLS
   ENDIF
   BUILD PROJECT stag FROM stag
   BUILD mtDLL stag from stag recomp
   STRTOFILE("","d:\t.txt")    && null log file
endif
#DEFINE HKEY_CURRENT_USER  -2147483647  && BITSET(0,31)+1
oFoxReg=NEWOBJECT("foxreg", HOME(1)+"FFC\registry")
oFoxReg.OpenKey("Software\Microsoft\Office\Common\Smart Tag\Actions\stag.MyStag", ;
   HKEY_CURRENT_USER, .T.)
oFoxReg.OpenKey(;
   "Software\Microsoft\Office\Common\Smart Tag\Recognizers\stag.MyStag", ;
   HKEY_CURRENT_USER, .T.)
DEFINE CLASS MyStag AS Session OLEPUBLIC
   IMPLEMENTS ISmartTagRecognizer IN STAGPATH
   IMPLEMENTS ISmartTagAction IN STAGPATH
   PROCEDURE ISmartTagRecognizer_get_ProgId() AS STRING
      logit()
      RETURN   "stag.MyStag"
   PROCEDURE ISmartTagRecognizer_get_Name(LocaleID AS Integer) AS STRING
      logit()
      RETURN "VFP NorthWind Customer Recognizer"
   PROCEDURE ISmartTagRecognizer_get_Desc(LocaleID AS Integer) AS STRING
      logit()
      RETURN "VFP NorthWind Customer ID Recognizer"
   PROCEDURE ISmartTagRecognizer_get_SmartTagCount() AS Integer
      logit()
      RETURN 1
   PROCEDURE ISmartTagRecognizer_get_SmartTagName(;
         SmartTagID AS Integer) AS STRING
      logit()
      If SmartTagID = 1
         RETURN STNAME
         EndIf
      RETURN ""
   PROCEDURE ISmartTagRecognizer_get_SmartTagDownloadURL(;
         SmartTagID AS Integer) AS STRING
      logit()
      RETURN ""
   PROCEDURE ISmartTagRecognizer_Recognize(cText AS STRING, ;
         DataType AS Integer, ;
         LocaleID AS Integer, RecognizerSite AS VARIANT) AS VOID
      logit(ctext+' '+TRANSFORM(LEN(CTEXT)))
      LOCAL i,  mat,cWord,propbag
      i = 1
      DO WHILE i <= LEN(cText)
         IF ISALPHA(SUBSTR(cText,i))
            mst = i
            DO WHILE i <= LEN(cText) AND ;
                  (ISALPHA(SUBSTR(cText,i)) or ;
                  ISDIGIT(SUBSTR(cText,i)))
               i=i+1
            ENDDO
            IF mst # i
               cWord = SUBSTR(cText,mst,i-mst)
               IF SEEK(cWord,"Customer")
                  * Ask for a property bag
                  propbag = ;
                     RecognizerSite.GetNewPropertyBag()
                  * Commit the smart tag
                  propbag.write("test","value")
                  propbag.write("test2","value2")
                     RecognizerSite.CommitSmartTag(STNAME, ;
                       mst, LEN(cWord), propbag)
                    propbag=.null.
               ENDIF
            ENDIF
         ENDIF
         i=i+1
      ENDDO
***********************
   PROCEDURE ISmartTagAction_get_ProgId() AS STRING
      logit()
      RETURN "stag.MyStag"
   PROCEDURE ISmartTagAction_get_Name(LocaleID AS Integer) AS STRING
      logit()
      RETURN "Customer Actions"
   PROCEDURE ISmartTagAction_get_Desc(LocaleID AS Integer) AS STRING
      logit()
      RETURN  "Provides actions for VFP Customer data"
   PROCEDURE ISmartTagAction_get_SmartTagCount() AS Integer
      logit()
      RETURN 1
   PROCEDURE ISmartTagAction_get_SmartTagName(SmartTagID AS Integer) AS
         STRING
      logit()
      IF SmartTagID = 1
         RETURN STNAME
      EndIf
      RETURN ""
   PROCEDURE ISmartTagAction_get_SmartTagCaption(SmartTagID AS Integer, ;
         LocaleID AS Integer) AS STRING
      logit(TRANSFORM(SmartTagID ))
      RETURN  "Customer Lookup"
   PROCEDURE ISmartTagAction_get_VerbCount(SmartTagName AS STRING) AS
         Integer
      logit(SmartTagName )
      If SmartTagName = STNAME
            RETURN FCOUNT()+1
         ENDIF
         RETURN 0
   PROCEDURE ISmartTagAction_get_VerbID(SmartTagName AS STRING, ;
         VerbIndex AS Integer) AS Integer
      logit(SmartTagName +', '+ TRANSFORM(VerbIndex ))
      RETURN VerbIndex
   PROCEDURE ISmartTagAction_get_VerbCaptionFromID(VerbID AS Integer, ;
         _ApplicationName AS STRING, LocaleID AS Integer) AS STRING
      logit(TRANSFORM(VerbID )+' '+_ApplicationName +;
         ' '+TRANSFORM(LocaleID))
      IF VerbId <= FCOUNT()
         RETURN "View "+FIELD(VerbID)
      ENDIF
      RETURN "Visit customer Web site"
   PROCEDURE ISmartTagAction_get_VerbNameFromID(VerbID AS Integer) AS
         STRING
      logit(TRANSFORM(VerbID))
      IF VerbId <= FCOUNT()
         RETURN FIELD(VerbID)
      ENDIF
      RETURN "Visit Web site"
   PROCEDURE ISmartTagAction_InvokeVerb(VerbID AS Integer, ;
         cApplicationName AS STRING, ;
         Target AS VARIANT, oProperties AS VARIANT, ;
         cText AS STRING, Xml AS STRING) AS VOID
      logit(TRANSFORM(VerbID )+' '+cApplicationName +' '+cText+' ';
          +Xml+' '+TRANSFORM(oProperties.count))
      LOCAL i,cProp
      oProperties.write("iitest","iivalue")
      oProperties.write("iitest2","iivalue2")
      FOR i = 1 to oProperties.count
         cProp = oProperties.keyfromindex(i-1)
         logit(cProp)
         logit(oProperties.read(cprop))
      endfor
      LOCAL fExcel,fWord
      DO case
      CASE capplicationname = "Excel.Application.10"
         fExcel = .t.
         logit(m.target.cells[1,1].value)
      CASE capplicationname = "Word.Application.10"
         fWord = .t.
*         logit(m.target.range
      ENDCASE
      IF verbId > FCOUNT()
         LOCAL oie as internetexplorer.application
         oie = NEWOBJECT("internetexplorer.application")
         oie.navigate2("localhost/"+ctext+".html")
         oie.visible=1
      else
         IF SEEK(cText,"customer")
            DO case
            case fExcel
               target.cells[1,2].value = ;
   ALLTRIM(TRANSFORM(EVALUATE(FIELD(VerbID))))
               target.Columns(2).columnWidth = 25
            case fWord
               target.insertAfter(' '+;
   ALLTRIM(TRANSFORM(EVALUATE(FIELD(VerbID)))))
            otherwise
               DECLARE Integer MessageBox IN WIN32API ;
                  as msgbox ;
                  Integer,string,string, integer
               msgbox(0,;
   ALLTRIM(TRANSFORM(EVALUATE(FIELD(VerbID)))), ;
                  ctext+"="+company,0)
            endcase
         ELSE
            logit("not found")
         ENDIF
      ENDIF
   PROCEDURE Init
      logit()
      SET EXACT ON
      SET EXCLUSIVE off
      SET PATH TO DATAPATH
      USE customer order cust_id shared
   PROCEDURE Destroy
      logit()
   PROCEDURE MyDoCmd(cCmd as String)
      &cCmd
   PROCEDURE MyEval(cExp as String)
      RETURN &cExp
   PROCEDURE Error(nError, cMethod, nLine)
      logit(TRANSFORM(nError)+' '+TRANSFORM(nLine)+' '+MESSAGE())
ENDDEFINE
#if .f.
DEFINE CLASS STagAction AS StagRecognizer OLEPUBLIC
   PROCEDURE Error(nError, cMethod, nLine)
      logit(PROGRAM()+" "+TRANSFORM(nError)+' '+TRANSFORM(nLine)+' '+MESSAGE())
ENDDEFINE
#endif
   FUNCTION Logit(cStr)
TEXT TO mystr TEXTMERGE NOSHOW
<<DATETIME()>> <<PROGRAM(PROGRAM(-1)-1)>> <<cStr>>
ENDTEXT
      STRTOFILE(myStr,"D:\t.TXT",.T.)
```

# Design de callback do Visual FoxPro

O Visual FoxPro torna possível para o desenvolvedor criar objetos COM, que publicam interfaces que os clientes podem implementar. Este cenário de callback é quase idêntico a objetos Visual FoxPro levantando eventos para clientes. Este exemplo consiste em uma classe principal de servidor COM chamada IDEMO, que também publica uma interface de eventos, chamada DemoEvents.

O código do cliente tem uma única classe chamada cCallBack, que implementa DemoEvents.

IDEMO tem um método chamado BuyStock, que os clientes podem chamar para comprar algumas ações. O método BuyStock tem apenas um comentário onde o código pode ser colocado para comprar as ações. No entanto, antes e depois desse código, o método chama métodos na classe DemoEvents. Se o cliente não tem um procedimento de callback definido usando o método SetCallBack, então as chamadas aos métodos DemoEvents não fazem nada. No entanto, se houver um objeto de callback, então esses métodos serão chamados no cliente.

```foxpro
CLEAR ALL
IF PROGRAM() != "IDEMO"
   ?"this file MUST BE NAMED 'idemo.prg'"
   RETURN
ENDIF
IF .t.
   IF FILE("idemo.dll")
      DECLARE integer DllUnregisterServer IN idemo.dll
      DllUnregisterServer()
      CLEAR DLLS
   ENDIF
   BUILD PROJECT idemo FROM idemo
   BUILD DLL idemo from idemo recomp
endif
clear
oCallback = NEWOBJECT("cCallback")    && the event callback
ostock=newOBJECT("idemo.idemo")       && the business COM obj
ostock.setcallback(oCallBack)         && like BindEvents
?ostock.BuyStock("MSFT",10000 )       && invoke a method
ostock.setcallback(.null.)            && like UnBindEvents
?ostock.BuyStock("MSFT",20000 )       && this one doesn't fire events
*This is the actual implementation of the event interface
DEFINE CLASS cCallback as session
   implements iDemoEvents in idemo.dll
   procedure iDemoEvents_BeforeBuyStock(cStock as String, qty AS Number)
      ?program(),cstock,qty
   procedure iDemoEvents_AfterBuyStock(cStock as String, qty AS Number)
      ?program(),cstock,qty
enddefine
*the rest of this file is used in the COM server
DEFINE CLASS idemo as session olepublic
   oc = .null.
   PROCEDURE init
      this.SetCallBack(.null.)    && set callback to default
   PROCEDURE setcallback(oC as Variant)
      IF ISNULL(oc)
         && dummy instance that does nothing: virtual function
         this.oc = NEWOBJECT("DemoEvents")
      else
         IF VARTYPE(oc) != 'O'
            COMRETURNERROR(PROGRAM(),"callback must be obj")
         ENDIF
         this.oc = GETINTERFACE(oC,"iDemoEvents","idemo.idemo")
      endif
   procedure MyDoCmd(cCmd as String) as Variant
      &cCmd
   procedure MyEval(cExpr as String) as Variant
      return &cExpr
   procedure BuyStock(cStock as String, qty AS Number) as Boolean
      this.oc.BeforeBuyStock(cStock, qty)
      *here we buy the stock
      this.oc.AfterBuyStock(cStock, qty)
   FUNCTION Error(nError, cMethod, nLine)
      COMreturnerror(cMethod+'  err#='+str(nError,5)+'  line='+;
         str(nline,6)+' '+message(),_VFP.ServerName)
      && this line is never executed
enddefine
*Just an interface definition that should be implemented by outside callers
DEFINE CLASS DemoEvents as session olepublic
   procedure BeforeBuyStock(cStock as String, qty AS Number)
   procedure AfterBuyStock(cStock as String, qty AS Number)
enddefine
```

O COM permite que objetos interajam uns com os outros de várias formas. Cada adição de novas capacidades COM ao Visual FoxPro, incluindo funcionalidade simples de cliente COM, implementação de interface e suporte a servidor e cliente com early binding, forneceu muitas novas capacidades.
