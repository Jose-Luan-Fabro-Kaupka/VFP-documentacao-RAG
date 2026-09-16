# Evento Deactivate

Ocorre quando um objeto de contêiner, como um formulário, não está mais ativo porque nenhum de seus objetos contidos tem o foco.

```foxpro
PROCEDURE Object.Deactivate
```

# Observações

Aplica-se a: Objeto Form | Objeto FormSet | Objeto Page | Objeto ProjectHook | Objeto ToolBar

Os eventos Activate e Deactivate ocorrem somente quando você está movendo o foco dentro de um aplicativo. Mover o foco para ou de um formulário em outro aplicativo não dispara nenhum dos eventos. O evento Deactivate não ocorre ao descarregar um formulário.

Quando um novo objeto é ativado, programaticamente ou interativamente, o evento Deactivate do objeto previamente ativo ocorre e o evento Activate do novo objeto ocorre.

Para objetos Form, clicar na área de trabalho do Visual FoxPro faz o evento Deactivate de um formulário ocorrer e desativa um formulário de usuário ativo. Esta melhoria fornece melhor integração com a função BINDEVENT( ) para ativar e desativar formulários.

Para objetos ToolBar, Deactivate ocorre quando a barra de ferramentas é ocultada usando o método Hide.

Para objetos ProjectHook, Deactivate ocorre quando você clica fora da janela Projeto ou chama o comando ACTIVATE WINDOW para uma janela diferente.
