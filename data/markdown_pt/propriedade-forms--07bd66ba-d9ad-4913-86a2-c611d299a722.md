# Propriedade Forms

Uma matriz para acessar formulários individuais em um conjunto de formulários. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.Forms(nIndex)
```

# Valor de retorno
 **nIndex**
Identifica exclusivamente um formulário em um conjunto de formulários.

# Observações

Aplica-se a: Objeto FormSet | Variável de sistema _SCREEN

Use a propriedade Forms para alterar as configurações de propriedades de formulários em um conjunto de formulários sem usar a propriedade Name dos formulários. Você pode usar a propriedade Forms em conjunto com a propriedade FormCount para percorrer todos os formulários de um conjunto e realizar uma ação. Por exemplo, o código a seguir altera as legendas de todos os formulários de um conjunto:

```foxpro
FOR x = 1 TO THISFORMSET.FormCount
   THISFORMSET.Forms(x).Caption = THISFORMSET.Forms(x).Caption;
      + "[Read Only]"
ENDFOR
```
