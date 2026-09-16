# Comando MODIFY CLASS

Abre o Class Designer, permitindo que você modifique uma definição de classe existente ou crie uma nova definição de classe.

```foxpro
MODIFY CLASS ClassName [OF ClassLibraryName1]
   [AS cBaseClassName [FROM ClassLibraryName2]]
   [NOWAIT] [METHOD MethodName] [SAVE]
```

#### Parâmetros
 **ClassName**
Especifica o nome da definição de classe a modificar ou criar.
**OF ClassLibraryName1**
Especifica o nome da biblioteca de classes visual .vcx que contém a definição de classe. Se você estiver criando uma nova definição de classe e a biblioteca de classes visual .vcx já existir, a definição de classe é adicionada a ela. Uma extensão de arquivo .vcx é assumida para a biblioteca de classes visual. Certifique-se de incluir a extensão de arquivo se a biblioteca de classes visual que você especificar tiver uma extensão de arquivo diferente de .vcx. Se a biblioteca de classes visual .vcx que você especificar estiver atualmente na lista de pesquisa SET CLASSLIB, a biblioteca de classes visual é removida da lista de pesquisa.
**AS cBaseClassName**
Especifica a classe na qual a definição de classe é baseada. Você pode especificar qualquer classe base do Visual FoxPro, exceto Column e Header. Você também pode especificar uma classe definida pelo usuário se incluir a cláusula FROM ClassLibraryName2 que especifica o nome do arquivo de biblioteca de classes visual (.vcx) que contém a classe definida pelo usuário. Se você omitir AS cBaseClassName , a definição de classe é baseada na classe base FormSet do Visual FoxPro.
**FROM ClassLibraryName2**
Especifica o nome da biblioteca de classes visual .vcx que contém a classe definida pelo usuário especificada com cBaseClassName .
**METHOD MethodName**
Especifica um evento ou método para o qual a janela Code é aberta no Class Designer. A cláusula METHOD permite que você comece imediatamente a editar o código de evento ou método no Class Designer. MethodName suporta a sintaxe de objeto do Visual FoxPro. Por exemplo, para editar imediatamente o código do evento Click de uma caixa de texto chamada txtFirstName na classe chamada MyClass em uma biblioteca de classes visual chamada MyClassLibrary, use o seguinte comando: MODIFY CLASS MyClass OF MyClassLibrary METHOD txtFirstName.Click Se você incluir apenas um nome de evento ou método na cláusula METHOD, a janela Code é aberta para o evento ou método da classe. Por exemplo, para editar imediatamente o código do evento Click de uma classe chamada MyClass em uma biblioteca de classes visual chamada MyClassLibrary, use o seguinte comando: MODIFY CLASS MyClass OF MyClassLibrary METHOD Click
**NOWAIT**
Continua a execução do programa depois que o Class Designer é aberto. O programa não aguarda que o Class Designer seja fechado, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY CLASS NOWAIT. Se você omitir NOWAIT quando MODIFY CLASS é emitido em um programa, o Class Designer é aberto e a execução do programa é pausada até que o Class Designer seja fechado. NOWAIT é efetivo apenas a partir de um programa. Não tem efeito em MODIFY CLASS quando emitido da janela Command. Se NOWAIT for incluído com a cláusula METHOD, certifique-se de colocar NOWAIT antes da cláusula METHOD ou NOWAIT será ignorado.
**SAVE**
Deixa o Class Designer aberto depois que outra janela é ativada. Se você omitir SAVE, o Class Designer é fechado quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido da janela Command.

# Observações

Use MODIFY CLASS para modificar uma definição de classe existente ou para criar uma nova definição de classe e salvá-la em uma biblioteca de classes visual .vcx. Você pode abrir a biblioteca de classes visual .vcx com SET CLASSLIB, permitindo que você acessar as definições de classe dentro da biblioteca de classes visual .vcx.
