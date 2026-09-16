# Controle do bloqueio de chamadas

Para melhorar a escalabilidade dos aplicativos, o Visual FoxPro fornece objetos SingleUse e threading de modelo Apartment como formas de controlar problemas de bloqueio de chamadas.

# Objetos SingleUse

Você pode fazer com que cada instância de uma classe OLEPUBLIC seja executada em uma instância separada do componente definindo a propriedade Instancing da classe OLEPUBLIC como SingleUse na caixa de diálogo Informações do Projeto. Isso significa que, embora o componente tenha um único thread, cada instância da classe SingleUse tem seu próprio thread de execução. O comportamento de objetos SingleUse difere entre servidores .exe e .dll.

### Objetos SingleUse em servidores EXE

Com a propriedade Instancing definida como SingleUse, cada instância inicia um novo processo EXE. No Windows 2000 ou posterior, cada processo em execução aparece no Gerenciador de Tarefas. Com a configuração MultiUse, a primeira instância inicia um novo processo, mas cada nova instância de objeto compartilha o mesmo processo da primeira.

### Objetos SingleUse em servidores DLL

A propriedade Instancing é ignorada para .dlls multithread e é lida somente para a biblioteca de tempo de execução VFP9R.dll. Servidores criados para uso com a biblioteca de tempo de execução VFPVersionNumberT.dll, em que VersionNumber representa o número da versão desta edição, são sempre MultiUse, independentemente da configuração. Em geral, você deve sempre definir Instancing como MultiUse para servidores em processo VFPVersionNumberR.dll. Se defini-la como SingleUse, somente uma instância de um objeto desse servidor poderá ser criada. Ocorrerá um erro se você tentar instanciar mais objetos.

Somente em raras circunstâncias seria desejável usar SingleUse. De fato, componentes do Microsoft Transaction Server exigem MultiUse. Objetos SingleUse geralmente exigem mais memória do que vários objetos em um componente multithread. Contudo, há motivos para usar objetos SingleUse. Por exemplo, você pode isolar atividades de alto risco em processos separados. Se o objeto sofrer um erro fatal, os demais processos não serão afetados. Por outro lado, um erro fatal em um componente multithread encerra todos os threads.

# Threading de modelo Apartment

Os servidores de Automação do Visual FoxPro oferecem suporte ao threading de modelo Apartment. O Microsoft Transaction Server utiliza servidores marcados como apartment-threaded e oferece melhor proteção de threads e escalabilidade por meio de serialização e marshaling.

No Visual FoxPro, o threading de modelo Apartment fornece segurança de thread. Cada thread funciona como um apartamento: todos os objetos criados no thread residem nesse apartamento e desconhecem objetos de outros apartamentos. Cada objeto de modelo Apartment (como um servidor de Automação do Visual FoxPro) só pode ser acessado por um thread, aquele que criou o objeto. Contudo, um servidor de objetos (como o Microsoft Transaction Server) pode oferecer suporte a vários objetos, cada um acessado simultaneamente por threads diferentes. Os dados comuns mantidos pelo servidor de objetos devem ser protegidos contra colisões de threads.

O threading de modelo Apartment oferece os seguintes benefícios:
 - Todos os objetos criados por um cliente em determinado thread são criados no mesmo apartamento (thread) da DLL. Chamadas feitas no mesmo thread a esses objetos não exigem marshaling entre threads, sendo mais eficientes.
- Como um objeto só é acessado no thread em que foi criado, as chamadas são serializadas para que uma chamada nunca seja interrompida por outra de outro thread.
- Os argumentos de chamadas entre threads passam por marshaling, e o thread chamador é bloqueado. Essa sincronização de dados protege o estado do thread chamador.

DLLs apartment-threaded não podem criar seus próprios threads; na primeira vez que um thread cliente solicita um objeto fornecido pela DLL, um novo apartamento é criado e o evento Init do objeto é executado nesse apartamento. Todos os objetos cliente de thread único solicitados por esse cliente residirão no mesmo apartamento e compartilharão dados globais. Todos os objetos PRIVATE (incluindo formulários) criados pelos objetos públicos também residirão no apartamento.

Embora o Visual FoxPro não forneça uma forma de os apartamentos acessarem uns aos outros, um cliente multithread pode obter uma referência a um objeto no Thread A e passá-la a um objeto no Thread B.

Para obter mais informações sobre threading de modelo Apartment, procure por "Apartment-Model Threading" na biblioteca MSDN.

A implementação do threading de modelo Apartment do Visual FoxPro elimina conflitos no acesso a dados globais por vários threads, fornecendo a cada apartamento sua própria cópia dos dados globais. Isso significa que todos os objetos criados no thread existem nesse apartamento e desconhecem objetos de outros apartamentos.

O Visual FoxPro usa armazenamento local de thread para guardar um conjunto exclusivo de dados globais do aplicativo e do ambiente para cada thread (apartamento). Assim, duas instâncias da mesma classe criadas em threads diferentes não podem acessar os dados uma da outra. Contudo, se essas duas instâncias residirem no mesmo thread, cada objeto poderá acessar os dados do outro. Isso pode causar problemas de temporização nos aplicativos. De fato, desde que dois objetos no mesmo thread sejam criados a partir de classes OLEPUBLIC no mesmo servidor .dll, os dados desses objetos são comuns entre eles (Observação: você pode usar a classe Session para fornecer a cada objeto uma datasession privada exclusiva.)

Além do armazenamento local de thread, o Visual FoxPro também fornece a cada projeto (arquivo .dll) um conjunto exclusivo de dados globais. Objetos criados em projetos diferentes (servidores .dll) não podem acessar os dados globais uns dos outros, mesmo que residam no mesmo thread.
