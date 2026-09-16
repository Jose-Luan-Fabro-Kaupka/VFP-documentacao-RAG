# Tabela de registro de manipuladores de eventos do Report Builder

O aplicativo padrão do report builder, ReportBuilder.App, contém uma tabela de consulta interna que atribui comportamento específico a eventos do construtor. A tabela define se certas combinações objeto-evento são ignoradas ou direcionadas a classes específicas para manipulação.

Para mais informações sobre as classes de manipulação de eventos, consulte o código-fonte de reportbuilder.app contido na pasta XSource sob o diretório HOME() do Visual FoxPro.

Como está integrada ao aplicativo, esta tabela de consulta não pode ser modificada diretamente. ReportBuilder.App tem um mecanismo que permite copiar a tabela para o disco para que você possa ajustar as configurações padrão e até adicionar suas próprias classes de manipulador para aumentar ou substituir as padrão.

Consulte Como: configurar o tratamento de eventos do Report Builder para mais informações.

Neste tópico:
 - A estrutura da tabela de registro de manipuladores de eventos
- Tipos de classes de manipulador
- Como o Report Builder processa eventos

# Estrutura da tabela

ReportBuilder.App usa uma tabela de consulta interna para determinar qual classe de manipulador instanciar para uma determinada combinação de EventType e objeto de relatório (conforme especificado pelo registro atualmente selecionado no cursor FRX, que pode ser um controle de relatório, uma banda de relatório ou o próprio registro de cabeçalho do relatório). A estrutura desta tabela é mostrada abaixo:

| Nome do campo | Tipo (tamanho) | Descrição |
| --- | --- | --- |
| REC_TYPE | C (1) | Especifica o tipo de classe de manipulador que o registro define. |
| HNDL_CLASS | C (35) | Especifica o nome da classe. A classe será instanciada usando uma chamada NEWOBJECT () que assume que a biblioteca de classes será encontrada em SET CLASSLIB ou SET PATH do Visual FoxPro. |
| HNDL_LIB | C (50) | Especifica a biblioteca de classes. Pode ser uma biblioteca de classes visual (.vcx) ou não visual (.prg). |
| EVENTTYPE | I | Especifica o tipo de evento. Use um valor de -1 para correspondência "curinga". Consulte Understanding Report Builder Events para uma lista de tipos de evento possíveis. |
| OBJTYPE, OBJCODE | I, I | Especifica o tipo de controle de relatório. Esses campos são equivalentes aos campos OBJTYPE e OBJCODE nas tabelas de origem do layout de relatório (.frx). Use um valor de -1 para correspondência "curinga". Consulte Estruturas de tabela de arquivos de tabela (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx) para links onde a estrutura dos arquivos de origem do layout de relatório (.frx) é documentada. |
| NATIVE | L | Indica "substituição de comportamento nativo". Para a combinação tipo de evento/objeto de relatório deste registro, o comportamento nativo do Designer deve ser permitido. |
| DEBUG | L | Indica "substituição de manipulador de depuração". Para a combinação tipo de evento/objeto de relatório deste registro, uma interface de usuário especial de "depuração" será exibida em vez da classe de manipulador especificada por HNDL_CLASS. |
| FLTR_ORDR | C (1) | Define a ordem em que os manipuladores Filter são processados. Somente para registros de REC_TYPE="F". |
| NOTES | C (50) | Este campo não é usado por ReportBuilder.App, mas é exibido no navegador da tabela de registro de manipuladores de eventos do report builder. (Para mais informações, consulte Caixa de diálogo Event Handler Registry (Report Builder) .) |

Quaisquer campos adicionais nesta tabela são ignorados pelo report builder.

# Tipos de classes de manipulador

Classes definidas na tabela de registro podem ser de vários tipos:

