# Como: configurar janelas Browse ou grids

Você pode alterar a configuração de uma janela browse ou grid das seguintes maneiras:
 - Reorganizando colunas
- Alterando larguras de colunas
- Ajustando colunas aos dados automaticamente
- Ativando e desativando linhas de grade
- Dividindo uma janela Browse
- Bloqueando colunas

Para obter mais informações, consulte Janela Browse e controle Grid.

# Reorganizando colunas

Você pode reorganizar colunas na ordem desejada.

> **Observação:** Reorganizar colunas não afeta a estrutura real da tabela.

### Para reorganizar uma coluna em uma janela browse
- Abra a tabela em uma janela browse.
- Insira o cursor na coluna que deseja mover.
- No menu Table, clique em Move Field. O cursor muda de forma para indicar que você pode mover a coluna.
- Para mover a coluna, pressione as teclas LEFT ARROW ou RIGHT ARROW.
- Quando terminar, pressione a tecla ENTER.

Você também pode arrastar o cabeçalho da coluna para o novo local.

### Para reorganizar uma coluna em um grid
- Arraste o cabeçalho da coluna para o novo local.

# Alterando larguras de colunas

Você pode alterar a largura de uma coluna.

> **Observação:** Redimensionar a largura da coluna não afeta o comprimento do campo nem a estrutura da tabela. Para alterar o comprimento real dos campos, modifique a estrutura da tabela usando o Table Designer.

### Para alterar a largura de uma coluna em uma janela browse
- Abra a tabela em uma janela browse.
- Insira o cursor em uma coluna que deseja redimensionar.
- No menu Table, clique em Size Field. O cursor muda de forma para indicar que você pode redimensionar a coluna.
- Para aumentar o tamanho da coluna, pressione a tecla RIGHT ARROW. Para diminuir, pressione a tecla LEFT ARROW.
- Quando terminar, pressione a tecla ENTER.

Você também pode arrastar entre os cabeçalhos das colunas para redimensionar a coluna à esquerda do cursor.

### Para alterar a largura de uma coluna em um grid
- Arraste entre os cabeçalhos das colunas para redimensionar a coluna à esquerda do cursor.

# Ajustando colunas aos dados automaticamente

Você pode redimensionar colunas para ajustar automaticamente aos dados que contêm.

### Para redimensionar uma coluna aos dados
- Clique duas vezes entre os cabeçalhos das colunas à direita da coluna que deseja redimensionar automaticamente.

### Para redimensionar todas as colunas aos dados
- Clique duas vezes na área à esquerda do primeiro cabeçalho de coluna.

### Ativando e desativando linhas de grade

Você pode desativar as linhas de grade em uma janela browse.

### Para ativar ou desativar linhas de grade
- Abra a tabela em uma janela browse.
- No menu View, clique em Grid Lines.

# Dividindo uma janela Browse

Você pode dividir a janela browse em janelas esquerda e direita para examinar duas áreas diferentes na tabela ou visualizar registros nos modos browse e edit ao mesmo tempo.

> **Dica:** Por padrão, as duas janelas de uma janela browse dividida estão vinculadas. Quando você seleciona e modifica registros em uma janela, suas alterações são refletidas na outra janela. Se desejar que as duas janelas funcionem independentemente, por exemplo, para rolar um painel sem afetar o outro, clique em Link Partitions no menu Table para que não esteja selecionado.

### Para dividir uma janela browse
- Abra a tabela em uma janela browse.
- No menu Table, clique em Resize Partitions. O cursor muda de forma para indicar que você pode dividir a janela browse.
- Para aumentar o tamanho da janela browse esquerda, pressione a tecla RIGHT ARROW. Para diminuir o tamanho, pressione a tecla LEFT ARROW.
- Quando terminar, pressione a tecla ENTER.

Você também pode posicionar o cursor na área escura no canto inferior esquerdo da janela browse e arrastar o canto para aumentar o tamanho da janela browse esquerda.

Para redimensionar uma janela browse dividida, execute as mesmas etapas para dividir uma janela browse.

# Bloqueando colunas

Você exibe apenas determinadas colunas enquanto percorre a tabela bloqueando essas colunas. Por exemplo, pressionar a tecla TAB para mover pelas colunas à direita não faz com que as colunas bloqueadas rolem para fora da janela browse ou grid.

### Para bloquear todas as colunas à esquerda de uma coluna
- Clique com o botão direito na área entre os cabeçalhos das colunas à direita da coluna que deseja bloquear.

Uma linha separadora de coluna vertical, que aparece 1 pixel mais larga que a linha que separa as outras colunas, indica a área onde as colunas bloqueadas terminam e as colunas normais começam.

### Para desbloquear todas as colunas
- Clique com o botão direito entre quaisquer cabeçalhos de coluna.

Todas as colunas são desbloqueadas.

> **Observação:** Quando qualquer coluna rola para a esquerda fora da visualização e está bloqueada, permanece oculta até que o bloqueio seja removido. Essa funcionalidade pode ser útil se você deseja bloquear as colunas no meio do grid e não exibir as colunas anteriores ou posteriores. O método Column SetFocus não funciona se uma coluna estiver bloqueada e oculta da visualização, por exemplo, rolada para fora do lado esquerdo. Para obter mais informações, consulte Método SetFocus.

Por exemplo, suponha que um grid contenha cinco colunas e a fonte de dados tenha dez colunas. Quando você rola duas colunas para a direita, a primeira e a segunda colunas rolam para a esquerda e saem da visualização. Quando você clica com o botão direito no cabeçalho da coluna das duas primeiras colunas visíveis, que na verdade são a terceira e a quarta colunas, as duas primeiras colunas ocultas, bem como a primeira coluna visível, ficam bloqueadas. No entanto, você não pode rolar para a esquerda para visualizar todas as colunas bloqueadas.
