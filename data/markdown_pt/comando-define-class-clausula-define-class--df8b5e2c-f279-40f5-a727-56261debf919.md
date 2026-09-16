# Comando DEFINE CLASS - Cláusula DEFINE CLASS

Especifica o nome da classe a criar e a classe pai usada para criar a nova classe. Você também pode tornar possível que clientes de automação acessem a classe quando incluída em um servidor de automação.

```foxpro
DEFINE CLASS ClassName1 AS ParentClass [OF ClassLibrary] [OLEPUBLIC]
[Other DEFINE CLASS clauses]
```

#### Parâmetros
 **DEFINE CLASS ClassName1 AS ParentClass**
Especifica o nome da classe a criar e a classe pai a ser usada como classe base. A classe pai pode ser uma classe base do Visual FoxPro, como a classe Form, ou outra classe ou subclasse definida pelo usuário. Você também pode criar subclasses das classes Exception e Session, além das classes base do Visual FoxPro. Observação Se você especificar Custom como ParentClass , o Visual FoxPro cria uma classe definida pelo usuário não visual . Se você especificar Session como ParentClass , o Visual FoxPro cria uma classe definida pelo usuário não visual que mantém sua própria sessão de dados privada. A cláusula ADD OBJECT não está disponível quando você especifica Session como ParentClass porque um objeto Session não é um contêiner. Para obter mais informações, consulte Objeto Session . Para obter mais informações sobre classes base do Visual FoxPro, consulte Classes base no Visual FoxPro . Você também pode usar a cláusula AS para implementar tipagem forte. A funcionalidade IntelliSense está disponível para referências de objetos e variáveis somente quando são fortemente tipadas. Para obter mais informações, consulte Como: implementar tipagem forte para código de classe, objeto e variável .
**[OF ClassLibrary ]**
Torna possível especificar uma biblioteca de classes para AS ParentClass sem precisar especificar explicitamente o caminho para a biblioteca de classes que a contém, como ao usar os comandos SET CLASSLIB ou SET PROCEDURE. ClassLibrary pode ser um arquivo de biblioteca de classes (.vcx), programa (.prg) ou programa compilado (.fxp). A ClassLibrary especificada pode conter um caminho relativo, desde que o Visual FoxPro possa localizar a biblioteca em seus caminhos de pesquisa de biblioteca de classes usuais. Se o Visual FoxPro não encontrar a ClassLibrary especificada quando você tentar instanciar uma instância da classe, o Visual FoxPro gera um erro. O Visual FoxPro adiciona ClassLibrary ao projeto durante o processo de compilação automaticamente se o programa que contém a classe estiver incluído no projeto. Ao usar a cláusula OF ClassLibrary, certifique-se de que o programa atual não tenha o mesmo nome de classe que o especificado na cláusula OF ClassLibrary. Observação Se uma referência OF < ProgramFile> for usada em um programa que está vinculado dentro de um aplicativo executável, o nome de <ProgramFile> deve ter uma extensão de nome de arquivo .fxp e não .prg.
**[OLEPUBLIC]**
Especifica que clientes de automação podem acessar a classe quando incluída em um servidor de automação. Observação Se você incluir a palavra-chave OLEPUBLIC para uma classe cuja classe base é Session , a biblioteca de tipos gerada para um executável (.exe) ou biblioteca de vínculo dinâmico (.dll) contém somente suas propriedades e métodos personalizados. Todas as propriedades, métodos e eventos intrínsecos da classe base Session são excluídos da biblioteca de tipos. Este comportamento é suportado no Visual FoxPro 7.0 e posterior. Se você adicionar um programa com uma definição de classe criada como OLEPUBLIC a um projeto, pode criar um arquivo .exe ou .dll contendo a classe interativamente usando o Project Manager, os comandos BUILD EXE , BUILD DLL ou BUILD MTDLL. O .exe ou .dll se registra no sistema operacional automaticamente e torna-se disponível para qualquer cliente de automação. Para obter mais informações, consulte Como: criar servidores de automação , Como: compilar aplicativos , Comando BUILD EXE , Comando BUILD DLL ou Comando BUILD MTDLL .
**ENDDEFINE**
Indica o fim da definição de classe.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando DEFINE CLASS:

```foxpro
DEFINE CLASS Clause
   [Property_Definition_Clause]
   [PEMName_COMATTRIB Clause]
   [ADD OBJECT Clause]
   [IMPLEMENTS Clause]
   [Function_Procedure_Definition_Clause]
ENDDEFINE
```

Para obter mais informações e sintaxe completa, consulte Comando DEFINE CLASS. Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS, consulte os seguintes tópicos:
 - Cláusula Property Definition
- Cláusula PEMName_COMATTRIB
- Cláusula ADD OBJECT
- Cláusula IMPLEMENTS
- Cláusula Function or Procedure Definition

# Exemplo

O exemplo a seguir cria uma classe chamada MyForm a partir da classe base Form e cria uma propriedade protegida chamada Version. A classe também contém outra propriedade chamada Caption, que não é protegida. A definição de classe inicializa os valores padrão de Version e Caption para as cadeias de caracteres "1.0" e "My Form", respectivamente.

```foxpro
DEFINE CLASS MyForm AS Form
   PROTECTED Version
   Version = "1.0"
   Caption = "My Form"
ENDDEFINE
```
