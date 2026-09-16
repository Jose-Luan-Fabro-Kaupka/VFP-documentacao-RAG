# Exemplo Format Input and Validate Data in a Text Box

Arquivo: ...\Samples\Solution\Controls\TXT_EDT\Textbox.scx

Este exemplo mostra como definir propriedades de text box para facilitar a entrada de dados pelo usuário no formato exigido.

| Format | Property | Setting |
| --- | --- | --- |
| Allow Only Digits | InputMask | 999999999 |
| Select On Entry | SelectOnEntry | .T. |
| All Uppercase | Format | ! |
| Read-Only | ReadOnly | .T. |
| US Telephone Number | InputMask | (999) 999-9999 |
| Password text | PasswordChar | * |
| Date Formatting | DateFormat | a number between 0 and 14 |

# Validating Input

O código a seguir no evento Valid de um text box impede que o usuário saia do text box se a letra "a" estiver no texto:

```foxpro
IF "a"$ THIS.Value
   #DEFINE MESSAGE_LOC "The text box value cannot contain the letter 'a'"
   MESSAGEBOX(MESSAGE_LOC,48+0+0)
   RETURN 0
ELSE
   RETURN .T.
ENDIF
```
