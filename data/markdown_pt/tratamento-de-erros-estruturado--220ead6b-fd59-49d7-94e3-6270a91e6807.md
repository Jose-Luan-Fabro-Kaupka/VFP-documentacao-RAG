# Tratamento de erros estruturado

Você pode usar o comando TRY...CATCH...FINALLY como estrutura de controle a para lidar com erros ou exceções que podem ocorrer em seu código em tempo de execução. A estrutura TRY...CATCH...FINALLY contém blocos de código TRY, CATCH e FINALLY para que você possa especificar instruções que podem gerar erros, instruções para lidar com esses erros e instruções para executar operações de limpeza.

A estrutura TRY...CATCH...FINALLY começa com a instrução TRY, que marca o início do bloco TRY. No bloco TRY, você pode especificar código que pode produzir erros em tempo de execução. Se o seu programa completar o bloco TRY sem gerar um erro ou exceção, ele ignora o bloco CATCH e procura o bloco FINALLY próximo ao final da estrutura, se existir, e executa as instruções correspondentes. Se o bloco FINALLY não existir, a execução do programa continua fora da estrutura na primeira instrução após a instrução ENDTRY, que marca o final da estrutura TRY...CATCH...FINALLY.

> **Observação:** O Visual FoxPro permite a existência de estruturas TRY...CATCH...FINALLY que não possuem blocos CATCH e FINALLY, que escalam o erro para um manipulador de erros de nível superior.

Você também pode aninhar estruturas TRY...CATCH...FINALLY em um bloco TRY, CATCH ou FINALLY.

As seções a seguir descrevem as tarefas de tratamento de erros que você pode executar nesses blocos de código:
 - Gerando Exceções
- Capturando exceções
- Exceções crescentes
- Saindo TRY...CATCH...FINALLY Imediatamente
- Usando comandos em TRY...CATCH...FINALLY
- Executando instruções FINALLY

Para obter mais informações, consulte TRY...CATCH...FINALLY Comando.

# Gerando Exceções

O Visual FoxPro gera ou "lança" uma exceção e cria um objeto Exception, que contém detalhes sobre o erro, quando ocorre um erro em um bloco TRY nos seguintes locais:
 - A linha de código. Isso inclui chamadas para procedimentos externos que contêm erros, mas não contêm seus próprios manipuladores de erros.
- Chamada de método A para objeto an quando o código do método the contém erros e o objeto the não contém código de evento Error. Caso contrário, se o código de evento Error existir, o evento Error para o objeto that tratará o erro, a menos que o método the contenha seu próprio manipulador de erros TRY...CATCH...FINALLY.

> **Observação:** Você não pode executar código quando o objeto Exception é criado. O objeto Exception criado sempre existe como uma instância da classe Exception base. Se você quiser usar uma subclasse da classe Exception, você deve relançar a exceção no bloco CATCH ou FINALLY. Somente arquivos de programa do Visual FoxPro (.prg) suportam objetos Exception, embora você possa lançar exceções de formulários executados no ambiente de design. Você não pode lançar objetos Exception de objetos COM em arquivos de biblioteca de vínculo dinâmico (.dll) ou arquivos executáveis ​​(.exe). Para obter mais informações, consulte Exception Classe .

Depois que o erro ocorre, o Visual FoxPro trata ou "captura" a exceção passando para a primeira instrução CATCH e procura as instruções apropriadas no bloco CATCH para tratar a exceção.

# Capturando ExceçõesO programa analisa as instruções CATCH na ordem em que aparecem no bloco CATCH para determinar se existem instruções para lidar com a exceção. Se o programa encontrar uma instrução CATCH que trata a exceção, o programa executa o código correspondente.

A instrução CATCH pode conter cláusulas opcionais TO e WHEN. Você pode armazenar uma referência ao objeto Exception criado especificando uma variável de memória usando o parâmetro VarName na cláusula TO. Se desejar estabelecer uma condição para a execução de um bloco CATCH, você pode especificar uma expressão lógica na cláusula WHEN que deve ser avaliada como True (.T.) antes das instruções na execução do bloco CATCH. As instruções CATCH funcionam de forma semelhante às instruções CASE, pois a cláusula WHEN deve ser avaliada como uma expressão lógica. Se as cláusulas TO e WHEN não existirem, a instrução CATCH será avaliada como CATCH WHEN .T. (Verdadeiro).

Depois que o programa executa instruções em um bloco CATCH, ele não retorna para a instrução TRY e não procura outras instruções CATCH. Em vez disso, o programa prossegue diretamente para a instrução FINALLY, se existir, para executar quaisquer instruções restantes. Caso contrário, o programa sai da estrutura TRY...CATCH...FINALLY e passa para a instrução que segue imediatamente ENDTRY.

# Escalando Exceções

Se quiser escalar ou "relançar" a exceção para um manipulador de erros de nível superior, você pode incluir uma instrução THROW. Você pode chamar THROW de qualquer bloco de código de uma estrutura TRY...CATCH...FINALLY. No entanto, você pode usar THROW em qualquer lugar do código onde exista um manipulador de erros para capturar a exceção. Você não pode chamar THROW da janela de comando the.

