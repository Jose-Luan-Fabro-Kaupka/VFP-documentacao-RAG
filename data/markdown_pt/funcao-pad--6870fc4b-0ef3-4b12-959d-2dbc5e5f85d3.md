# Função PAD( )

Retorna como uma cadeia de caracteres em maiúsculas o título de menu escolhido mais recentemente em uma barra de menu ou retorna um valor lógico indicando se um título de menu está definido para uma barra de menu ativa.

```foxpro
PAD([cMenuTitle [, cMenuBarName]])
```

#### Parâmetros
 **cMenuTitle**
Especifica o nome de um título de menu em uma barra de menu. Inclua este argumento para testar se o título de menu está definido para uma barra de menu ativa. Um valor lógico true (.T.) é retornado se o título de menu estiver definido; caso contrário, um valor lógico false (.F.) é retornado.
**cMenuBarName**
Especifica o nome da barra de menu que contém o título de menu cMenuTitle. Se cMenuBarName for omitido, presume-se que o título de menu esteja na barra de menu ativa atualmente.

# Valor de retorno

Character ou Logical

# Observações

Uma barra de menu deve estar definida e ativa para PAD( ) retornar um título de menu. Barras de menu são criadas e ativadas com DEFINE MENU e ACTIVATE MENU.

Você também pode usar PAD( ) com a barra de menu do sistema Visual FoxPro.

PAD( ) (executado sem nenhum de seus argumentos opcionais) retorna uma cadeia de caracteres vazia se uma barra de menu não estiver definida e ativa ou se você executar PAD( ) na janela Command.

# Exemplo

Neste exemplo, PAD( ) é usado para passar um título de menu a um procedimento.

A barra de menu do sistema Visual FoxPro atual é salva na memória com SET SYSMENU SAVE e todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Vários títulos de menu do sistema são criados com DEFINE PAD. Quando um título de menu é escolhido, PAD( ) é usado para passar o título de menu ao procedimento chamado `choice`. `choice` exibe o título de menu escolhido e o nome da barra de menu. Se você escolher o título de menu Exit, o menu do sistema Visual FoxPro original é restaurado.

```foxpro
*** Name this program PADEXAM.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
DEFINE PAD padSys OF _MSYSMENU PROMPT '\<System' COLOR SCHEME 3 ;
   KEY ALT+S, ''
DEFINE PAD padEdit OF _MSYSMENU PROMPT '\<Edit' COLOR SCHEME 3 ;
   KEY ALT+E, ''
DEFINE PAD padRecord OF _MSYSMENU PROMPT '\<Record' COLOR SCHEME 3 ;
   KEY ALT+R, ''
DEFINE PAD padWindow OF _MSYSMENU PROMPT '\<Window' COLOR SCHEME 3 ;
   KEY ALT+W, ''
DEFINE PAD padReport OF _MSYSMENU PROMPT 'Re\<ports' COLOR SCHEME 3 KEY ALT+P, ''
DEFINE PAD padExit OF _MSYSMENU PROMPT 'E\<xit' COLOR SCHEME 3 ;
   KEY ALT+X, ''
ON SELECTION MENU _MSYSMENU ;
   DO choice IN padexam WITH PAD(), MENU()
PROCEDURE choice
PARAMETERS gcPad, gcMenu
WAIT WINDOW 'You chose ' + gcPad + ;
   ' from menu ' + gcMenu NOWAIT
IF gcPad = 'PADEXIT'
   SET SYSMENU TO DEFAULT
ENDIF
```
