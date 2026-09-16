# Compilando código-fonte

No Visual FoxPro, você pode compilar código-fonte do Visual FoxPro em arquivos de tempo de execução criados com VFP9R.dll ou VFP9T.dll. Para mais informações sobre arquivos de tempo de execução, consulte Visual FoxPro Run-Time Libraries.

> **Observação:** Versões anteriores do Visual FoxPro exigiam o uso de substituição de macro ou avaliação de expressão para cada linha para executar código gerado em tempo de execução. Esse processo nem sempre era ideal devido às complexidades de executar grandes blocos de código e à penalidade de desempenho ao usar o operador de macro & ou a função EVALUATE( ).

O comando COMPILE está disponível no runtime para que suas aplicações possam gerar e compilar um arquivo de programa (.prg). A compilação em tempo de execução funciona com todos os arquivos suportados pelo comando COMPILE, incluindo programas, formulários, classes, etiquetas, relatórios e bancos de dados. Você pode usar a função STRTOFILE( ) para gravar seu código em um arquivo .prg.

Há algumas diferenças entre o compilador no produto de desenvolvimento e no runtime:
 - A opção "?" no comando COMPILE não está disponível no runtime porque servidores de automação não assistidos (.dlls) não permitem modos que envolvem entrada do usuário.
- O comando SET DEVELOPMENT não tem efeito no runtime. No produto completo, SET DEVELOPMENT faz o Visual FoxPro comparar a data e a hora de criação de um programa com as do arquivo de objeto compilado quando o programa é executado. Se SET DEVELOPMENT estiver definido como ON, a versão mais recente é sempre executada — programas desatualizados são recompilados automaticamente. No runtime, você deve chamar explicitamente o comando COMPILE para recompilar o código-fonte. Isso significa que chamar o comando DO no seu runtime nunca fará o arquivo .prg ser recompilado. Além disso, no runtime, o comando DO ignora a extensão do arquivo e procura um arquivo com extensão .fxp, mesmo se você especificar um arquivo .prg.
