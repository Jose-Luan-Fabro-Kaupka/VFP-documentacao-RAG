# Amostra Manipulate Text Programmatically

Arquivo: ...\Samples\Solution\Controls\TXT_EDT\Text.scx

Esta amostra ilustra o uso das propriedades SelStart, SelLength e SelText de uma caixa de edição para manipular o texto em tempo de execução. A amostra também conta os caracteres, palavras e parágrafos em um arquivo de texto e permite que um usuário pesquise uma cadeia de caracteres em um arquivo de texto.

# Formatando texto

O código a seguir está incluído no evento Click do botão que formata o texto selecionado em maiúsculas:

```foxpro
lo = THIS.Parent.edtText
lnOldStart = lo.SelStart
lnOldLength = lo.SelLength
lo.SelText = UPPER(lo.SelText)
lo.SelStart = lnOldStart
lo.SelLength = lnOldLength
```

Se você deseja especificar os atributos de fonte de seções selecionadas de texto, use um controle RichText.

# Pesquisando texto

Após obter o texto a ser pesquisado, o código a seguir percorre todo o texto na caixa de edição, comparando-o com a cadeia de caracteres de destino:

```foxpro
llKeepLooking = .T.
DO WHILE llKeepLooking
  FOR i = lnStart TO LEN(loEDT.Value)
    loEDT.SelStart = i
     loEDT.SelLength = lnLen
    IF loEDT.SelText = ALLTRIM(loCBO.Text) OR ;
         (!llCaseSensitive AND ;
         (UPPER(loEDT.SelText) = UPPER(ALLTRIM(loCBO.Text))))
      llFound = .T.
      llKeepLooking = .F.
      EXIT
    ENDIF
  ENDFOR
  IF !llFound
    lnChoice=MESSAGEBOX("Search string not found.", ;
        64+0+4)
    IF lnChoice = 6 && Yes
      llKeepLooking = .T.
      lnStart = 0
    ELSE
      llKeepLooking = .F.
    ENDIF
  ENDIF
ENDDO
```

> **Dica:** Certifique-se de definir a propriedade LockScreen do formulário como true (.T.) antes da pesquisa e false (.F.) após a pesquisa. Caso contrário, o formulário será repintado sempre que a propriedade SelStart da caixa de edição for alterada.
