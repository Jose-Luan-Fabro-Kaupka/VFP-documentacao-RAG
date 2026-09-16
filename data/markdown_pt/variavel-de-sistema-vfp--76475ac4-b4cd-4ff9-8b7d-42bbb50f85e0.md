# Variável de sistema _VFP

Referencia o objeto Application para a instância atual do Visual FoxPro. Existem duas versões da sintaxe.

```foxpro
_VFP.PropertyName[ = eValue]
```

```foxpro
_VFP.Method
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade para o objeto de aplicação.
**eValue**
Especifica um valor para a propriedade.
**Method**
Especifica um método a executar para o objeto de aplicação.

# Observações

Aplica-se a: Projects Collection (Visual FoxPro)

_VFP fornece acesso às coleções Objects e Projects.

A partir do Visual FoxPro 7, as propriedades Top, Height, Left, Width e hWnd de _VFP se aplicam apenas às propriedades da janela principal do Visual FoxPro. Em versões anteriores do Visual FoxPro, as propriedades Height e Width referiam-se às da área de cliente do Visual FoxPro (área onde o texto pode ser exibido). Agora, as propriedades Top, Height, Left e Width de _SCREEN são as da área de cliente do Visual FoxPro.
