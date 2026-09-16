# Função PRINTSTATUS( )

Retorna o status da impressora. Incluída para compatibilidade com versões anteriores.

```foxpro
PRINTSTATUS()
```

# Valor de retorno

Valor lógico. Para versões do Visual FoxPro executadas no Windows, PRINTSTATUS( ) sempre retorna True (.T.) se a impressora estiver conectada pelo Painel de Controle do Windows.

Em versões anteriores, se a impressora ou dispositivo de impressão estiver online, PRINTSTATUS( ) retorna True (.T.); caso contrário, retorna False (.F.).

# Observações

PRINTSTATUS( ) funciona de forma semelhante a SYS(13). Para obter mais informações, consulte SYS(13) - Status da impressora.

# Exemplo

```foxpro
? PRINTSTATUS()
*** Program Example ***
STORE PRINTSTATUS() TO glReady
IF NOT glReady
   WAIT 'Make sure printer is attached and turned on!' WINDOW
ELSE
   WAIT 'Printer is ready!' WINDOW
ENDIF
```
