# Rotina de biblioteca de API _Dialog( )

Exibe na tela uma caixa de diálogo que tem o esquema de cores especificado e contém o texto do corpo e o texto dos botões especificados.

```foxpro
int _Dialog(int scheme, char FAR *body_text, char FAR *button1,
            char FAR *button2, char FAR *button3, int default, int
 escape)
int scheme;                  /* Color scheme number. */
char FAR *body_text;         /* Text in dialog. */
char FAR *button1;         /* Button prompt. */
char FAR *button2;         /* Button prompt. */
char FAR *button3;         /* Button prompt. */
int default;                  /* Number of the default button. */
int escape;                  /* Number of the button to press if Esc. */
```

# Observações

_Dialog( ) retorna o número do botão que o usuário escolhe.

Para especificar menos de três botões para a caixa de diálogo exibida, especifique 0 como prompt de botão para deixar qualquer um dos três botões em branco. O parâmetro default especifica qual botão destacar na caixa de diálogo como botão padrão, e o parâmetro escape especifica qual botão processar como escolhido se o usuário pressionar ESC.

Se você não especificar botões, o Visual FoxPro exibe a caixa de diálogo e aguarda que o usuário pressione uma tecla ou clique o botão esquerdo do mouse. Se o usuário pressionar Esc, _Dialog( ) retorna o valor escape; caso contrário, retorna o valor default.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria quatro caixas de diálogo com três, duas, uma e nenhum botão.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DIALOG
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
   _PutValue(&val);
}
void FAR dialogEx(ParamBlk FAR *parm)
{
   int selection;
   selection = _Dialog(DIALOG_SCHEME, "Example dialog with 3 buttons.",
      "First", "Second", "Third", 2, 3);
   _PutStr("\nItem selected ="); putLong(selection);
   selection = _Dialog(DIALOG_SCHEME, "Example dialog with 2 buttons.",
      "First", "Second", 0, 2, 2);
   _PutStr("\nItem selected ="); putLong(selection);
   selection = _Dialog(DIALOG_SCHEME, "Example dialog with 1 button.",
      "First", (char *)0, (char *)0, 1, 1);
   _PutStr("\nItem selected ="); putLong(selection);
   selection = _Dialog(DIALOG_SCHEME, "Example dialog no buttons.",
      (char *)0, (char *)0, (char *)0, 1, 2);
   _PutStr("\nItem selected ="); putLong(selection);
}
FoxInfo myFoxInfo[] = {
   {"DIALOGEX", (FPFI) dialogEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
