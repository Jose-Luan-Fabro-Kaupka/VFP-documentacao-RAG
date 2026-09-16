# Amostra Criar um Formulário SDI

Arquivo: ...\Samples\Solution\Forms\Sdiform.scx

Esta amostra ilustra o suporte do Visual FoxPro a formulários SDI. Para criar um formulário SDI, basta definir a propriedade ShowWindow do formulário como 2 – s Top-Level Form. Formulários SDI não exigem que a janela do Visual FoxPro esteja visível.

# Adicionando Formulários

Existem duas maneiras de adicionar formulários a um formulário Top-Level (SDI). A primeira e mais fácil é criar um novo formulário e definir sua propriedade ShowWindow como 1 (In Top-Level form). Embora isso possa parecer o mais apropriado, nem sempre é a melhor solução porque a propriedade ShowWindow só pode ser definida em tempo de design.

Outro método é usar o comando ACTIVATE WINDOW. O código abaixo, da amostra SDIForm, mostra exatamente isso. Como este comando não é baseado em objetos, você deve referenciar um formulário pelo seu nome de janela (propriedade Name).

```foxpro
ACTIVATE WINDOW (thisform.oWindows[m.nGetWin].NAME) ;
IN WINDOW (thisform.name)
```

# Adicionando Menus

Menus também podem ser adicionados a formulários SDI. Agora há uma nova caixa de seleção Top-Level Form no menu View do Menu Designer, na caixa de diálogo General Options. Um menu Top-Level Form será gerado se você marcar essa opção e pode ser chamado conforme mostrado aqui.

```foxpro
DO sdiform.mpr WITH THISFORM,.T.
```

> **Observação:** Se itens de menu do sistema dependem da janela principal do Visual FoxPro estar visível, eles não produzirão os resultados esperados quando a janela principal do Visual FoxPro estiver oculta.

# Adicionando Barras de Ferramentas

Além de menus e janelas, você também pode adicionar barras de ferramentas aos seus formulários SDI. Barras de ferramentas são objetos como formulários; portanto, você pode aproveitar o modelo de objetos do Visual FoxPro e manter essa barra de ferramentas no escopo do formulário. A amostra de formulário SDI usa uma propriedade personalizada para criar e manter a barra de ferramentas no escopo.

```foxpro
SET CLASSLIB TO sditbar ADDITIVE
thisform.oToolbar=create("sditb1")
thisform.oToolbar.show
```
