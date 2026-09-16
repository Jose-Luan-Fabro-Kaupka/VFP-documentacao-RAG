# Desenvolvimento de bibliotecas de classes em equipes

Como bibliotecas de classes (.vcx files) são uma parte crucial da maioria dos aplicativos Visual FoxPro, equipes devem ser capazes de coordenar esforços de desenvolvimento ao criá-las. Trabalhar com bibliotecas de classes em uma equipe envolve muitas das mesmas questões de coordenação que qualquer conjunto de componentes de aplicativo, mas adiciona algumas questões exclusivas de classes:
 - Alterações em classes são propagadas não apenas para aplicativos que usam essas classes, mas para todas as subclasses derivadas delas.
- Várias classes são frequentemente armazenadas em um único arquivo de biblioteca, a unidade mínima que pode ser gerenciada por um sistema de controle de origem.

Como em formulários e programas complexos, é uma boa prática isolar o desenvolvimento em uma biblioteca de classes, para que um desenvolvedor possa fazer alterações na biblioteca sem afetar o trabalho de outros desenvolvedores. Idealmente, a equipe de desenvolvedores pode trabalhar com uma biblioteca de classes enquanto ela está sendo aprimorada por outro desenvolvedor, sem precisar se preocupar se alterações nas bibliotecas causarão problemas no aplicativo.

Quando uma classe é usada, o Visual FoxPro a armazena em cache no computador do usuário, mesmo depois que um formulário que usa a classe foi liberado. Você deve liberar explicitamente a classe antes que o Visual FoxPro a reconheça como não mais em uso. Se você usou uma classe durante a sessão atual (e ela está, portanto, em cache), mas deseja carregar uma nova versão da classe, certifique-se de liberar a classe para forçar o Visual FoxPro a recarregá-la da biblioteca alterada.

# Colocando bibliotecas de classes sob controle de origem

Quando você coloca uma biblioteca de classes sob controle de origem, apenas um desenvolvedor pode fazer check-out da biblioteca por vez. A biblioteca torna-se somente leitura para outros desenvolvedores. Como regra, isso não interfere no desenvolvimento do aplicativo, porque desenvolvedores podem usar e criar subclasses de uma biblioteca mesmo se ela for somente leitura. Enquanto os desenvolvedores do aplicativo trabalham com a versão somente leitura da biblioteca, o desenvolvedor da biblioteca de classes pode modificar todas as classes na biblioteca.

Se você usar esta abordagem, o desenvolvedor que está atualizando a biblioteca não deve fazer check-in do arquivo até que tenha sido concluído e testado. Caso contrário, outros desenvolvedores receberão a versão incompleta do arquivo quando atualizarem suas listas de arquivos de projeto ou obtiverem as versões mais recentes dos arquivos.

Se a biblioteca for muito complexa, você também pode considerar dividi-la em bibliotecas menores para desenvolvimento. Outra vantagem desta abordagem é que arquivos de biblioteca menores carregam mais rapidamente. No entanto, isso significa que classes diferentes podem ser concluídas e disponibilizadas em momentos diferentes.

Como cada abordagem tem suas vantagens, você deve examinar os requisitos de sua equipe de desenvolvimento e escolher a estratégia que melhor se adapta à forma como vocês trabalham.
