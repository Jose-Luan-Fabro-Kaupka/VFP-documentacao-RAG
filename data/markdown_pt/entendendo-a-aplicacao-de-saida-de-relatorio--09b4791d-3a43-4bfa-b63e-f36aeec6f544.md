# Entendendo a aplicação de saída de relatório

A aplicação de saída de relatório padrão (ReportOutput.app) cumpre as responsabilidades padrão de uma aplicação designada na variável _REPORTOUTPUT.
 - Aceita dois parâmetros, esperando um valor numérico como primeiro parâmetro.
- Armazena uma referência de objeto para uma instância de uma classe derivada de ReportListener na variável recebida como segundo parâmetro.
- A classe cuja instância é fornecida é determinada pelo valor do primeiro parâmetro.
- Se conseguir obter uma referência de objeto para uma classe apropriada, atribui o valor do primeiro parâmetro à propriedade OutputType do objeto.

> **Observação:** Para obter todas as informações sobre os requisitos de uma aplicação de saída de relatório, consulte Variável de sistema _REPORTOUTPUT.

Este tópico aborda detalhes da implementação desses requisitos pela aplicação padrão. Também descreve algumas funcionalidades adicionais fornecidas por ela.

# Coleção de referências ReportListener de ReportOutput.app

Você pode atribuir explicitamente uma referência de objeto ReportListener a uma variável chamando a aplicação de saída de relatório com a seguinte sintaxe:

```foxpro
LOCAL loRef
do (_REPORTOUTPUT) with <N>, loRef
IF ISNULL(loRef)
   * the Report Output Application did
   * not recognize the value <N>
ELSE
   ? loref.outputtype
   ? loref.class
ENDIF
```

Porém, em muitos casos, ReportOutput.app fornece uma referência de objeto ReportListener sem que você a atribua explicitamente a uma variável. Isso ocorre se SET REPORTBEHAVIOR estiver definido como `90` ou se você usar a cláusula OBJECT TYPE <N> no comando REPORT FORM ou LABEL.

ReportOutput.app mantém uma variável pública, _oReportOutput, derivada da classe Collection. Nessa coleção, armazena referências aos objetos derivados de ReportListener que forneceu. A coleção dá escopo global às referências ReportListener, permitindo que sejam reutilizadas com êxito por vários relatórios, independentemente de como ou onde a referência seja solicitada.

Fornecer um escopo consistente para ReportListener, usando a coleção de referências de ReportOutput.app ou estratégia semelhante, é necessário para encadear vários relatórios em um único resultado de saída. A coleção também oferece um mecanismo conveniente para recuperar essas referências antes e depois da execução do relatório.

Você pode recuperar a referência da coleção usando como chave o valor de cadeia de caracteres do OutputType apropriado:

```foxpro
#DEFINE PRINT_MODE 0
REPORT FORM ? OBJECT TYPE PRINT_MODE
LOCAL loRef
loRef = _oReportOutput[TRANSFORM(PRINT_MODE)]
? loRef.OutputType  && will be 0
? loRef.PageTotal && will be the total of pages
                  && from the last print run
```

Para obter mais informações, consulte Como: usar a coleção de referências da aplicação de saída de relatório.

> **Importante:** ReportOutput.app reserva-se o direito de usar valores de chave adicionais nessa coleção para outras finalidades além de referências de objetos ReportListener. Por exemplo, se você designar uma tabela de Registro de Saída de Relatório personalizada, ele armazenará o nome da tabela na coleção. Para obter mais informações, consulte Como: especificar uma tabela alternativa de Registro de Saída de Relatório.

# Parâmetros estendidos de ReportOutput.app

ReportOutput.app amplia o uso dos dois parâmetros obrigatórios de _REPORTOUTPUT, fornece um comportamento padrão se o segundo parâmetro não for incluído e adiciona um terceiro parâmetro opcional. A sintaxe apropriada é:

```foxpro
DO ReportOutput.app WITH ;
   nListenerType [,eListenerReference [,eUnload]]
```

