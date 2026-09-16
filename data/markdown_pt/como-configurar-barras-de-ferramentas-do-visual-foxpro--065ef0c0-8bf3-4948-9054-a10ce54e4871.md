# Como: configurar barras de ferramentas do Visual FoxPro

O Visual FoxPro inclui as seguintes barras de ferramentas personalizáveis.

| Ferramenta | Barras de ferramentas associadas | Comando |
| --- | --- | --- |
| Database Designer | Database | CREATE DATABASE |
| Form Designer | Form Controls Form Designer Color Palette Layout | CREATE FORM |
| Print Preview | Print Preview | |
| Query Designer | Query Designer | CREATE QUERY |
| Report Designer | Report Controls Report Designer Color Palette Layout | CREATE REPORT |

Você pode colocar na tela quantas barras de ferramentas precisar durante o trabalho. É possível acoplá-las à parte superior, inferior ou às laterais da tela para personalizar o ambiente de trabalho. O Visual FoxPro salva as posições das barras de ferramentas para que elas permaneçam onde foram colocadas pela última vez.

### Para acoplar uma barra de ferramentas
- Arraste a barra de ferramentas para a parte superior, inferior ou lateral da tela. -OU-
- Use o comando DOCK para acoplar a barra de ferramentas.

# Ativando e desativando barras de ferramentas

Por padrão, somente a barra de ferramentas Standard fica visível. Quando você usa uma ferramenta de design do Visual FoxPro (por exemplo, o Form Designer), o designer exibe as barras de ferramentas normalmente necessárias ao trabalhar com essa ferramenta. Entretanto, você pode ativar uma barra de ferramentas sempre que precisar.

### Para ativar uma barra de ferramentas
- Execute a ferramenta associada. –OU–

### Para desativar uma barra de ferramentas
- Feche a ferramenta associada. –OU–

Você também pode ativar e desativar programaticamente barras de ferramentas que já tenham sido ativadas usando os comandos DEACTIVATE WINDOW ou ACTIVATE WINDOW, como no exemplo a seguir.

```foxpro
IF WVISIBLE ("Color Palette")
DEACTIVATE WINDOW("Color Palette")
ENDIF
```

# Personalizando barras de ferramentas existentes

A maneira mais fácil de criar barras de ferramentas personalizadas é modificar as barras já fornecidas com o Visual FoxPro. Você pode:
 - Modificar uma barra de ferramentas existente adicionando ou removendo botões.
- Criar uma nova barra de ferramentas que contenha botões de barras existentes.

Você também pode definir barras de ferramentas personalizadas criando uma classe de barra de ferramentas personalizada usando código. Para obter detalhes, consulte Criando menus e barras de ferramentas.

Você pode modificar qualquer uma das barras de ferramentas fornecidas com o Visual FoxPro. Por exemplo, talvez queira remover um botão de uma barra existente ou copiar botões de uma barra para outra.

### Para modificar uma barra de ferramentas existente do Visual FoxPro
- No menu View, escolha Toolbars.
- Selecione a barra de ferramentas que deseja personalizar e escolha Customize.
- Remova botões da barra de ferramentas arrastando-os para fora dela.
- Adicione botões à barra selecionando uma categoria apropriada na caixa de diálogo Customize Toolbar e arrastando os botões apropriados para a barra.
- Conclua a barra de ferramentas escolhendo Close na caixa de diálogo Customize Toolbar e fechando a janela da barra. Dica: se você alterar uma barra de ferramentas do Visual FoxPro, poderá restaurar a configuração original dos botões selecionando-a na caixa de diálogo Toolbar e escolhendo Reset.

Você pode criar suas próprias barras de ferramentas compostas por botões de outras barras.

### Para criar sua própria barra de ferramentas
- No menu View, escolha Toolbars.
- Escolha New.
- Na caixa de diálogo New Toolbar, dê um nome à barra de ferramentas.
- Adicione botões à barra selecionando uma categoria na caixa de diálogo Customize Toolbar e arrastando os botões apropriados para a barra.
- Você pode reorganizar os botões na barra arrastando-os para a posição desejada.
- Conclua a barra de ferramentas escolhendo Close na caixa de diálogo Customize Toolbar e fechando a janela da barra. Observação: não é possível redefinir os botões de uma barra de ferramentas criada por você.

### Para excluir uma barra de ferramentas criada por você
- No menu View, escolha Toolbars.
- Selecione a barra de ferramentas que deseja excluir.
- Escolha Delete.
- Escolha OK para confirmar a exclusão. Observação: não é possível excluir as barras de ferramentas fornecidas pelo Visual FoxPro.
