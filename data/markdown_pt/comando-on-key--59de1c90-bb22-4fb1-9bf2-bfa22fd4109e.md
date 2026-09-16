# Comando ON KEY =

Incluído para compatibilidade com versões anteriores. Use o comando ON KEY LABEL em vez disso.

Executa um comando quando uma tecla ou combinação de teclas específica é pressionada durante um READ.

```foxpro
ON KEY
	[ = expN]
	[command]
```

#### Parâmetros
 command

 O comando a ser executado quando a tecla é pressionada é especificado com command.

 Corresponding

Key Codes Keystrokes

--------- -------------

272 - 281 Alt+Q, W, E, R, T, Y, U, I, O ,P*

286 - 294 Alt+A, S, D, F, G, H, J, K, L*

300 - 306 Alt+Z, X, C, V, B, N, M*

315 - 324 F1 to F10 function keys

327 Home

328 Up Arrow

329 Page Up

331 Left Arrow

333 Right Arrow

335 End

336 Down Arrow

337 Page Down

338 Ins (On the Macintosh, Help)

339 Del

340 - 349 Shift+F1 to Shift+F10

350 - 359 Ctrl+F1 to Ctrl+F10

360 - 369 Alt+F1 to Alt+F10*

370 Ctrl+Print Scrn

371 Ctrl+Left Arrow

372 Ctrl+Right Arrow

373 Ctrl+End

374 Ctrl+Page Down

375 Ctrl+Home

376 - 387 Alt+1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -, =*

388 Ctrl+Page Up

* No FoxPro para Macintosh, as combinações Alt+... são substituídas por Ctrl+Option+...

# Observações

ON KEY = está incluído para compatibilidade com versões anteriores. Use ON KEY LABEL em vez disso.

Pressionar a tecla ou combinação de teclas especificada quando um READ não está em vigor não executa o comando ON KEY =. ON KEY = normalmente usa DO para executar um procedimento.

Apenas um comando ON KEY = pode estar ativo por vez. Use ON KEY LABEL para executar comandos para várias teclas ou combinações de teclas.

= expN

 Se a tecla que você especifica é um caractere imprimível, especifique o valor ASCII da tecla com expN. Se a tecla não pode ser impressa, ou se você usa uma combinação de teclas, inclua um valor da tabela a seguir em expN.

# Exemplo

Neste exemplo, registros de CUSTOMER.DBF são exibidos para edição. Se você pressionar F1, o nome do campo atual é passado ao procedimento chamado SCRNHELP e uma mensagem é exibida em uma janela.

```foxpro
ON KEY = 315 DO scrnhelp WITH VARREAD()
SET TALK OFF
USE customer
SCATTER TO temp
DEFINE WINDOW input FROM 6,10 TO 18,70 PANEL
ACTIVATE WINDOW input
@ 1,3	SAY 'Customer: '	GET company
@ 3,3	SAY 'Address: '	GET address
@ 5,3	SAY 'City: '	GET city
@ 7,3	SAY 'State: '	GET state
@ 7,18	SAY 'Zip: ' 	GET zip
@ 9,8	SAY 'Press Esc to cancel or F1 for help'
READ
IF LASTKEY() = 27
	GATHER FROM temp
ENDIF
DEACTIVATE WINDOW input
RELEASE WINDOW input
PROCEDURE scrnhelp
PARAMETERS fieldname
DEFINE WINDOW help_me FROM 1,0 TO 4,79
ACTIVATE WINDOW help_me
@ 0,20 SAY 'Sorry, no help available for ' +  fieldname
WAIT
RELEASE WINDOW help_me
RETURN
```
