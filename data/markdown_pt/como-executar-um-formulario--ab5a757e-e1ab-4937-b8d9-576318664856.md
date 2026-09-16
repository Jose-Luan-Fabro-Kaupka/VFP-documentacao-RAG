# Como: executar um formulário

Você pode executar um formulário diretamente da interface ou em código de programa.

# Executar um formulário interativamente

Há várias maneiras de executar o formulário que você projetou.

Se você está trabalhando no Form Designer, pode testar o formulário clicando no botão Run na barra de ferramentas do Form Designer. Para reabrir o formulário no Form Designer, feche o formulário ou escolha o botão Modify Form na barra de ferramentas.

Você também pode executar um formulário de um projeto ou programaticamente.

### Para executar um formulário
- Na janela Project Manager , selecione o nome do formulário na guia Documents e escolha Run . -ou-
- Digite "DO FORM" na Command window. -ou-
- No menu Form, escolha Run Form . Você também pode escolher o botão Run na Standard toolbar.

Você também pode executar o formulário escolhendo Do no menu Program, escolhendo Form na caixa List Files of Type, selecionando o formulário e escolhendo Do.

> **Dica:** Ao executar um formulário, você pode alternar rapidamente para o modo Design clicando no botão Modify Form na Standard toolbar.

Para executar um formulário de um programa, inclua o comando DO FORM no código associado a um evento, em código de método ou em um programa ou procedimento.

# Nomear o objeto Form

Por padrão, quando você usa o comando DO FORM, o nome do objeto Form é o mesmo que o nome do arquivo .scx. Por exemplo, a linha de código a seguir executa Customer.scx. O Visual FoxPro cria automaticamente uma variável de objeto para o formulário chamada `customer`:

```foxpro
DO FORM Customer
```

### Para nomear um objeto Form
- Use a cláusula NAME do comando DO FORM.

Por exemplo, os comandos a seguir executam um formulário, criando dois nomes de variável de objeto de formulário:

```foxpro
DO FORM Customer NAME frmCust1
DO FORM Customer NAME frmCust2
```

# Manipular o objeto Form

Você pode associar um objeto Form a uma variável pública para que possa acessar o objeto Form através do nome da variável.

### Para associar um objeto Form a uma variável pública
- Use o comando DO FORM na Command window.

Por exemplo, os comandos a seguir, emitidos na Command window, abrem um formulário chamado `Customer` e alteram sua caption.

```foxpro
DO FORM Customer
Customer.Caption = "Hello"
```

Se você então emitir o comando a seguir na Command window, `O` é exibido na janela de saída ativa, indicando que `Customer` é um objeto:

```foxpro
? TYPE("Customer")
```

Se você emitir o comando DO FORM em um programa, o objeto Form tem escopo no programa. Se o programa ou procedimento for concluído, o objeto desaparece, mas o formulário permanece visível. Por exemplo, você poderia executar o programa a seguir:

```foxpro
*formtest.prg
DO FORM Customer
```

Depois de executar o programa, o formulário permanece visível e todos os controles no formulário estão ativos, mas `TYPE("Customer")` retorna `U` indicando que `Customer` é uma variável indefinida. O comando a seguir, emitido na Command window, geraria um erro:

```foxpro
Customer.Caption = "Hello"
```

No entanto, você pode acessar o formulário usando as propriedades ActiveForm Property, Forms Property e FormCount Property do objeto de aplicação.

# Definir escopo do formulário para a variável de objeto Form

Você pode vincular um formulário a um objeto Form.

### Para vincular um formulário a um objeto Form
- Use o comando DO FORM com a palavra-chave LINKED.

Se você incluir a palavra-chave LINKED, quando a variável associada ao objeto Form sair de escopo, o formulário é liberado.

Por exemplo, o comando a seguir cria um formulário vinculado à variável de objeto `frmCust2`:

```foxpro
DO FORM Customer NAME frmCust2 LINKED
```

Quando `frmCust2` é liberado, o formulário é fechado.

# Fechar um formulário ativo

Para permitir que os usuários fechem o formulário ativo clicando no botão fechar ou escolhendo Close no Control menu do formulário, defina a propriedade Closable do formulário.

### Para permitir que um usuário feche o formulário ativo
- Na janela Properties, defina a propriedade Closable como true (.T.). -ou-
- Use o comando RELEASE .

Por exemplo, você pode fechar e liberar o formulário `frmCustomer` emitindo o comando a seguir em um programa ou na Command Window (Visual FoxPro):

```foxpro
RELEASE frmCustomer
```

Você também pode permitir que um usuário feche e libere um formulário incluindo o comando a seguir no código do evento Click de um controle, como um command button com caption "Quit":

```foxpro
THISFORM.Release
```

Você também pode usar o comando RELEASE no código associado a um objeto no formulário, mas qualquer código que você incluiu no método Release não será executado.

> **Cuidado:** Quando você libera um formulário, libera da memória a variável de objeto criada para o formulário. Há uma única variável para um form set, então você não pode liberar formulários em um form set sem liberar o form set. Se você deseja liberar o form set, pode usar RELEASE THISFORMSET . Se você deseja remover um formulário da tela para que um usuário não possa mais vê-lo ou interagir com ele, pode usar THISFORM.Hide .
