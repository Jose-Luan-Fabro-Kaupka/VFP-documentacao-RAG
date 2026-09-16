# Suporte ao IntelliSense no Visual FoxPro

O Visual FoxPro inclui suporte ao IntelliSense para elementos nativos da linguagem Visual FoxPro, como comandos e funções do Visual FoxPro, e para classes, objetos instanciados e suas propriedades, métodos e eventos, objetos visuais, as variáveis de sistema _VFP e _SCREEN, controles Microsoft ActiveX e servidores COM. Você também pode adicionar suporte ao IntelliSense para bibliotecas de tipos registradas, tipos definidos pelo usuário, membros e elementos de código, valores enumerados e classes personalizadas.

A lista a seguir descreve alguns dos locais onde o Visual FoxPro fornece suporte ao IntelliSense:
 - Janelas onde você pode digitar código, como a janela Command, editores de arquivo de programa (.prg), janelas de código e a janela Watch no Visual FoxPro Debugger. Observação O suporte limitado ao IntelliSense está disponível na janela Watch. Para obter mais informações, consulte Estrutura de tabela IntelliSense . O suporte ao IntelliSense em arquivos de programa (.prg) para elementos como referências de classe, controles ActiveX e servidores COM existe somente quando esses elementos são fortemente tipados. Para obter mais informações, consulte Como: implementar tipagem forte para código de classe, objeto e variável .
- Contêineres e controles em designers do Visual FoxPro, como o Form Designer.

A tabela a seguir resume os locais onde o IntelliSense está disponível para elementos específicos do Visual FoxPro.

| Elemento do Visual FoxPro | Editor do Visual FoxPro | Janela de código | Janela Command |
| --- | --- | --- | --- |
| _SCREEN | A | A | A |
| _VFP / Applications | A | A | A |
| Objetos instanciados | A | | |
| Objetos visuais | S | A | |
| Referências de classe | S | S | |
| Controles ActiveX | S | A | |
| Servidores COM | S | S | |
| THIS, THISFORM, THISFORMSET | S | A | |
| Nomes de tabela e campo | A | | |
| Definido pelo usuário | A | A | A |

A = todos os membros apropriados S = somente membros fortemente tipados

# Suporte ao IntelliSense em tempo de execução

Recursos selecionados do IntelliSense estão disponíveis em tempo de execução em aplicativos Visual FoxPro 9.0 distribuídos. O IntelliSense pode ser controlado explicitamente em tempo de execução através de scripts FoxCode. Consulte Personalizando IntelliSense no Visual FoxPro na Ajuda para informações adicionais sobre como adicionar IntelliSense ao seu aplicativo em tempo de execução.

A tabela a seguir lista os recursos do IntelliSense que estão disponíveis em tempo de execução.

| Recurso | Descrição |
| --- | --- |
| Editor aberto com Comando MODIFY COMMAND | A coloração de sintaxe está disponível somente em um editor aberto com o comando MODIFY COMMAND. A coloração de sintaxe é suportada mesmo se a quebra de linha estiver desativada. |
| List Members | Disponível somente através do objeto oFoxCode em um script FoxCode. |
| Quick Info | Disponível somente através do objeto oFoxCode em um script FoxCode. |
| Variável de sistema _FOXCODE | Disponível em tempo de execução, mas você deve definir seu valor como o nome do arquivo de tabela usado pelo seu aplicativo em tempo de execução. |
| Variável de sistema _CODESENSE | Disponível em tempo de execução, esta variável de sistema contém o nome do aplicativo que fornece funcionalidade para o IntelliSense Manager. Por padrão, o aplicativo é FoxCode.app, que também contém a biblioteca para os scripts FoxCode comuns. Observação Um aplicativo não é explicitamente necessário para suporte ao IntelliSense em tempo de execução. Por padrão, _CODESENSE contém a cadeia de caracteres vazia em tempo de execução. Você deve definir seu valor como o nome do aplicativo IntelliSense usado pelo seu aplicativo em tempo de execução. |
| _VFP.EditorOptions | A Propriedade EditorOptions não é definida em tempo de execução. Você deve definir explicitamente a propriedade em tempo de execução para habilitar o suporte ao IntelliSense. |
| FoxCode Field Type = C (Command) | Suportado em tempo de execução. |
| FoxCode Field Type = F (Function) | Suportado em tempo de execução. |
| FoxCode Field Type = U (User) | Suportado em tempo de execução. |
| FoxCode Field Type = S (Script) | Suportado em tempo de execução. |

A tabela a seguir lista os recursos do IntelliSense que não estão disponíveis em tempo de execução.

| Recurso | Descrição |
| --- | --- |
| Atalhos de teclado | Atalhos de teclado do IntelliSense não estão disponíveis em tempo de execução para funcionalidade Automatic List Members, Quick Info ou List Values. |
| Comandos de menu | Os comandos IntelliSense List Members e Quick Info no menu Edit não estão disponíveis nos editores do Visual FoxPro em tempo de execução. |
| List Values | Não suportado em tempo de execução. |
| Suporte a objetos nativos | Não suportado em tempo de execução. |
| Tipagem de variáveis | Não suportado em tempo de execução. |
| Lista de uso mais recente | Não suportado em tempo de execução. |
| FoxCode Field Type = T (Typing) | Não suportado em tempo de execução. |
| FoxCode Field Type = O (COM Typing) | Não suportado em tempo de execução. |
| FoxCode Field Type = P (Property) | Não suportado em tempo de execução. |
| FoxCode Field Type = E (XML) | Não suportado em tempo de execução. |
