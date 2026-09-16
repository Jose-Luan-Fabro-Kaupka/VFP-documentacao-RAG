# Como: criar instâncias de classes com o Class Browser

Você pode criar instâncias de classes no Class Browser para visualizar instâncias dessas classes. Por exemplo, se você criar uma instância de um formulário ou classe de formulário, o formulário é criado e exibido.

> **Observação:** Ao criar uma instância de uma classe, o código no evento Init e possivelmente outros eventos é executado. Antes de criar uma instância, saiba qual código está associado às suas classes. Se a classe requer um ambiente particular que não foi configurado, o Visual FoxPro gera erros. O Class Browser não fornece tratamento de erros para classes definidas pelo usuário.

### Para criar uma instância de uma classe
- Abra a biblioteca de classes ou formulário no Class Browser .
- Na lista de classes do Class Browser , selecione a classe ou formulário do qual deseja criar uma instância.
- Arraste o ícone de classe que aparece ao lado da lista de tipos no Class Browser para a janela principal do Visual FoxPro. Observação Se você arrastar um formulário ou classe de formulário para a janela principal do Visual FoxPro, o formulário é criado e exibido. Se você arrastar um controle para a janela principal do Visual FoxPro, o controle é adicionado ao objeto _SCREEN. Para obter mais informações, consulte Variável de sistema _SCREEN .

Para criar uma instância da classe sem exibi-la, pressione e segure a tecla SHIFT durante a operação de arrastar. Para suprimir mensagens de erro ao criar instâncias, pressione e segure a tecla CTRL durante a operação de arrastar.

Para chamar a função NEWOBJECT( ) ou CREATEOBJECT( ) apropriada para instanciar a classe, você pode arrastar o ícone de classe para a janela Command.

### Para remover um objeto do objeto _SCREEN
- Use o método RemoveObject para _SCREEN .

Por exemplo, suponha que você arraste a classe VCR de Buttons.vcx na pasta ...\Samples\Classes do Visual FoxPro para um formulário. Você pode remover a instância da classe de _SCREEN digitando a seguinte linha de código na janela Command:

```foxpro
_SCREEN.RemoveObject("VCR1")
```
