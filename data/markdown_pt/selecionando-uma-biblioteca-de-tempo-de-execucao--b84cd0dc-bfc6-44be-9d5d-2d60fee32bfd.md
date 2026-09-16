# Selecionando uma biblioteca de tempo de execução

Você pode ter uma necessidade de aplicação, como uma Internet Server Application nos FoxISAPI Automation Server Samples, em que deseja instanciar um formulário para usar no mapeamento para HTML equivalente. O impacto de eliminar vários recursos não críticos usando a biblioteca de tempo de execução multithreaded do Visual FoxPro melhorará o desempenho geral de suas aplicações de servidor multithreaded.

Um equívoco comum sobre a escolha do servidor é que uma aplicação escalará automaticamente bem apenas construindo o .dll para usar o novo tempo de execução. Muitas vezes você pode fazer isso, mas também deve considerar questões envolvendo o uso de chamadas de API do Visual FoxPro, escalabilidade, reentrância e contenção de recursos.

# Usando chamadas de API do Visual FoxPro

Ao usar bibliotecas FLL do Visual FoxPro ou bibliotecas DLL padrão do Windows que fazem chamadas de API do Visual FoxPro, há algumas questões das quais você precisa estar ciente ao projetar seus servidores. A API do Visual FoxPro não determina facilmente a qual projeto (.dll) uma chamada específica pertence. Portanto, há um potencial, embora raro, de uma chamada de API ser feita contra o projeto errado (.dll - thread local storage). Isso pode ocorrer se sua biblioteca FLL/DLL criar uma instância de um servidor .dll do Visual FoxPro diferente antes de fazer sua chamada de API. Há várias soluções possíveis se seu servidor experimentar este problema:
 - Crie uma cópia separada do arquivo da biblioteca de tempo de execução multithreaded do Visual FoxPro e coloque a cópia na mesma pasta do seu servidor .dll. O servidor sempre pesquisará primeiro na pasta do servidor antes de tentar localizar arquivos na pasta System do Windows ou na pasta do processo do cliente. Ao ter sua própria biblioteca de tempo de execução atendendo-o, um servidor não experimentará conflitos potenciais de outros .dlls (assumindo que esses outros .dlls não estejam na mesma pasta). Como este comportamento (cópia/renomeação automática do tempo de execução) ocorre por padrão com o tempo de execução principal do Visual FoxPro, as questões de API acima se manifestam apenas na biblioteca de tempo de execução multithreaded do Visual FoxPro.
- Limite sua aplicação a um único servidor .dll. Se você está usando vários servidores .dll (projetos), pode haver potencial para conflitos de API. Lembre-se de que um projeto pode conter muitos OLEPUBLICs, então você não precisa ter um projeto separado para cada OLEPUBLIC. Esteja ciente de que em servidores de computador compartilhados, é possível que pessoas instalem outros servidores COM do Visual FoxPro, que podem potencialmente entrar em conflito com o seu se executados simultaneamente.

# Questões de escalabilidade

O tempo de execução multithreaded no Visual FoxPro permite servidores in-process do Visual FoxPro muito escaláveis. Embora a escalabilidade de seus servidores seja tratada automaticamente pelo tempo de execução, certos loops de código apertados podem não permitir que a troca de threads ocorra com frequência. Por exemplo, um loop DO WHILE muito apertado pode causar isso. Se você experimentar problemas de escalabilidade, pode incluir código como o exemplo a seguir, que força o processador a trocar de thread:

```foxpro
DECLARE Sleep IN Win32API INTEGER
SLEEP(0)
```

Embora você possa usar multithreading em uma máquina com um único processador, considere que isso pode não fornecer exatamente os resultados que você espera. Por exemplo, em uma máquina com um único processador, o multithreading resulta em uma melhoria de desempenho percebida apenas com uma mistura de tarefas longas e curtas. Chamadas de método multithreaded, conforme descrito neste exemplo, podem parecer mais lentas.

No exemplo, os métodos A e B são chamados ao mesmo tempo. Em um componente single-threaded, as solicitações são serializadas, de modo que B não começa até que A tenha terminado. Com multithreading, as duas threads ativas disputam a atenção do processador.

Não apenas o tempo médio de conclusão percebido aumenta, mas mais tempo de processador é gasto alternando entre threads.

O problema é que os métodos A e B levam aproximadamente a mesma quantidade de tempo.

