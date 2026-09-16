# Como: definir propriedades para objetos

Você pode definir ou alterar propriedades em tempo de design ou programaticamente.

> **Observação:** Algumas propriedades são avaliadas em tempo de design; portanto, quaisquer variáveis de memória ou matrizes usadas em expressões para essas propriedades devem estar no escopo em tempo de design. Propriedades somente leitura em tempo de design, como a propriedade Class de um objeto, são exibidas em itálico na lista de propriedades da janela Properties.

### Para definir ou editar o valor de uma propriedade
- Clique em um objeto no formulário.
- Na lista de propriedades da janela Properties, selecione uma propriedade.
- Na caixa de configurações da propriedade, digite ou escolha a configuração desejada para a propriedade selecionada.

Você também pode selecionar um objeto na caixa de objetos da janela Properties.

Se a propriedade requer um valor de caractere, você não precisa incluir o valor entre aspas. Por exemplo, se deseja que o caption de um formulário exiba Customer, digite `Customer` na caixa de configurações da propriedade. No entanto, se deseja que o caption exiba "Customer" com aspas (""), digite `"Customer"` na caixa de configurações da propriedade.

# Definindo propriedades para expressões

Você pode definir certas propriedades para os resultados de expressões ou funções na janela Properties. O Visual FoxPro avalia a expressão de uma propriedade quando você a insere na janela Properties e quando o objeto é inicializado em tempo de design ou de execução. Depois que o objeto é criado, a configuração da propriedade não muda até que você ou o usuário a altere explicitamente.

> **Cuidado:** Se você definir uma propriedade para o resultado de uma função definida pelo usuário, o Visual FoxPro avalia a função quando você define a propriedade ou quando modifica ou executa o formulário. Se existir um erro na função definida pelo usuário, talvez você não consiga abrir seu formulário.

### Para definir uma propriedade para uma expressão
- Na lista de propriedades, selecione a propriedade para a qual deseja inserir uma expressão.
- Na caixa de configurações da propriedade, digite um sinal de igual (=) seguido da expressão.

Por exemplo, você pode indicar a tabela ativa no momento em que o formulário é executado selecionando a propriedade Caption do formulário e digitando `=ALIAS( )` na caixa de configurações da propriedade.

Você também pode especificar expressões para propriedades usando a caixa de diálogo Expression Builder. Para abrir o Expression Builder, selecione a propriedade desejada e clique no botão Function na janela Properties.

Você também pode definir a propriedade para a função definida pelo usuário no evento Init do objeto, como no exemplo a seguir:

`THIS.Caption = myfunction( )`

No entanto, se existir um erro na função definida pelo usuário, você ainda não conseguirá executar o formulário, mas poderá modificá-lo.
