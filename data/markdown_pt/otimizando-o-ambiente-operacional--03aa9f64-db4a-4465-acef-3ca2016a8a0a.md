# Otimizando o ambiente operacional

Você pode otimizar o desempenho do Visual FoxPro aproveitando ao máximo o hardware e o ambiente operacional do computador. As seções a seguir descrevem como otimizar essas áreas:
 - Maximizando a memória e a memória virtual
- Gerenciando o disco rígido

# Maximizando a memória e a memória virtual

Fornecer ao computador o máximo de memória possível é a maneira mais eficaz de otimizar o sistema para o Visual FoxPro. Você também pode usar a memória de forma mais eficiente fechando todos os outros aplicativos em execução. Para maximizar o uso da memória do computador durante a execução do Visual FoxPro, siga estas diretrizes:
 - Não execute outros aplicativos do Windows enquanto estiver executando o Visual FoxPro.
- Use somente os programas residentes na memória necessários à operação.
- Simplifique a exibição da tela.

Você pode liberar memória simplificando a forma como as janelas e os planos de fundo são exibidos no monitor.
 - Use uma cor ou um padrão no plano de fundo da área de trabalho em vez de papel de parede.
- Use a menor resolução de tela que seja prática. Quanto maior a resolução, mais memória o computador exige e mais lentos parecem os elementos gráficos e da interface do usuário. Para monitores compatíveis com VGA que usam um driver de modo estendido, como Video 7 ou 8514, o driver VGA padrão oferece exibição mais rápida, mas resolução mais baixa e menor suporte a cores.

Para aumentar o número de aplicativos que podem ser executados simultaneamente, o Microsoft Windows oferece suporte à memória virtual, transferindo da memória para o disco rígido, em um arquivo de paginação, os segmentos de código usados há mais tempo. Como regra geral, as configurações padrão do Windows para gerenciar a memória virtual atendem aos requisitos da maioria dos usuários e são recomendadas.

> **Observação:** O arquivo de paginação não melhora o desempenho do Visual FoxPro nem substitui uma quantidade maior de memória.

# Gerenciando o disco rígido

O gerenciamento do disco rígido pode melhorar a velocidade geral do produto. Para obter o melhor desempenho, disponibilize bastante espaço em disco. Se houver pouco espaço livre, você poderá melhorar o desempenho do Visual FoxPro removendo dados desnecessários ou adquirindo um disco de maior capacidade.

O desempenho de entrada/saída cai significativamente quando o disco está quase cheio. Quanto mais espaço livre houver, maior será a probabilidade de haver blocos contíguos disponíveis. O Visual FoxPro usa esse espaço para alterações e adições em arquivos de banco de dados, tabela, índice, memo e temporários. Aumentar o espaço livre melhora o desempenho dos comandos que alteram ou adicionam dados aos arquivos e reduz o tempo necessário para lê-los em resposta às consultas.

A maneira como o Windows e o Visual FoxPro gerenciam arquivos no disco pode afetar muito o desempenho do aplicativo. As seções a seguir discutem o gerenciamento de arquivos em diretórios e de arquivos temporários:
 - Gerenciando arquivos em diretórios
- Gerenciando arquivos temporários

### Gerenciando arquivos em diretórios

À medida que um diretório fica mais cheio de arquivos, o sistema operacional demora mais para localizá-los. A velocidade das pesquisas em diretórios é um fator que o Visual FoxPro não controla. Para melhorá-la, reduza o número de arquivos nos diretórios:
 - Use o Project Manager do Visual FoxPro para criar e gerenciar arquivos, separe arquivos de programa em diretórios distintos e evite criar muitos arquivos gerados.
- Ao distribuir o aplicativo, crie um aplicativo ou arquivo executável (.exe) em vez de muitos arquivos gerados individualmente. Isso reduz o número de arquivos nos subdiretórios e melhora o desempenho.
- Se excluir muitos arquivos de um diretório, copie os restantes para um novo diretório ou otimize-o com um utilitário de desfragmentação. A exclusão não acelera automaticamente as pesquisas: o arquivo apenas é marcado para exclusão e ainda participa delas.
- Ao salvar arquivos, use caminhos curtos para melhorar o desempenho. Por exemplo, em vez de um caminho muito longo como "C:\Program Files\Microsoft Visual FoxPro\...", tente usar caminhos menores.

### Gerenciando arquivos temporários

O Visual FoxPro cria arquivos temporários para várias operações, como edição, indexação e classificação. Sessões de edição de texto também podem criar uma cópia temporária ou de backup (.bak). Por padrão, os arquivos temporários são criados no mesmo diretório usado pelo Windows, a menos que você especifique outro local.

> **Dica:** Na maioria dos casos, especifique um único local para todos os arquivos temporários do Visual FoxPro. Verifique se ele contém espaço suficiente para todos os arquivos temporários possíveis.

Para obter mais informações, consulte Como: especificar o local dos arquivos temporários.

#### Pesquisando arquivos temporários

Quando o Visual FoxPro pesquisa arquivos temporários, por exemplo ao usar SYS(2023) - Temporary Path para recuperar o caminho ou quando TMPFILES, EDITWORK, PROGWORK e SORTWORK não especificam outro local no arquivo de configuração, a API GetTempPath do Windows é usada. GetTempPath pesquisa uma sequência de variáveis que varia conforme o sistema operacional. O Microsoft Windows 2000 e posteriores incluem variáveis de usuário para armazenar esse local, enquanto Windows 95, 98 e Me incluem somente variáveis globais de ambiente.

No Windows 2000 e posteriores, GetTempPath e, portanto, SYS(2023), TMPFILES, EDITWORK, PROGWORK e SORTWORK pesquisam por padrão a variável de usuário TMP. Se ela não especificar um local, o Visual FoxPro pesquisa estas variáveis na ordem indicada:
 - Variável de sistema TMP.
- Variável de usuário TEMP.
- Variável de sistema TEMP.

Se essas variáveis não especificarem um local, o padrão será a unidade e o caminho inicial ou a pasta Temp no diretório Documents and Settings do usuário.

> **Observação:** Se mais de um valor for especificado para TMP ou TEMP, o primeiro será usado.

No Windows 95, 98 e Me, GetTempPath pesquisa as variáveis globais de sistema TMP e TEMP, nessa ordem, e depois o diretório atual.

Para obter mais informações, consulte SYS(2023) - Temporary Path e Termos especiais para arquivos de configuração.