Esta seção descreve o tratamento de cada parâmetro por ReportOutput.app.

### Primeiro parâmetro: nListenerType

Ao avaliar nListenerType, ReportOutput.App aceita todos os números maiores ou iguais a `-1`, o valor padrão da propriedade ListenerType de ReportListener, como instruções para fornecer uma referência ReportListener do tipo apropriado.

> **Observação:** Se nListenerType for um número, mas não um inteiro, ReportOutput.app aceitará o valor, porém usará somente sua parte inteira como o tipo solicitado.

Se nListenerType for `-1`, ele fornecerá uma referência a um objeto instanciado da classe base ReportListener. Se for maior que `-1`, ReportOutput.app iniciará o seguinte processo de avaliação para determinar qual classe derivada de ReportListener deve fornecer a referência:
 - Primeiro, ReportOutput.app verifica se existe uma referência em cache a um objeto anteriormente fornecido para esse valor. Se encontrar, reutiliza-a.
- Se não houver referência em cache, ReportOutput.app verifica sua tabela de registro em busca de instruções do usuário correspondentes ao valor. A tabela é descrita mais adiante neste tópico.
- Se não houver instruções do usuário, usa os padrões internos da tabela a seguir.

| Valor de nListenerType | Classe padrão que fornece a referência ReportListener |
| --- | --- |
| 0 | Classe básica ReportListener User Feedback |
| 1 | Classe básica ReportListener User Feedback |
| 2 | Classe base ReportListener |
| 3 | Classe base ReportListener |
| 4 | Classe básica ReportListener XML |
| 5 | Classe básica ReportListener HTML |
| 999 | Classe básica ReportListener Debug |

> **Observação:** Na tabela, observe que uma única classe ReportListener pode tratar vários valores de nListenerType. ReportOutput.app atribui o valor recebido de nListenerType à propriedade OutputType do objeto. Essa atribuição faz parte dos requisitos especificados para qualquer aplicação de saída de relatório. Se o objeto for uma instância de classe derivada de ReportListener, ReportOutput.app espera que ele decida se deve reatribuir sua própria propriedade ListenerType com base em OutputType ou manter os valores separados. Se for uma instância da classe base ReportListener, ReportOutput.app também atribui nListenerType à propriedade ListenerType. Para obter mais informações, consulte Propriedade OutputType (Visual FoxPro) e Propriedade ListenerType.

ReportOutput.app reserva todos os valores de nListenerType menores que `-1` para expor funcionalidades adicionais além de sua responsabilidade especificada de fornecer referências ReportListener. Dois desses valores, -100 e -200, são abordados mais adiante neste tópico.

### Segundo parâmetro: eListenerReference

ReportOutput.app trata eListenerReference como opcional. Se não for recebido, simplesmente armazena em cache, na coleção de referências, uma referência a uma instância da classe ReportListener apropriada. Isso permite configurar várias referências antes de precisar delas para relatórios.

Se receber eListenerReference, ReportOutput.app aceitará uma variável declarada, como no exemplo da seção anterior, ou uma cadeia de caracteres que represente a variável. Se a variável representada pela cadeia ainda não existir, ReportOutput.app a inicializará como PUBLIC.

Você também pode usar uma cadeia de caracteres em eListenerReference para atribuir um ReportListener a um membro de objeto. Por exemplo:

```foxpro
#DEFINE PREVIEW_MODE 1
Ox = CREATEOBJECT("custom")
Ox.addProperty("myReportListener")
DO (_REPORTOUTPUT) WITH PREVIEW_MODE, "ox.myReportListener"
REPORT FORM ? OBJECT ox.MyReportListener
? ox.myReportListener.Name
```

Se o membro não existir, mas ReportOutput.app puder verificar que o objeto existe, o membro será criado. Ele consegue percorrer hierarquias de contenção de objetos para essa finalidade. Por exemplo:

```foxpro
#DEFINE PREVIEW_MODE 1
Ox = CREATEOBJECT("form")
Ox.addobject("myChildObject","custom")
DO (_REPORTOUTPUT) WITH PREVIEW_MODE, "ox.myChildObject.RL"
REPORT FORM ? OBJECT ox.myChildObject.RL
? ox.myChildObject.RL.PageTotal
```

