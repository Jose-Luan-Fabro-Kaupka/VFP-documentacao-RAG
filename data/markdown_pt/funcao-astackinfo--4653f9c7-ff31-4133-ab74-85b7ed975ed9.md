# Função ASTACKINFO( )

Cria um array e o preenche com informações sobre o estado atual da pilha de chamadas.

```foxpro
ASTACKINFO(ArrayName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array para armazenar informações sobre a pilha de chamadas. A tabela a seguir descreve as informações retornadas pela função ASTACKINFO( ): Elemento do array Descrição 1 Nível da pilha de chamadas 2 Nome do arquivo do programa atual 3 Nome do módulo ou objeto 4 Nome do arquivo de origem do módulo ou objeto 5 Número da linha no arquivo de origem do objeto 6 Conteúdo da linha de origem

# Valor de retorno

Numérico

# Observações

ASTACKINFO( ) preenche um array com informações sobre toda a pilha de chamadas. Combina a funcionalidade das funções SYS(16) e PROGRAM( ) enquanto adiciona novo suporte para números de linha em cada nível da pilha de chamadas. O valor retornado é o número de níveis de programa ou linhas do array retornado.

ASTACKINFO( ) preenche o 6º elemento do array somente se o conteúdo da linha de origem estiver disponível; caso contrário, ele ficará vazio.

ASTACKINFO( ) fornece, nos 2º e 4º elementos respectivamente, o nome do arquivo atual e, se o arquivo estiver vinculado em um APP ou outro arquivo separado, um caminho completo para o programa de vinculação.

O 4º elemento contém as informações do arquivo de origem original. Para objetos, estas são as mesmas informações retornadas por SYS(16), mesmo quando vinculados dentro de aplicações.

> **Observação:** ASTACKINFO() pode não ser capaz de recuperar informações sobre arquivos de programa (.prg). Neste caso, o Visual FoxPro exibe o 2º elemento de forma semelhante à função SYS(16). Para mais informações, consulte SYS(16) - Executing Program File Name .

# Exemplo

Um formulário sem modal vinculado em um arquivo APP (myAppl.app) com um botão da classe buttons.vcx (também no APP). O desenvolvedor executa myAppl.app no Visual FoxPro para exibir o formulário (o formulário permanece aberto porque este não é o Visual FoxPro em tempo de execução). Quando o usuário clica no botão para executar o relatório, o relatório (que existe fora de myAppl.app) chama um formulário de consulta em seu evento BeforeOpenTables.

Este formulário de consulta (getcusts.scx), que reside dentro de myAppl.app, emite uma chamada a ASTACKINFO( ) [e então exibe o array resultante como no exemplo a seguir].

```foxpro
ASTACKINFO(myarray)
DISPLAY MEMO LIKE myarray
myArray
(1,1)   1                                    && Stack level = 1
(1,2)   c:fp\myAppl.app                        && Current program
(1,3) frmRerport.PrintReport.Click         && Object
(1,4) c:fp\myclassesuttons.vct         && Object source file name
(1,5) 42                              && Line number in the source
(1,6) THISFORM.DoReport()                  && in the source
(2,1)   2                                    && Stack level = 2
(2,2) c:fp\myAppl.app
(2,3) frmRerport.DoReport
(2,4) c:fpormsrmRerport.sct         && Module source file name
(2,5) 31
(2,6) DO RunListReport                     && in the source
(3,1)   3                                    && Stack level = 3
(3,2) c:fp\myAppl.app
(3,3)
(3,4) c:fp\programs
unlisterport.prg   && Module source file name
(3,5) 12
(3,6) REPORT FORM myreport1.frx            && in the source
(4,1)   4                                    && Stack level = 4
(4,2) c:fp
eports\myreport1.frt
(4,3) myreport1.DataEnvironment.BeforeOpenTables
(4,4) c:fp
eports\myreport1.frt          && Module source file name
(4,5) 31
(4,6) DO FORM getcusts                     && in the source
(5,1)   5                                    && Stack level = 5
(5,2) c:fp\myAppl.app
(5,3) getcusts.init
(5,4) c:fporms\getcusts.sct            && Module source file name
(5,5) 2
(5,6) ASTACKINFO(myarray)                  && in the source
```
