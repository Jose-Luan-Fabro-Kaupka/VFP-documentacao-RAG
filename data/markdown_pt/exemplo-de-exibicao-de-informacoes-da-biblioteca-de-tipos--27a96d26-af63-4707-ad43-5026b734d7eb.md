# Exemplo de exibição de informações da biblioteca de tipos

Arquivo: ...\Samples\Solution\Winapi\Typelib.scx

O exemplo TYPELIB usa uma classe do Visual FoxPro chamada Typelib, armazenada em ...\Samples\Classes\Typelib.vcx. Essa classe container possui um controle ActiveX com vários métodos para ler informações da biblioteca de tipos de qualquer arquivo .dll, .exe ou .tlb.

A classe wrapper Typelib economiza tempo ao realizar grande parte do trabalho. O método ExportTypeLib dessa classe exporta o conteúdo de uma biblioteca de tipos especificada para um arquivo de texto.

```foxpro
THISFORM.typelib1.TypeLibName = THISFORM.txtFileName.Value
THISFORM.typelib1.ExportTypeLib()
```

Ao examinar o arquivo de texto gerado, você perceberá que uma biblioteca de tipos pode conter várias Type Infos. Cada Type Info representa uma classe específica. Quando você gera um novo EXE ou DLL de um projeto usando o Visual FoxPro, cada classe marcada como OLEPUBLIC gera um Custom OLE Server separado.

> **Observação:** Há apenas um arquivo .exe/.dll, mas ele pode conter vários servidores (um para cada classe OLEPUBLIC). O Visual FoxPro gera um único arquivo TLB para o projeto. Esse arquivo de biblioteca de tipos contém uma Type Info separada para cada classe OLEPUBLIC.

Cada Type Info (classe OLEPUBLIC) também contém descrições de funções. Elas representam todas as propriedades e métodos de uma classe. Para métodos, a biblioteca de tipos contém os tipos dos parâmetros e do retorno. Alguns tipos possíveis são Boolean, string e variant. Como o Visual FoxPro não tipa fortemente as variáveis de memória, muitos tipos usados em seus métodos personalizados serão variant.

Ao examinar as funções exportadas, você notará entradas duplicadas para muitas propriedades. Isso ocorre porque os usuários podem definir ou obter o valor da propriedade. Algumas linguagens, como Visual Basic, permitem executar código quando uma dessas propriedades é acessada ou atribuída. Assim, a biblioteca de tipos representa uma única propriedade com duas entradas. Se houver apenas uma, a propriedade será somente leitura. Propriedades e métodos marcados como Hidden ou Protected não aparecerão na biblioteca de tipos.
