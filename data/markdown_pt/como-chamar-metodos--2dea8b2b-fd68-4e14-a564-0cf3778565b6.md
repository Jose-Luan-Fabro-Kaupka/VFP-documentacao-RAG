# Como: chamar métodos

Depois que um objeto foi criado, você pode chamar os métodos desse objeto de qualquer lugar em seu aplicativo.

### Para chamar um método
- Use esta sintaxe: Parent.Object.Method

As instruções a seguir chamam métodos para exibir um formulário e definir o foco em uma caixa de texto:

```foxpro
frsFormSet.frmForm1.Show
frsFormSet.frmForm1.txtGetText1.SetFocus
```

Métodos que retornam valores e são usados em expressões devem terminar com parênteses abertos e fechados. Por exemplo, a seguinte instrução define o caption de um formulário para o valor retornado pelo método definido pelo usuário `GetNewCaption`:

```foxpro
Form1.Caption = Form1.GetNewCaption()
```

> **Observação:** Parâmetros passados a métodos devem ser incluídos entre parênteses após o nome do método; por exemplo, Form1.Show(nStyle) passa nStyle para o código do método Show de Form1.