### Terceiro parâmetro: eUnload

Você pode liberar explicitamente uma referência ReportListener da coleção de ReportOutput.app:

```foxpro
#DEFINE PRINT_MODE 0
_oReportOutput.Remove[TRANSFORM(PRINT_MODE))
```

Contudo, ReportOutput.app fornece um terceiro parâmetro para que você peça à aplicação que gerencie essa referência sem acessar diretamente a coleção. O parâmetro permite liberar explicitamente a referência ou liberá-la e receber imediatamente uma nova instância, como no exemplo:

```foxpro
#DEFINE PRINT_MODE 0
#DEFINE OUTPUTAPP_LOADTYPE_RELOAD 2
   DO (_reportoutput) WITH ;
      PRINT_MODE , ox, OUTPUTAPP_LOADTYPE_RELOAD
```

Estes são os valores reconhecidos para eUnload.

| Valor do parâmetro eUnload | Uso |
| --- | --- |
| Não passado, Logical False (.F.) ou passado com tipo diferente de lógico ou numérico. | Ignorado. ReportOutput.app fornece o comportamento padrão: carrega um ReportListener ou executa outra atividade conforme nListenerType. |
| Logical True (.T.) ou valor numérico 1. | ReportOutput.app não fornece uma referência de objeto ReportListener. Verifica um objeto ReportListener usando uma chave determinada por nListenerType e o remove da coleção se encontrado. |
| Todos os valores numéricos maiores que 1. | ReportOutput.app remove da coleção uma referência de objeto ReportListener, se encontrada, e carrega novamente a referência apropriada. Armazena-a na variável indicada em eListenerReference. |

# Tabela de registro ReportListener de ReportOutput.app

ReportOutput.app fornece referências de objetos ReportListener padrão de acordo com a tabela de valores nListenerType e nomes de classes da seção anterior. Você pode usar uma tabela de registro para substituir essas configurações.

ReportOutput.app utiliza a mesma estrutura de tabela de configuração ou registro usada pelas classes básicas ReportListener. O código a seguir mostra a estrutura básica. Você pode adicionar campos de qualquer tipo, e a ordem não é significativa para os componentes da aplicação de saída nem para as classes básicas.

```foxpro
CREATE TABLE (CONFIG_TABLE_NAME) ;
   (objtype i, ;
    objcode i, ;
    objname v(60), ;
    objvalue v(60), ;
    objinfo m)
```

Tanto ReportOutput.app quanto as classes básicas ReportListener oferecem recursos para criar a tabela. Para obter mais informações sobre como criá-la e designá-la como tabela de registro da aplicação, consulte Como: especificar uma tabela alternativa de Registro de Saída de Relatório.

> **Observação:** ReportOutput.app e as classes básicas ReportListener usam essa estrutura de maneiras diferentes e exigem índices diferentes. Porém, não importa qual componente crie a tabela nem se você a criar vazia, como no exemplo acima. Cada componente criará os registros e índices necessários ao ser direcionado à tabela.

ReportOutput.app reserva o intervalo `100-999` para valores do campo Objtype na tabela de configuração. Usa Objtype igual a `100` para representar registros de classes ReportListener. A tabela a seguir mostra o uso desses registros.

| Campo | Uso | Observações |
| --- | --- | --- |
| OBJTYPE | 100 | O valor 100 identifica um registro de ReportListener. |
| OBJCODE | nListenerType | Os valores deste campo são comparados ao primeiro parâmetro fornecido a ReportOutput.app. |
| OBJNAME | Classe a instanciar | O nome pode ser ReportListener (a classe base). |
| OBJVALUE | Biblioteca de classes (.vcx) ou arquivo de procedimento (.prg) que contém a definição da classe. | Pode ficar em branco se o nome da classe for ReportListener. |
| OBJINFO | Módulo/aplicação que contém a biblioteca. | Pode ficar em branco se a biblioteca ou o arquivo de procedimento estiver vinculado à aplicação. |

