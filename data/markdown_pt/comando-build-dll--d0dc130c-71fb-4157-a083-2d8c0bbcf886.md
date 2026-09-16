# Comando BUILD DLL

Cria uma biblioteca de vínculo dinâmico (.dll) de thread única do Windows, ou servidor Automation, usando definições de classe de um projeto Visual FoxPro.

```foxpro
BUILD DLL DLLFileName FROM ProjectName [RECOMPILE]
```

#### Parâmetros
 **DLLFileName**
Especifica o nome do arquivo da biblioteca de vínculo dinâmico a ser compilada. A extensão de arquivo padrão é .dll.
**FROM ProjectName**
Especifica o nome do projeto a partir do qual a biblioteca de vínculo dinâmico é compilada. O projeto deve conter uma classe designada como OLEPUBLIC ou uma mensagem de erro é exibida. Para designar uma classe como OLEPUBLIC em código de programa, inclua a palavra-chave OLEPUBLIC em DEFINE CLASS . Para designar uma classe como OLEPUBLIC no Class Designer, escolha Class Info no menu Class e selecione a caixa de seleção OLE Public.
**[RECOMPILE]**
Especifica que o projeto seja compilado antes que a biblioteca de vínculo dinâmico seja compilada. Todos os programas e arquivos de formato; código-fonte de formulário, etiqueta, relatório e biblioteca de classes visuais; e procedimentos armazenados em bancos de dados no projeto são compilados.

# Observações

BUILD DLL registra o servidor automaticamente na lista Server Classes na guia Servers da caixa de diálogo Project Information.
