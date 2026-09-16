# Guia Servers, Caixa de diálogo Project Information

Exibe classes localizadas em servidores, sua biblioteca de classes, instancing, descrição, tipo e informações de Help.

> **Observação:** As alterações feitas na guia Servers exigem que você recompile o .dll ou .exe para que as novas configurações entrem em vigor.
 **Server Classes**
Exibe uma lista de todas as classes disponíveis, tanto .vcx quanto em código, que estão marcadas como OLEPublic. Cada classe na lista tem um arquivo .pjx correspondente.
**Class Library**
Exibe o caminho do diretório da biblioteca de classes na qual a classe selecionada está armazenada.
**Class Name**
Exibe o nome da classe.
**Instancing**
Exibe uma das seguintes opções: Single Use Especifica que você pode criar uma instância da classe tanto dentro do Visual FoxPro quanto fora dele usando Automation. Cada solicitação de uma instância da classe por um cliente Automation fora do projeto faz com que uma cópia separada do servidor Automation seja iniciada. Cada instância tem um único thread de execução. Embora instâncias separadas exijam mais memória, escolher Single Use permite que o sistema operacional aplique multitarefa preemptiva. Instancing tem como padrão Single Use quando você cria um novo projeto contendo classes OLEPUBLIC. Essa configuração é apropriada para compilar servidores EXE. Not Creatable Especifica que você pode criar instâncias da classe somente dentro do Visual FoxPro. Multi Use Especifica que você pode criar uma instância da classe tanto dentro do Visual FoxPro quanto fora dele usando Automation. Cada solicitação de uma instância da classe por um cliente Automation fora do projeto faz com que uma cópia já em execução do servidor Automation seja fornecida como origem da nova instância. Depois que o servidor foi criado, outros aplicativos podem usar a mesma instância. Instancing tem como padrão Multi Use quando você cria um servidor COM .dll.
**Description**
Exibe uma pequena descrição da classe. Por padrão, o Visual FoxPro registra a notação completa Project.Server como descrição. Isso garante chaves de registro consistentes. Você pode especificar uma Description diferente aqui.
**Help file**
Exibe o arquivo de Help associado ao servidor. Selecione o botão de diálogo para exibir a caixa de diálogo Open se nenhum arquivo estiver listado.
**Help context ID**
Exibe o ID de contexto do arquivo de Help associado ao aplicativo, se um arquivo de Help for distribuído com o aplicativo.
**Project name**
Exibe o nome do projeto associado às classes de servidor.
**Typelib description**
Exibe uma descrição da biblioteca de classes na qual a classe selecionada é baseada.
