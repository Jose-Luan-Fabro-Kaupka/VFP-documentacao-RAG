# Caixa de diálogo Opções do Coverage Profiler

Permite especificar a sensibilidade de caminho, o formato da caixa de diálogo e o ambiente, e as marcas usadas para marcar linhas de código que são executadas em seu programa ou aplicação, e as fontes para exibição e código.
 **Use Smart Pathing**
Define o Coverage Profiler para fazer certas suposições sobre a localização de arquivos em seu projeto ou aplicação conforme a forma como os arquivos estão listados no log de cobertura. Por padrão, o Coverage Profiler solicita que você localize os arquivos de origem referenciados no log de cobertura. Se você marcar esta opção, o Coverage Profiler assume que as pastas nas quais você já localizou arquivos contêm arquivos de origem adicionais que você precisa. Desmarque esta opção para obter controle mais completo ou se você tiver arquivos de origem com o mesmo nome em pastas diferentes.
**Register Add-Ins when run**
Define o Coverage Profiler para manter para uso futuro as informações de caminho e nome dos Add-Ins conforme você os executa, para que você possa localizá-los na lista suspensa da Caixa de diálogo Add-Ins do Coverage Profiler.
**Mark all code while log loads**
Marca linhas de código conforme o Coverage Profiler processa o log de cobertura (.log). Esta configuração pode reduzir o desempenho de carregamento, especialmente em arquivos maiores.

# Marcas de cobertura
 **Executed**
Permite digitar um caractere ou vários caracteres, como asteriscos, para marcar cada linha de código executada.
**Not Executed**
Permite digitar um caractere ou vários caracteres para marcar cada linha de código que não é executada. Uma barra vertical é o caractere padrão. Observação Algumas linhas no código, como comentários, instruções DEFINE CLASS e ELSE, e linhas dentro de TEXT... ENDTEXT não aparecem nos logs de cobertura porque não são executáveis. Além disso, linhas quebradas por símbolos de continuação (ponto e vírgula) são consideradas como uma única linha de código e são marcadas apenas na última linha.

# Modo de inicialização
 **Coverage**
Especifica que o aplicativo Coverage Profiler abre como um analisador de cobertura, marcando o código que realmente é executado em projetos ou aplicações selecionados.
**Profile**
Especifica que o aplicativo Coverage Profiler abre como um profiler, determinando a quantidade de tempo necessária para executar linhas de código no projeto ou aplicação selecionado.

# Ambiente
 **Coverage frame**
Especifica que o aplicativo Coverage Profiler abre na área de trabalho do Windows.
**FoxPro frame**
Especifica que o aplicativo Coverage Profiler abre dentro da janela principal do Visual FoxPro.

# Fontes
 **Display Font**
Permite especificar a fonte usada no painel Source List da janela Coverage Profiler.
**Code Font**
Permite especificar a fonte usada no painel Source Code da janela Coverage Profiler.
**Set as default**
Salva as opções selecionadas no registro do Windows. As configurações de Startmode e Environment entram em vigor quando você reinicia o Coverage Profiler.
