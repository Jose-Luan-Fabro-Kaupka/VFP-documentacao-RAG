# Definindo propriedades de botões de opção

Para ajustar manualmente elementos individuais de um botão de opção ou grupo de botões de comando no Form Designer, escolha Edit no menu de atalho do grupo.

Você pode definir propriedades em botões individuais na Properties Window (Visual FoxPro). Você também pode definir essas propriedades em tempo de execução especificando o nome do botão de opção e a configuração de propriedade desejada. Por exemplo, a linha de código a seguir, incluída no código de método ou evento de algum objeto no mesmo formulário que o grupo de botões de opção, define o caption de `optCust` no grupo de botões de opção `opgChoices`:

```foxpro
THISFORM.opgChoices.optCust.Caption = "Sort by Customer"
```

Você também pode definir essas propriedades em tempo de execução usando a propriedade Buttons Property e especificando o número de índice do botão de opção no grupo. Por exemplo, se `optCust` é o terceiro botão no grupo, a linha de código a seguir também define o caption de `optCust`:

```foxpro
THISFORM.opgChoices.Buttons(3).Caption = "Sort by Customer"
```

Para definir propriedades em todos os botões de um grupo, use o método SetAll do grupo.

Por exemplo, a linha de código a seguir desabilita todos os botões em um grupo de botões de opção chamado `opgMyGroup` em um formulário:

```foxpro
THISFORM.opgMyGroup.SetAll("Enabled",.F., "OptionButton")
```

# Habilitando e desabilitando botões em um grupo

O exemplo anterior mostra como desabilitar programaticamente todos os botões de opção em um grupo. Quando os botões estão desabilitados, são exibidos nas cores especificadas nas propriedades DisabledBackColor, DisabledForeColor dos botões de opção. Você também poderia definir a propriedade Enabled Property (Visual FoxPro) do grupo de botões de opção como false (.F.) para desabilitar o grupo; no entanto, não haveria indicação visual para o usuário.

# Determinando qual botão de opção está selecionado

Você pode usar a propriedade Value Property do grupo de botões de opção para determinar qual botão de opção no grupo está selecionado. Se a fonte de controle do botão é numérica, você tem cinco botões de opção em um grupo. Se o terceiro botão está selecionado, a propriedade Value do grupo de botões de opção é 3; se nenhum botão de opção está selecionado, a propriedade Value do grupo de botões de opção é 0.

Você também pode determinar o caption do botão de opção selecionado usando as propriedades Value Property e Buttons Property do grupo. Por exemplo, a linha de código a seguir armazena a propriedade Caption Property (Visual FoxPro) do botão de opção selecionado em uma variável `cSelected`.

```foxpro
oGroup = THISFORM.opg1
cSelected = oGroup.Buttons(oGroup.Value).Caption
```

# Filtrando listas com botões de opção

Se você tem um pequeno conjunto de filtros de tabela predeterminados, pode usar botões de opção para permitir que os usuários alternem entre os filtros.

O exemplo a seguir assume um formulário com uma caixa de lista (`lstCustomers`) e um grupo de botões de opção que contém três botões de opção.
 Configurações de propriedade da caixa de lista
| Objeto | Propriedade | Configuração |
| --- | --- | --- |
| lstCustomers | RowSourceType | 2 - Alias |
| lstCustomers | RowSource | Customer |

Os filtros são definidos no código de evento Click dos botões de opção.
 Código de evento para filtrar uma lista quando os usuários escolhem um botão de opção
| Objeto | Evento | Código |
| --- | --- | --- |
| optAll | Click | SET FILTER TO GO TOP THISFORM.lstCustomers.Requery |
| optCanada | Click | SET FILTER TO customer.country = "Canada" GO TOP THISFORM.lstCustomers.Requery |
| optUK | Click | SET FILTER TO customer.country = "UK" GO TOP THISFORM.lstCustomers.Requery |

Quando o usuário fecha o formulário, não se esqueça de redefinir o filtro incluindo SET FILTER TO no evento Click do botão de fechamento ou no evento Destroy Event.

> **Dica:** Para atualizar uma lista quando a fonte da lista pode ter mudado, use o método Requery.
