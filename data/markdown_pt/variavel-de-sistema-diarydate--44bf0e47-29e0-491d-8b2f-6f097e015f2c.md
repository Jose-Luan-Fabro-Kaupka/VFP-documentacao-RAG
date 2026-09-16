# Variável de sistema _DIARYDATE

Contém a data atual no Calendar/Diary.

```foxpro
_DIARYDATE = dExpression
```

#### Parâmetros
 **dExpression**
Especifica a data para o Calendar/Diary.

# Observações

Com _DIARYDATE, você pode exibir o Calendar/Diary com uma data específica selecionada ou pode retornar a data selecionada do Calendar/Diary.

Por padrão, a data atual é armazenada em _DIARYDATE. Quando você abre o Calendar/Diary, a data atual é selecionada. Você pode armazenar uma data diferente em _DIARYDATE para que o Calendar/Diary abra com esta nova data selecionada.

Selecionar uma nova data quando o Calendar/Diary está aberto faz com que a nova data seja armazenada em _DIARYDATE. Quando você fecha o Calendar/Diary, _DIARYDATE contém a última data selecionada.

# Exemplo

No exemplo de programa a seguir, o Calendar/Diary abre com 28 de março de 2001 selecionado e o valor de _DIARYDATE aparece abaixo. 4 de julho de 1776 é então armazenado em _DIARYDATE e _DIARYDATE é exibido novamente. O programa então usa a função DATE( ) para selecionar a data atual e exibe _DIARYDATE.

```foxpro
SET CENTURY ON
STORE {^2001-03-28} TO _DIARYDATE
=MESSAGEBOX(DTOC(_DIARYDATE),64)
ACTIVATE WINDOW calendar
=MESSAGEBOX("Change date to July 4, 1776",48))
STORE {^1776-07-04} TO _DIARYDATE
=MESSAGEBOX(DTOC(_DIARYDATE),64)
=MESSAGEBOX("Change date to today's date",48)
STORE DATE() TO _DIARYDATE
=MESSAGEBOX(DTOC(_DIARYDATE),64)
RELEASE WINDOW calendar
```
