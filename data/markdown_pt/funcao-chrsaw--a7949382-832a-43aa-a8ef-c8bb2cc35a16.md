# Função CHRSAW( )

Determina se um caractere está presente ou não no buffer do teclado.

```foxpro
CHRSAW([nSeconds])
```

#### Parâmetros
 **nSeconds**
Especifica o tempo em segundos que CHRSAW( ) aguarda antes de verificar o buffer do teclado. O buffer do teclado é verificado imediatamente se você omitir nSeconds. Incluir nSeconds permite que você use CHRSAW( ) para uma variedade de atividades temporizadas. Por exemplo, seu programa pode fechar um aplicativo se uma tecla não for pressionada por um número específico de segundos.

# Valor de retorno

Lógico

# Observações

CHRSAW( ) retorna True (.T.) se um caractere estiver presente no buffer do teclado, e False (.F.) se não estiver. CHRSAW( ) não afeta o conteúdo do buffer do teclado.

# Exemplo

No exemplo a seguir, o sistema exibe uma janela contendo campos de entrada criados com comandos @ ... GET e aguarda 5 segundos por entrada do teclado. Se uma tecla não for pressionada neste período, CHRSAW( ) retorna False (.F.) e o programa termina.

```foxpro
SET TALK OFF
DEFINE WINDOW wEnter FROM 7,10 to 13,70 PANEL
ACTIVATE WINDOW wEnter
@ 1,3 SAY 'Customer: '   GET gcCustomer  DEFAULT SPACE(40)
@ 3,3 SAY 'Address:  '   GET gcAddress  DEFAULT SPACE(40)
WAIT WINDOW 'Waiting for input' NOWAIT
IF NOT CHRSAW(5)
   DEACTIVATE WINDOW wEnter
   CLEAR GETS
ELSE
   READ
   DEACTIVATE WINDOW wEnter
ENDIF
RELEASE WINDOW wEnter
WAIT
CLEAR
```
