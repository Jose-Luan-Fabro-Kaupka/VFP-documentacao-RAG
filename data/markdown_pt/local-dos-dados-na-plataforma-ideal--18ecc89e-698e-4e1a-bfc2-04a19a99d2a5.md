# Local dos dados na plataforma ideal

Você obtém o máximo desempenho ao armazenar dados e outros atributos do banco de dados na plataforma ideal. A melhor plataforma para um determinado elemento depende de como ele é acessado e atualizado. Por exemplo, você pode armazenar uma cópia local de uma tabela de servidor, como um diretório de códigos postais usado como tabela de pesquisa, e atualizar a cópia local somente quando a tabela de back-end for alterada.

A tabela a seguir lista alguns elementos comuns de aplicativos e exemplos de onde localizá-los para obter o desempenho ideal.
 Localização dos elementos por plataforma
| Elemento | Local | Tipo | Observações |
| --- | --- | --- | --- |
| Tabelas | Local | Cópias locais de tabelas de pesquisa do servidor; tabelas pequenas e alteradas com pouca frequência | Use um carimbo de data/hora, se houver suporte do servidor remoto, para comparar e, opcionalmente, atualizar a tabela local de acordo com quaisquer alterações na tabela de origem de back-end. |
| Remoto | Tabelas grandes ou alteradas com frequência | | |
| Regras | Local | Regras em exibições remotas | Você pode usar DBSETPROP( ) para armazenar regras de campo e de registro em uma exibição remota. Seu aplicativo pode usar essas regras locais para verificar a validade dos dados antes de enviá-los ao back-end como uma atualização de tabelas remotas. |
| Remoto | Regras em nível de linha e de coluna em tabelas base remotas | | |
| Procedimentos armazenados | Local | Procedimentos armazenados do Visual FoxPro | |
| Remoto | Procedimentos armazenados em um servidor remoto | Use a função de passagem SQL SQLEXEC( ) para chamar procedimentos armazenados em um servidor remoto. | |
| Transações | Local | Transações do Visual FoxPro | |
| Remoto | Transações do servidor | | |
| Gatilhos | Exibições locais | Sem gatilhos em exibições | |
| Remoto | Gatilhos do servidor | | |

Para reduzir o tráfego de rede durante pesquisas, você pode optar por armazenar localmente não apenas tabelas de pesquisa alteradas com pouca frequência, mas também as alteradas com frequência. Por exemplo, você pode baixar a lista de clientes da sua empresa e atualizá-la somente quando as informações dos clientes forem alteradas.

Para isso, você pode programar seu aplicativo para comparar o carimbo de data/hora da cópia local da tabela com o carimbo de data/hora dos dados de back-end (se o servidor remoto oferecer suporte a carimbos de data/hora) e atualizar a cópia local somente se a tabela do servidor tiver sido alterada. Você também pode adicionar um botão de comando ao formulário que force o download imediato da tabela, permitindo que os usuários atualizem sua cópia da tabela local sob demanda.
