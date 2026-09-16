# Propriedades DynamicBackColor, DynamicForeColor

Especifica as cores de fundo e de primeiro plano de um objeto Column. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicBackColor [= "cExpression"]
Column.DynamicForeColor [= "cExpression"]
```

# Valor de retorno
 **cExpression**
Especifica uma expressão de caracteres que é avaliada em tempo de execução para um único valor de cor. O valor da cor é reavaliado em tempo de execução sempre que o controle Grid é atualizado.

# Observações

Aplica-se a: Objeto Column

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar essas propriedades.

Você pode usar as propriedades DynamicBackColor e DynamicForeColor para criar efeitos especiais, como exibir as linhas de número ímpar em verde e as linhas de número par em cinza.

# Exemplo

O exemplo a seguir usa a propriedade DynamicBackColor e o método SetAll para especificar as cores de fundo dos registros em um controle Grid. Se o número de um registro exibido na grade é par, o DynamicBackColor do registro é branco; caso contrário, DynamicBackColor é verde.

Um controle Grid é colocado em um formulário, e a tabela `customer` é aberta e seu conteúdo exibido no Grid. A propriedade Caption é usada para especificar um cabeçalho diferente (Customer ID) para o campo CUST_ID. Um botão de comando é colocado no formulário para fechá-lo.

```foxpro
CLOSE ALL  && Close tables and databases
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  IN 0  && Opens Customer table
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .f.  && Disable the Control menu box
frmMyForm.AddObject('cmdCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject('grdGrid1','Grid')  && Add Grid control
frmMyForm.grdGrid1.Left = 25  && Adjust Grid position
frmMyForm.grdGrid1.SetAll("DynamicBackColor", ;
   "IIF(MOD(RECNO(), 2)=0, RGB(255,255,255) ;
   , RGB(0,255,0))", "Column")  && Alternate white and green records
frmMyForm.grdGrid1.Visible = .T.  && Grid control visible
frmMyForm.cmdCommand1.Visible =.T.  && "Quit" Command button visible
frmMyForm.grdGrid1.Column1.Header1.Caption = 'Customer ID'
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close Form
      CLOSE ALL  && Close table and database
ENDDEFINE
```
