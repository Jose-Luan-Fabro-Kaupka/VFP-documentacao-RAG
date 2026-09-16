# Comando SET PALETTE

Especifica se a paleta de cores padrão do Visual FoxPro é usada.

```foxpro
SET PALETTE ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Restaura a paleta de cores padrão do Visual FoxPro.
**OFF**
Substitui a paleta de cores padrão do Visual FoxPro por paletas de cores dos gráficos .bmp e objetos OLE.

# Observações

Objetos OLE e gráficos .bmp podem conter paletas de cores que determinam como os gráficos e objetos aparecem quando são exibidos. A paleta de cores do primeiro gráfico ou objeto exibido é usada para todos os gráficos ou objetos subsequentes. Como uma única paleta de cores é usada para todos os gráficos e objetos, as cores de alguns dos gráficos e objetos podem ser alteradas de maneira inesperada.

A paleta de cores padrão do Visual FoxPro foi projetada para melhorar a aparência de exibição de vários gráficos .bmp e objetos OLE.
