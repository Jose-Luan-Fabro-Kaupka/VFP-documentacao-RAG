# Evento Paint

Ocorre quando um formulário ou barra de ferramentas é repintado.

```foxpro
PROCEDURE Object.Paint
```

# Observações

Aplica-se a: Objeto Form | Objeto ToolBar

Um formulário ou barra de ferramentas é repintado quando parte ou todo o formulário ou barra de ferramentas é exposto depois de ter sido movido ou redimensionado, ou depois que uma janela que cobria o formulário ou barra de ferramentas foi movida.

Usar um método Refresh em um evento Resize força a repintura de todo o objeto sempre que o usuário redimensiona o formulário ou barra de ferramentas.

O evento Paint pode ser chamado com frequência; portanto, evite realizar manipulação de dados ou chamar comandos ou funções que estabeleçam um estado modal.

Usar um evento Paint para certas tarefas pode causar um evento em cascata. Em geral, evite usar um evento Paint para o seguinte:
 - Mover ou redimensionar um formulário ou controle.
- Alterar quaisquer variáveis que afetem tamanho ou aparência, como definir a propriedade BackColor de um objeto.
- Chamar o método Refresh. Observação Um evento Resize pode ser mais apropriado para algumas dessas tarefas.
