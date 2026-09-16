# A classe Report Builder Event

Encapsula atributos do evento do report builder na estrutura reportbuilder.app. Também expõe alguns métodos úteis da estrutura.

Se você decidir criar suas próprias classes de manipulador, seu código precisará interagir com o objeto parâmetro oEvent que a estrutura do builder passa aos métodos das classes de filtro e manipulador.

```foxpro
oEvent.PropertyName [= eValue]
oEvent.Method( ... )
```

# Propriedades

| PropertyName | Type | eValue |
| --- | --- | --- |
| BuilderPath | C | Contém o caminho de reportbuilder.app , com uma barra invertida final. |
| CommandClauses | O | Contém uma referência ao terceiro parâmetro passado ao report builder. Consulte Understanding Report Builder Events para obter mais informações sobre parâmetros do report builder. |
| DefaultRecno | I | Especifica a posição inicial do ponteiro de registro no cursor FRX. |
| DefaultSessionId | I | Contém o Data Session Id do Report Designer, o quarto parâmetro passado pelo Report Designer. |
| EventType | I | Contém o segundo parâmetro passado pelo Report Designer. |
| FrxCursor | O | Uma instância da FRX Cursor Foundation Class contendo algumas funções úteis para interagir com o cursor FRX. |
| HandleMode | I | Indica como o Builder trata eventos. 1 (Padrão) Processamento regular de eventos. 2 Modo de depuração. Abre o navegador FRX/depurador de eventos. Filtros não são executados. 3 O Event Inspector exibe os detalhes do evento recebido em uma janela messagebox. Filtros não são executados. 4 O Builder repassa todos os eventos de volta ao Designer para comportamento normal. |
| FrxSessionId | I | Data Session do Report Builder, em que o cursor FRX está aberto. |
| MultiSelect | L | True (.T.) se vários objetos estão selecionados no Report Designer. |
| ObjCode | I | O valor do campo frx.OBJCODE do registro inicialmente selecionado no cursor FRX. |
| ObjType | I | O valor do campo frx.OBJTYPE do registro inicialmente selecionado no cursor FRX. |
| Protected | L | Indica se o Report Designer foi iniciado com a palavra-chave PROTECTED. (Mesmo valor que CommandClauses.Protected.) |
| ReturnFlags | I | O valor desta propriedade será retornado ao Report Designer no primeiro parâmetro passado pelo Report Designer. Inicialmente definido como 0 (sem interceptação, sem alteração). Use .setHandledByBuilder(.T.) e .setReloadChanges(.T.) para configurar o flag de retorno apropriadamente. |
| SelectedObjectCount | I | Especifica o número de objetos de relatório selecionados no layout, determinado contando CURPOS=.T. no cursor FRX (não contando o registro de cabeçalho). |
| SessionData | O | Uma referência a um objeto gerenciador de pares nome-valor usado para armazenar dados entre invocações do Report Builder |
| UniqueId | C | Contém o valor do campo UNIQUEID do registro inicialmente selecionado no cursor FRX. |

# Métodos

| Method | Description |
| --- | --- |
| GetEventTypeText( [ iEvent ] ) | Retorna uma cadeia de caracteres contendo o nome de um determinado tipo de evento. |
| GetTargetTypeText( [ iObjType , iObjCode ] ) | Retorna uma cadeia de caracteres contendo o nome de um determinado objeto de relatório. |
| GetExpression( cDefExpr , cDataType , cCalledFrom ) | Exibe uma caixa de diálogo GETEXPR e retorna uma cadeia de caracteres contendo a expressão resultante. Garante que a caixa de diálogo getExpression seja exibida na sessão de dados do Report Designer. |
| Handle( [ iObjType , iObjCode ] ) | Localiza uma classe de manipulador, instancia-a e chama o método Execute(). |
| GetExtensionEditor() | Localiza uma classe Extension Editor na tabela de registro de manipuladores, instancia-a e retorna a referência do objeto. Para obter mais informações, consulte Report Builder Event Handler Registry Table . |
| ToString() | Retorna uma cadeia de caracteres "dump" de todos os valores de propriedade do objeto, adequada para exibição em uma chamada MESSAGEBOX. |
| SetHandledByBuilder( .T. | .F. ) | Define o bit "Event handled By" na propriedade ReturnFlags para suprimir (ou habilitar) o comportamento padrão do Report Designer. |
| SetReloadChanges( .T. | .F. ) | Define o bit "Reload FRX changes" na propriedade ReturnFlags para que alterações feitas no cursor FRX sejam refletidas (ou não refletidas) no layout do relatório. |

> **Observação:** Se sua classe faz alterações no cursor FRX que precisam ser recarregadas no layout, ela deve chamar o método .SetReloadChanges(.T.).
