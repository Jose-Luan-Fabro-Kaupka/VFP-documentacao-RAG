# Protegendo e ocultando membros de classe

Ao criar e adicionar propriedades e métodos a uma classe no Class Designer, você pode especificar um dos seguintes níveis de visibilidade para a propriedade ou o método: Public, Protected ou Hidden. Ao criar uma classe usando o comando DEFINE CLASS, você pode designar propriedades e métodos como Hidden ou Protected usando as palavras-chave PROTECTED e HIDDEN.

Por padrão, propriedades e métodos em uma definição de classe são Public, o que significa que o código em outras classes ou procedimentos pode definir essas propriedades ou chamar esses métodos. No entanto, certas classes podem precisar restringir os usuários de alterar suas propriedades ou chamar seus métodos de fora da classe. Você pode designar as propriedades e métodos que adiciona a uma classe como Protected, o que restringe o acesso aos membros da classe e das subclasses. Você também pode designar propriedades e métodos como Hidden, o que restringe o acesso apenas aos membros da classe.

Por exemplo, suponha que você crie uma classe que armazena informações de funcionários e não deseja permitir que os usuários alterem a data de contratação do funcionário. Você pode designar a data de contratação como Protected e, em vez disso, fornecer um método que retorna a data de contratação para que os usuários possam visualizá-la, se necessário. O exemplo de código a seguir cria a classe Employee usando o comando DEFINE CLASS e designa a propriedade HireDate como Protected usando a palavra-chave PROTECTED e contém o método GetHireDate que retorna a data de contratação:

```foxpro
DEFINE CLASS Employee AS CUSTOM
   PROTECTED HireDate
   First_Name = ""
   Last_Name = ""
   Address = ""
   HireDate = { - - }
   PROCEDURE GetHireDate
      RETURN This.HireDate
   ENDPROC
ENDDEFINE
```

Para obter mais informações, consulte Comando DEFINE CLASS.

A amostra do Visual FoxPro, Display a Stop Watch Sample, também ilustra o uso de propriedades e métodos protegidos em uma classe.