| Valor | Tipo | Descrição |
| --- | --- | --- |
| H | Event Handler | Indica uma classe de manipulador para uma combinação específica de evento do construtor / objeto de relatório. |
| F | Filter Handler | Indica uma classe de manipulador que será invocada para cada evento do report builder e pode impedir que o evento seja tratado pelo report builder. |
| X | Exit Handler | Indica uma classe de manipulador que será invocada após o processamento do evento, mas antes que o report builder retorne o controle ao Designer, como um processo de "limpeza". |
| G | GetExpression Wrapper | Indica uma classe que será invocada no lugar da caixa de diálogo GETEXPR nativa em qualquer caixa de diálogo do report builder. |
| E | Run-time Extension Editor | Indica uma classe que será invocada quando o botão de comando Edit settings é selecionado na guia Other da Caixa de diálogo Propriedades do controle de relatório . |
| M | Multi-select dialog tab | Indica uma classe Page Object que será automaticamente adicionada ao pageframe na Caixa de diálogo Multiple Selection (Report Builder) . |

# API do Event Handler

Classes Event Handler podem ser de qualquer classe base do Visual FoxPro, mas devem implementar a API do Event Handler. A API do Event Handler tem os seguintes atributos:
 - Um método chamado Execute que aceita um único parâmetro de referência de objeto.

O que a classe realmente faz no método Execute( oEvent ) não é especificado, embora para classes Event Handler provavelmente precisem definir os sinalizadores de retorno:

```foxpro
DEFINE CLASS MyHandler AS Custom
    PROCEDURE Execute( oEvent )
        * You can alter oEvent.returnFlags to suit
        oEvent.SetHandledByBuilder(.T. | .F. )
        oEvent.SetReloadChanges( .T. | .F. )
    ENDPROC
ENDDEFINE
```

Este método recebe uma referência a um objeto que representa o evento que ocorreu. O manipulador deve atribuir o valor ReturnFlags apropriado para indicar qual ação o designer deve tomar em seguida quando o construtor terminar e retornar o controle.

Event Handlers:
 - São identificados por um valor REC_TYPE de "H".
- Geralmente são instanciados somente para uma combinação específica de tipo de evento do designer e tipo de objeto de relatório.

Para mais informações sobre as propriedades e métodos da referência de objeto passada à classe de manipulador no método `Execute()`, consulte A classe de evento do Report Builder.

# API do Filter Handler

Classes Filter podem ser de qualquer classe base do Visual FoxPro, mas devem implementar a API do Event Handler (consulte acima) mais uma propriedade pública adicional, allowToContinue:

```foxpro
DEFINE CLASS MyFilter AS Custom
    allowToContinue = .T.
    PROCEDURE Execute( oEvent )
        * decide whether or not to process the event
        THIS.allowToContinue = .T.
        * You can optionally alter oEvent.returnFlags to suit
        oEvent.SetHandledByBuilder(.T. | .F. )
        oEvent.SetReloadChanges( .T. | .F. )
    ENDPROC
ENDDEFINE
```

Classes Filter Handler:
 - São identificadas por um valor REC_TYPE de "F".
- São instanciadas para cada evento do report builder.
- São processadas na ordem indicada pelo campo FLTR_ORDR.
- Podem impedir o processamento adicional do evento definindo sua propriedade AllowToContinue como falso ( .F. )
- Podem aplicar pré-processamento ao cursor FRX antes que o evento seja processado por uma classe Event Handler.

# Exit Handlers

Classes Exit Handler devem suportar a API do Event Handler.

Classes Exit Handler:
 - São identificadas por um valor REC_TYPE de "X".
- Em geral são uma forma de executar algum código no momento da limpeza.
- São processadas somente se uma classe Event Handler foi localizada e executada anteriormente. Se um manipulador Filter impediu o processamento adicional, os Exit handlers não serão processados.
- Como todas as classes de manipulador, têm a oportunidade de alterar o valor oEvent.ReturnFlags, mas é uma prática muito ruim fazer isso.

# API do GetExpression Wrapper

Você pode substituir a implementação da caixa de diálogo GETEXPR usada no report builder registrando uma classe de REC_TYPE="G" no registro de manipuladores. A classe deve suportar o método GetExpression() conforme mostrado neste exemplo:

```foxpro
DEFINE CLASS MyGetExpr AS Custom
    PROCEDURE GetExpression( cDefExpr, cDataType, cCalledFrom, oEvent )
        LOCAL cExpression
        GETEXPR TO cExpression DEFAULT cDefExpr
        RETURN cExpression
    ENDPROC
ENDDEFINE
```