> **Cuidado:** Chamar o comando THROW fora da estrutura TRY...CATCH...FINALLY e sem um manipulador de erros apropriado faz com que seu programa seja encerrado.

Se você usar THROW fora da seção TRY...CATCH onde a exceção lançada é tratada por uma rotina ON ERROR ou pelo sistema Visual FoxPro em vez de um evento Error, a execução do programa não retornará ao local onde o A instrução THROW ocorre. O exemplo a seguir mostra como a linha de código `?2` não é executada. Este comportamento difere de um comportamento de erro tradicional em que a execução do programa retorna ao local onde ocorreu o erro:

```foxpro
ON ERROR ? ERROR()
DO myProc1
PROCEDURE myProc1
   ?1
   THROW 11
   ?2
ENDPROC
```

Lembre-se, a intenção de chamar THROW é escalar a exceção para um manipulador de erros de nível superior.

Se um bloco TRY...CATCH externo existir em torno de uma instrução THROW quando ela for chamada de dentro de um bloco CATCH ou FINALLY, o Visual FoxPro reatribuirá a variável de memória especificada na cláusula TO de the referência de objeto do objeto exception anterior para referência de objeto an para o objeto exception mais recente criado pela exceção lançada. Se não existir nenhuma estrutura externa TRY...CATCH, o Visual FoxPro lançará a exceção para uma rotina ON ERROR ou um evento error, se existirem. Caso contrário, o Visual FoxPro exibirá a mensagem de erro de sistema apropriada.

# Saindo de TRY...CATCH...FINALLY ImediatamenteVocê pode sair de um bloco de código imediatamente incluindo uma instrução EXIT em um bloco TRY ou CATCH. O programa retoma a execução do código na instrução FINALLY, se existir, ou na linha imediatamente após a instrução ENDTRY.

# Usando comandos em TRY...CATCH...FINALLY

Você pode usar diferentes comandos do Visual FoxPro que afetam o modo como o código normalmente é executado em um bloco TRY ou CATCH. Entretanto, se você usar um desses comandos que não são permitidos para um bloco específico, o Visual FoxPro gerará um erro em tempo de execução. As instruções FINALLY sempre são executadas antes de manipular esses comandos, exceto quando CANCEL ou QUIT é usado. A tabela a seguir lista os comandos do Visual FoxPro que você pode ou não usar em um bloco TRY, CATCH ou FINALLY.

| Comando | TRY | CATCH | FINALLY |
| --- | --- | --- | --- |
| CANCEL | Sim | Sim | Sim |
| CLEAR ALL | Sim | Não | Não |
| CLOSE ALL | Sim | Sim | Sim |
| DOEVENTS | Sim | Sim | Sim |
| ERROR | Sim | Sim | Sim |
| EXIT | Sim | Sim | Sim |
| LOOP | Não | Não | Não |
| QUIT | Sim | Sim | Sim |
| RELEASE | Sim | Sim | Sim |
| RESUME | Sim | Sim | Sim |
| RETRY | Não | Não | Não |
| RETURN | Não | Não | Não |
| RETURN TO MASTER | Não | Não | Não |
| RETURN TO <NomeProcedimento> | Não | Não | Não |
| SET STEP ON | Sim | Sim | Sim |
| SUSPEND | Sim | Sim | Sim |
| THROW | Sim | Sim | Sim |

> **Nota:** Você pode incluir comandos como LOOP em um bloco, desde que você o coloque dentro de uma instrução de controle embedded, como FOR EACH...ENDOR ou DO WHILE...ENDDO . Você pode chamar o comando ERROR dos blocos TRY , CATCH ou FINALLY. TRY...CATCH...FINALLY lida com o comando ERROR como qualquer outra exceção ou uso do comando THROW.

# Executando instruções FINALLY

Se o programa localizar a instrução FINALLY, ele executará o código que está no bloco FINALLY. O bloco FINALLY geralmente limpa quaisquer recursos alocados pelo bloco TRY e é sempre o último código a ser executado. O controle before sai da estrutura TRY...CATCH...FINALLY.

O bloco FINALLY sempre é executado quando ocorre uma exceção, não tratada ou não, mesmo se outro manipulador de exceção, como a rotina ON ERROR ou o evento Error do objeto an, estiver em vigor.

> **Nota:** Você não pode transfer controlar explicitamente seu programa diretamente em um bloco CATCH ou FINALLY. Você não pode ignorar a instrução FINALLY se ela existir, a menos que você use o comando CANCEL para interromper a continuação do programa. Se desejar ignorar a instrução FINALLY, você precisará fornecer o código no início do bloco FINALLY que verifica uma condição e sai do bloco se essa condição for atendida.

Após a execução do bloco FINALLY, o programa prossegue para a instrução imediatamente após a instrução ENDTRY. A instrução ENDTRY encerra a estrutura TRY...CATCH...FINALLY.
