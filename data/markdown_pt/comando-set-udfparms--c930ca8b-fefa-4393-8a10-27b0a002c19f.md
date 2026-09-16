# Comando SET UDFPARMS

Especifica se o Visual FoxPro passa variáveis por valor ou por referência para parâmetros em procedimentos e funções definidas pelo usuário (UDFs).

```foxpro
SET UDFPARMS TO VALUE | REFERENCE
```

#### Parâmetros
 **TO VALUE**
Passa variáveis para parâmetros por valor. Ao passar variáveis por valor, o procedimento ou função pode alterar o valor na variável; no entanto, o valor original da variável no programa chamador não é alterado. (Padrão) Observação Usar SET UDFPARMS TO VALUE não afeta a cláusula WITH no comando DO, que, por padrão, passa argumentos para parâmetros por referência.
**TO REFERENCE**
Passa variáveis para parâmetros por referência. Ao passar variáveis por referência, o procedimento ou função pode alterar o valor na variável, o que altera o valor original da variável no programa chamador.

# Observações

Independentemente da configuração de SET UDFPARMS, você pode forçar a passagem de variáveis por valor ou por referência. Para obter mais informações, consulte Como: passar dados para parâmetros por referência e Como: passar dados para parâmetros por valor.

# Exemplo

O exemplo a seguir ilustra a diferença entre passar variáveis por valor e por referência.

```foxpro
*** Pass variable by value. ***
CLEAR
SET TALK OFF
WAIT 'Press a key to pass by value' WINDOW
SET UDFPARMS TO VALUE
STORE 1 TO gnX
*** The value of gnX does not change. ***
@ 2,2 SAY 'UDF value: ' + STR(plusone(gnX))
@ 4,2 SAY 'Value of gnX: ' + STR(gnX)
*** Pass variable by reference ***
WAIT 'Press a key to pass by reference' WINDOW
CLEAR
SET UDFPARMS TO REFERENCE
STORE 1 TO gnX
*** The value of gnX changes. ***
@ 2,2 SAY 'UDF value: ' + STR(plusone(gnX))
@ 4,2 SAY 'Value of X: ' + STR(gnX)
SET UDFPARMS TO VALUE
*** This is a UDF that adds one to a number ***
FUNCTION plusone
PARAMETER gnZ
gnZ = gnZ + 1
RETURN gnZ
*** End of UDF ***
```

O exemplo a seguir é o exemplo acima com variáveis passadas por valor e por referência através do uso de parênteses e @, respectivamente.

```foxpro
*** Pass variable by value ***
CLEAR
SET TALK OFF
WAIT 'Press a key to pass by value' WINDOW
STORE 1 TO gnX
@ 2,2 SAY 'UDF value: ' + STR(plusone((gnX)))
@ 4,2 SAY 'Value of gnX: ' + STR(gnX)
*** Pass variable by reference ***
WAIT 'Press a key to pass by reference' WINDOW
CLEAR
STORE 1 TO gnX
@ 2,2 SAY 'UDF value: ' + STR(plusone(@gnX))
@ 4,2 SAY 'Value of gnX: ' + STR(gnX)
*** This is a UDF that adds one to a number ***
FUNCTION plusone
PARAMETER gnZ
gnZ = gnZ + 1
RETURN gnZ
*** End of UDF ***
```
