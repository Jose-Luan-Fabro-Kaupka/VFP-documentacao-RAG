# Como: estender formulários com conjuntos de formulários

Você pode manipular vários formulários como um grupo incluindo-os em um conjunto de formulários. Um conjunto de formulários tem estes benefícios:
 - Você pode mostrar ou ocultar todos os formulários em um conjunto de formulários de uma vez.
- Você pode organizar visualmente vários formulários de uma vez para controlar suas posições relativas.
- Como todos os formulários em um conjunto de formulários são definidos em um único arquivo .scx com um único ambiente de dados, você pode sincronizar automaticamente os ponteiros de registro em vários formulários. Se você alterar o ponteiro de registro em uma tabela pai em um formulário, os registros filhos em outro formulário são atualizados e exibidos. Observação Todos os formulários e todos os objetos nos formulários são carregados quando você executa o conjunto de formulários. Carregar muitos formulários com vários controles pode levar vários segundos.

# Criando um novo conjunto de formulários

Um conjunto de formulários é um contêiner pai para um ou mais formulários. Quando você está no Form Designer, pode criar um conjunto de formulários.

### Para criar um conjunto de formulários
- No menu Form, escolha Create Formset.

Se você não deseja trabalhar com vários formulários como um grupo de formulários, não precisa criar um conjunto de formulários. Depois de criar um conjunto de formulários, você pode adicionar formulários a ele.

# Adicionando e removendo formulários

Depois de criar um conjunto de formulários, você pode adicionar novos formulários e remover formulários.

### Para adicionar formulários adicionais a um conjunto de formulários
- No menu Form, escolha Add New Form.

### Para remover um formulário de um conjunto de formulários
- Na caixa Form na parte inferior do Form Designer, selecione o formulário.
- No menu Form, escolha Remove Form.

Se você tem um único formulário em um conjunto de formulários, pode remover o conjunto de formulários para ter apenas o formulário.

### Para remover um conjunto de formulários
- No menu Form, escolha Remove Formset.

Formulários são salvos em formato de tabela em um arquivo com extensão .scx. Quando você cria um formulário, a tabela .scx contém um registro para o formulário, um registro para o ambiente de dados e dois registros para uso interno. Um registro é adicionado para cada objeto que você adiciona ao formulário ou ao ambiente de dados. Se você criar um conjunto de formulários, um registro adicional é adicionado para o conjunto de formulários e para cada novo formulário. O contêiner pai de cada formulário é o conjunto de formulários. O contêiner pai de cada controle é o formulário em que ele é colocado.

> **Dica:** Ao executar um conjunto de formulários, você pode não querer que todos os formulários no conjunto de formulários estejam inicialmente visíveis. Defina a propriedade Visible como false (.F.) para formulários que não deseja exibir quando o conjunto de formulários é executado. Defina a propriedade Visible como true (.T.) quando desejar que os formulários sejam exibidos.