Por exemplo, se o método B exigisse apenas três fatias de tempo para ser concluído, o usuário do sistema perceberia uma grande melhoria na capacidade de resposta do método B — e apenas uma leve degradação no tempo necessário para executar o método A.

Os cenários em que o multithreading mostra sua melhor vantagem são aqueles em que a maioria das threads passa uma porcentagem substancial do tempo bloqueada — por exemplo, aguardando E/S de arquivo — de modo que outras threads possam estar executando código em qualquer momento.

Se você está considerando uma aplicação em uma máquina com um único processador com características que fornecem bloqueio mínimo de threads, pode querer considerar usar a biblioteca de tempo de execução principal do Visual FoxPro. Em máquinas multiprocessador e na maioria das outras aplicações, você deve considerar usar a biblioteca de tempo de execução multithreaded do Visual FoxPro para servidores .dll.

# Reentrância

No modelo apartment, reentrância refere-se à seguinte sequência de eventos:
 - A thread de execução de um apartment entra no código de um objeto porque uma propriedade ou método foi invocado.
- Enquanto a thread está na propriedade ou método, outra thread invoca uma propriedade ou método do objeto, e a Automation serializa esta solicitação — ou seja, enfileira a solicitação até que a thread que possui o apartment do objeto termine o membro que está executando atualmente.
- Antes que a thread chegue ao final do membro, ela executa código que cede o controle do processador.
- A Automation diz à thread para começar a executar a solicitação serializada, de modo que a thread reentra no código do objeto.

A nova solicitação pode ser para o membro que a thread já estava executando — caso em que a thread entra no membro uma segunda vez — ou pode ser para outro membro. Se o segundo membro não ceder, ele terminará o processamento antes do primeiro membro. Se ele alterar dados em nível de módulo que o primeiro membro estava usando, o resultado pode ser infeliz.

Ao serializar chamadas de propriedade e método para cada apartment, a Automation protege você da reentrância — a menos que seu código ceda o controle do processador. Formas pelas quais seu código pode ceder o controle do processador incluem:
 - Chamar DoEvents.
- Invocar as propriedades ou métodos de um objeto em outra thread ou em outro processo. Definir a propriedade Application.AutoYield como false (.F.) suspenderá o processamento de eventos intermitentes entre linhas de código em execução.
- Invocar um método cross-thread ou cross-process de dentro de um método.

A menos que você tenha escrito cuidadosamente todo o código de um objeto para que não importe se dois membros estão executando ao mesmo tempo, você não deve incluir código que ceda o controle do processador.

# Contenção de recursos

A biblioteca de tempo de execução multithreaded do Visual FoxPro protegerá os objetos de acessar os dados de aplicação uns dos outros. Isso inclui globais de ambiente declarados e intrínsecos. Alguns recursos apresentam problemas potenciais de contenção, incluindo:
 - Arquivos
- Registro
- Dados

A E/S de arquivo apresenta contenções de recursos que podem ser facilmente tratadas por código, já que o gerenciamento de arquivos é feito pelo sistema operacional. Ao usar um arquivo, seu servidor pode abrir (e bloquear) um arquivo para que outros objetos vejam que o arquivo está em uso. Um servidor adequadamente escrito pode lidar com este cenário aguardando que o arquivo esteja disponível ou tratando o erro de outra forma. Arquivos também podem ser abertos compartilhados, caso em que seu servidor deve estar ciente de que outros objetos podem potencialmente alterar valores.

Um cenário comum é apresentado com arquivos INI nos quais diferentes objetos podem ler ou gravar valores. O processo de ler e depois gravar um valor em um arquivo INI requer duas etapas. Portanto, há um potencial de que o valor lido por um cliente não seja necessariamente o mesmo que ele substitui depois se outro cliente alterá-lo primeiro, produzindo necessidade de resolução de conflitos.

Assim como os arquivos INI, o Registro armazena configurações que podem ser acessadas por vários clientes. Suas aplicações devem usar rotinas comuns da API do Windows para acessar o Registro. Novamente, o design do seu servidor deve refletir que existe um potencial de valores de chave do Registro mudarem entre o momento em que a chave é lida e o momento em que é gravada. As rotinas da API do Windows trabalham para evitar a necessidade de resolução de conflitos.

Dados é um recurso complicado de tratar. Felizmente, a rica linguagem Visual FoxPro disponível nos tempos de execução fornece todas as informações e funcionalidades necessárias para lidar com questões de contenção de recursos. Para obter mais informações sobre como lidar com dados compartilhados, consulte Programming for Shared Access.
