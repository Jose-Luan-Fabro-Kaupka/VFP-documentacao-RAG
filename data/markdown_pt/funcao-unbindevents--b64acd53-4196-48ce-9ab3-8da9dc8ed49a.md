# Função UNBINDEVENTS( )

Você pode usar UNBINDEVENTS( ) para desvincular, ou desanexar, um evento que foi originalmente vinculado a um objeto Visual FoxPro usando BINDEVENT( ). Para desanexar eventos de objetos Component Object Model (COM), use a função EVENTHANDLER( ). Há três versões da sintaxe.

```foxpro
UNBINDEVENTS(oEventSource, cEvent, oEventHandler, cDelegate)
```

```foxpro
UNBINDEVENTS(oEventObject)
```

```foxpro
UNBINDEVENTS(hWnd [, nMessage])
```

#### Parâmetros
 **oEventSource**
Especifica a fonte do evento, que deve ser um objeto Visual FoxPro válido.
**oEventObject**
Especifica uma referência de objeto, que pode ser usada como fonte do evento ou manipulador de eventos.
**cEvent**
Especifica o nome do evento, método ou propriedade que você deseja desvincular.
**oEventHandler**
Especifica o objeto que está manipulando o evento.
**cDelegate**
Especifica o método delegado que manipula o evento para oEventHandler .
**hWnd**
Especifica o identificador inteiro da janela para a qual os eventos são desvinculados. Se hWnd for 0, todos os hWnds são desvinculados. Se o parâmetro nMessage não for incluído, todas as vinculações de mensagens do Windows para o identificador de janela hWnd são desvinculadas.
**nMessage**
Especifica uma mensagem válida do Windows (Win Msg) que é desvinculada. Consulte o MSDN (Microsoft Developer Network) para informações sobre mensagens do Windows.

# Valor de retorno

Tipo de dados Numeric. UNBINDEVENTS( ) retorna o número de eventos desvinculados se a desvinculação for bem-sucedida. UNBINDEVENTS( ) retorna o valor 0 se não existirem eventos para desvincular. O Visual FoxPro gera um erro se UNBINDEVENTS( ) falhar ao desvincular eventos disponíveis para desvinculação.

# Observações

A tabela a seguir descreve as formas de usar UNBINDEVENTS( ).

| Sintaxe | Ação |
| --- | --- |
| UNBINDEVENTS(oEventSource, cEvent, oEventHandler, cDelegate) | Desvincula um evento específico de um manipulador de eventos. |
| UNBINDEVENTS(oEventObject) | Desvincula todos os eventos associados a este objeto. Isso inclui eventos vinculados a ele como fonte de evento e seus métodos delegados que servem como manipuladores de eventos. |
| UNBINDEVENTS(hWnd [, nMessage]) | Desvincula todos ou eventos específicos de mensagem do Windows (Win Msg). |

Se um evento estiver ocorrendo e UNBINDEVENTS( ) ou o método delegado que manipula o evento for chamado, o evento e seu método delegado terminam de executar antes de UNBINDEVENTS( ) desvincular o evento.

Você pode chamar a função AEVENTS( ) para recuperar informações sobre todos os eventos e métodos delegados anexados a um objeto específico.

# Exemplo

O exemplo a seguir mostra como desfazer uma chamada BINDEVENTS( ) que mantém o Class Browser posicionado no lado direito da área de trabalho do Visual FoxPro, independentemente de como a área de trabalho é redimensionada. UNBINDEVENTS( ) desanexa o evento Resize da variável de sistema _SCREEN do objeto `oHandler`:

```foxpro
PUBLIC oHandler
oHandler=NEWOBJECT("myhandler")
DO (_browser)
BINDEVENT(_SCREEN,"Resize",oHandler,"myresize")
UNBINDEVENTS(_SCREEN,"Resize",oHandler,"myresize")
DEFINE CLASS myhandler AS Session
   PROCEDURE myresize
   _obrowser.left = _SCREEN.Width - _obrowser.width
   RETURN
ENDDEFINE
```
