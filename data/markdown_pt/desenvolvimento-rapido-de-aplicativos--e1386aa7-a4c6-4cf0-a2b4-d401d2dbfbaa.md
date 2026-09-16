# Desenvolvimento rápido de aplicativos

Independentemente do método de programação que você escolher, você precisa de uma boa estratégia para tornar o desenvolvimento de aplicativos cliente/servidor rápido e eficiente. Como o Visual FoxPro facilita a prototipagem e construção rápida de aplicativos, você pode optar por projetar e construir um protótipo local do seu aplicativo e depois fazer upsizing e implementá-lo em etapas contra uma fonte de dados remota. Se você tiver acesso a uma fonte de dados remota durante o processo de desenvolvimento, pode optar por prototipar seu aplicativo contra a fonte de dados remota, usando views remotas.

# Construindo um protótipo com views

O primeiro passo no desenvolvimento de um aplicativo cliente/servidor Visual FoxPro pode ser construir um protótipo. Ao prototipar seu aplicativo, talvez módulo a módulo, você descobre alterações e aprimoramentos no design do aplicativo no início do processo de desenvolvimento. Você pode então refinar seu design de forma eficiente contra pequenos armazenamentos de dados de amostra antes de adicionar a camada adicional de complexidade inerente ao trabalho com grandes conjuntos de dados remotos e heterogêneos. Para obter mais informações, consulte Upsizing Visual FoxPro Databases.

### Criando um protótipo local com views locais

Um protótipo local para um aplicativo cliente/servidor é um aplicativo Visual FoxPro funcional que usa views locais para acessar tabelas locais. Você usa views no protótipo cliente/servidor porque o aplicativo cliente/servidor final usará views remotas para acessar dados remotos. Ao prototipar seu aplicativo com views locais, você está um passo mais perto do aplicativo final.

Construir um protótipo local é especialmente prático se você não tiver acesso constante a uma fonte de dados remota durante o desenvolvimento ou se não quiser usar dados remotos para prototipar seu aplicativo. Views locais acessam tabelas Visual FoxPro locais, em vez de tabelas de fonte de dados remota. Você cria os dados locais, no entanto, para imitar a estrutura dos dados no servidor. Usar dados locais para representar dados remotos é um método de desenvolver e testar rapidamente o design básico do aplicativo. Você também pode acelerar o desenvolvimento limitando a quantidade de dados selecionados nas views. Para obter mais informações, consulte Working with Views (Visual FoxPro).

### Planejando para upsizing

Upsizing é o processo que cria um banco de dados no servidor remoto com a mesma estrutura de tabela, dados e potencialmente muitos outros atributos do banco de dados Visual FoxPro original. Com upsizing, você pega um aplicativo Visual FoxPro existente e migra para um aplicativo cliente/servidor. Para obter mais informações, consulte Upsizing Visual FoxPro Databases.

Quando você constrói um aplicativo que eventualmente fará upsizing, faz escolhas sobre o design da arquitetura do aplicativo e o modelo de programação baseados em obter o máximo desempenho contra uma fonte de dados remota. Para obter mais informações, consulte Client/Server Design for High Performance.

### Prototipando com views remotas

Se você tem acesso a uma fonte de dados remota e deseja usar dados remotos diretamente ao desenvolver seu aplicativo cliente/servidor, pode construir seu protótipo usando views remotas. Ao prototipar usando views remotas, você pula a etapa de upsizing porque seus dados já estão localizados em um servidor remoto e você já tem views remotas para acessar esses dados.

# Implementando seu aplicativo cliente/servidor

Você pode simplificar o teste e a depuração do aplicativo implementando o aplicativo prototipado em etapas. Ao implementar um aplicativo prototipado em etapas, você adiciona aprimoramentos multiusuário, move os dados para a fonte de dados remota e testa e depura o aplicativo, módulo a módulo, de maneira sistemática.

Ao implementar seu aplicativo, você pode usar sintaxe nativa do servidor e acessar funcionalidade específica do servidor, como procedimentos armazenados em um servidor remoto, com tecnologia SQL pass-through. Para obter mais informações, consulte Enhancing Applications Using SQL Pass-Through Technology.

# Otimizando seu aplicativo

Depois que seu aplicativo estiver totalmente implementado contra dados remotos e você concluir a fase de teste e depuração, pode ajustar a velocidade e o desempenho de todo o aplicativo. Para obter mais informações, consulte Optimizing Client/Server Performance.
