# Extensões Report XML MemberData

O Visual FoxPro 9.0 fornece atributos de metadados estendidos para membros de classe no Class Designer usando XML em um formato de documento especificado pelo VFP MemberData Schema. Embora o Sistema de Relatórios do Visual FoxPro não compartilhe o Class Designer, ele compartilha o esquema MemberData para fins semelhantes de extensibilidade. Usando extensões MemberData com relatórios, você pode:
 - Especificar instruções personalizadas em tempo de design para elementos individuais de layout de relatório, para uso por meio de ganchos de evento expostos pelos Report and Label Designers.
- Fornecer instruções dinâmicas para elementos individuais de layout de relatório que podem ser executadas por um objeto derivado de ReportListener em tempo de execução.

Este tópico descreve os componentes do esquema MemberData usados para relatórios e fornece exemplos usando documentos XML MemberData ao projetar e executar relatórios.

# Design do documento Report XML MemberData

O Report MemberData, como o Class Design MemberData, contém uma sequência de elementos sob um nó raiz `VFPData`. Para uma listagem completa do esquema MemberData compartilhado (.xsd), consulte MemberData Extensibility. A tabela a seguir descreve os atributos especificados para uso em relatórios.

> **Observação:** O esquema permite que os usuários adicionem atributos não explicitamente especificados. Quaisquer ferramentas que você criar para analisar ou criar o XML devem permitir a possibilidade de atributos adicionais desconhecidos presentes para um ou mais elementos na sequência. As ferramentas também devem lidar com a possibilidade de atributos não marcados como obrigatórios pelo esquema estarem ausentes para um ou mais elementos. O exemplo em tempo de execução neste tópico fornece um modelo para este comportamento.

A coluna Style dos arquivos de definição de relatório e etiqueta (tabelas .frx e .lbx) é reservada para armazenamento de Report MemberData. Para obter mais informações sobre a estrutura de relatórios e etiquetas, consulte Understanding and Extending Report Structure.

Você pode usar o Report Builder Application padrão para inserir documentos XML da estrutura necessária em registros de relatório e etiqueta para elementos individuais de layout. Você pode examinar os resultados para ver documentos de exemplo de Report XML MemberData. Para obter mais informações, consulte How to: Assign Structured Metadata to Report Controls.

