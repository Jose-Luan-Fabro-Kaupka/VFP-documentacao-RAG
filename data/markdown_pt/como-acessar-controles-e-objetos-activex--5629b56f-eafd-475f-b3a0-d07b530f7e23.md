# Como: acessar controles e objetos ActiveX

Você pode usar qualquer controle ActiveX disponível no seu computador. Para usar um controle ActiveX, você o adiciona a um formulário e, em seguida, define suas propriedades, escreve handlers para seus eventos ou chama seus métodos. Você pode adicionar um controle ActiveX a um formulário usando a barra de ferramentas Form Controls ou o OLE Container Control, ou usando código. Para detalhes sobre como adicionar um controle ActiveX no Form Designer, consulte Sharing Information and Adding OLE.

Você pode criar um controle ActiveX em código da mesma forma que criaria qualquer controle Visual FoxPro. No entanto, antes de criar o controle, você deve determinar o nome da biblioteca de classes do controle, que está armazenado no registro do Windows. Se você não tem outra forma de determinar o nome da biblioteca de classes, use o Form Designer para criar o controle (como descrito na seção anterior) e, em seguida, obtenha a propriedade OLEClass do controle.

Objetos ActiveX podem ser criados diretamente com CREATEOBJECT( ) e não requerem uma instância de um formulário.

### Para criar um controle ActiveX em código
- Chame a função CREATEOBJECT( ) para criar um formulário.
- Chame o método AddObject do novo formulário para adicionar o controle, especificando olecontrol como a classe. Você deve passar o nome da biblioteca de classes do controle como o terceiro parâmetro do método AddObject.

Por exemplo, o programa a seguir cria um novo formulário e adiciona um controle listview a ele:

```foxpro
oMyForm = CREATEOBJECT("form")
oMyForm.AddObject("oleListview","olecontrol", ;
   "MSComctlLib.ListViewCtrl")
```

Depois de criar o formulário e o controle, você pode exibir o formulário chamando seu método Show Method (Visual FoxPro) e exibir o controle definindo sua propriedade Visible Property (Visual FoxPro) como true:

```foxpro
oMyForm.oleListview.Visible = .T.
oMyForm.Show
```

Alguns controles ActiveX não são projetados principalmente para serem usados interativamente por um usuário. Por exemplo, um controle timer não oferece suporte a métodos para interação do usuário. Mesmo assim, você ainda pode criar o controle em um formulário porque o controle geralmente disponibiliza um componente visível padrão, como um ícone. Frequentemente você não poderá alterar ou redimensionar o ícone.

Se você não deseja que seu aplicativo exiba o ícone para controles não interativos, pode ocultar o controle definindo a propriedade Visible Property (Visual FoxPro) de seu controle OLE container como false, ou definir sua propriedade Left Property (Visual FoxPro) com um valor negativo (como –100) que o move para fora da parte visível da tela. Alternativamente, você pode colocar o controle em um formulário que nunca é tornado visível (ou seja, para o qual o método Show nunca é chamado). Em todos os casos, você ainda pode chamar os métodos do controle como se o controle estivesse visível.
