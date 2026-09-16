# Comando SET KEYCOMP

Controla a navegação por teclas do Visual FoxPro.

```foxpro
SET KEYCOMP TO DOS | WINDOWS
```

# Observações

SET KEYCOMP determina as teclas e combinações de teclas que você usa para mover-se pela interface do Visual FoxPro acessando controles como botões, caixas de listagem, menus e assim por diante. O efeito de SET KEYCOMP depende do controle.

Use SET KEYCOMP quando desejar usar teclas familiares para você.

Para navegar no Microsoft Windows usando teclas MS-DOS, emita o seguinte:

```foxpro
SET KEYCOMP TO DOS
```

Você pode especificar a opção DOS ou WINDOWS (padrão).

Você pode especificar uma configuração inicial de SET KEYCOMP em seu arquivo de configuração do Visual FoxPro, Config.fpw. Por exemplo, a seguinte linha, quando colocada em seu arquivo de configuração, tem o efeito de SET KEYCOMP TO DOS:

```foxpro
KEYCOMP = DOS
```

Esta seção descreve como as opções DOS e WINDOWS afetam o Visual FoxPro.

| Botões padrão | |
| --- | --- |
| DOS | O botão padrão em uma caixa de diálogo tem o foco; sua aparência não muda. Ele é escolhido quando você pressiona CTRL+ENTER. |
| WINDOWS | O botão padrão em uma caixa de diálogo pode mudar de aparência quando você se move entre controles. Ele pode ficar esmaecido ou ter o foco (é cercado por uma borda em negrito) para indicar que é o padrão atual. Ele é escolhido quando você pressiona ENTER. Pressionar ENTER sempre executa a ação do botão padrão. |

Para uma ilustração de como o botão padrão muda de aparência em uma caixa de diálogo, emita SET KEYCOMP TO WINDOWS, escolha Open no menu File e então pressione TAB para mover-se pela caixa de diálogo Open.

| Teclas de acesso | |
| --- | --- |
| DOS | Uma tecla de acesso para um controle é uma única tecla. Se você não estiver em um controle que tenha direcionamento por teclado (uma combo box ou uma list box), pode pressionar a tecla de acesso para escolhê-lo. |
| WINDOWS | Uma tecla de acesso para um controle pode ser uma única tecla ou uma combinação de teclas. Se o controle atual tiver direcionamento por teclado (uma combo box ou uma list box), pode pressionar ALT mais a tecla de acesso para escolher o controle. Para escolher outros controles, pode pressionar a tecla de acesso ou ALT mais a tecla de acesso. |

| Combo boxes | |
| --- | --- |
| DOS | Quando uma combo box tem o foco, você pode abri-la pressionando ENTER ou a BARRA DE ESPAÇO. O direcionamento por teclado dentro de uma combo box não está disponível até que a combo box esteja aberta. |
| WINDOWS | Quando uma combo box tem o foco, você pode abri-la pressionando a BARRA DE ESPAÇO, ALT+SETA PARA CIMA ou ALT+SETA PARA BAIXO. O direcionamento por teclado dentro de uma combo box está disponível quando a combo box tem o foco e quando está aberta. Por exemplo, uma combo box selecionada contém uma lista de unidades disponíveis. Se as unidades A, B e C estiverem disponíveis e a unidade B estiver exibida atualmente, você pode escolher a unidade C sem abrir a combo box pressionando C ou a tecla SETA PARA BAIXO. A unidade C é escolhida e você passa para o próximo controle. |

| Botões de opção | |
| --- | --- |
| DOS | Pressione a tecla TAB quando um grupo de botões de opção estiver selecionado para mover-se entre os botões de opção. |
| WINDOWS | Pressione a tecla TAB quando um grupo de botões de opção estiver selecionado para mover-se dos botões de opção para o próximo controle. Para mover-se entre um conjunto de botões de opção, pressione as teclas SETA PARA CIMA e SETA PARA BAIXO. |

| Janela Browse | |
| --- | --- |
| DOS | Um campo não é selecionado ao entrar no campo. |
| WINDOWS | Um campo é automaticamente selecionado ao entrar no campo. |
