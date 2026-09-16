# Evento GotFocus

Ocorre quando um objeto recebe o foco, por ação do usuário ou por meio de código.

```foxpro
PROCEDURE Object.GotFocus
```

# Observações

Aplica-se a: controle CheckBox | controle ComboBox | controle CommandButton | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | objeto Form | controle ListBox | controle OLE Bound | controle OLE Container | controle OptionButton | controle Spinner | controle TextBox (Visual FoxPro)

Use o evento GotFocus para especificar ações a ocorrer quando um objeto recebe o foco. Por exemplo, ao anexar um evento GotFocus a cada controle em um Form, você pode orientar um usuário exibindo instruções breves ou mensagens na barra de status. Você também pode fornecer indicações visuais habilitando, desabilitando ou exibindo outros controles que dependem do controle que tem o foco.

Um controle recebe o foco por ação do usuário, como um clique do mouse, ou quando o método SetFocus é chamado em código.

> **Observação:** Um objeto pode receber o foco somente se suas propriedades Enabled e Visible estiverem definidas como true (.T.). Para personalizar a interface de teclado para mover o foco, defina a ordem de tabulação ou especifique teclas de acesso para controles em um formulário. O evento GotFocus ocorre depois do evento Activate para o contêiner do controle.
