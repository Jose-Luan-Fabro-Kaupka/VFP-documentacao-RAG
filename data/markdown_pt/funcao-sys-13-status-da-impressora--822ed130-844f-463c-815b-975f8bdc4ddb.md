# Função SYS(13) - Status da impressora

Retorna o status da impressora. Incluída para compatibilidade com versões anteriores.

```foxpro
SYS(13)
```

# Valor de retorno

Valor de caracteres. Para versões do Visual FoxPro executadas no Windows, SYS(13) sempre retorna READY.

Em versões anteriores, se a impressora não estiver pronta, SYS(13) retorna OFFLINE. Se a impressora estiver pronta, SYS(13) retorna READY. SYS(13) também pode retornar os seguintes valores nas condições especificadas:
 - Se a impressora estiver conectada a uma porta COM e a impressora retornar Clear To Send Data ou Data Set Ready, SYS(13) retorna READY.
- Se a impressora estiver conectada a uma porta paralela e a impressora retornar Out of Paper, I/O Error, Time Out, Printer Busy ou Printer Not Selected, SYS(13) retorna OFFLINE.

# Exemplo

```foxpro
IF SYS(13) = 'OFFLINE'
   WAIT WINDOW 'Printer is offline'
ENDIF
```
