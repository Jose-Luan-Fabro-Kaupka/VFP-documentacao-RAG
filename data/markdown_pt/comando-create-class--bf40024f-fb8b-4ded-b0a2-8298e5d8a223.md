# Comando CREATE CLASS

Abre o Class Designer, permitindo que você crie uma nova definição de classe.

```foxpro
CREATE CLASS ClassName | ? [OF ClassLibraryName1 | ?]
[AS cBaseClassName [FROM ClassLibraryName2]] [NOWAIT]
```

#### Parâmetros
 **ClassName**
Especifica o nome da definição de classe a ser criada.
**?**
Exibe a caixa de diálogo New Class, na qual você pode especificar o nome da definição de classe a ser criada.
**OF ClassLibraryName1**
Especifica o nome da biblioteca de classes visuais .vcx a ser criada. Se a biblioteca de classes visuais .vcx já existir, a definição de classe é adicionada a ela. Uma extensão de arquivo .vcx é assumida para a biblioteca de classes visuais. Certifique-se de incluir a extensão de arquivo se a biblioteca de classes visuais que você especificar tiver uma extensão de arquivo diferente de .vcx.
**?**
Exibe a caixa de diálogo New Class, na qual você pode especificar o nome de uma biblioteca de classes visuais .vcx nova ou existente à qual a definição de classe será adicionada.
**AS cBaseClassName**
Especifica a classe na qual a definição de classe é baseada. Você pode especificar qualquer classe base do Visual FoxPro, exceto Column e Header. Você também pode especificar uma classe definida pelo usuário se incluir a cláusula FROM ClassLibraryName2 que especifica o nome do arquivo de biblioteca de classes visuais (.vcx) contendo a classe definida pelo usuário. Se você omitir AS cBaseClassName, a definição de classe é baseada na classe base FormSet do Visual FoxPro.
**FROM ClassLibraryName2**
Especifica o nome da biblioteca de classes visuais .vcx contendo a classe definida pelo usuário especificada com cBaseClassName.
**NOWAIT**
Continua a execução do programa depois que o Class Designer é aberto. O programa não aguarda o fechamento do Class Designer, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE CLASS NOWAIT. Se você omitir NOWAIT, quando CREATE CLASS é emitido em um programa, o Class Designer é aberto e a execução do programa pausa até que o Class Designer seja fechado. Incluir NOWAIT não tem efeito em CREATE CLASS quando emitido na janela Command.

# Observações

Use CREATE CLASS para criar uma definição de classe e salvá-la em uma biblioteca de classes visuais .vcx. Você pode abrir a biblioteca de classes visuais .vcx com SET CLASSLIB, permitindo acessar as definições de classe dentro da biblioteca de classes visuais .vcx.
