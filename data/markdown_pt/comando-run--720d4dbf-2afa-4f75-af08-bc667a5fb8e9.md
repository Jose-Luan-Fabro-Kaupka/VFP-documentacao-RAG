# Comando RUN | !

Executa comandos ou programas externos do sistema operacional.

```foxpro
RUN [/N] WindowsCommand | ProgramName
```

```foxpro
! [/N] WindowsCommand | ProgramName
```

#### Parâmetros
 **WindowsCommand**
Especifica um comando executável do Windows a ser executado.
**ProgramName**
Especifica o programa ou aplicativo do Windows a ser executado.
**/N**
Especifica NOWAIT. Inclua /N para executar outro aplicativo baseado no Windows.

# Observações

Você pode emitir RUN na Janela de Comando ou em um programa.

> **Observação:** Para usar RUN, Command.com ou Cmd.exe deve estar localizado onde a variável de ambiente COMSPEC possa encontrá-lo.

> **Cuidado:** Não use RUN para executar programas de reorganização de disco, como CHKDSK, a partir do Visual FoxPro. Esses programas modificam o conteúdo do disco de uma maneira que pode impedir o funcionamento adequado do Visual FoxPro.

### RUN e Visual FoxPro

O comando RUN (sem o parâmetro /N) usa a seguinte ordem de sequência para determinar qual programa usar ao executar o comando RUN especificado:
 - Arquivo PIF nomeado — se o programa que você especificar em RUN não tiver uma extensão, o Visual FoxPro primeiro procura um Program Information File (PIF) com o nome que você especificar. Se o arquivo PIF for encontrado, o programa especificado no PIF é executado com os parâmetros do PIF.
- Arquivo FOXRUN.PIF — se um arquivo PIF nomeado não puder ser encontrado, o comando RUN procura o arquivo Foxrun.pif padrão. Se este arquivo for encontrado, o programa especificado em Foxrun.pif é executado com os parâmetros do PIF.
- Variável de ambiente COMSPEC — se nenhum arquivo PIF for encontrado que atenda aos critérios acima, o comando RUN usa o programa SHELL especificado pela variável de ambiente COMSPEC do sistema operacional Windows. Essa variável normalmente aponta para Cmd.exe; no entanto, em sistemas operacionais mais antigos, como o Windows 98, apontará para Command.com.

> **Observação:** Para o Visual FoxPro 9, o arquivo Foxrun.pif não é mais instalado no diretório raiz do Visual FoxPro, de modo que não é mais usado por padrão. O comportamento padrão para o Visual FoxPro 9 é que um comando RUN (sem o parâmetro /N) deve usar o programa SHELL especificado pela variável de ambiente COMSPEC. Foxrun.pif agora é instalado no diretório Tools do Visual FoxPro, se necessário.

Um PIF permite executar outros programas no Windows. Você pode especificar parâmetros para o programa, como se o programa é executado em uma janela ou em tela cheia, a quantidade de memória alocada para o programa e assim por diante.

Se for usado, Foxrun.pif deve estar no mesmo diretório que VFPVersionNumber.exe, onde VersionNumber representa o número da versão desta release do Visual FoxPro.

A menos que seja necessário, um arquivo PIF deve ser evitado, pois o comando RUN usa automaticamente Command.com para chamar o programa especificado no arquivo PIF. Por exemplo, se seu arquivo PIF especificasse Cmd.exe como o programa a ser executado, o Visual FoxPro teria Command.com chamando Cmd.exe para executar o comando RUN especificado, o que pode não ser o comportamento desejado. É preferível que o comando RUN use diretamente o programa SHELL especificado pela variável de ambiente COMSPEC do sistema operacional.

> **Observação:** No Windows XP, você pode visualizar e editar a variável de ambiente COMSPEC clicando com o botão direito no ícone Meu Computador na área de trabalho e selecionando a caixa de diálogo Propriedades (guia Avançado).

### /N

/N significa NOWAIT. Inclua a letra N para executar outro aplicativo baseado no Windows e retornar o controle imediatamente ao Visual FoxPro. Por exemplo, a instrução a seguir abre o acessório Mapa de Caracteres do Windows:

```foxpro
! /N CHARMAP.EXE
```

O exemplo a seguir abre a caixa de diálogo Propriedades de Exibição do Windows:

```foxpro
! /N CONTROL COLOR
```

Um aplicativo baseado no Windows executado com RUN /N ou ! /N se comporta da mesma forma que quando você o abre pelo Windows Explorer ou selecionando Executar no menu Iniciar. Você pode alternar entre o aplicativo e o Visual FoxPro ou FoxPro for Windows usando as operações padrão do Windows.

Você pode incluir um valor numérico opcional imediatamente após /N para especificar como o aplicativo baseado no Windows é aberto. Não inclua espaços entre /N e o valor numérico. A tabela a seguir lista o valor numérico que você pode incluir e descreve o estado do aplicativo baseado no Windows quando aberto.

| Valor | Atributos do aplicativo |
| --- | --- |
| 1 | Ativo e tamanho normal. |
| 2 | Ativo e minimizado. |
| 3 | Ativo e maximizado. |
| 4 | Inativo e tamanho normal. |
| 7 | Inativo e minimizado. |

### Executando programas externos no Visual FoxPro

Por padrão, Foxrun.pif executa o programa externo especificado em uma janela. No Visual FoxPro, a Janela de Comando FoxPro Run é fechada depois que o programa ou comando externo termina de ser executado.

Você pode usar o editor PIF do Windows para personalizar Foxrun.pif. Você pode editar o PIF para especificar se a Janela de Comando FoxPro Run inativa é deixada aberta ou fechada (o padrão no Visual FoxPro) com a caixa de seleção Close Window on Exit. Você também pode abrir programas externos em tela cheia selecionando Full Screen; alocar memória para o programa; e assim por diante.

### Certificação Windows 2000 Logo

Se você planeja enviar seu aplicativo para certificação Windows Logo, não deve usar o comando RUN, pois ele pode violar potencialmente os requisitos de System Group Policy. Em vez disso, você deve usar DECLARE DLL com ShellExecuteEx.API.
