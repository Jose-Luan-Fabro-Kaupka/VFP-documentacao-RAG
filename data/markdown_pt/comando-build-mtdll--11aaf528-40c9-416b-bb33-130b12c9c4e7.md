# Comando BUILD MTDLL

Cria uma biblioteca de vínculo dinâmico (.dll) multithread do Windows, ou servidor de Automação, usando definições de classe de um projeto.

```foxpro
BUILD MTDLL MTDLLFileName FROM ProjectName [RECOMPILE]
```

#### Parâmetros
 **MTDLLFileName**
Especifica o nome do arquivo da biblioteca de vínculo dinâmico a ser compilada. A extensão padrão do arquivo é .dll.
**FROM ProjectName**
Especifica o nome do projeto a partir do qual a biblioteca de vínculo dinâmico será compilada. O projeto deve conter uma classe designada como OLEPUBLIC; caso contrário, será exibida uma mensagem de erro. Para designar uma classe como OLEPUBLIC no código do programa, inclua a palavra-chave OLEPUBLIC em DEFINE CLASS. Para designar uma classe como OLEPUBLIC no Class Designer, escolha Class Info no menu Class e marque a caixa de seleção OLE Public.
**[RECOMPILE]**
Especifica que o projeto seja compilado antes da construção da biblioteca de vínculo dinâmico. São compilados todos os arquivos de programa e de formato; o código-fonte de formulários, etiquetas, relatórios e bibliotecas de classes visuais; e os procedimentos armazenados nos bancos de dados do projeto.

# Observações

BUILD MTDLL registra automaticamente o servidor na lista Server Classes da guia Servers da caixa de diálogo Project Information.

O runtime do Visual FoxPro que cria arquivos .dll multithread cria somente servidores em processo. Muitos comandos e funções de entrada do usuário não são compatíveis. Para obter mais informações, consulte Interoperabilidade e a Internet.