| Nome do nó | Tipo de nó | Nó pai | Observações e uso recomendado |
| --- | --- | --- | --- |
| VFPData | Element (required) | None | Nó raiz do documento MemberData. |
| reportdata | Element (required) | VFPData | Um elemento contendo metadados para um registro específico da tabela de definição de relatório ou etiqueta. |
| name | Attribute (required) | reportdata | Compartilhado com Class Designer MemberData. Pode ser usado, com o atributo type, para filtrar e gerenciar registros MemberData de relatório em um armazenamento global comum, como FoxCode.dbf. Para obter mais informações, consulte _FOXCODE System Variable. Observação Embora este atributo seja obrigatório, um valor vazio é permitido. |
| type | attribute | reportdata | Compartilhado com Class Designer MemberData. Pode ser usado, com o atributo name, para filtrar e gerenciar registros em um armazenamento global. Observação Quando o Report Builder Application padrão cria Report MemberData, ele coloca o valor " R " no atributo type, para distinguir esses registros de outros tipos de MemberData. |
| script | attribute | reportdata | Compartilhado com Class Designer MemberData e especificado, de forma semelhante ao seu uso no design de classe, para uso em extensões de relatório em tempo de design. |
| class | attribute | reportdata | Especificado para conter o nome de uma classe a ser usada para qualquer um dos seguintes: Um modelo em tempo de design, do qual extensões do Report Builder podem aplicar atributos. Extensões do Report Builder que adotam esta abordagem devem documentar os atributos que transferem da classe modelo para o elemento de relatório ou etiqueta. Uma classe auxiliar para projetar o elemento de relatório ou etiqueta. Extensões do Report Builder que adotam esta abordagem devem especificar uma interface obrigatória para essas classes e invocar os métodos especificados durante eventos de design. A classe auxiliar tem acesso à sessão de dados privada do Report Builder e à cópia da tabela de relatório ou etiqueta. Uma classe auxiliar associada ao elemento de script em tempo de design. Extensões do Report Builder que adotam esta abordagem podem enviar o script à classe auxiliar para processamento, ou podem executar o script diretamente, enviando uma referência ao objeto auxiliar como parâmetro ao script. Uma classe modelo instanciada em tempo de execução por um ReportListener. O ReportListener pode transferir atributos dinamicamente da classe modelo, documentando o conjunto de atributos a serem transferidos. Esta abordagem permite que todos os elementos de layout, em todos os relatórios, compartilhem alterações que você faz na classe modelo, emulando herança de classe. Uma classe auxiliar instanciada por um ReportListener para auxiliar o processamento em tempo de execução de um elemento específico de layout de relatório e associada ao processamento de script em tempo de execução. |
| classlib | attribute | reportdata | Especificado para conter o nome da biblioteca de classes ou arquivo de procedimento (.vcx ou .prg) do qual a classe auxiliar ou modelo será instanciada. Extensões de relatório devem assumir uma extensão de arquivo vcx se nenhuma for incluída. Observe que a biblioteca de classes ou arquivo de procedimento deve estar acessível à extensão. Para um resumo de como o Visual FoxPro encontra definições de classe, consulte a seção Remarks do SET CLASSLIB Command. |
| declass | attribute | reportdata | Especificado para conter o nome de uma classe DataEnvironment em uma biblioteca de classes visual (.vcx) a ser usada como modelo para registros Cursor e Relation neste relatório ou etiqueta na implementação do evento Load DataEnvironment do Report Builder Application padrão. O Report Builder Application também grava código vinculando uma instância desta classe aos eventos DataEnvironment em tempo de execução do relatório. Para obter mais informações, consulte How to: Load Data Environments for Reports. Observação O Report Builder Application usa o registro de cabeçalho (primeiro registro) na tabela de definição de relatório ou etiqueta para armazenar informações da classe DataEnvironment, porque essas informações são globais ao relatório. É uma boa prática seguir esta convenção, armazenando dados globais no documento XML MemberData do primeiro registro. No exemplo em tempo de execução incluído neste tópico, uma extensão de relatório em tempo de execução opta por verificar este registro para script apropriado aos eventos BeforeReport e AfterReport. Esses eventos são de natureza global e não associados a nenhum elemento ou registro específico de layout de relatório ou etiqueta. |
| declasslib | attribute | reportdata | Especificado para conter o nome do arquivo da biblioteca de classes visual ou arquivo de procedimento do qual a classe DataEnvironment deve ser instanciada, quando o atributo declass contém o nome de uma classe DataEnvironment, conforme descrito acima. Como alternativa, o Report Builder Application padrão oferece aos usuários a capacidade de associar registros DataEnvironment de outro relatório ou etiqueta (arquivo .frx ou .lbx) ao relatório. Quando os usuários fazem esta escolha, o Report Builder Application armazena o nome do relatório ou etiqueta usado como modelo DataEnvironment neste atributo. |
| execute | attribute | reportdata | Especificado para script usado em extensões de relatório em tempo de execução. |
| execwhen | attribute | reportdata | Especificado para condições a serem avaliadas por extensões de relatório em tempo de execução para determinar se e quando o conteúdo do script do atributo execute deve ser executado. Dica Como mostrado no código de exemplo neste tópico, condições execwhen podem ser avaliadas de forma flexível; diferentemente das condições Print When em um relatório, elas não precisam avaliar diretamente para um resultado lógico. |

# Report XML MemberData em tempo de design

Como descrito na tabela acima, o Report Builder Application usa os atributos `declass` e `declasslib` do Report XML MemberData armazenado no registro de cabeçalho do arquivo de definição de relatório ou etiqueta. Por padrão, ele não usa nenhum outro MemberData que você armazena no relatório ou etiqueta. No entanto, você pode facilmente aproveitar a arquitetura de extensão do Report Builder Application para ler e usar o XML.

A classe a seguir implementa o mecanismo de manipulador de saída do Report Builder Application. Quando registrada com o Report Builder Application, esta classe recebe informações sobre o evento do Report Designer que ocorreu e se o Report Builder Application fez alterações no elemento de layout de relatório atual. Se o elemento de layout contém texto e ocorreram alterações, o objeto manipulador verifica uma classe modelo no XML MemberData. Se uma existir e tiver uma propriedade com o nome `Fontname`, o manipulador pergunta ao usuário se a fonte da classe modelo deve ser aplicada ao elemento de layout de relatório.

