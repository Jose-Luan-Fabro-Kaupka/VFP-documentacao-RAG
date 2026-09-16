# Como: ocultar um formulário

Você pode ocultar um formulário para que ele não fique visível ao usuário. Quando o formulário está oculto, o usuário não pode interagir com ele, mas você ainda tem controle programático total sobre o formulário.

### Para ocultar um formulário
- Use o método Hide. Por exemplo, no código associado ao evento Click de um botão de comando, você pode incluir a seguinte linha de código: THISFORM.Hide

Quando o usuário clica no botão de comando, o formulário permanece na memória, mas não fica visível.

# Liberação de formulários

Você pode permitir que um usuário libere um formulário quando terminar de interagir com ele. Depois de liberar um formulário, você não poderá mais acessar suas propriedades e métodos.

### Para liberar um formulário
- Chame o método Release.

Por exemplo, no código associado ao evento Click de um botão de comando, você pode incluir a seguinte linha de código:

```foxpro
THISFORM.Release
```

Quando o usuário clica no botão de comando, o formulário é fechado.
