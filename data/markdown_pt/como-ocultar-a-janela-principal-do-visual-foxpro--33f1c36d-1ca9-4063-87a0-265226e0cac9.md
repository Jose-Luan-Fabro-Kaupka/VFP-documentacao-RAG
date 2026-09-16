# Como: ocultar a janela principal do Visual FoxPro

Se você estiver executando um formulário de nível superior, pode não querer que a janela principal do Visual FoxPro esteja visível. Você pode usar a propriedade Visible (Visual FoxPro) do objeto Application para ocultar e exibir a janela principal do Visual FoxPro conforme necessário.

### Para ocultar a janela principal do Visual FoxPro
- No evento Init do formulário, inclua a seguinte linha de código: Application.Visible = .F.
- No evento Destroy do formulário, inclua a seguinte linha de código: Application.Visible = .T.

Certifique-se de também fornecer uma forma de fechar o formulário usando `THISFORM.Release` em algum método ou evento.

> **Observação:** Você também pode incluir a seguinte linha em um arquivo de configuração para ocultar a janela principal do Visual FoxPro: SCREEN = OFF
