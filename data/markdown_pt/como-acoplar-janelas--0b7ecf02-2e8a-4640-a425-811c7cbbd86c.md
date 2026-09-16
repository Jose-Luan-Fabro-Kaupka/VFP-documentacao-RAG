# Como: acoplar janelas

Você pode acoplar determinadas janelas do Ambiente de Desenvolvimento Integrado (IDE) do Visual FoxPro à janela da área de trabalho do Visual FoxPro, entre si ou a formulários definidos pelo usuário. As seguintes janelas podem ser acopladas:
- Call Stack
- Command
- Data Session (View)
- Debugger
- Document View
- Locals
- Output
- Properties
- Trace
- Watch

> **Observação:** Historicamente, nas versões anteriores do Visual FoxPro, a janela Data Session sempre foi chamada de janela View. Além disso, a linguagem usada para controlar essa janela, como HIDE WINDOW, ACTIVATE WINDOW e WONTOP( ), também se refere a ela como janela View.

Quando você arrasta uma janela acoplável até um limite da janela da área de trabalho do Visual FoxPro, ela se reposiciona junto ao limite escolhido. O estado e o local das janelas acopladas são mantidos desde a última sessão do usuário.

Para acoplar janelas programaticamente e obter seus estados de acoplamento, consulte Comando DOCK e Função ADOCKSTATE( ).

Você pode alterar o estado acoplável de uma janela.

### Para ativar ou desativar o estado acoplável
- Clique com o botão direito do mouse na barra de título de uma janela aberta e acoplável.
- Clique em Dockable para ativar ou desativar o estado acoplável da janela. Uma marca de seleção aparecerá quando a janela for acoplável. -OU-
- Clique na janela desejada para torná-la ativa.
- No menu Window, clique em Dockable para ativar ou desativar o estado acoplável da janela. Uma marca de seleção aparecerá quando a janela for acoplável.

Para obter mais informações sobre como obter programaticamente o estado acoplável de uma janela, consulte Função WDOCKABLE( ).

# Modos de acoplamento

Você pode acoplar janelas em três modos diferentes:
- Acoplamento normal: as janelas são acopladas a um limite da janela da área de trabalho do Visual FoxPro.
- Acoplamento vinculado: as janelas são acopladas umas às outras e compartilham um contêiner de janelas acopláveis.
- Acoplamento com guias: as janelas são acopladas umas às outras e compartilham toda a janela por meio de guias.

Você pode usar o acoplamento com guias e o acoplamento vinculado em conjunto.

### Para criar um acoplamento normal
- Verifique se o estado de acoplamento da janela ou das janelas está definido como Dockable.
- Arraste a barra de título da janela até um limite da janela da área de trabalho do Visual FoxPro.

### Para criar um acoplamento vinculado
- Verifique se o estado de acoplamento da janela ou das janelas está definido como Dockable.
- Arraste a barra de título da janela desejada até um limite ou uma zona de acoplamento da janela de destino.

A zona de acoplamento é indicada quando a janela que você está arrastando muda de forma para se ajustar à janela de destino. O Visual FoxPro cria uma barra de título adicional para janelas acopladas por vínculo.

### Para criar um acoplamento com guias
- Verifique se o estado de acoplamento da janela ou das janelas está definido como Dockable.
- Arraste a barra de título da janela desejada até a barra de título da janela de destino.

O Visual FoxPro adiciona guias ao limite inferior das janelas acopladas.

### Para desacoplar janelas
- Para desacoplar janelas acopladas normalmente, arraste a barra de título da janela desejada para longe do limite compartilhado. -ou-
- Para desacoplar janelas acopladas por vínculo, arraste a barra de título da janela desejada para longe da janela compartilhada. -ou-
- Para desacoplar janelas acopladas por guia, arraste a guia da janela desejada para longe da janela compartilhada.

Você pode desativar o comportamento de acoplamento mantendo pressionada a tecla CTRL enquanto arrasta uma janela.

Excluir ou editar o arquivo de recursos FoxUser.dbf, que contém suas configurações, restaura ou altera as configurações padrão das janelas. Para obter mais informações sobre como alterar as configurações, consulte Estrutura do arquivo de recursos FoxUser.
