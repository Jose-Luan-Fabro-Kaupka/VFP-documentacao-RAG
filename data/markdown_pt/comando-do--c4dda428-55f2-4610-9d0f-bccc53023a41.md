# Comando DO

Executa um programa ou procedimento do Visual FoxPro.

> **Dica:** Você pode executar um programa que executa outro programa que executa outro programa e assim por diante incluindo comandos DO aninhados adicionais em um arquivo de programa. Para obter mais informações sobre níveis de aninhamento de programas, consulte Capacidades do sistema do Visual FoxPro .

```foxpro
DO ProgramName1 | ProcedureName [IN ProgramName2] [WITH ParameterList]
```

#### Parâmetros
 **ProgramName1**
Especifica o nome do programa a ser executado. Se você não incluir uma extensão com o programa que executa, o Visual FoxPro procura e executa versões do programa na seguinte ordem: Executável (.exe) Aplicativo (.app) Compilado (.fxp) Programa (.prg) Para executar um menu, formulário ou consulta específica usando o comando DO, você deve incluir a extensão do arquivo (.mpr, .spr ou .qpr).
**ProcedureName**
Especifica o nome do procedimento a ser executado. O Visual FoxPro primeiro procura o procedimento no programa em execução. Se o procedimento não for localizado ali, o Visual FoxPro procura o procedimento nos arquivos de procedimento abertos com SET PROCEDURE. Você pode incluir a cláusula IN ProgramName2 para informar ao Visual FoxPro que procure o procedimento em um arquivo que você especificar. Vários procedimentos em uma versão executável (.exe) ou em um aplicativo (.app) podem ter o mesmo nome. Quando você usa o comando DO para iniciar um procedimento em uma versão executável ou em um aplicativo, o Visual FoxPro procura apenas o programa principal da versão executável ou do aplicativo pelo procedimento especificado.
**IN ProgramName2**
Executa um procedimento no arquivo de programa especificado com ProgramName2. Quando o arquivo é localizado, o procedimento é executado. Se o arquivo de programa não puder ser localizado, a mensagem "File does not exist" é exibida. Se o arquivo de programa for localizado, mas o procedimento especificado não estiver no arquivo de programa, a mensagem "Procedure is not found" é exibida.
**WITH ParameterList**
Especifica parâmetros a serem passados ao programa ou procedimento. Os parâmetros listados em ParameterList podem ser expressões, variáveis de memória, literais, campos ou funções definidas pelo usuário. Por padrão, os parâmetros são passados a programas e procedimentos por referência. Você pode passar um parâmetro por valor colocando-o entre parênteses. Consulte o Comando SET UDFPARMS para uma discussão sobre passagem de parâmetros por valor ou referência. O número máximo de parâmetros que você pode passar a um programa ou procedimento é 26. Para obter mais informações sobre passagem de parâmetros, consulte o Comando LPARAMETERS e o Comando PARAMETERS .

# Observações

Quando você usa DO para executar um programa, os comandos contidos no arquivo de programa são executados até que ocorra uma das seguintes situações:
 - RETURN é encontrado.
- CANCEL é executado.
- Outro DO é emitido.
- O final do arquivo é alcançado.
- QUIT é executado.

Quando a execução do programa é concluída, o controle é retornado a um dos seguintes:
 - Programa que chamou DO
- Janela de comando
- Sistema operacional

Se você escolher Do no menu Program e executar um programa em um diretório em uma unidade diferente do diretório ou unidade atual, o Visual FoxPro altera automaticamente o diretório e a unidade padrão para o diretório e a unidade que contêm o programa.

Você também pode modificar como um aplicativo procura dados e recursos, como funções, procedimentos, arquivos executáveis e assim por diante, usando SYS(2450) - Ordem de pesquisa do caminho do aplicativo.
