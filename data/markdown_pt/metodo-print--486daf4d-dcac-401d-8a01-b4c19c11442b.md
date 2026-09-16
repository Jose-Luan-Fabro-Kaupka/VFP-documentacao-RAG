# Método Print

Imprime uma cadeia de caracteres em um formulário.

```foxpro
 [FormSet.] Object.Print [(cText, iCurrentX, iCurrentY)]
```

#### Parâmetros
 **cText**
Especifica a cadeia de caracteres a imprimir. Se você omitir cText , uma linha em branco é impressa. Observação Este método não é suportado se BITMAP=OFF.
**iCurrentX**
Especifica a coordenada x para impressão.
**iCurrentY**
Especifica a coordenada y para impressão.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

A cadeia de caracteres é impressa no formulário, começando na posição especificada pelas propriedades CurrentX e CurrentY do formulário. Quando um retorno de carro é incluído, CurrentX é aumentado pela largura de cText (igual ao valor retornado por TextWidth) e CurrentY permanece inalterado.

Quando o método Print termina, as propriedades CurrentX e CurrentY são definidas para o ponto imediatamente após o último caractere impresso.

# Exemplo

O exemplo a seguir define um formulário que demonstra os parâmetros do método Print.

```foxpro
CLEAR
PUBLIC x
x=NEWOBJECT("frmSimpleForm")
x.visible=1
DEFINE CLASS frmSimpleForm as Form
   PROCEDURE init
      * generates ctext parameter of strings to print on the form
      * changes currentx and currenty parameters for the strings
      FOR i = 1 TO 10
         IF .t.
            thisform.Print(TRANSFORM(i),20*i,20*i)
         ELSE
            thisform.CurrentX=20*i
            thisform.CurrentY=20*i
            thisform.Print(TRANSFORM(i))
         ENDIF
      ENDFOR
ENDDEFINE
```
