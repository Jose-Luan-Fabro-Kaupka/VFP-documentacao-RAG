# Função NEWOBJECT( )

Cria uma nova classe ou objeto diretamente de um arquivo de biblioteca de classes visual (.vcx) ou arquivo de programa (.prg) sem abrir o arquivo.

```foxpro
NEWOBJECT(cClassName [, cModule [, cInApplication | 0
   [, eParameter1, eParameter2, ...]]])
```

#### Parâmetros
 **cClassName**
Especifica a classe ou objeto da qual a nova classe ou objeto é criada.
**cModule**
Especifica um arquivo .vcx ou programa Visual FoxPro (.prg, .fxp, .mpr, .app, .exe e assim por diante) contendo a classe ou objeto especificado com cClassName. O padrão é um arquivo .vcx. Se você especificar um arquivo de programa, deve incluir uma extensão. Observação Uma biblioteca de classes pode ter um alias. Para especificar uma classe ou objeto de uma biblioteca de classes com alias, inclua o alias da biblioteca de classes seguido de um ponto e o nome do objeto. Quando possível, especifique o nome do programa compilado (.fxp) quando uma classe estiver armazenada em um arquivo de programa (.prg). Isso garante que a classe seja carregada do arquivo de definição de classe adequado. Se cModule for omitido, ou for a cadeia de caracteres vazia ou o valor nulo, o Visual FoxPro procura a classe ou objeto na seguinte ordem: classes base do Visual FoxPro. Classes no programa atual. Bibliotecas de classes abertas com SET CLASSLIB. Classes em arquivos de procedimento abertos com SET PROCEDURE. Classes na cadeia de execução de programa do Visual FoxPro. O registro OLE se SET OLEOBJECT estiver ON.
**cInApplication**
Especifica a aplicação Visual FoxPro (.exe ou .app) contendo o arquivo .vcx especificado com cModule. Você deve incluir uma extensão para a aplicação. CInApplication é ignorado se cModule for omitido, ou se cInApplication for a cadeia de caracteres vazia ou o valor nulo. Se você quiser usar o parâmetro cInApplication, deve especificar o nome do arquivo .vcx para cModule. Você não pode passar o nome de um arquivo .prg ou programa compilado (.fxp).
**0**
Especifica que a classe ou objeto é instanciada sem executar nenhum código de evento ou método na classe ou objeto. Este recurso não é suportado em aplicações de runtime. Todas as classes ou objetos filhos da classe pai também são instanciados. O código de evento ou método na classe ou objeto filho não é executado. Esta opção fornece a capacidade de visualizar a estrutura de uma classe ou objeto (com a função AMEMBERS( ), por exemplo) sem abrir a classe ou objeto no Class ou Form Designer. Observe que o código na classe ou objeto nunca deve ser executado — a execução de código não é suportada e pode tornar o Visual FoxPro instável. Você nunca deve chamar explicitamente um evento ou método, ou definir propriedades. Definir propriedades pode chamar métodos Access e Assign.
**eParameter1 , eParameter2 , ...**
Especifica parâmetros opcionais passados ao procedimento do evento Init da classe ou objeto.

# Valor de retorno

Object

# Observações

Para atribuir a referência de objeto retornada por NEWOBJECT( ) a uma variável ou elemento de matriz, use o sinal de igual (=) ou o comando STORE. Se um objeto atribuído a uma variável ou elemento de matriz for liberado, a variável ou elemento de matriz contém o valor nulo. Para remover a variável ou elemento de matriz da memória, use o comando RELEASE.

Para NEWOBJECT( ), o Visual FoxPro executa um SET CLASSLIB ou SET PROCEDURE interno para o segundo ou terceiro parâmetros usando a cláusula ADDITIVE onde os parâmetros são usados primeiro para determinar a ordem de pesquisa. Se esses parâmetros já existirem na lista SET CLASSLIB ou SET PROCEDURE, o Visual FoxPro reorganiza a ordem na lista para que venham primeiro. O Visual FoxPro então localiza todas as classes, cria o objeto e chama os eventos Init. Por fim, o Visual FoxPro restaura a lista SET CLASSLIB ou SET PROCEDURE original se a instalação não alterou a lista.

Objetos OLE são criados com a seguinte sintaxe para cClassName:

```foxpro
ApplicationName.Class
```

Por exemplo, para criar uma planilha do Microsoft Excel, que suporta Automation, use a seguinte sintaxe:

```foxpro
oExcelSheet = NEWOBJECT('Excel.Sheet')
```
