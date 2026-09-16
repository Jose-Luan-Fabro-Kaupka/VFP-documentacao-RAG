# Visual FoxPro como back end de aplicativo

Uma forma diferente de integrar o Visual FoxPro em uma solução corporativa é usá-lo como um componente, mas não necessariamente como o aplicativo principal. Na prática, você o trataria como um back end para um aplicativo escrito com outro produto. Nesse caso, o usuário não veria o Visual FoxPro diretamente. Em vez disso, a interface do usuário do aplicativo seria escrita com ferramentas do outro aplicativo e se comunicaria com o Visual FoxPro em segundo plano para obter ou manipular dados.

O Visual FoxPro funciona bem nesse papel porque pode disponibilizar seu mecanismo de banco de dados, que oferece acesso rápido a dados para outros aplicativos. Além disso, o Visual FoxPro pode disponibilizar seus objetos e conjuntos de comandos para outros programas, incluindo objetos personalizados que você criar.

# Disponibilizar dados do Visual FoxPro para outros programas

Uma forma de um aplicativo corporativo aproveitar o Visual FoxPro é usar o mecanismo de banco de dados do Visual FoxPro para armazenar e gerenciar dados. Isso oferece armazenamento e capacidade de consulta de alto desempenho para outros programas.

Os programas podem se conectar a dados do Visual FoxPro usando o provedor OLE DB do Visual FoxPro. Esse provedor expõe o mecanismo de banco de dados do Visual FoxPro a comandos SQL padrão do Visual FoxPro.

Por exemplo, um aplicativo pode usar o Microsoft Excel como ferramenta de cálculo para análise complexa de dados. Se os dados a serem manipulados são altamente fluidos, pode não fazer sentido armazená-los em uma planilha, mas em um banco de dados. A planilha poderia então ser escrita para usar o provedor OLE DB do Visual FoxPro para se conectar ao banco de dados, extrair as informações relevantes e exibi-las em uma planilha para processamento adicional.

Outro exemplo pode ser um aplicativo de quiosque, como um ponto de informações em um aeroporto ou centro de convenções. Você poderia criar a exibição de informações com um programa de autoria multimídia. Mas se parte dos dados no aplicativo mudasse com frequência, seria trabalhoso alterar páginas na apresentação. Em vez disso, o programa de apresentação poderia se conectar a um banco de dados do Visual FoxPro usando o provedor OLE DB e extrair dados em tempo de execução.

Para mais informações, consulte os tópicos de ajuda do provedor OLE DB do Visual FoxPro.

# Disponibilizar objetos e comandos do Visual FoxPro para outros programas

Além de disponibilizar dados do Visual FoxPro para outros programas como parte de uma solução corporativa, você pode expor objetos e comandos do Visual FoxPro. Outros aplicativos podem chamar os métodos e definir propriedades de objetos no Visual FoxPro, incluindo não apenas os objetos base, mas objetos definidos em classes personalizadas.

Por exemplo, você pode criar um aplicativo no Microsoft Excel que armazena dados em um banco de dados do Visual FoxPro. Além de simplesmente ler e gravar os dados, o Microsoft Excel pode chamar comandos do Visual FoxPro para exibir um formulário como uma caixa de diálogo. Um uso possível é coletar dados para uma view parametrizada.

Outra forma de expor objetos do Visual FoxPro é criar um servidor Automation. Isso permite criar objetos específicos do aplicativo que podem executar quase qualquer função que você possa programar no Visual FoxPro, com a vantagem adicional de poder distribuir o servidor.

Um uso para um servidor personalizado é criar um objeto que inclua um conjunto de regras de negócio que garantam a integridade dos dados que outro aplicativo passa a ele. Por exemplo, você pode criar um objeto no Visual FoxPro para armazenar informações de funcionários que não apenas valida se o aplicativo passou informações válidas de funcionário, mas verifica o nível de acesso do usuário para garantir que ele tenha permissão de segurança para fazer as alterações de funcionário.

Um servidor personalizado também pode expor um objeto que incorpora lógica complexa para atualizar ou ler informações. Por exemplo, um objeto de entrada de pedidos pode não apenas armazenar o pedido, mas também manter um log de transações de pedidos, atualizar o inventário, calcular comissão de vendas e assim por diante.

Esse tipo de servidor Automation é ideal para criar a camada intermediária de um aplicativo corporativo de três camadas. Nesse modelo, os dados formam o nível mais baixo e o aplicativo forma o mais alto. A funcionalidade está no meio e fornece uma visão específica e independente do aplicativo dos dados que incorpora regras de negócio (ou outras capacidades de processamento de dados) que não pertencem adequadamente aos dados nem ao aplicativo isoladamente.

Para informações sobre como criar servidores Automation personalizados, consulte Como: criar servidores Automation em Compartilhamento de informações e adição de OLE.

# Criar um data warehouse usando o Visual FoxPro

Além de criar seu aplicativo no Visual FoxPro, você pode usar o programa para criar e manter um data warehouse, ou uma versão dos seus dados otimizada para relatórios. Para criar um data warehouse, você faz uma cópia dos dados necessários para relatórios e os disponibiliza para os usuários que precisam deles. Ao manter esses dados separados dos dados em produção, você pode:
 - Estruturá-los para tornar os relatórios mais fáceis ou mais rápidos do que se os usuários criassem relatórios a partir dos dados em produção.
- Colocar dados para relatórios em um local separado dos dados em produção, o que reduz contenção de dados, melhora o desempenho e pode disponibilizar dados para usuários que não devem ver dados em produção por motivos de segurança.

