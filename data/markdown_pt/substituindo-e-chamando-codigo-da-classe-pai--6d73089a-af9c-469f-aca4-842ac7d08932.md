# Substituindo e chamando código da classe pai

Quando você cria uma classe, a classe herda automaticamente todas as propriedades, métodos e eventos da classe pai. Por exemplo, se existe código para um evento na classe pai, esse código é executado quando o evento ocorre para um objeto baseado em uma subclasse criada da classe pai.

As seções a seguir descrevem como você pode substituir ou executar código de método ou evento da classe pai:
 - Overriding Parent Class Code
- Calling Parent Class Code

# Substituindo código da classe pai

Geralmente, você deseja adicionar funcionalidade a uma nova classe ou ao objeto criado dessa classe além da funcionalidade original. No entanto, você pode substituir o código de método ou evento herdado da classe pai. Por exemplo, suponha que você cria uma subclasse ou adiciona um objeto baseado na subclasse a um contêiner, como um formulário. Você pode escrever novo código para o evento Click da classe para substituir o código de evento na classe pai. Em ambos os casos, o novo código, não o código original, é executado em tempo de execução.

Você também pode impedir que o comportamento padrão da classe base ocorra em um método ou evento da subclasse. Para impedir o comportamento da classe base, inclua a palavra-chave NODEFAULT no código de método ou evento que você adiciona.

Por exemplo, o programa a seguir usa a palavra-chave NODEFAULT no evento KeyPress de uma caixa de texto para impedir que os caracteres digitados sejam exibidos na caixa de texto:

```foxpro
frmKeyExample = CREATEOBJECT("test")
frmKeyExample.Show
READ EVENTS
DEFINE CLASS myForm AS FORM
   ADD OBJECT text1 AS TEXTBOX
   PROCEDURE text1.KeyPress
      PARAMETERS nKeyCode, nShiftAltCtrl
      NODEFAULT
      IF BETWEEN(nKeyCode, 65, 122) && Between 'A' and 'z'
         This.Value = ALLTRIM(This.Value) + "*"
         ACTIVATE SCREEN      && Send output to main Visual FoxPro window.
         ?? CHR(nKeyCode)
      ENDIF
   ENDPROC
   PROCEDURE Destroy
      CLEAR EVENTS
   ENDPROC
ENDDEFINE
```

# Chamando código da classe pai

Você pode otimizar o design de classes adicionando e executando código em diferentes níveis na hierarquia de classes ou contêineres.

Para executar código de método ou evento na classe pai além do código para o mesmo método ou evento na subclasse, preceda o código de método ou evento da subclasse com a função DODEFAULT( ) ou o operador de resolução de escopo (::).

> **Dica:** Quando você usa a função DODEFAULT( ), não precisa saber o nome da classe pai. No entanto, para determinar todas as classes na hierarquia de classes de um objeto, use a função ACLASS( ). Para obter mais informações, consulte ACLASS( ) Function .

Por exemplo, suponha que você tenha uma classe chamada cmdGoBottom baseada na classe CommandButton que possui o seguinte código em seu evento Click:

```foxpro
GO BOTTOM
THISFORM.Refresh
```

Este código move o ponteiro de registro da tabela para o final da tabela. Quando você cria um botão de comando, por exemplo, cmdGoBottom1, baseado na classe cmdGoBottom e adiciona a um formulário, pode decidir executar o código no evento Click da classe pai e exibir uma mensagem indicando que o ponteiro de registro da tabela está posicionado no final da tabela. Suponha que você adicione apenas a seguinte linha de código ao evento Click de cmdGoBottom1 para exibir a mensagem "At the Bottom of the Table":

```foxpro
WAIT WINDOW "At the Bottom of the Table" TIMEOUT 1
```

Quando você executa o formulário, a mensagem é exibida; no entanto, o ponteiro de registro não se move porque o código no evento Click de cmdGoBottom1 substitui o da classe pai. Para garantir que o código no evento Click da classe pai também seja executado, inclua as seguintes linhas de código em vez disso no evento Click de cmdGoBottom1:

```foxpro
DODEFAULT()
WAIT WINDOW "At the Bottom of the Table" TIMEOUT 1
```

As linhas de código a seguir no evento Click de cmdGoBottom1 mostram como realizar a mesma tarefa usando o operador de resolução de escopo (::) e o nome da classe pai:

```foxpro
cmdGoBottom::Click()
WAIT WINDOW "At the Bottom of the Table" TIMEOUT 1
```

Como outro exemplo, a biblioteca de classes visuais Buttons.vcx no diretório Visual FoxPro ...\Samples\Classes contém duas classes de botão de comando: cmdOK e cmdCancel. Suponha que um botão de comando criado da classe cmdOK exista em um formulário. O código no evento Click do botão de comando libera o formulário quando você clica no botão. No entanto, a classe de botão de comando cmdCancel é uma subclasse da classe cmdOK. Suponha que você deseja descartar alterações feitas em uma tabela quando clica em um botão de comando criado da classe cmdCancel. Você pode adicionar funcionalidade ao evento Click da classe cmdCancel que chama o código de método na classe cmdOK usando o seguinte código de exemplo:

```foxpro
IF USED() AND CURSORGETPROP("Buffering") != 1
   TABLEREVERT(.T.)
ENDIF
DODEFAULT()
```

O código adicionado à classe cmdCancel reverte alterações na tabela usando a função TABLEREVERT( ) antes de usar a função DODEFAULT( ) para chamar o código na classe cmdOK para liberar o formulário.

> **Observação:** Você não precisa adicionar a função TABLEUPDATE( ) à classe cmdOK porque as alterações são gravadas em uma tabela em buffer por padrão quando a tabela é fechada.

Para obter mais informações, consulte DODEFAULT( ) Function e :: Scope Resolution Operator.
