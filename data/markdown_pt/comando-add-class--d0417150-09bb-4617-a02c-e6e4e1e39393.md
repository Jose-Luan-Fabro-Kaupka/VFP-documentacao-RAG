# Comando ADD CLASS

Adiciona uma definição de classe a uma biblioteca de classes visuais .vcx.

```foxpro
ADD CLASS ClassName [OF ClassLibraryName1] TO ClassLibraryName2
   [OVERWRITE]
```

#### Parâmetros
 **ClassName**
Especifica o nome da definição de classe adicionada à biblioteca de classes visuais .vcx ClassLibraryName2 . Se você omitir a cláusula opcional OF ClassLibraryName1, o Visual FoxPro procura a definição de classe em quaisquer bibliotecas de classes visuais .vcx abertas com SET CLASSLIB. O Visual FoxPro gera um erro se a definição de classe não puder ser localizada ou se já existir uma definição de classe com o nome que você especificar em ClassLibraryName2 .
**OF ClassLibraryName1**
Especifica uma biblioteca de classes visuais .VCX da qual a definição de classe é copiada.
**TO ClassLibraryName2**
Especifica a biblioteca de classes visuais .vcx à qual a definição de classe é adicionada. Se você especificar uma biblioteca de classes visuais .vcx que não existe, o Visual FoxPro cria a biblioteca de classes visuais e adiciona a definição de classe à biblioteca.
**OVERWRITE**
Especifica que uma definição de classe com o mesmo nome da definição de classe que você especificar com ClassName é substituída. Uma mensagem de erro é gerada se você omitir OVERWRITE e já existir uma definição de classe com o mesmo nome que ClassName na biblioteca de classes visuais .vcx.

# Observações

Use ADD CLASS para adicionar uma definição de classe a uma biblioteca de classes ou para copiar uma definição de classe de uma biblioteca de classes visuais .vcx para outra. Uma definição de classe não pode ser adicionada a partir de um programa ou aplicativo Visual FoxPro (.prg ou .app) ou de um arquivo de procedimentos.
