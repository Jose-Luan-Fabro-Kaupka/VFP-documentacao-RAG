# Função PARAMETERS( )

Retorna o número de parâmetros passados ao programa, procedimento ou função definida pelo usuário chamado mais recentemente.

```foxpro
PARAMETERS()
```

# Valor de retorno

Numeric

# Observações

PARAMETERS( ) é útil para determinar quantos parâmetros são passados a um programa, procedimento ou função definida pelo usuário.

> **Observação:** O valor retornado por PARAMETERS() é redefinido cada vez que um programa, procedimento ou função definida pelo usuário é chamado ou quando ON KEY LABEL é executado. Diferentemente de PARAMETERS(), a função PCOUNT() não é redefinida, portanto PCOUNT() pode ser preferível na maioria das situações de programação.

# Exemplos

O Exemplo 1 chama um procedimento e exibe em uma janela wait o número de parâmetros passados.

O Exemplo 2 usa um procedimento para exibir a média de 4 valores.

```foxpro
* Example 1
DO testpar WITH 1,2,3
PROCEDURE testpar
PARAMETERS gn1,gn2,gn3
gcMessage = 'PARAMETERS() ='+ALLTRIM(STR(PARAMETERS()))
WAIT WINDOW (gcMessage)
RETURN
* Example 2
SET TALK OFF
gnVal1 = 10
gnVal2 = 20
gnVal3 = 30
gnVal4 = 15
gnMin = getavg(gnVal1, gnVal2, gnVal3, gnVal4)
? 'Average value is '
?? gnMin
* This user-defined function permits up to 9 parameters to be passed.
* It uses the PARAMETERS() function to determine how many
* were passed and returns the average value.
FUNCTION getavg
PARAMETERS gnPara1,gnPara2,gnPara3,gnPara4,gnPara5, ;
   gnPara6,gnPara7,gnPara8,gnPara9
IF PARAMETERS() = 0
   RETURN 0
ENDIF
gnResult = 0
FOR gnCount = 1 to PARAMETERS()
   gcCompare = 'gnPara' +(STR(gnCount,1))
   gnResult = gnResult + EVAL(gcCompare)
ENDFOR
gnResult = gnResult / (gnCount - 1)
RETURN gnResult
```
