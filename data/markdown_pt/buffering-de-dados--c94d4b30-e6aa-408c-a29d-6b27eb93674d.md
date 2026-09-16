# Buffering de dados

Se você deseja proteger dados durante atualizações, use buffers. O buffering de registro e tabela do Visual FoxPro ajuda a proteger operações de atualização e manutenção de dados em registros individuais e em múltiplos registros de dados em ambientes multiusuário. Os buffers podem testar, bloquear e liberar registros ou tabelas automaticamente.

Com buffering, você pode detectar e resolver facilmente conflitos em operações de atualização de dados: o registro atual é copiado para um local de memória ou disco gerenciado pelo Visual FoxPro. Outros usuários ainda podem acessar o registro original simultaneamente. Quando você sai do registro ou tenta atualizar o registro programaticamente, o Visual FoxPro tenta bloquear o registro, verificar se nenhuma outra alteração foi feita por outros usuários e, em seguida, gravar as alterações. Após tentar atualizar dados, você também deve resolver conflitos que impedem que as alterações sejam gravadas na tabela original.

# Escolhendo um método de buffering

Antes de habilitar o buffering, avalie o ambiente de dados para escolher o método de buffering e as opções de bloqueio que melhor se adequam às necessidades de edição da sua aplicação, aos tipos e tamanhos de registros e tabelas, como as informações são usadas e atualizadas e outros fatores. Depois de habilitar o buffering, ele permanece em vigor até você desabilitar o buffering ou fechar a tabela.

O Visual FoxPro tem dois tipos de buffering: registro e tabela.
 - Para acessar, modificar e gravar um único registro por vez, escolha buffering de registro. O buffering de registro fornece validação de processo apropriada com impacto mínimo nas operações de atualização de dados de outros usuários em um ambiente multiusuário.
- Para armazenar em buffer as atualizações de vários registros, escolha buffering de tabela. O buffering de tabela fornece a maneira mais eficaz de lidar com vários registros em uma tabela ou registros filhos em um relacionamento um-para-muitos.
- Para fornecer proteção máxima aos dados existentes, use transações do Visual FoxPro. Você pode usar transações isoladamente, mas ganha eficácia adicional usando transações como wrappers para comandos de buffering de registro ou tabela.

# Escolhendo um modo de bloqueio

O Visual FoxPro fornece buffering em dois modos de bloqueio: pessimista e otimista. Essas escolhas determinam quando um ou mais registros são bloqueados e como e quando são liberados.

# Buffering pessimista

O buffering pessimista impede que outros usuários em um ambiente multiusuário acessem um registro ou tabela específica enquanto você está fazendo alterações nele. Um bloqueio pessimista fornece o ambiente mais seguro para alterar registros individuais, mas pode tornar as operações do usuário mais lentas. Este modo de buffering é mais semelhante ao mecanismo de bloqueio padrão em versões anteriores do FoxPro, com o benefício adicional de buffering de dados integrado.

# Buffering otimista

O buffering otimista é uma maneira eficiente de atualizar registros porque os bloqueios são feitos somente no momento em que o registro é gravado, minimizando o tempo em que qualquer usuário monopoliza o sistema em um ambiente multiusuário. Quando você usa buffering de registro ou tabela em views, o Visual FoxPro impõe bloqueio otimista.

O valor da propriedade Buffering, definido com a função CURSORSETPROP( ), determina os métodos de buffering e bloqueio.

A tabela a seguir resume os valores válidos para a propriedade Buffering.

| Para habilitar | Use este valor |
| --- | --- |
| Sem buffering. O valor padrão. | 1 |
| Bloqueios pessimistas de registro que bloqueiam o registro agora e atualizam quando o ponteiro se move ou mediante TABLEUPDATE( ). | 2 |
| Bloqueios otimistas de registro que aguardam até o ponteiro se mover e, em seguida, bloqueiam e atualizam. | 3 |
| Bloqueios pessimistas de tabela que bloqueiam o registro agora e atualizam posteriormente mediante TABLEUPDATE( ). | 4 |
| Bloqueio otimista de tabela que aguarda até TABLEUPDATE( ) e, em seguida, bloqueia e atualiza registros editados. | 5 |

O valor padrão para Buffering é 1 para tabelas e 3 para views. Se você usar buffering para acessar dados remotos, a propriedade Buffering é 3, buffering otimista de linha, ou 5, buffering otimista de tabela. Para obter mais informações sobre acesso a dados em tabelas remotas, consulte Como: consultar múltiplas tabelas e views.

> **Observação:** Defina MULTILOCKS como ON para todos os modos de buffering acima de 1.
