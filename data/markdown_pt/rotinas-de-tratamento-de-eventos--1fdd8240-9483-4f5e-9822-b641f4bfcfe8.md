# Rotinas de tratamento de eventos

Estas rotinas de API permitem criar manipuladores de eventos e processar eventos do Visual FoxPro.
 **Rotina de biblioteca de API _ActivateHandler( )**
Adiciona um manipulador de função ao final da lista de manipuladores de eventos.
**Rotina de biblioteca de API _ActivateIdle( )**
Adiciona uma rotina à lista de rotinas chamadas quando o Visual FoxPro aguarda uma entrada do usuário ou o tempo limite de um evento.
**Rotina de biblioteca de API _DeActivateHandler( )**
Remove o manipulador especificado da lista do processador de eventos.
**Rotina de biblioteca de API _DeActivateIdle( )**
Remove a rotina especificada do loop de inatividade.
**Rotina de biblioteca de API _DefaultProcess( )**
Fornece o processamento padrão para um evento retornado por _GetNextEvent( ) quando ele não exige tratamento especial.
**Rotina de biblioteca de API _GetNextEvent( )**
Lê o próximo evento em EventRec e retorna o tipo do evento.
**Rotina de biblioteca de API _InKey( )**
Retorna a próxima tecla digitada durante o período de tempo limite, especificado como um número de pulsos do temporizador do MS-DOS.
**Rotina de biblioteca de API _MousePos( )**
Preenche pt com a posição atual do mouse.
**Rotina de biblioteca de API _MousePosP( )**
Preenche pt com a posição atual do mouse em pixels.
