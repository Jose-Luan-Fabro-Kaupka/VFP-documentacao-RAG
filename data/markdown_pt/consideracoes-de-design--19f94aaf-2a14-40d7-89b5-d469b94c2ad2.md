# Considerações de design

Algumas das decisões de design tomadas por você afetam a forma como partes do aplicativo são criadas. Algumas das considerações que você precisa levar em conta incluem:
 - Tarefas centrais ou comuns executadas pelos usuários.
- Tamanho do conjunto de dados necessário.
- Um ou vários usuários.
- Pessoas que fazem parte dos usuários do aplicativo.
- Dados locais ou remotos.

# Atividades comuns dos usuários

Mesmo que seus usuários finais trabalhem com clientes, pedidos e peças, a forma como trabalham com essas informações determinará como seu aplicativo deverá lidar com os dados. Um formulário de entrada de pedidos pode ser necessário para alguns aplicativos, mas não seria uma boa ferramenta para gerenciar estoque ou acompanhar vendas, por exemplo.

# Tamanho do banco de dados

Se você trabalha com grandes conjuntos de dados, precisa considerar questões de desempenho. Talvez seja conveniente alterar a forma como os usuários navegam pelos dados. Por exemplo, se houver um pequeno número de registros em uma tabela, você pode permitir que os usuários naveguem pelos registros da tabela, um registro de cada vez. No entanto, se houver muitos registros, considere oferecer outras formas de acesso aos dados, por exemplo, usando listas, caixas de diálogo, filtros, consultas personalizadas e assim por diante. Para obter mais informações, consulte Otimização de aplicativos, Uso de controles e Exibição de dados em exibições.

# Um usuário versus vários usuários

É recomendável criar o aplicativo pressupondo que vários usuários acessarão o banco de dados ao mesmo tempo. O Visual FoxPro facilita a programação para acesso compartilhado. Programação para acesso compartilhado descreve técnicas para permitir que vários usuários acessem simultaneamente o banco de dados.

# Considerações internacionais

Se você sabe que seu aplicativo será usado apenas em um ambiente de idioma único, não precisa se preocupar com internacionalização. Por outro lado, se deseja expandir seu mercado ou se os usuários podem lidar com dados internacionais ou configurações de ambiente, considere esses fatores ao criar o aplicativo. Desenvolvimento de aplicativos internacionais aborda as questões que você precisará tratar ao desenvolver aplicativos para uso internacional.

# Dados locais versus remotos

Se o aplicativo lidar com dados remotos, você os gerenciará de forma diferente dos dados nativos do Visual FoxPro. Criação de exibições explica como criar exibições de dados locais ou remotos.

# Backup do código-fonte

Em todo desenvolvimento de aplicativos, é recomendável fazer cópias de backup completas dos arquivos de programa originais antes de compilar um aplicativo. Armazene as cópias de backup separadamente dos aplicativos compilados.

> **Observação:** Mantenha cópias separadas dos programas-fonte originais para uso futuro. Não é possível recriar os programas-fonte a partir do código compilado.