> **Observação:** Para obter mais informações sobre o registro de manipuladores e filtros personalizados na tabela de registro do Report Builder Application e a implementação da API necessária, consulte Report Builder Event Handler Registry Table. O uso do mecanismo de manipulador de saída é conveniente, mas ilustra apenas uma fração do potencial que você tem para interações em tempo de design usando ganchos de evento do Report Designer e Report XML MemberData.
```foxpro
DEFINE CLASS TemplateObjectHandler AS Custom
* register this as an exit handler
PROCEDURE Execute( oEvent )
  IF BITTEST(oEvent.ReturnFlags,1) AND ;
    INLIST(FRX.ObjType,5,8) AND NOT EMPTY(FRX.STYLE)
    LOCAL lcAlias, loX
    lcAlias = "T"+SYS(2015)
    TRY
      XMLTOCURSOR(FRX.Style,lcAlias)
      SELECT (lcAlias)
      IF NOT EMPTY(Class) AND ;
        MESSAGEBOX("(Re)apply Font from Template Object?",4) = 6
        IF EMPTY(ClassLib)
          loX = CREATEOBJECT(ALLTRIM(Class))
        ELSE
          loX = NEWOBJECT(ALLTRIM(Class),ALLTRIM(Classlib))
        ENDIF
        IF VARTYPE(loX) = "O" AND ;
          PEMSTATUS(loX,"Fontname",5)
          REPLACE Fontface WITH loX.Fontname IN FRX
        ELSE
          MESSAGEBOX("Could not apply template.")
        ENDIF
      ENDIF
    CATCH WHEN .T.
      * not valid XML
      * or other error occurred
    FINALLY
      IF USED(lcAlias)
        USE IN (lcAlias)
      ENDIF
      SELECT FRX
    ENDTRY
  ENDIF
  RETURN .T.
ENDPROC
ENDDEFINE
```

# Report XML MemberData em tempo de execução

O exemplo a seguir aproveita a arquitetura de processamento de efeitos em tempo de execução sugerida em Considerations for Creating New Report Output Types.

A superclasse no exemplo, FXMemberData, é uma classe derivada personalizada que implementa a API FX simples e adequada para ser chamada por uma instância da classe FXListener, conforme descrito nesse tópico. FXMemberData é um objeto de efeito com a capacidade de ler e analisar Report XML MemberData, colocando os resultados em um cursor indexado em uma coluna, `FRXRecno`, associando cada registro aos elementos da tabela de definição de relatório ou etiqueta original.

FXMemberData executa seu serviço no início da execução do relatório. Para o restante da execução do relatório, se o valor de seu membro `ApplyMemberData` estiver definido como True (`.T.`), FXMemberData posiciona o ponteiro de registro de seu cursor adequadamente para o evento de relatório atual, mas não executa nenhuma outra ação.

Ter este tipo de objeto evita a necessidade de cada ReportListener ou objeto de efeito que requer acesso aos metadados estruturados analisar o documento XML separadamente. Com os metadados facilmente acessíveis a eles neste cursor comum, cada objeto que usa os dados pode SELECT as colunas de interesse em um cursor privado separado, com colunas adicionais para alterações dinâmicas que possam querer fazer em tempo de execução para seus próprios propósitos.

> **Observação:** Para encontrar o cursor relevante criado por FXMemberData ou um provedor semelhante, outros objetos podem investigar o FRXDataSession para encontrar um cursor da estrutura correta, analisando o XML eles mesmos se não conseguirem encontrar um. Alternativamente, eles podem observar uma convenção simples, mostrada aqui como MemberDataAlias, de uma propriedade ReportListener contendo o alias apropriado. Observe que FXMemberData usa o método AddProperty para anexar esta propriedade a qualquer ReportListener.

