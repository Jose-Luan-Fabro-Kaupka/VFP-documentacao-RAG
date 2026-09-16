# Como: acoplar barras de ferramentas

No Visual FoxPro, você pode acoplar barras de ferramentas do sistema ou definidas pelo usuário somente à janela principal do Visual FoxPro. Assim como nas janelas da IDE do Visual FoxPro, as barras de ferramentas sempre têm precedência quando são acopladas mais perto de uma borda.

As barras de ferramentas não oferecem suporte a acoplamento vinculado ou em guias. Não é possível acoplar outras janelas a barras de ferramentas. Barras de ferramentas nunca podem ser acopladas dentro de uma janela nem compartilhar a mesma área de acoplamento com um formulário.

### Para acoplar uma barra de ferramentas
- Arraste a barra de ferramentas para a parte superior da janela principal do Visual FoxPro. Ela será reposicionada junto ao limite escolhido. -OU-
- Chame o comando DOCK com os valores apropriados. -OU-
- Use o método Dock da barra de ferramentas.

Para obter mais informações, consulte Comando DOCK e Método Dock.

### Para desacoplar uma barra de ferramentas
- Mova o ponteiro do mouse sobre o lado esquerdo da barra até que ele se transforme em uma seta de movimentação.
- Arraste a barra para fora da janela principal do Visual FoxPro.
- -OU-
- Chame o comando DOCK com os valores apropriados. Você também pode usar o método Dock ou Move. Ao usar Move, as coordenadas especificadas devem ficar fora da área de acoplamento.

Para obter mais informações, consulte Método Move (Visual FoxPro).

Quando uma barra de ferramentas é acoplada à borda da janela principal do Visual FoxPro, sua barra de título fica oculta e sua borda muda para uma linha simples. A barra também é redimensionada para uma única linha de botões. A janela é redimensionada para que a barra não oculte informações na tela. Por exemplo, se ela for acoplada na parte superior, a tela será deslocada para baixo pela altura da barra.

Para obter mais informações sobre estado de acoplamento e código para eventos de acoplamento, consulte Acoplamento de formulários.
