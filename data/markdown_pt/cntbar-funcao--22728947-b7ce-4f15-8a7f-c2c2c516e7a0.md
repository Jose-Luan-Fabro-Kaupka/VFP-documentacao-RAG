# CNTBAR( ) Função

Retorna o número de itens de menu em um menu definido pelo usuário ou no menu do sistema Visual FoxPro.

```foxpro
CNTBAR(cMenuName)
```

#### Parâmetros
 **cMenuName**
Especifica o nome do menu para o qual CNTBAR( ) retorna o número de itens de menu. Para obter uma lista dos nomes de menu do sistema Visual FoxPro, consulte o tópico Nomes de menu do sistema.

# Valor de retorno
Numérico

# Observações
Se um menu definido pelo usuário for criado com a opção PROMPT em DEFINE POPUP, o Visual FoxPro avaliará o número de itens de menu quando você emitir ACTIVATE POPUP. Para tal menu, CNTBAR( ) retorna um valor significativo somente após você ativar o menu. No entanto, se os itens de menu no menu forem criados com DEFINE BAR, CNTBAR( ) poderá determinar o número de itens de menu antes de emitir ACTIVATE POPUP.

# Exemplo
No exemplo de programa a seguir, denominado CNTBAR.prg, um título de menu é adicionado ao menu do sistema. O menu `popEnv` é criado com quatro itens de menu. O programa coloca um caractere de marca em cada item quando o item é selecionado. CNTBAR( ) é usado dentro de um loop para exibir inicialmente marcas próximas aos itens de menu apropriados.

```foxpro
*** You must name this program CNTBAR.PRG ***
CLEAR
SET TALK OFF
DEFINE PAD padEnv OF _MSYSMENU PROMPT 'E\<nvironment';
   KEY ALT+R, 'ALT+R'
ON PAD padEnv OF _MSYSMENU ACTIVATE POPUP popEnv
DEFINE POPUP popEnv MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF popEnv PROMPT '\<Status Bar'
DEFINE BAR 2 OF popEnv PROMPT '\<Clock'
DEFINE BAR 3 OF popEnv PROMPT '\<Extended Video'
DEFINE BAR 4 OF popEnv PROMPT 'St\<icky'
ON SELECTION POPUP popEnv DO enviropop IN cntbar.prg
FOR i = 1 TO CNTBAR('popEnv')
   DO CASE
      CASE PRMBAR('popEnv', i) = 'Status Bar'
         IF _WINDOWS or _MAC
            SET MARK OF BAR i OF popEnv TO SET('STATUS BAR') = 'ON'
         ELSE
            SET MARK OF BAR i OF popEnv TO SET('STATUS') = 'ON'
         ENDIF
      CASE PRMBAR('popEnv', i) = 'Clock'
         SET MARK OF BAR i OF popEnv TO  SET('CLOCK') = 'ON'
      CASE PRMBAR('popEnv', i) = 'Extended Video'
         SET MARK OF BAR i OF popEnv TO  SROW() > 25
      CASE PRMBAR('popEnv', i) = 'Sticky'
         SET MARK OF BAR i OF popEnv TO  SET('STICKY') = 'ON'
   ENDCASE
ENDFOR
PROCEDURE enviropop
DO CASE
   CASE PROMPT() = 'Status'
      IF mrkbar('popEnv', BAR())
         DO CASE
            CASE _WINDOWS OR _MAC
               SET STATUS BAR OFF
            CASE _DOS
               SET STATUS OFF
            OTHERWISE
         ENDCASE
         SET MARK OF BAR BAR() OF popEnv TO .F.
      ELSE
         DO CASE
            CASE _WINDOWS OR _MAC
               SET STATUS BAR ON
            CASE _DOS
               SET STATUS ON
            OTHERWISE
         ENDCASE
         SET MARK OF BAR BAR() OF popEnv TO .T.
      ENDIF
CASE PROMPT() = 'Clock'
   IF mrkbar('popEnv', BAR())
      SET CLOCK OFF
      SET MARK OF BAR BAR() OF popEnv TO .F.
   ELSE
      DO CASE
         CASE _WINDOWS OR _MAC
            SET STATUS BAR ON
            SET CLOCK STATUS
         CASE _DOS
            SET CLOCK ON
         OTHERWISE
      ENDCASE
      SET MARK OF BAR BAR() OF popEnv TO .T.
   ENDIF
CASE PROMPT() = 'Extended Video'
   IF MRKBAR('popEnv', BAR())
      SET DISPLAY TO VGA25
      SET MARK OF BAR BAR() OF popEnv TO .F.
   ELSE
      SET DISPLAY TO VGA50
      SET MARK OF BAR BAR() OF popEnv TO .T.
   ENDIF
CASE PROMPT() = 'Sticky'
   IF MRKBAR('popEnv', BAR())
      DO CASE
         CASE _WINDOWS OR _MAC
            WAIT WINDOW 'STICKY is always on in this Visual FoxPro version'
         CASE _DOS
            SET STICKY OFF
         OTHERWISE
      ENDCASE
      SET MARK OF BAR BAR() OF popEnv TO .F.
   ELSE
      DO CASE
         CASE _WINDOWS OR _MAC
            WAIT WINDOW 'STICKY is always ON in Visual FoxPro'
         CASE _DOS
            SET STICKY ON
         OTHERWISE
      ENDCASE
       SET MARK OF BAR BAR() OF popEnv TO .T.
   ENDIF
ENDCASE
```
