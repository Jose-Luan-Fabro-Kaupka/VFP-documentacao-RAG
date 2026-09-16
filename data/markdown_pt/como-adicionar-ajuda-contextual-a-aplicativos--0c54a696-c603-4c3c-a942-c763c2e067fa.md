# Como: adicionar Ajuda contextual a aplicativos

Adicionar Ajuda contextual a aplicativos permite que os usuários acessem tópicos relacionados às tarefas que executam ou aos elementos da interface exibidos no aplicativo. Por exemplo, se um usuário estiver visualizando um formulário de entrada de dados, você poderá configurar a Ajuda contextual para fornecer um tópico especificamente relacionado a esse formulário.

Você pode escolher o nível de detalhe da Ajuda contextual a ser implementado no aplicativo. Por exemplo, pode associar um tópico a um formulário ou associar tópicos mais detalhados a cada controle e campo do formulário.

Em geral, os usuários acessam a Ajuda contextual pressionando a tecla F1. Por padrão, F1 está habilitada para essa finalidade.

> **Observação:** Embora seja possível mapear qualquer tecla para ativar a Ajuda contextual usando o comando ON KEY LABEL, pressionar F1 é um padrão reconhecido para a Ajuda; portanto, não se recomenda redefinir essa tecla. Para obter mais informações, consulte Comando ON KEY LABEL.

Para adicionar Ajuda contextual, você deve especificar um arquivo de Ajuda para o aplicativo e atribuir tópicos específicos aos objetos do aplicativo.

# Especificando um arquivo de Ajuda

### Para especificar um arquivo de Ajuda para o aplicativo
- Use o comando SET HELP para especificar o nome do arquivo de Ajuda que deseja usar. Dica: esse comando geralmente é incluído no código de configuração do programa principal do aplicativo.

Para obter mais informações, consulte Comando SET HELP.

Por exemplo, a linha de código a seguir define o arquivo de Ajuda HTML MyHelp.chm como o arquivo a ser usado:

```foxpro
SET HELP TO MyHelp.chm
```

# Atribuindo tópicos de Ajuda

Você pode atribuir tópicos específicos de Ajuda a objetos do aplicativo, como formulários, controles ou barras de ferramentas.

### Para atribuir um tópico de Ajuda a um objeto
- Em tempo de design, selecione o objeto ao qual deseja atribuir um tópico.
- No menu Window, clique em Properties Window.
- Na janela Properties, defina a propriedade HelpContextID com o número associado ao tópico no arquivo de Ajuda.

Para obter mais informações, consulte Propriedade HelpContextID (Visual FoxPro).

> **Observação:** Para atribuir tópicos de Ajuda a títulos ou comandos de menu, inclua o comando SET TOPIC no procedimento associado ao título ou comando de menu. Para obter mais informações, consulte Comando SET TOPIC.
