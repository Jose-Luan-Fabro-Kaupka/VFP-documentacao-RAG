# Exemplo de vinculação, acionamento, desvinculação e recuperação de eventos

Arquivo: ...\Samples\Solution\Toledo\FrmEvents.scx

Este exemplo demonstra como vincular eventos, acionar eventos programaticamente, desvincular eventos e recuperar eventos para a variável de sistema _SCREEN, ou seja, a janela principal do Visual FoxPro. No exemplo, você pode acionar manualmente um evento vinculado de _SCREEN selecionando um evento na caixa de combinação, ou chamar os mesmos eventos e seus respectivos manipuladores usando o mouse.

Para obter mais informações sobre _SCREEN, consulte Variável de sistema _SCREEN.

# Vinculação de eventos

Para responder a eventos do Visual FoxPro, use a função BINDEVENT( ). Neste exemplo, a função BINDEVENT( ) é chamada no método personalizado InitBindEvent e vincula vários eventos de _SCREEN aos métodos do formulário. Quando um dos eventos de _SCREEN ocorre, o método manipulador associado é chamado:

```foxpro
BINDEVENT(_SCREEN,"Resize",ThisForm,"screenresize")
BINDEVENT(_SCREEN,"Mousedown",ThisForm,"screenmousedown")
BINDEVENT(_SCREEN,"Mouseup",ThisForm,"screenmouseup")
BINDEVENT(_SCREEN,"Rightclick",ThisForm,"screenrightclick")
BINDEVENT(_SCREEN,"Dblclick",ThisForm,"screendblclick")
```

Para obter mais informações, consulte Função BINDEVENT( ) e Evento Init.

# Acionamento programático de eventos

Para acionar eventos programaticamente, use a função RAISEEVENT( ). Neste exemplo, quando a caixa de combinação é selecionada, o evento InteractiveChange usa o valor retornado para acionar programaticamente o evento especificado.

```foxpro
RAISEEVENT(_SCREEN,this.Value)
```

Para obter mais informações, consulte Função RAISEEVENT( ) e Evento InteractiveChange.

# Desvinculação de eventos

Para desvincular manipuladores de eventos, use a função UNBINDEVENTS( ). Neste exemplo, o método personalizado UnbindHandlers desvincula eventos de _SCREEN.

```foxpro
UNBINDEVENTS(_SCREEN)
```

Para obter mais informações, consulte Função UNBINDEVENTS( ).

# Recuperação de vínculos de eventos

Para recuperar vínculos de eventos existentes em uma matriz, use a função AEVENTS( ). Neste exemplo, o método personalizado ScreenDblClick, vinculado ao evento DblClick de _SCREEN, usa a função AEVENTS( ) para informar o número de vínculos de eventos:

```foxpro
AEVENTS(laEvents,Thisform)
```

Para obter mais informações, consulte Função AEVENTS( ) e Evento DblClick.
