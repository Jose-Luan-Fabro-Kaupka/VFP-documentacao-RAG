# Aplicativo Coverage Profiler

Um aplicativo de cobertura grava informações sobre as linhas de código em um arquivo que são executadas. Um aplicativo de profiling fornece informações sobre as linhas que foram realmente executadas, quantas vezes uma linha é executada, duração e mais. Cobertura e profiling permitem que um desenvolvedor identifique áreas problemáticas em um aplicativo, especialmente código ignorado e gargalos de desempenho.

O Visual FoxPro Coverage Profiler é fornecido em duas partes, um objeto Coverage engine que você pode usar ou personalizar e um aplicativo de várias janelas que você pode usar para analisar programas e projetos. Os arquivos de origem do Coverage Profiler não são instalados por padrão. Para usar esses arquivos, expanda o arquivo XSource.zip na pasta \Tools\XSource do diretório principal do Visual FoxPro.

O aplicativo Coverage Profiler (Coverage.app) fornece várias formas de visualizar os dados fornecidos pelo Coverage engine. Coverage.app é uma subclasse da classe Coverage engine. Você pode automatizar a cobertura ou modificar a interface do usuário para atender às suas necessidades, executar Coverage.app em modo não assistido e não exibir a janela do aplicativo, ou usar recursos do engine sem usar a interface.

Na inicialização, Coverage.app suspende o registro de cobertura habilitado com o comando SET COVERAGE. Quando você libera o objeto de cobertura, o aplicativo oferece uma opção para restaurar a configuração SET COVERAGE.

# Nesta seção
 **Arquivo de log do Coverage Profiler**
Descreve como o Visual FoxPro Coverage Profiler usa um arquivo de log, que consiste em registros em linhas delimitadas por vírgulas.
**Como: examinar cobertura e perfil de aplicativo**
Fornece informações sobre como o Coverage Profiler pode fornecer informações precisas e úteis sobre seu projeto ou aplicativo.
**Modificação do Coverage Profiler**
Descreve como alterar a configuração padrão do aplicativo Coverage Profiler para que ele possa ser executado dentro da janela principal do Visual FoxPro, em vez de em uma janela separada.
**Add-Ins do Coverage Profiler**
Descreve como escrever add-ins e aprimorar o aplicativo Coverage Profiler.
**Como: registrar cobertura de código**
Explica como a cobertura de código fornece informações sobre quais linhas de código foram executadas e quanto tempo levou para executá-las. Você pode usar essas informações para refinar seu código para desempenho e garantir que testou adequadamente o código.
**Conservando espaço em disco durante execuções de cobertura**
Discute como você pode alterar o tamanho de alguns campos das tabelas de trabalho do engine para tornar essas tabelas um pouco menores e evitar erros de "sem espaço em disco" durante execuções de cobertura.
**Objeto Coverage Engine**
Descreve a classe Coverage engine e suas propriedades, métodos e eventos.

# Seções relacionadas
 **Ferramentas de produtividade de desenvolvimento**
Fornece informações sobre ferramentas de desenvolvedor fornecidas para desenvolvimento de aplicativos dentro do aplicativo Visual FoxPro e da linguagem.
**Visão geral do IntelliSense**
Fornece informações sobre o IntelliSense, que exibe informações em janelas pop-up e listas suspensas que auxiliam na sintaxe de conclusão de instruções e funções.
**Hooks do Project Manager**
Descreve como você pode acessar um projeto programaticamente, permitindo manipular um projeto como um objeto.
**Automatizando tarefas de teclas com macros**
Descreve como você pode gravar e salvar pressionamentos de teclas em macros usando a caixa de diálogo Macros.