Somente uma classe pode ser registrada como o GetExpressionWrapper padrão. Se houver mais de um registro de `REC_TYPE`="G," somente o primeiro localizado será usado pelo report builder.

### O parâmetro cCalledFrom

O report builder passa à classe GetExpressionWrapper um parâmetro indicando qual tipo de expressão está sendo editada. Os valores possíveis são:
 - "PrintWhenExpression"
- "FieldExpression"
- "OleBoundField"
- "OleBoundExpression"
- "BandGroupOnExpression"
- "VariableValueToStore"
- "VariableInitialValue"

# API do Run-time Extension Editor

Você pode substituir a implementação da caixa de diálogo que aparece quando você clica no botão de comando Edit settings no grupo Run-time extensions na guia Other do Report Builder registrando uma classe no registro de manipuladores com um `REC_TYPE` de "E". A classe deve suportar a API do Event Handler. Se implementar uma classe de formulário, o formulário deve ser emitido como uma janela MODAL.

Uma classe de editor de extensão de tempo de execução deve fazer o seguinte no método Execute():
 - Ler o XML de metadados do campo STYLE.
- Apresentar uma interface de usuário para permitir que o usuário edite os metadados.
- Salvar um fragmento XML válido de volta no campo STYLE.
- Diferentemente dos outros tipos de manipulador mostrados acima, não deve tentar definir os sinalizadores de retorno.

Somente uma classe pode ser registrada como o RuntimeExtensionEditor padrão. Se houver mais de um registro "E" na tabela de registro de manipuladores, o primeiro encontrado será usado.

# Adicionando guias à caixa de diálogo de seleção múltipla

Você pode adicionar páginas ao pageframe na Caixa de diálogo Multiple Selection (Report Builder) registrando uma classe no registro de manipuladores com um `REC_TYPE` de "M".

A classe deve ser derivada do Page Object. Se a página contém um Container Object que implementa `.LoadFromFrx()` e `.SaveToFrx()`, esses métodos serão chamados automaticamente pela caixa de diálogo de seleção múltipla nos momentos apropriados:

```foxpro
DEFINE CLASS pagAlign AS page
    Caption = "Alignment"
    Name    = "pagAlign"
    ADD OBJECT Panel1 AS panelAlign
ENDDEFINE
DEFINE CLASS panelAlign as Container
    BorderWidth = 0
    Width = 300
    Height = 300
    Event = null
    frxCursor = null
    ADD OBJECT Check1 AS Checkbox WITH ;
        Caption = "Align to leftmost object", ;
        Top = 100, Left = 50, Width = 150, Value=.F.
    PROCEDURE LoadFromFrx()
        * No initialization required
        RETURN .T.
    ENDPROC
    PROCEDURE SaveToFrx()
        IF THIS.Check1.Value
            LOCAL curSel
            curSel = SELECT()
            SELECT MIN(hpos) AS hpos FROM frx ;
                WHERE curpos AND objcode<>53 ;
                INTO CURSOR query
            newHpos = query.hpos
            USE IN query
            SELECT frx
            SCAN FOR curpos AND RECNO()>1
                REPLACE hpos WITH m.newHpos
            ENDSCAN
            SELECT (m.curSel)
        ENDIF
        RETURN .T.
    ENDPROC
ENDDEFINE
```

Este exemplo adiciona uma guia à caixa de diálogo de seleção múltipla com uma única caixa de seleção que, se marcada, definirá a posição horizontal de todos os objetos selecionados para a do objeto posicionado mais à esquerda na seleção.

O objeto container pode implementar qualquer um dos seguintes PEMs:
 - O método LoadFromFrx() é chamado durante a inicialização do formulário e é um bom lugar para ler valores do cursor frx para inicializar valores dos controles no container.
- O método SaveToFrx() é chamado quando o usuário clica em OK . Retorne FALSE se desejar impedir que a caixa de diálogo seja fechada.
- Se definida, a propriedade Event receberá uma referência ao objeto Event do report builder. (Consulte A classe de evento do Report Builder para mais informações.)
- Se definida, a propriedade frxCursor receberá uma referência ao objeto membro frxCursor do objeto Event, por conveniência. (Consulte Classe Foundation FRX Cursor para mais informações.)

