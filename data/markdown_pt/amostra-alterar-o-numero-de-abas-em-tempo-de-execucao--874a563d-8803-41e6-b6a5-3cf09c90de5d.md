# Amostra Alterar o Número de Abas em Tempo de Execução

Arquivo: ...\Samples\Solution\Controls\Pgframe\Pfsam1.scx

Esta amostra ilustra o uso de um page frame com abas. O número de abas muda dinamicamente quando o usuário escolhe um novo valor em um spinner. Quando o usuário seleciona uma aba, uma caixa de listagem exibe valores específicos da aba.

### Para alterar o número de abas em tempo de execução
- Defina a propriedade PageCount para o número desejado de páginas.

A caixa de listagem nesta amostra está posicionada no formulário, não em nenhuma das páginas do page frame. Este posicionamento permite ter um único controle visível em todas as suas páginas.

Dois métodos de formulário definidos pelo usuário definem as legendas nas abas e garantem que os valores na caixa de listagem correspondam: UpdateList e SetCaption.

# Método UpdateList

UpdateList é chamado quando o número de abas muda e quando o usuário seleciona uma nova aba.

```foxpro
LOCAL lnPage, lcHigh, lcLow
#define NO_MATCH_LOC 'No Matching Names for '
DIMENSION THISFORM.aCustomers[1,2]
lnPage = THISFORM.pgfRolodex.activepage
THISFORM.aCustomers[1,1] = NO_MATCH_LOC + ;
   THISFORM.pgfRolodex.Pages(lnPage).Caption
THISFORM.aCustomers[1,2] = ""
lcHigh = substr(THISFORM.pgfrolodex.Pages(lnPage).caption,3,1)
lcLow = substr(THISFORM.pgfrolodex.Pages(lnPage).caption,1,1)
SELECT company, phone FROM customer;
   WHERE company <= lcHigh and company => lcLow;
   ORDER BY company;
   INTO ARRAY THISFORM.aCustomers

THISFORM.lstCustomers.Requery
THISFORM.lstCustomers.Value = 1
```

# Método SetCaption

SetCaption é chamado nos eventos UpClick e DownClick do spinner para calcular quais legendas devem aparecer nas abas.

```foxpro
THISFORM.LockScreen = .T.
FOR n = 1 to THISFORM.pgfRolodex.PageCount
   FirstLetter = SUBSTR(THISFORM.Alphabet,((n - 1)*ROUND(LEN(THISFORM.Alphabet)/THISFORM.pgfRolodex.PageCount,0))+1,1)
   IF n = THISFORM.pgfRolodex.PageCount   &&last page
      LastLetter = right(THISFORM.Alphabet,1)
   ELSE
      LastLetter = SUBSTR(THISFORM.Alphabet,((n)*ROUND(LEN(THISFORM.Alphabet)/THISFORM.pgfRolodex.PageCount,0)),1)
   ENDIF
   THISFORM.pgfRolodex.Pages(n).Caption = FirstLetter + "-" + LastLetter
ENDFOR
THISFORM.LockScreen = .F.
```

Alphabet é uma propriedade de formulário definida pelo usuário usada para determinar as legendas de cada aba. Para obter a mesma funcionalidade em idiomas diferentes, defina a propriedade Alphabet como uma cadeia de caracteres contendo todas as letras do alfabeto do idioma de destino.