Um data warehouse é um instantâneo dos dados no momento em que você o cria. Você atualiza os dados no warehouse periodicamente, agendando a atualização conforme as necessidades de relatórios do seu aplicativo.

Por exemplo, imagine que você está criando um aplicativo para gerenciar uma biblioteca, incluindo um inventário de materiais. Durante o dia, o sistema está em uso constante enquanto os usuários fazem check-in e check-out de materiais e consultam o sistema para localizar ou reservar livros. Além de gerenciar essas transações individuais, os bibliotecários querem analisar a biblioteca para determinar fatos como quais materiais são os mais populares, quais livros estão atrasados e assim por diante.

Para ajudar na análise, o aplicativo pode criar um data warehouse com as informações de transação. O aplicativo pode armazenar os dados no warehouse periodicamente, talvez todas as noites, e os bibliotecários podem criar consultas sem afetar o desempenho do sistema durante o dia. Além disso, o data warehouse pode excluir detalhes sobre os usuários da biblioteca, porque essas informações não são necessárias para a análise e podem ser consideradas confidenciais.

Para obter o máximo benefício de um data warehouse, crie-o em um servidor separado dos dados em produção. Se os dados em produção e o data warehouse estiverem no mesmo servidor, você ainda pode obter o benefício de ter dados otimizados no warehouse. Porém, conforme os usuários fazem consultas no warehouse, eles podem gerar grande volume de tráfego de rede, o que pode afetar o desempenho do sistema em produção.

Ao criar o data warehouse, você pode simplesmente copiar os arquivos em produção para arquivos paralelos no data warehouse. Alternativamente, você pode reestruturar os dados no warehouse para otimizá-los para relatórios. Por exemplo, você pode criar índices para os dados do warehouse que reduzam a sobrecarga de relatórios.

Como outro exemplo, os dados no aplicativo em produção devem ser normalizados para evitar duplicação de dados. Porém, no data warehouse pode ser útil combinar tabelas que de outra forma seriam separadas; isso pode eliminar a necessidade de fazer join de tabelas, facilitando para usuários menos experientes criar relatórios.

Você também pode adequar o nível de detalhe no data warehouse às necessidades de relatórios do seu aplicativo. Para máxima flexibilidade, você deve armazenar o mesmo nível de detalhe no data warehouse que tem nos dados em produção. Porém, se os usuários quisessem criar apenas relatórios resumidos (como planilhas ou gráficos), você poderia consolidar dados detalhados do aplicativo e armazenar apenas dados resumidos no data warehouse.

# Usar o Visual FoxPro como mecanismo de busca na World Wide Web

Se sua solução corporativa envolve criar um servidor World Wide Web para a Internet, você pode incorporar o Visual FoxPro ao aplicativo como mecanismo de busca. Isso permite disponibilizar o poder do seu banco de dados do Visual FoxPro para qualquer pessoa que possa acessar seu servidor Web, seja na Internet ou via intranet da empresa.

Por exemplo, imagine que, como parte da intranet da sua empresa, você quer disponibilizar um diretório de funcionários. Os funcionários poderiam apontar seus navegadores para uma página "Buscar funcionário", que exibiría uma página parecida com um formulário do Visual FoxPro, contendo caixas de texto para inserir critérios. Para realizar uma busca, os usuários inseririam o nome do funcionário, ramal, departamento, cargo ou qualquer outra informação disponível e escolheriam um botão Buscar agora. Em um ou dois momentos, veriam uma listagem dos funcionários que atendiam aos critérios de busca. Eles poderiam então salvar essa listagem como um arquivo de texto que poderia ser importado para outro programa, como um processador de texto.

### Entender o Visual FoxPro como mecanismo de busca na Web

Em geral, para usar o Visual FoxPro como servidor de informações para a Web, você precisa destes componentes:
 - Um servidor Web existente com serviço HTTP, em execução no sistema operacional Microsoft Windows NT ou Windows 2000.
- Um aplicativo Visual FoxPro que possa ser chamado como servidor Automation. Esse aplicativo pode ser executado em qualquer servidor acessível ao servidor Web.
- Um meio de exibir resultados de busca, que geralmente consiste em um modelo de página Web no qual você pode inserir dados.

A sequência usual de eventos que envolvem uma busca do Visual FoxPro na Web é esta:
 - O usuário exibe a página de busca do seu aplicativo apontando um navegador Web para ela. A página de busca inclui qualquer texto e gráficos que você desejar, além de caixas de texto nas quais os usuários podem inserir texto de busca.
- O usuário escolhe um botão "Buscar agora". Os dados do formulário preenchido são enviados ao servidor Web para processamento, junto com o nome do aplicativo de busca da sua página Web.
- O servidor Web chama seu aplicativo usando o protocolo ISAPI (Internet Server API), passando um parâmetro contendo as informações de busca.
- Seu aplicativo busca no banco de dados. Quando obtém resultados, os insere em um modelo de página Web e envia a página Web de volta ao servidor como um fluxo de caracteres.
- O servidor Web envia a página de resultados ao navegador que iniciou a busca.
- O navegador exibe a página de resultados para o usuário.

Se você já criou páginas Web, a maior parte das etapas desse processo provavelmente é familiar. Por exemplo, você pode já saber como criar páginas Web. Mesmo que não esteja familiarizado com design de páginas Web, provavelmente encontraria o processo de criar essas páginas relativamente fácil.

Para um exemplo de como usar o Visual FoxPro como mecanismo de busca na Web, consulte a amostra Foxisapi.dll no diretório Visual FoxPro ...\Samples\Servers\Foxisapi. Consulte o arquivo Readme.txt nesse diretório para detalhes sobre como executar o exemplo.
