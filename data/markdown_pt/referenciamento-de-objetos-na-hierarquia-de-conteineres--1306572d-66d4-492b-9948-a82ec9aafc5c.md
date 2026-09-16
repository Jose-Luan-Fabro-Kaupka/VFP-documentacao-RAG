# Referenciamento de objetos na hierarquia de contêineres

O contêiner e a hierarquia de classes são duas entidades separadas. Os objetos são referenciados na hierarquia de contêineres, enquanto o Visual FoxPro busca o código de evento subindo pela hierarquia de classes.

Para manipular um objeto, você precisa identificá-lo em relação à hierarquia de contêineres. Por exemplo, para manipular um controle em um formulário em um conjunto de formulários, você precisa referenciar o conjunto de formulários, o formulário e, em seguida, o controle.

Você pode comparar a referência de um objeto dentro de sua hierarquia de contêineres a fornecer ao Visual FoxPro um endereço para seu objeto. Quando você descreve a localização de uma casa para alguém fora de seu quadro de referência imediato, você precisa indicar o país, o estado ou região, a cidade, a rua ou apenas o número da rua da casa, dependendo da distância. Caso contrário, pode haver confusão.

A ilustração a seguir mostra uma possível situação de aninhamento de contêineres.
 Contêineres aninhados

Para desabilitar o controle na coluna da grade, você precisa fornecer o seguinte endereço:

```foxpro
Formset.Form.PageFrame.Page.;
 Grid.Column.Control.Enabled = .F.
```

A propriedade ActiveForm do objeto de aplicação (_VFP) permite manipular o formulário ativo mesmo se você não conhecer o nome do formulário. Por exemplo, a seguinte linha de código altera a cor de fundo do formulário ativo, independentemente do conjunto de formulários ao qual pertence:

```foxpro
_VFP.ActiveForm.BackColor = RGB(255,255,255)
```

Da mesma forma, a propriedade ActiveControl permite manipular o controle ativo no formulário ativo. Por exemplo, a seguinte expressão digitada na Janela de Inspeção (Visual FoxPro) exibe o nome do controle ativo em um formulário conforme você seleciona interativamente os vários controles:

```foxpro
_VFP.ActiveForm.ActiveControl.Name
```

# Referenciamento relativo

Ao referenciar objetos dentro da hierarquia de contêineres (por exemplo, no evento Click de um botão de comando em um formulário em um conjunto de formulários), você pode usar alguns atalhos para identificar o objeto que deseja manipular. A tabela a seguir lista propriedades ou palavras-chave que facilitam a referência a um objeto dentro da hierarquia de objetos:

| Propriedade ou palavra-chave | Referência |
| --- | --- |
| Parent | O contêiner imediato do objeto. |
| THIS | O objeto. |
| THISFORM | O formulário que contém o objeto. |
| THISFORMSET | O conjunto de formulários que contém o objeto. |

> **Observação:** Você pode usar THIS, THISFORM e THISFORMSET apenas em código de método ou evento.

A tabela a seguir fornece exemplos de uso de THISFORMSET, THISFORM, THIS e Parent para definir propriedades de objetos:

| Comando | Onde incluir o comando |
| --- | --- |
| THISFORMSET.frm1.cmd1.Caption = "OK" | No código de evento ou método de quaisquer controles em qualquer formulário do conjunto de formulários. |
| THISFORM.cmd1.Caption = "OK" | No código de evento ou método de qualquer controle no mesmo formulário em que cmd1 está. |
| THIS.Caption = "OK" | No código de evento ou método do controle cuja legenda você deseja alterar. |
| THIS.Parent.BackColor = RGB(192,0,0) | No código de evento ou método de um controle em um formulário. O comando altera a cor de fundo do formulário para vermelho escuro. |
