# Modificação do Coverage Profiler

Por padrão, o aplicativo Coverage Profiler é executado em uma janela separada. Você pode reconfigurá-lo para ser executado dentro da janela principal do Visual FoxPro alterando a Opção de Ambiente. Na Caixa de Diálogo Opções do Coverage Profiler, altere a seleção Ambiente de Coverage frame para FoxPro frame e reinicie o Coverage Profiler.

Você também pode usar a caixa de diálogo Opções do Coverage Profiler para modificar as seguintes características do Coverage Profiler.

| Característica | Descrição |
| --- | --- |
| Add-Ins | Especifica se Add-Ins são registrados no Coverage Profiler conforme são usados. Para obter mais informações, consulte a seção "." |
| Marcas de Cobertura | Especifica se o Coverage Profiler marca o código que é executado ou o código que não é executado. Especifica o(s) caractere(s) usado(s) para marcar o código. Especifica quando o código é marcado. |
| Fontes | Especifica as fontes usadas no Coverage Profiler como código e em exibições. |
| Caminho Inteligente | Especifica se o Coverage Profiler busca automaticamente arquivos em locais especificados anteriormente. |
| Modo de Inicialização | Especifica se o Coverage Profiler abre no Modo de Cobertura ou de Perfil. |

# Garantindo relevância no Coverage Profiler

Para ajudar a garantir que os arquivos processados pelo Coverage Profiler sejam os arquivos corretos:
 - Defina o diretório do seu projeto como padrão antes de iniciar o registro de cobertura para que os arquivos referenciados sejam relativos.
- Evite renomear objetos dinamicamente. O Coverage Profiler não encontrará objetos se você os renomear em tempo de execução.
- Evite usar arquivos de origem com exatamente o mesmo nome raiz, mesmo com extensões diferentes. Internamente, o Coverage Profiler não pode distinguir entre eles.
- Certifique-se de que seu projeto contenha apenas as versões corretas de arquivos muito modificados.
- Certifique-se de que seu projeto não contenha várias cópias de um arquivo em subdiretórios.
- Execute uma compilação para a execução de cobertura: Certifique-se de que as informações de depuração estão em seu aplicativo. Desative Encrypt. Use RECOMPILE ou Compilar Tudo para forçar uma compilação nova de todo o código-fonte. Execute a compilação imediatamente antes da execução de cobertura para que você saiba que o código-fonte corresponde exatamente ao código objeto.

Algumas linhas no código, como comentários, instruções DEFINE CLASS e ELSE, e linhas dentro de TEXT ... ENDTEXT não aparecem nos logs de cobertura porque nem sequer são potencialmente executáveis. Além disso, linhas quebradas por símbolos de continuação (ponto e vírgula) são consideradas como uma única linha de código e marcadas apenas na última linha.
