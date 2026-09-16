# Exemplo Add New Items to a Combo Box

Arquivo: ...\Samples\Solution\Controls\Combobox\Lookup.scx

Este exemplo ilustra como adicionar texto inserido pelo usuário a um drop-down de combo box e fornecer capacidade de lookup.

# Adicionar texto do usuário a um drop-down de Combo Box

Um combo box permite que um usuário insira texto ou selecione um item de uma lista drop-down. Você também pode adicionar o texto que um usuário digita no combo box como um novo item na lista drop-down, para que o usuário não precise digitar o mesmo texto várias vezes.

Existem várias formas de adicionar texto do usuário à lista drop-down de um combo box, dependendo da configuração da propriedade RowSourceType do combo box. Neste exemplo, o RowSourceType dos combo boxes é 1 - Value. Se o valor que o usuário insere ainda não está na lista drop-down de cboCombo, o código a seguir adiciona uma vírgula e o novo valor ao RowSource:

```foxpro
cCountryName = ALLTRIM(Custs.Country)
IF ATC(m.cCountryName,THIS.RowSource)=0 AND !EMPTY(m.cCountryName)
   THIS.RowSource=THIS.RowSource+","+m.cCountryName
ENDIF
```

O combo box no exemplo Manipulate Text Programmatically Sample tem um RowSourceType de 0 - None. O código a seguir no evento Valid de cboSearchString em ...\Samples\Solution\Controls\TXT_EDT\Text.scx adiciona um valor inserido pelo usuário à lista drop-down do combo box:

```foxpro
IF !EMPTY(THIS.Text)
   FOR i = 1 TO THIS.ListCount
      IF THIS.List(i) = THIS.Text
         RETURN
      ENDIF
   ENDFOR
   THIS.AddItem(THIS.Text)
ENDIF
```

Se o RowSource do combo box é uma matriz, você precisa adicionar o texto do usuário à matriz e chamar o método Requery do combo box.

Se o RowSource é uma tabela ou um cursor, você precisa adicionar um registro, REPLACE o campo em branco com o valor inserido pelo usuário e Requery o combo box.

# Fornecer capacidade de lookup

Além de ilustrar como adicionar itens a um combo box, este exemplo demonstra três formas de permitir que um usuário filtre uma tabela para valores específicos. Um usuário pode fazer o seguinte:
 - Inserir valores em um combo box.
- Selecionar um item de uma lista drop-down.
- Inserir valores parciais em um combo box para pesquisa incremental.

### Inserir valores em um Combo Box

O código principal está associado ao evento LostFocus de cboCombo. Depois de garantir que o usuário inseriu um valor, o código LostFocus seleciona os registros que correspondem ao texto do usuário e define a propriedade RecordSource da grade para o conjunto de resultados.

```foxpro
cDisplayValue = ALLTRIM(THIS.DisplayValue)
IF THIS.Value = "(All)"
   SELECT country AS location,* FROM CUSTOMER;
      INTO CURSOR Custs
   thisform.grdcust.recordsource = "Custs"
ELSE
   SELECT country AS location,* FROM CUSTOMER ;
    WHERE UPPER(ALLTRIM(Customer.Country)) = UPPER(m.cDisplayValue);
    INTO CURSOR Custs
   THISFORM.grdCust.RecordSource = "Custs"
ENDIF
```

### Selecionar um item de uma lista drop-down

Basicamente o mesmo código de lookup está associado ao evento InteractiveChange de cboDrop – se o Value do combo box é "(All)", seleciona todos os registros no cursor; caso contrário, seleciona os registros que correspondem à escolha do usuário.

### Inserir valores parciais para pesquisa incremental

O código no evento InteractiveChange de cboIntSearch executa o lookup cada vez que o usuário digita um caractere no combo box.

```foxpro
#DEFINE DELKEY 127
LPARAMETERS nKeyCode, nShiftAltCtrl
LOCAL cDisplayValue
IF nKeyCode = DELKEY
   cDisplayValue = ALLTRIM(THIS.DisplayValue)
   IF LEN(m.cDisplayValue)=1
      cDisplayValue = ""
   ELSE
      cDisplayValue = LEFT(cDisplayValue,LEN(cDisplayValue)-1)
   ENDIF
ELSE
   cDisplayValue = ALLTRIM(THIS.DisplayValue)+CHR(nKeyCode)
ENDIF
THISFORM.LockScreen = .T.
DO CASE
CASE EMPTY(m.cDisplayValue)
   THISFORM.grdCust.RecordSource = " "
CASE THIS.Value = "(All)"
   SELECT country AS location,* FROM CUSTOMER;
      INTO CURSOR Custs
   THISFORM.grdCust.RecordSource = "Custs"
OTHERWISE
   SELECT country AS location,* FROM CUSTOMER ;
    WHERE UPPER(ALLTRIM(Customer.Country)) = UPPER(m.cDisplayValue);
    INTO CURSOR Custs
   THISFORM.grdCust.RecordSource = "Custs"
ENDCASE
THISFORM.ResetCombos(THIS)
THISFORM.LockScreen = .F.
```
