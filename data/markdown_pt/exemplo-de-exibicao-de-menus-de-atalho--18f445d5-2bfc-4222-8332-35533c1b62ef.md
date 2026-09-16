# Exemplo de exibição de menus de atalho

Arquivo: ...\Samples\Solution\Menus\Shortcut.scx

Este exemplo ilustra a exibição de menus de atalho quando um usuário "clica com o botão direito" em um objeto. Depois de criar um menu de atalho no Designer de Menus, o código do formulário para ativar o menu é muito simples. O código a seguir está associado ao evento RightClick do formulário:

```foxpro
DO frmshort.mpr WITH THIS
```

O código a seguir está associado ao evento RightClick das caixas de edição do formulário:

```foxpro
DO edtshort.mpr WITH THIS
```

# O menu FRMSHORT

O menu FRMSHORT foi projetado para receber um parâmetro de objeto. O código a seguir está incluído no código de configuração do menu:

```foxpro
PARAMETER oREF
#PREPOP
```

A diretiva de geração `#PREPOP` faz com que o código da limpeza do menu seja gerado antes do comando ACTIVATE POPUP. Isso permite desabilitar ou habilitar itens de menu em tempo de execução, bem como exibir marcas de seleção ao lado dos itens de menu.

O código associado aos itens de menu define propriedades do objeto que foi passado ao .mpr como parâmetro. Por exemplo, o item Sempre visível define a propriedade AlwaysOnTop do formulário.

O código a seguir, incluído no código de limpeza do menu, exibe uma marca de seleção ao lado do item Sempre visível quando a propriedade AlwaysOnTop do formulário está definida como verdadeira (.T.).

```foxpro
SET MARK OF BAR 4 OF frmshort TO oRef.AlwaysOnTop
```

# O menu EDTSHORT

O menu EDTSHORT também aceita um parâmetro de objeto em seu código de configuração. Como não é necessário exibir uma marca de seleção ao lado dos itens desse menu, a diretiva de geração #PREPOP não é usada.

Para conhecer uma forma alternativa de exibir menus de atalho, consulte o exemplo Criar menus de atalho dinâmicos.