Uma segunda classe derivada de FXMemberData, FXProcessMemberDataScript, mostra algumas estratégias para usar os atributos `Execute` e `ExecWhen` do Report XML MemberData. Esta classe avalia `ExecWhen` para determinar quando invocar o script em `Execute`. Se determinar que deve processar o script, verifica se uma linha `PARAMETERS` ou `LPARAMETERS` é a primeira linha no script. Se não, adiciona uma instrução `LPARAMETERS` ao início do script, para permitir passar todos os parâmetros recebidos pelo método ApplyFX da API da classe de efeito, que efetivamente permite que objetos de efeito manipulem e ajustem todos os parâmetros dos eventos de relatório. A instrução `LPARAMETERS` que cria também inclui uma referência ao objeto FX como primeiro parâmetro, antes de todos os parâmetros recebidos no método ApplyFx. Após fazer esses ajustes, usa a função EXECSCRIPT( ) para processar o script, passando esses parâmetros ao script.
```foxpro
* to use this class, follow the pattern
* illustrated for use of the FXListener class,
* as follows :
LOCAL loPrimaryRL
* the following line assumes availability of
* the class definition for FXListener listed in
* code example in the topic
* Considerations for Creating New Report Output Types:
loPrimaryRL = CREATEOBJECT("FXListener")
* add successor ReportListeners if desired
loPrimaryRL.FXs.Add("FXProcessMemberDataScript")
* or use its superclass if you don't
* need script processing but want to
* parse the XML MemberData:
* loPrimaryRL.FXs.Add("FXMemberData")
* add other effect objects to the collection
* as required
* Effect class suitable for calling
* by FXListener example class
* Because it works with unknown attributes
* and unknown memberdata requirements,
* FXMemberData requires that the values you use
* for all custom attributes be evaluated by
* XMLTOCURSOR() as a string.  Values
* that do not evaluate as a string will error.
* This behavior makes it possible
* for you or other users to use multiple data types
* for the same custom attributes on different FRX
* records.
* When you use a non-string value, you should
* re-datatype it as appropriate for use in your code.
* (Use EVAL() or otherwise translate the data
* type as needed.)
DEFINE CLASS FXMemberData AS Custom
   MemberDataAlias = ""
   ApplyMemberData = .F.
   PROCEDURE ApplyFX(toListener, tcProgram,;
                     tP1, tP2, tP3, tP4, tP5, tP6, ;
                     tP7, tP8, tP9, tP10, tP11, tP12)
      LOCAL liSession, liSelect, llInBeforeReport
      llInBeforeReport = (ATC("BeforeReport", tcProgram) > 0)
      IF (llInBeforeReport OR THIS.ApplyMemberData) AND ;
         (TYPE("toListener.FRXDataSession") = "N" AND ;
              toListener.FRXDataSession > -1)
         liSession = SET("DATASESSION")
         SET DATASESSION TO (toListener.FRXDataSession)
         liSelect = SELECT()
         IF llInBeforeReport
             * pull the memberdata out of the FRX for later use
             THIS.PullMemberData(toListener)
         ENDIF
         IF THIS.ApplyMemberData
            * this FX object
            * might apply the results of
            * the memberdata pull
            * or it might just make them
            * available to other FX objects
            * after the initial read
            SELECT (THIS.MemberDataAlias)
            THIS.UseMemberData(;
                 toListener, tcProgram,;
                 @tP1, @tP2, @tP3, @tP4, @tP5, @tP6, ;
                 @tP7, @tP8, @tP9, @tP10, @tP11, @tP12)
         ENDIF
         SELECT (liSelect)
         SET DATASESSION TO (liSession)
      ENDIF
   ENDPROC
   PROTECTED PROCEDURE UseMemberData(toListener, tcProgram,;
                        tP1, tP2, tP3, tP4, tP5, tP6, ;
                        tP7, tP8, tP9, tP10, tP11, tP12)
       LOCAL lnFRXRecno
       lnFRXRecno = -1
       DO CASE
       CASE ATC(".Before",tcProgram) > 0 OR ATC(".After",tcProgram) > 0
          DO CASE
          CASE RAT("REPORT",UPPER(tcProgram)) = (LEN(tcProgram)-5)
             lnFRXRecNo = 1
             * pull global data
          CASE VARTYPE(tP2) = "N" && Band events
             lnFRXRecNo = tP2
          OTHERWISE
             * called inappropriately
          ENDCASE
       CASE VARTYPE(tP1) = "N"  && Render, other events
          lnFRXRecno = tP1
       OTHERWISE
          * called inappropriately
       ENDCASE
       IF NOT SEEK(lnFRXRecno,THIS.MemberDataAlias,"FRXRecno")
          lnFRXRecno = -1
       ENDIF
       RETURN (lnFRXRecno # -1)
   ENDPROC
   PROTECTED PROCEDURE PullMemberData(toListener)
      LOCAL lcAlias, lcTempAlias, lcAttributes, liIndex, loAttr
      IF TYPE("toListener.MemberDataAlias") = "C" AND ;
         NOT EMPTY(toListener.MemberDataAlias)
         lcAlias = toListener.MemberDataAlias
      ELSE
         lcAlias = "M"+SYS(2015)
         toListener.AddProperty("MemberDataAlias", lcAlias)
         * "publish" this for others in case they want it
      ENDIF
      THIS.MemberDataAlias = lcAlias
      lcTempAlias = "T" + SYS(2015)
      CREATE CURSOR (lcAlias)  ;
                    (FRXRecno I, Name M, Type M, ;
                     ExecWhen M, Execute M, Class M, ;
                     ClassLib M, DEClass M, DEClassLib M)
      * we're going to take every attribute, whether
      * we understand the column or not,
      * but we'll start off with the
      * core set minus script since script attribute is
      * officially reserved for design-time use
      lcAttributes = ;
          "|FRXRecno|ExecWhen|Execute|Class|" + ;
          "Classlib|Name|Type|DEClass|DEClassLib|"
      SELECT FRX
      SCAN FOR NOT EMPTY(Style)
          TRY
             XMLTOCURSOR(Style,lcTempAlias)
          CATCH WHEN .T.
             * not valid XML
          FINALLY
             IF USED(lcTempAlias)
                IF RECCOUNT(lcTempAlias) > 0
                   SELECT (lcTempAlias)
                   FOR liIndex = 1 TO FCOUNT()
                       IF ATC("|"+FIELD(liIndex)+"|",lcAttributes) = 0
                          ALTER TABLE (lcAlias) ;
                           ADD COLUMN (FIELD(liIndex)) M
                          lcAttributes = lcAttributes + ;
                           FIELD(liIndex) + "|"
                       ENDIF
                   ENDFOR
                   SCATTER MEMO NAME loAttr
                   INSERT INTO (lcAlias) FROM NAME loAttr
                   REPLACE FRXRecno WITH RECNO("FRX") IN (lcAlias)
                ENDIF
                USE IN (lcTempAlias)
             ENDIF
          ENDTRY
          loAttr = NULL
       ENDSCAN
       SELECT (lcAlias)
       INDEX ON FRXRecno TAG FRXRecno
   ENDPROC
ENDDEFINE
DEFINE CLASS FXProcessMemberDataScript AS FXMemberData
   ApplyMemberData = .T.
   PROTECTED PROCEDURE UseMemberData(toListener, tcProgram,;
                        tP1, tP2, tP3, tP4, tP5, tP6, ;
                        tP7, tP8, tP9, tP10, tP11, tP12)
       IF DODEFAULT(toListener, tcProgram,;
                    @tP1, @tP2, @tP3, @tP4, @tP5, @tP6, ;
                    @tP7, @tP8, @tP9, @tP10, @tP11, @tP12)

          * We are now positioned on the correct
          * record by the parent class,
          * and can take action based on the memberdata contents.
          * For example, if we're in BeforeReport,
          * we could instantiate a collection of the appropriate
          * template objects for each label or text record that has a
          * class and classlib available.
          * For each EvaluateContents or Render
          * event we can call methods of the class or
          * apply font attributes to the runtime result.
          LOCAL loMemberdata, llExecute
          SCATTER MEMO NAME loMemberdata
          IF NOT EMPTY(loMemberdata.Execute)
             IF EMPTY(loMemberdata.ExecWhen)
                llExecute = .T.
             ELSE
                DO CASE
                CASE ATC(loMemberData.ExecWhen,tcProgram) > 0
                   * simple event evaluation
                   * ExecWhen contains an event name
                   * Note that each event, via script,
                   * could potentially change the contents of
                   * ExecWhen to hold another value (the next
                   * event during which this script
                   * should be evaluated)
                   llExecute = .T.
                CASE (TYPE(loMemberdata.ExecWhen) = "L") AND ;
                   EVALUATE(loMemberdata.ExecWhen)
                   * ExecWhen contains a logical expression
                   * to be evaluated
                   llExecute = .T.
                CASE ATC(SUBSTR(tcProgram,RAT(".",tcProgram) + 1),;
                         loMemberData.ExecWhen) > 0
                   * ExecWhen contains a delimited string of events
                   llExecute = .T.
                ENDCASE
             ENDIF
             IF llExecute
                IF NOT (BETWEEN(ATC("PARAM", ;
                        ALLTRIM(CHRTRAN(loMemberData.Execute,;
                        CHR(10)+CHR(13), ;
                        SPACE(2)))),1,2))
                   * add a parameters statement; this adjustment
                   * should just happen the first time
                   * any FRX record is processed.
                   loMemberData.Execute = ;
                   "LPARAMETERS toFX, toListener, tcProgram,;"+ ;
                    CHR(13) + CHR(10) + ;
                   "tP1, tP2, tP3, tP4, tP5, tP6,"+;
                   "tP7, tP8, tP9, tP10, tP11, tP12" + ;
                    CHR(13) + CHR(10) + ;
                   loMemberData.Execute
                   REPLACE Execute WITH loMemberData.Execute
                ENDIF
                ExecScript(loMemberData.Execute,;
                    THIS, toListener, tcProgram,;
                    @tP1, @tP2, @tP3, @tP4, @tP5, @tP6, ;
                    @tP7, @tP8, @tP9, @tP10, @tP11, @tP12)
             ENDIF
          ENDIF
       ENDIF
   ENDPROC

ENDDEFINE
```

