# Exemplo Run Multiple Instances of a Form

Arquivo: ...\Samples\Solution\Forms\Launch.scx

Este exemplo demonstra a execução de várias instâncias de um formulário. `aForms` é uma propriedade de matriz do formulário que lança as várias instâncias. O código a seguir está associado ao evento Click do botão de comando que lança vários formulários:

Obter o número do último elemento na matriz

```foxpro
nInstance = ALEN(THISFORM.aForms)
```

Determinar as propriedades Top e Left para cascatear os novos formulários. Essas configurações são passadas como parâmetros quando as instâncias do formulário são lançadas.

```foxpro
IF nInstance > 1 AND ;
   TYPE('THISFORM.aForms[nInstance -1]') = 'O'
   nFormTop = THISFORM.aForms[nInstance -1].Top + 1
   nFormLeft = THISFORM.aForms[nInstance -1].Left + 1
ELSE
   nFormTop = 1
   nFormLeft = 1
ENDIF
```

Definir o caption para refletir o número da instância

```foxpro
cFormCaption = "Instance" + ALLTRIM(STR(nInstance))
```

Executar o formulário e atribuir a variável de objeto ao elemento da matriz. A palavra-chave Linked indica que todas as instâncias serão liberadas quando a matriz for liberada. Sem `LINKED`, os formulários de múltiplas instâncias persistiriam após a matriz ser liberada.

```foxpro
DO FORM Multi NAME THISFORM.aForms[nInstance] WITH ;
   nFormTop, nFormLeft, cFormCaption LINKED
```

Redimensionar a matriz para que mais instâncias do formulário possam ser lançadas.

```foxpro
DIMENSION THISFORM.aForms[nInstance + 1]
```
