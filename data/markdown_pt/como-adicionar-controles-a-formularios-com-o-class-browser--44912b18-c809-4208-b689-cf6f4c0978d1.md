# Como: adicionar controles a formulários com o Class Browser

Você pode adicionar controles do Class Browser ao projetar ou executar um formulário.

### Para adicionar controles a um formulário ou contêiner
- No Form Designer , abra o formulário.
- Na janela Class Browser Window , abra o arquivo de biblioteca de classes que contém a classe do objeto que você deseja adicionar ao formulário.
- Na lista Class, selecione o nome da classe e depois arraste o ícone da classe para o formulário. O ícone da classe está localizado acima da lista Class.

### Para visualizar a classe de um controle em um formulário ou em um contêiner
- No Form Designer , selecione o controle.
- No menu Tools, escolha Class Browser . O Class Browser abre e exibe a classe do controle que você selecionou no formulário.

Você pode projetar seus formulários para que seja possível adicionar objetos de uma classe do Class Browser no formulário enquanto ele está em execução. Você pode querer projetar uma classe de formulário que tenha esse recurso como uma de suas propriedades.

### Para adicionar objetos em um formulário em execução ou em um contêiner em um formulário
- Execute o formulário.
- Abra o Class Browser e visualize a lista de classes contendo a classe do objeto que você deseja adicionar ao formulário.
- Selecione a classe desejada e arraste o ícone da classe do Class Browser para o formulário.
- Um novo objeto aparece no formulário baseado na classe que você selecionou no Class Browser . Dica Você também pode adicionar uma instância da classe selecionada a qualquer contêiner posicionando o ponteiro do mouse sobre o contêiner e digitando a seguinte linha de código na janela Command: _oBrowser.FormAddObject(SYS(1270))

### Para visualizar a classe de um controle em um formulário em execução
- Defina o foco no controle.
- No menu Tools, escolha Class Browser . O Class Browser avalia _SCREEN.ActiveForm.ActiveControl e exibe a classe do controle que você selecionou no formulário.