Para usar um efeito de processamento de script desta natureza, você pode adicionar o seguinte documento XML MemberData a um controle Field ou Expression no layout de relatório que contém um valor numérico. Este exemplo fornece alterações automáticas de cor para valores numéricos abaixo de 0, usando o evento EvaluateContents, e formata os números negativos com parênteses, usando o método Render.

> **Dica:** Observe que o atributo ExecWhen indica que o script deve ser processado nesses dois pontos especificando uma cadeia de caracteres delimitada (" |EvaluateContents|Render| "). Esta é uma de várias formas alternativas de avaliar ExecWhen fornecidas pela classe FXProcessMemberDataScript.
```foxpro
<VFPData>
<reportdata name="" type="R" script=""
execwhen="|EvaluateContents|Render|"
execute=
"DO CASE
 CASE ATC("Render",tcProgram) > 0
  * Render's 7th parameter is
  * cContentstoBeRendered
  * notice the conversion from Unicode to DBCS
  tP7 = VAL(STRCONV(tp7,6))
  IF tp7 < 0
     tP7 =  "("+TRANS(ABS(tp7)) + ")"
  ELSE
     tP7 = TRANS(tP7)
  ENDIF
  * convert back to Unicode for use by the native ReportListener:
  tP7 = STRCONV(tp7,5)
OTHERWISE
  * EvaluateContents' second parameter
  * is objProperties
   IF VARTYPE(tP2.value) = "N" AND ;
      tP2.value < 0
      tP2.penred = 255
      tP2.penblue = 0
      tP2.pengreen = 0
      tP2.reload = .T.
   ENDIF
ENDCASE"
class="" classlib="" declass="" declasslib=""/>
</VFPData>
```

