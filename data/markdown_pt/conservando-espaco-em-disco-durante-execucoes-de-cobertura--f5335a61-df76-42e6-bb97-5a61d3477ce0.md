# Conservando espaço em disco durante execuções de cobertura

Se você encontrar erros de "sem espaço em disco" durante execuções de cobertura, pode alterar o tamanho de alguns dos campos da tabela de trabalho do mecanismo para tornar essas tabelas um pouco menores.

Os valores padrão desses campos são 115, porque permite nomes de caminho longos e nomes longos de objetos e métodos. Valores maiores que 115 não são recomendados, porque dois desses campos podem ser usados em chaves concatenadas em que a soma de quaisquer dois comprimentos de campo não deve exceder o comprimento máximo da chave (240).

Não diminua o campo Hostfile a menos que tenha certeza de que os comprimentos de seus arquivos de origem totalmente qualificados não serão excedidos. Caso contrário, o mecanismo pode gerar erros ao tentar encontrar as versões não compiladas desses arquivos.

Se você sabe que aninha pageframes e grades em várias camadas de contêiner ou que tende a usar nomes de classe muito longos, especifique valores maiores que o comprimento máximo de cadeia de caracteres que os campos ObjClass ou Executing provavelmente conterão, mais uma margem de erro. Você pode querer examinar os arquivos de origem e destino primeiro para ver como o mecanismo usa esses campos.

Quando você diminuiu o tamanho dos campos ObjClass ou Executing, cuidado com estatísticas de cobertura e profiling repentinamente incorretas. Embora o Profiler não gere erros óbvios ao analisar o log, erros estatísticos ocorrerão se nomes de objetos e métodos estiverem sendo truncados nos campos.

Normalmente, você usa os valores das propriedades iLenHostfile, iLenObjClass e iLenExecuting para alterar o tamanho desses campos. Você pode até alterá-los dinamicamente enquanto o Coverage está aberto, antes de abrir um log de cobertura que é excepcionalmente grande.

> **Observação:** Quando você abriu um log, não altere esses valores até estar pronto para avaliar um novo log, ou você pode encontrar erros estatísticos quando o código de novas entradas de destino for marcado.

No entanto, se você definiu COV_TOPSPEED true (.T.) no arquivo de cabeçalho COV_TUNE.H, para aumentar a velocidade forçando o mecanismo a fazer chamadas em linha, o mecanismo usa constantes também definidas em COV_TUNE.H, em vez de valores de propriedade, para determinar o tamanho desses campos. (Esses valores são usados repetidamente, para garantir comparações exatas, enquanto o mecanismo analisa linhas de código.) Se você definir COV_TOPSPEED true (.T.), deve definir os valores em COV_TUNE.H diretamente.