Pode haver mais de um registro no registro de manipuladores definido com `REC_TYPE`="M,". Cada classe de página será carregada na caixa de diálogo como uma guia separada.

# Como o report builder processa eventos

Quando o report builder é invocado, o Report Designer passa um ID de tipo de evento, com uma cópia do arquivo FRX aberto em uma sessão de dados privada. O objeto de relatório ao qual o evento se aplica geralmente é identificado pela localização do ponteiro de registro no cursor FRX. O report builder observa os valores OBJTYPE e OBJCODE no registro selecionado e então consulta a tabela de registro de manipuladores.

#### 1. Todos os Filter Handlers são processados

O construtor seleciona todos os registros da tabela de registro de manipuladores com `REC_TYPE`="F", ordenados por `FLTR_ORDR`, e instancia cada classe de filtro em sequência, invocando o método Execute().

Se o valor de sua propriedade allowToContinue for verdadeiro (`.T.`), a próxima classe de manipulador de filtro é instanciada.

Se o valor de sua propriedade allowToContinue for falso (`.F.`), nenhum processamento adicional ocorre - ReportBuilder.App define o Bit 0 no parâmetro ReturnFlags para indicar ao designer que o evento do construtor foi tratado com sucesso.

Importante:
 - O valor especificado no campo FLTR_ORDR é importante, porque um filtro com valor menor (prioridade maior) pode impedir o processamento adicional, tanto pelo próximo filtro na fila quanto por uma classe Event Handler apropriada.
- Cada Filter Handler tem a oportunidade de definir os sinalizadores de retorno do evento, mas estes só serão respeitados se o Filter definir seu allowToContinue como falso ( .F. ), porque se o processamento continuar, o Event Handler subsequente assumirá que pode definir esses sinalizadores como desejar, possivelmente substituindo qualquer configuração feita pelo Filter Handler.

#### 2. Uma classe Event Handler apropriada é instanciada

O report builder em seguida procura uma classe Event Handler específica para instanciar e tratar o evento.

A tabela de registro permite correspondências "curinga", para que não seja necessário ter um registro separado para cada combinação única de evento do construtor + objeto de relatório. O construtor usa buscas progressivamente mais gerais na tabela de registro de manipuladores para registros não excluídos.

O construtor generalizará progressivamente as buscas, aplicando valores curinga até encontrar uma correspondência:

| Sequência | REC_TYPE | EVENTTYPE | OBJTYPE | OBJCODE |
| --- | --- | --- | --- | --- |
| 1 | "H" | (Exato) | (Exato) | (Exato) |
| 2 | "H" | (Exato) | (Exato) | -1 |
| 3 | "H" | (Exato) | -1 | -1 |
| 4 | "H" | -1 | -1 | -1 |

Se ainda nenhum registro correspondente for encontrado, o evento do construtor será ignorado (ambos os bits do parâmetro ReturnFlags serão limpos) e o controle retornará ao designer para o comportamento nativo do Visual FoxPro.

Se uma correspondência for encontrada, a classe é instanciada e seu método Execute() é invocado.

#### 3. Todos os Exit Handlers são processados

Depois que o Event Handler correspondente foi executado, o report builder seleciona todos os registros da tabela de consulta com `REC_TYPE`="X," ordenados por `FLTR_ORDR`, e instancia cada classe em sequência, invocando o método Execute().

### Sobre múltiplos objetos selecionados

A tabela de registro de manipuladores de eventos padrão inclui um registro para um MultiSelectHandler registrado em um `OBJTYPE` de 99. Consulte Caixa de diálogo Multiple Selection (Report Builder) para um exemplo de manipulador de seleções múltiplas.

O construtor detecta quando vários controles de relatório estão selecionados no layout e trata este caso como um `OBJTYPE` único:

```foxpro
COUNT FOR curpos AND RECNO() > 1 TO oEvent.SelectedObjectCount
IF oEvent.SelectedObjectCount > 1
    oEvent.OBJTYPE = 99
    oEvent.OBJCODE = 0
ELSE
    oEvent.OBJTYPE = frx.OBJTYPE
    oEvent.OBJCODE = frx.OBJCODE
ENDIF
```

Desta forma, uma classe Event Handler específica pode ser registrada para tratar seleções múltiplas.