> **Dica:** O documento XML bem formado acima mostra várias referências de caracteres escapados dentro do script; por exemplo, um caractere como < deve ser armazenado como a referência de entidade < quando faz parte do valor de um atributo ou nó de elemento em XML. Quando você cria o script usando a interface da caixa de texto Run-time Extensions do Report Builder Application, pode digitar esses caracteres normalmente, sem usar as referências de entidade. O Report Builder Application armazena o documento corretamente, escapando os caracteres conforme necessário, quando você salva o XML.

A classe a seguir é outra definição de classe seguindo a API FX. Diferentemente de FXMemberData e suas classes derivadas, FXMemberDataAware não entende XML e não lê o MemberData diretamente. Em vez disso, lê o cursor produzido por FXMemberData e entende sua estrutura. Se encontrar o cursor em seu ambiente, usa o cursor, adicionando colunas se desejado. Se o cursor não estiver disponível, fornece uma instância temporária de FXMemberData durante o método BeforeReport, para que este objeto temporário possa criar o cursor.

FXMemberDataAware é uma classe abstrata, não executando nenhum serviço durante a execução do relatório. No entanto, você pode derivar muitas classes FX de FXMemberDataAware, cada uma com um propósito especializado. Se você adicionar instâncias de cada FX à coleção de um FXListener, todas compartilham o mesmo cursor MemberData durante a execução do relatório. Elas também podem criar cursores de extensão MemberData privados relacionados ao cursor compartilhado, conforme necessário.
```foxpro
DEFINE CLASS FXMemberDataAware AS Custom
   MemberDataAlias = ""
   HasMemberData = .F.

   PROCEDURE ApplyFX(toListener, tcProgram,;
                     tP1, tP2, tP3, tP4, tP5, tP6, ;
                     tP7, tP8, tP9, tP10, tP11, tP12)

      IF ATC("BeforeReport",tcProgram) > 0
         THIS.VerifyMemberData(toListener)
      ENDIF
      IF ATC("AfterReport",tcProgram) > 0
         THIS.DetachMemberData(toListener, .T.)
      ENDIF

    ENDPROC
   PROCEDURE VerifyMemberData(toListener)
      IF toListener.FRXDataSession = -1
         RETURN .F.
      ENDIF
      LOCAL loMemberData, liSelect, liSession
      liSession = SET("DATASESSION")
      SET DATASESSION TO (toListener.FRXDataSession)
      liSelect = SELECT()
      IF (EMPTY(THIS.MemberDataAlias) OR ;
         (NOT USED(THIS.MemberDataAlias)))
         * can be supplied by the Listener
         * by leveraging a different FX object,
         * but might not be, so in this case
         * let's scarf it up with a temporary object
         IF (NOT PEMSTATUS(toListener,"MemberDataAlias",5)) OR ;
            EMPTY(toListener.MemberDataAlias)
            THIS.MemberDataAlias = "M" + SYS(2015)
            toListener.AddProperty("MemberDataAlias", ;
                        THIS.MemberDataAlias)
         ELSE
            THIS.MemberDataAlias = toListener.MemberDataAlias
         ENDIF
         IF NOT USED(THIS.MemberDataAlias)
            * could be sharing
            loMemberData = NEWOBJECT("FXMemberData")
            loMemberData.MemberDataAlias = THIS.MemberDataAlias
            loMemberData.ApplyMemberData = .F.
            loMemberData.ApplyFX(toListener, "BeforeReport")
            SET DATASESSION TO (toListener.FRXDataSession)
            IF USED(THIS.MemberDataAlias)
               * we can proceed...
               THIS.AlterMemberDataInfo()
            ENDIF
          ENDIF
       ENDIF
       THIS.HasMemberData = USED(THIS.MemberDataAlias)
       SELECT (liSelect)
       loMemberData = NULL
       SET DATASESSION TO (liSession)
       RETURN THIS.HasMemberData
    ENDPROC

    PROTECTED PROCEDURE AlterMemberDataInfo()
      * Hook for derived classes
      * to add their own columns,
      * or even to create private cursors
      * in the FRX Data session that
      * function in relation to the MemberData
      * shared cursor.
    ENDPROC

    PROCEDURE DetachMemberData(toListener, tlCloseMemberDataTable)
       IF tlCloseMemberDataTable AND toListener.FRXDataSession > -1
          LOCAL liSession
          liSession = SET("DATASESSION")
          SET DATASESSION TO (toListener.FRXDataSession)
          IF USED(THIS.MemberDataAlias)
             USE IN (THIS.MemberDataAlias)
             IF PEMSTATUS(toListener,"MemberDataAlias",5)
                toListener.MemberDataAlias = ""
             ENDIF
          ENDIF
          SET DATASESSION TO (liSession)
       ENDIF
       THIS.MemberDataAlias = ""
       THIS.HasMemberData = .F.

    ENDPROC

ENDDEFINE
```
