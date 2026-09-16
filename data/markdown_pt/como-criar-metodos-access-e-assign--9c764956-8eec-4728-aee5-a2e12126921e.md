# Como: criar métodos Access e Assign

Você pode criar métodos Access e Assign para novas propriedades personalizadas, propriedades nativas do Visual FoxPro ou propriedades personalizadas existentes. Você pode criá-los ao adicionar ou editar propriedades personalizadas. Para obter mais informações sobre métodos Access e Assign, consulte Métodos Access e Assign. Para obter informações sobre como adicionar propriedades personalizadas a formulários, conjuntos de formulários e classes, consulte Como: adicionar propriedades e métodos a um formulário e Como: adicionar propriedades a classes.

Você pode criar métodos Access e Assign interativamente no Form Designer ou Class Designer. Para criar métodos Access e Assign para propriedades de formulários e conjuntos de formulários, use o Form Designer. Para criar métodos Access e Assign para propriedades de classes de controles e outros objetos, use o Class Designer. Você também pode criar métodos Access e Assign programaticamente.

### Para criar um método Access ou Assign ao adicionar uma nova propriedade
- Na caixa de diálogo Nova propriedade, selecione a caixa Access Method, a caixa Assign Method ou ambas.
- Quando terminar de criar a propriedade, clique em Add .

Quando você cria um método Access ou Assign, o novo método é adicionado ao final da lista de propriedades na janela Propriedades e aparece com o sufixo _access ou _assign.

Para obter mais informações, consulte Caixa de diálogo Nova propriedade.

### Para criar um método Access ou Assign para uma propriedade nativa do Visual FoxPro
- Se você estiver no Form Designer, no menu Form, escolha New Method . -OU- Se você estiver no Class Designer, no menu Class, escolha New Method .
- Na caixa Nome da caixa de diálogo Novo método, digite o nome da propriedade nativa do Visual FoxPro seguido do sufixo _ACCESS ou _ASSIGN .
- Quando terminar de criar o método, clique em Add .

Para obter mais informações, consulte Caixa de diálogo Novo método

### Para criar um método Access ou Assign para propriedades personalizadas existentes
- Se você estiver no Form Designer, no menu Form, escolha Edit Property/Method . -OU- Se você estiver no Class Designer, no menu Class, escolha Edit Property/Method .
- Na caixa de diálogo Editar propriedade/método, selecione a propriedade desejada.
- Selecione a caixa Access Method, a caixa Assign Method ou ambas.
- Clique em Apply e, em seguida, Close .

Para obter mais informações, consulte Caixa de diálogo Editar propriedade/método.

Quando você cria um método Access ou Assign para uma propriedade personalizada existente, o novo método é adicionado ao final da lista de propriedades na janela Propriedades e aparece com o sufixo _access ou _assign.

### Para criar métodos Access e Assign programaticamente
- Use o comando DEFINE CLASS e inclua a cláusula PROCEDURE.

> **Observação:** Em métodos Assign, você deve incluir uma instrução PARAMETERS ou LPARAMETERS para que, quando você tentar atribuir um valor a uma propriedade em tempo de execução, o Visual FoxPro possa aceitar o valor e passá-lo ao método Assign.

Para obter mais informações, consulte Comando DEFINE CLASS.

Por exemplo, o código a seguir cria uma classe chamada MyClass com métodos Access e Assign chamados MyProperty_ACCESS e MyProperty_ASSIGN para a propriedade personalizada MyProperty. MyProperty_ACCESS responde a consultas sobre o valor de MyProperty, enquanto MyProperty_ASSIGN responde a alterações no valor de MyProperty.

> **Observação:** O método Assign inclui uma instrução LPARAMETERS para que possa aceitar o valor que é passado a ele.

```foxpro
DEFINE CLASS MyClass AS Custom
   MyProperty = 100
   PROCEDURE MyProperty_ACCESS
      WAIT WINDOW 'This is the Access method';
         +  ' ' + PROGRAM()
      RETURN THIS.MyProperty
   ENDPROC

   PROCEDURE MyProperty_ASSIGN
      LPARAMETERS tAssign
      WAIT WINDOW 'This is the Assign method';
          + ' ' + PROGRAM()
   ENDPROC
ENDDEFINE
```

O exemplo de código a seguir cria uma classe Form chamada frmMyForm com um método Assign chamado Left_ASSIGN para a propriedade nativa Left do formulário. Left_ASSIGN realiza validação simples no valor da propriedade e é executado quando é feita uma tentativa de atribuir um valor à propriedade. Se você tentar alterar a propriedade Left para um valor negativo, o método Assign exibe uma mensagem e deixa o valor inalterado. Se você tentar alterar a propriedade Left para um valor não negativo, o método define a propriedade para o valor especificado.

> **Observação:** O método Assign inclui uma instrução LPARAMETERS para que possa aceitar o valor que é passado a ele.

```foxpro
DEFINE CLASS frmMyForm AS Form
   PROCEDURE Left_ASSIGN
      LPARAMETERS tAssign
      DO CASE
         CASE tAssign < 0 && Value passed is negative.
            WAIT WINDOW 'Value must be greater than 0'
         OTHERWISE  && Value passed is not negative.
            THIS.Left = tAssign
      ENDCASE
   ENDPROC
ENDDEFINE
```

# Criando métodos THIS_ACCESS

Você pode criar métodos THIS_ACCESS no Form Designer, Class Designer ou programaticamente.

### Para criar um método THIS_ACCESS
- No menu Form no Form Designer ou no menu Class no Class Designer, escolha New Method .
- Na caixa de diálogo Novo método, digite THIS_ACCESS .
- Clique em Add . Quando criado, o método THIS_ACCESS aparece na janela Propriedades. Para adicionar código ao método, clique duas vezes no método na janela Propriedades.

### Para criar métodos THIS_ACCESS programaticamente
- Use o comando DEFINE CLASS e inclua a palavra-chave THIS_ACCESS.

Para obter mais informações, consulte Comando DEFINE CLASS.

O exemplo de código a seguir cria uma classe Form chamada MyForm com um método THIS_ACCESS, que contém uma instrução LPARAMETER com um nome de membro de objeto e algum código para executar. A primeira linha de código cria um formulário chamado oTempForm usando a função CREATEOBJECT( ). A segunda linha de código tenta atribuir um valor à propriedade Caption do formulário. Esta ação executa o método THIS_ACCESS e passa o nome da propriedade Caption ao método. O método THIS_ACCESS exibe o nome do membro do objeto, ou 'Caption' neste exemplo, usando o comando de interrogação (?), e então retorna uma referência de objeto para o formulário.

A terceira linha tenta exibir o valor da propriedade Caption do formulário usando o comando ?. Esta ação executa THIS_ACCESS novamente, passa o nome da propriedade Caption ao método, exibe 'Caption' e retorna uma referência de objeto para o formulário. O valor da propriedade Caption, 'abc', é então finalmente exibido.

```foxpro
oTempForm = CREATEOBJECT('MyForm')
oTempForm.Caption = 'abc'
? oTempForm.Caption
DEFINE CLASS MyForm AS Form
   PROCEDURE THIS_ACCESS
      LPARAMETER cMemberName
      IF cMemberName = 'caption'
         ? cMemberName
      ENDIF
      RETURN THIS
   ENDPROC
ENDDEFINE
```

Para obter mais informações, consulte Comando DEFINE CLASS.
