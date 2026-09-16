# Propriedade MacDesktop

Especifica se um formulário é colocado na janela principal do Visual FoxPro. Incluída para compatibilidade com versões anteriores.

```foxpro
Object.MacDesktop[ = nValue]
```

# Valores da propriedade
 **nValue**
Configurações da propriedade MacDesktop: 0 (Padrão) Automático. O formulário fica contido na janela principal do Visual FoxPro conforme SET MACDESKTOP. Se estiver ON, o formulário existe no nível da área de trabalho do Macintosh; se estiver OFF, fica na janela principal. 1 Área de trabalho do Macintosh. O formulário pode ser movido e redimensionado independentemente da janela principal. 2 Área de trabalho do Visual FoxPro. O formulário fica contido na janela principal e não pode ser movido para fora dela.

# Observações

Aplica-se a: objeto Form

A propriedade MacDesktop permite substituir, para formulários individuais, a configuração estabelecida com SET MACDESKTOP. SET MACDESKTOP afeta janelas definidas pelo usuário e janelas do sistema, como Browse, View e Form Designer. Por padrão, as janelas definidas pelo usuário seguem essa configuração.

MacDesktop permite controlar se os aplicativos se assemelham a aplicativos do Macintosh ou do Windows.
