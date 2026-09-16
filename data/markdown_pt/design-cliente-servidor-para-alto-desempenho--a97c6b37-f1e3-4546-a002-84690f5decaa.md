# Design cliente/servidor para alto desempenho

Construir uma aplicação cliente/servidor rápida e de alto desempenho com Visual FoxPro envolve tirar proveito da tremenda velocidade do mecanismo do Visual FoxPro. Você faz isso com novas técnicas, como usar acesso a dados baseado em conjuntos em vez da navegação local tradicional, construir consultas parametrizadas para baixar apenas os dados que você precisa, localizar tabelas na plataforma ideal e aproveitar procedimentos armazenados tanto do Visual FoxPro quanto remotos.

Quando você projeta uma aplicação local ou de servidor de arquivos, determina as consultas, formulários, menus e relatórios que sua aplicação usará ou criará. Quando você projeta uma aplicação cliente/servidor, realiza toda a análise de sistema normal mais análise adicional que se relaciona especificamente a aplicações cliente/servidor. Você precisa pensar sobre onde os dados usados por consultas, formulários, menus e relatórios estarão localizados e como acessará essas informações. Por exemplo, você pode se perguntar:
 - Quais tabelas serão armazenadas no servidor remoto quando a aplicação for implementada?
- Quais tabelas seriam mais eficientemente armazenadas como tabelas de consulta locais?
- Quais views você precisará para acessar dados remotos?
- Quais regras de negócio o servidor impõe e como sua aplicação interagirá com essas regras?

Depois de determinar os componentes básicos de sua aplicação cliente/servidor, você pode começar a projetar como sua aplicação acessará e atualizará dados.
