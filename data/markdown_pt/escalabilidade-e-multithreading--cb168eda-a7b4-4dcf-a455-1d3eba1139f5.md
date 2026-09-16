# Escalabilidade e multithreading

Quando um componente tem uma thread de execução, o código de apenas um objeto pode ser executado em um determinado momento. O recurso Automation do Component Object Model (COM) trata essa situação serializando solicitações. Ou seja, as solicitações são enfileiradas e processadas uma de cada vez até que todas sejam concluídas.

Em um ambiente operacional multithread, a serialização protege objetos de thread única de solicitações de clientes sobrepostas — ou seja, de código em uma propriedade ou método sendo executado enquanto uma ou mais solicitações de clientes anteriores ainda estão em execução. Solicitações sobrepostas podem causar erros de dados internos se os objetos não são projetados para reentrância.

A serialização é, portanto, um recurso extremamente importante da Automation. No entanto, a serialização de componentes de thread única significa que as solicitações às vezes são bloqueadas. Por exemplo, suponha que você está usando um objeto Widget que tem dois métodos, spin e flip.
 - O método Spin leva de vários segundos a meia hora para ser concluído.
- O método Flip é quase instantâneo.

Como aplicações de 32 bits são multitarefa preemptiva, uma segunda aplicação poderia chamar o método Flip enquanto o método Spin já está em execução. O método Flip curto é bloqueado até que o método Spin longo seja concluído.

Quando operações curtas são bloqueadas por operações longas, a produtividade sofre e a frustração do usuário aumenta. Componentes que se comportam dessa forma são considerados com baixa escalabilidade. Ou seja, funcionam mal se muitas solicitações de duração mista são feitas.

O Visual FoxPro fornece dois recursos de componente para abordar escalabilidade e evitar chamadas bloqueadas — instanciação SingleUse e objetos multithread. Para detalhes, consulte Controlling Call Blocking.
