# Planejando um aplicativo internacional

Ao projetar um aplicativo para uso internacional, você pode reduzir o custo e o tempo para o mercado em vez de modificá-lo posteriormente para uso internacional. Ao se preparar para projetar um aplicativo internacional, certifique-se de considerar o seguinte:
 - Dados aceitáveis para um aplicativo internacional.
- Escrever código para um aplicativo internacional.
- Considerações de design para a interface do usuário.

Preparar um aplicativo internacional geralmente envolve as seguintes etapas: criar dados, escrever código e projetar uma interface do usuário. As seções a seguir contêm mais informações sobre essas considerações.

# Determinando dados aceitáveis para aplicativos internacionais

Para determinar dados aceitáveis para um aplicativo internacional, considere o seguinte:
 - Locales dos usuários do aplicativo.
- Idiomas que afetam a página de código usada para preparar dados.

Os locales dos seus usuários determinam o conteúdo cultural dos dados, bem como os idiomas que afetam a página de código. Uma página de código é um conjunto de caracteres que um computador usa para exibir dados corretamente, frequentemente para lidar com caracteres internacionais. Caracteres internacionais incluem caracteres que possuem marcas diacríticas. Marcas diacríticas são colocadas sobre, sob ou através de letras para indicar alterações de som em relação à forma não marcada. Por exemplo, as marcas diacríticas mais comuns são o acento grave (` como em à), acento agudo (' como em á), acento circunflexo (^ como em â), til (~ como em ã), trema (¨ como em ä) e barra (/ como em ø), todos usados em conjunto com vogais.

Normalmente, os dados são marcados automaticamente com a página de código apropriada quando você trabalha com eles. No entanto, se você atribuir manualmente uma página de código a uma tabela, ou de outra forma fizer a página de código mudar, os usuários podem não reconhecer alguns ou todos os dados exibidos. Para obter mais informações, consulte Code Pages in Visual FoxPro.

Alguns idiomas, como chinês, coreano e japonês, usam conjuntos de caracteres de byte duplo (DBCS) para representar seus dados. Se seu aplicativo puder ser executado nesses ambientes, você pode precisar usar funções especiais de manipulação de cadeias de caracteres e sequências de ordenação para que o aplicativo funcione corretamente. Para obter mais informações, consulte Application Creation with Double-Byte Character Sets.

# Escrevendo código para aplicativos internacionais

Um aplicativo consiste em um componente de aplicativo e um componente de interface do usuário. O componente de aplicativo contém o código que é executado para todos os locales, incluindo código que processa as cadeias de caracteres e gráficos usados na interface do usuário. O componente de interface do usuário contém gráficos, cadeias de caracteres e configurações relacionadas a vários locales, como datas, moedas, valores numéricos e separadores.

Ao projetar seu aplicativo, mantenha os componentes de aplicativo e de interface do usuário separados, pois componentes independentes tornam o aplicativo mais fácil de localizar e manter.

Por exemplo, você não precisa percorrer o código-fonte para localizar elementos de interface quando eles são componentes separados. Para obter mais informações, consulte Modifying International Applications.

# Projetando a interface do usuário para aplicativos internacionais

Os menus, formulários, controles, barras de ferramentas e bitmaps usados na interface do usuário devem ser apropriados para os locales do aplicativo que você projeta. Por exemplo, se você projetar o aplicativo para usuários na Alemanha e na França, as caixas de diálogo devem ser grandes o suficiente para exibir instruções localizadas em alemão e francês. Além disso, as imagens usadas em ícones e bitmaps devem ser culturalmente apropriadas e corretas para que os usuários nos locales de destino possam entendê-las. Para obter mais informações, consulte Designing for Localization.

# Testando aplicativos internacionais

Ao testar aplicativos internacionais, lembre-se de verificar o seguinte:
 - Dependências de país e idioma para o aplicativo.
- Dados do aplicativo e interface do usuário para conformidade com os padrões do locale para data e hora, valores numéricos, moeda, separadores de lista e medidas.
