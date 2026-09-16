# Propriedade AutoHideScrollBar

Mostra ou oculta a barra de rolagem em um controle ListBox. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** Se a list box estiver vazia ou se todos os itens na list box estiverem visíveis, a barra de rolagem não é exibida.

```foxpro
ListBox.AutoHideScrollBar [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor que determina quando uma barra de rolagem é visível em uma list box. A tabela a seguir lista os valores de nValue. nValue Descrição 0 Sempre mostrar barra de rolagem. (Padrão) 1 Mostrar barra de rolagem somente se os itens na list box não puderem ser exibidos completamente.

# Observações

Aplica-se a: controle ListBox

Ao desenhar barras de rolagem, o Visual FoxPro respeita a configuração da propriedade IntegralHeight.

# Exemplo

O exemplo a seguir cria uma list box em um formulário e especifica um array como origem dos itens na list box. Na classe de list box definida pelo usuário, lstMyListbox, a propriedade AutoHideScrollBar é definida como 1 para que a barra de rolagem apareça somente se o número de itens na list box não puder ser exibido completamente. Redimensione o formulário para ajustar o tamanho da list box.

As etapas executadas neste exemplo são as seguintes:
 - Limpar a janela principal do Visual FoxPro usando o comando CLEAR.
- Criar um array chamado gaMyListArray usando o comando DIMENSION.
- Preencher o array com letras usando os comandos FOR...ENDFOR e STORE.
- Criar um formulário usando a função CREATEOBJECT( ).
- Adicionar um controle CommandButton baseado na classe definida pelo usuário cmdMyCmdButton chamando o método AddObject.
- Adicionar um controle ListBox baseado na classe personalizada lstMyListBox chamando o método AddObject.
- Especificar um array como tipo de origem de linha da list box definindo a propriedade RowSourceType como 5 (Array).
- Especificar o array gaMyListArray como origem de linha da list box definindo a propriedade RowSource.
- Mostrar o botão de comando definindo a propriedade Visible.
- Mostrar a list box definindo a propriedade Visible.
- Exibir o formulário chamando o método Show do formulário.
- Iniciar o processamento de eventos chamando o comando READ EVENTS.
- Definir a classe definida pelo usuário cmdMyCmdButton baseada no controle CommandButton usando o comando DEFINE CLASS. O código no comando DEFINE CLASS define propriedades para a classe definida pelo usuário e define procedimentos.
- Definir a classe definida pelo usuário lstMyListBox baseada no controle ListBox usando o comando DEFINE CLASS. O código no comando DEFINE CLASS define propriedades para a classe definida pelo usuário e define procedimentos.

```foxpro
CLEAR
DIMENSION gaMyListArray(10)
FOR gnCount = 1 to 10
   STORE REPLICATE(CHR(gnCount+64),6) TO gaMyListArray(gnCount)
NEXT
frmMyForm = CREATEOBJECT('Form')
frmMyForm.AddObject('cmbCommand1','cmdMyCmdBtn')
frmMyForm.AddObject('lstListBox1','lstMyListBox')
frmMyForm.lstListBox1.RowSourceType = 5
frmMyForm.lstListBox1.RowSource = 'gaMyListArray'
frmMyForm.cmbCommand1.Visible =.T.
frmMyForm.lstListBox1.Visible =.T.
frmMyForm.Show
READ EVENTS
DEFINE CLASS cmdMyCmdBtn AS CommandButton
   Caption = '\<Quit'
   Cancel = .T.
   Left = 125
   Top = 210
   Height = 25
   PROCEDURE Click
      CLEAR EVENTS
      CLEAR
ENDDEFINE
DEFINE CLASS lstMyListBox AS ListBox
   Left = 10
   Top = 30
   Anchor = 5
   AutoHideScrollBar = 1
ENDDEFINE
```