ReportOutput.app especifica Objtype igual a `110` para armazenar outras configurações para uso próprio. Usa registros com Objtype `110` e Objcode `1` para filtrar registros ReportListener com base em critérios especificados pelo usuário. Registros com Objtype `110` e outros valores de Objcode são reservados para outros usos de configuração, mas não são usados atualmente.

A tabela a seguir descreve o uso dos campos para registros de filtro.

| Campo | Uso | Observações |
| --- | --- | --- |
| OBJTYPE | 110 | O valor 110 identifica um registro de configuração de ReportOutput.app. |
| OBJCODE | 1 | Para registros com Objtype 110, o valor 1 identifica um registro de filtro. |
| OBJNAME | não usado | Os registros de filtro ignoram este campo. |
| OBJVALUE | não usado | Os registros de filtro ignoram este campo. |
| OBJINFO | Expressão de filtro | A expressão colocada neste campo é incluída em LOCATE ao pesquisar a tabela de registro por uma classe apropriada para determinado nListenerType. O comando LOCATE é construído assim: #DEFINE OUTPUTAPP_OBJTYPE_LISTENER 100 LOCATE FOR ObjType = ; OUTPUTAPP_OBJTYPE_LISTENER AND ; (ObjCode = iType) ; &cFilter ; AND (NOT DELETED()) |

Para obter mais informações, consulte Como: registrar ReportListeners e OutputTypes personalizados na tabela de Registro de Saída de Relatório.

# Valores de retorno de ReportOutput.app

Uma aplicação de saída de relatório deve ser modal, pois precisa retornar um valor ao mecanismo de relatório do Visual FoxPro durante o processamento de um comando REPORT FORM ou LABEL. O Visual FoxPro recebe esse valor por eListenerReference, passado por referência; o mecanismo nativo não reconhece um valor retornado por ReportOutput.app.

Porém, ReportOutput.app fornece um valor de retorno se for chamado como função, representando o sucesso ou a falha da tarefa indicada por nListenerType:

```foxpro
? ReportOutput(5, "oRL")
* returns .T.
DISPLAY MEMO LIKE oRL
* Shows that the call above
* declares the variable oRL PUBLIC if
* it is not already in scope,
* because it was passed as a string
* stores a reference to the HTMLListener
* Foundation class in this variable.
? ReportOutput(25,"oRlx")
* returns .F.
DISPLAY MEMO LIKE oRLx
* Shows that the call above does
* not declare the variable oRLx
```

# Ajustes de ReportOutput.app em tempo de compilação

O código-fonte de ReportOutput.app está disponível em um arquivo zip na pasta XSource do diretório \Tools do Visual FoxPro. Para obter mais informações, consulte Pasta XSource.

Você pode incluir o código-fonte de ReportOutput.app em suas aplicações. Para obter mais informações, consulte Incluindo arquivos de relatório para distribuição. Ao fazer isso, pode editar as constantes definidas da saída de relatório, localizadas no arquivo de cabeçalho ReportOutput.h, para ajustar o comportamento dos relatórios.

A tabela abaixo apresenta exemplos de itens disponíveis no arquivo de cabeçalho para ajuste.

| Constante #DEFINE | Valor padrão | Edite esta configuração para alterar: |
| --- | --- | --- |
| OUTPUTAPP_INTERNALDBF | "_ReportOutputConfig" | Nome da tabela de registro interna. |
| OUTPUTAPP_EXTERNALDBF | "OutputConfig" | Nome padrão da tabela de registro em disco. |
| OUTPUTAPP_REFVAR | _oReportOutput | Nome da variável pública da coleção de referências. |
| OUTPUTAPP_BASELISTENER_CLASSLIB | "Listener.VCX" | Biblioteca de classes que contém as classes ReportListener padrão. |
| OUTPUTAPP_CLASS_PRINTLISTENER | "UpdateListener" | Nome da classe usada por padrão para tratar o valor 0 de eListenerType (impressão). |
