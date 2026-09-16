# Como: ver valores armazenados

Na janela Debugger, você pode ver facilmente os valores em tempo de execução de variáveis, elementos de matriz, propriedades e expressões nas seguintes janelas:
 - Locals Window
- Watch Window
- Trace Window

# Visualizando valores armazenados na janela Locals

A janela Locals exibe todas as variáveis, matrizes, objetos e membros de objetos visíveis em qualquer programa, procedimento ou método na pilha de chamadas. Por padrão, os valores do programa em execução no momento são exibidos na janela Locals.

### Para visualizar valores armazenados na janela Locals
- Na lista Locals For, escolha o programa ou procedimento.

Você pode explorar matrizes ou objetos clicando no sinal de mais (+) ao lado do nome da matriz ou do objeto nas janelas Locals e Watch. Ao explorar, você pode ver os valores de todos os elementos nas matrizes e todas as configurações de propriedades nos objetos.

Você também pode alterar os valores em variáveis, elementos de matriz e propriedades nas janelas Locals e Watch selecionando a variável, o elemento de matriz ou a propriedade, clicando na coluna Value e digitando um novo valor.

# Visualizando valores armazenados na janela Watch

Você pode ver valores armazenados na janela Watch. O valor e o tipo da expressão aparecem na lista da janela Watch. Valores que mudaram são exibidos em vermelho na janela Watch.

> **Observação:** Você não pode inserir expressões que criem objetos na janela Watch.

### Para ver valores armazenados na janela Watch
- Na caixa Watch da janela Watch, digite qualquer expressão válida do Visual FoxPro e pressione ENTER.

Você também pode selecionar variáveis ou expressões na janela Trace ou em outras janelas do Debugger e arrastá-las para a janela Watch.

### Para remover um item da lista da janela Watch
- Selecione o item e escolha uma das seguintes opções: Pressione DEL. -ou- No menu de atalho, escolha Delete Watch.

### Para editar um watch
- Clique duas vezes no watch na janela Watch e edite no local.

# Visualizando valores armazenados na janela Trace

Você pode ver valores armazenados na janela Trace como uma dica de valor.

### Para ver valores armazenados na janela Trace
- Na janela Trace, mova o cursor para o elemento cujo valor você deseja exibir. No Visual FoxPro 9.0, você pode exibir o valor de constantes de compilação #DEFINE.
 Uma dica de valor na janela Trace
