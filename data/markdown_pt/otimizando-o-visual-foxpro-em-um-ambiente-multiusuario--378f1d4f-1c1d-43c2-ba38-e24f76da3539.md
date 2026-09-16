# Otimizando o Visual FoxPro em um ambiente multiusuário

Ao executar o Visual FoxPro ou aplicativos Visual FoxPro em um ambiente multiusuário, você pode melhorar o desempenho gerenciando o armazenamento de arquivos temporários e controlando a forma como as tabelas são compartilhadas.

# Gerenciando arquivos temporários

Na maioria dos ambientes multiusuários, recomenda-se salvar arquivos temporários em discos locais ou na memória quando computadores em rede contêm grandes quantidades de espaço livre em disco. Redirecionar o armazenamento de arquivos temporários pode melhorar o desempenho reduzindo o acesso frequente à unidade de rede.

Em redes pequenas com computadores em rede mais antigos e discos rígidos lentos, você pode obter melhor desempenho deixando os arquivos temporários do Visual FoxPro no servidor de arquivos; no entanto, em caso de dúvida, direcione arquivos temporários para o disco local. Ao trabalhar em redes grandes e muito utilizadas, sempre redirecione arquivos temporários para o disco local.

Ao salvar todos os arquivos temporários em um único diretório em uma unidade de disco rígido local, você pode apagar com segurança o conteúdo do diretório de arquivos temporários no servidor de arquivos antes de cada sessão do Visual FoxPro. Esta ação purga o sistema de quaisquer arquivos temporários que foram criados, mas não apagados pelo Visual FoxPro devido a uma reinicialização do sistema ou perda de energia.

Para obter mais informações sobre arquivos temporários, consulte Optimizing the Operating Environment e How to: Specify the Location of Temporary Files.

# Compartilhando tabelas

Se os usuários compartilham tabelas em uma rede, a forma como você gerencia o acesso a elas pode afetar o desempenho.
 - Evite abrir e fechar tabelas repetidamente.
- Faça buffer de operações de gravação em tabelas que não são compartilhadas.
- Forneça acesso exclusivo a tabelas.
- Limite o tempo de bloqueio de tabelas.

### Fornecendo acesso exclusivo

Você pode melhorar o desempenho dos comandos APPEND, REPLACE e DELETE e de operações executadas em momentos em que nenhum outro usuário precisa de acesso aos dados, por exemplo, atualizações noturnas, abrindo arquivos de dados para uso exclusivo. Quando as tabelas estão abertas para uso exclusivo, o desempenho melhora porque o Visual FoxPro não precisa testar o status de bloqueios de registro ou arquivo.

Para abrir arquivos de dados para uso exclusivo, use a cláusula EXCLUSIVE nos comandos USE e OPEN DATABASE. Para obter mais informações, consulte USE Command e OPEN DATABASE Command.

### Limitando o tempo de bloqueio de tabelas

Você pode reduzir a contenção entre usuários pelo acesso de gravação a uma tabela ou registro encurtando o tempo de bloqueio de um registro ou tabela. Em vez de bloquear um registro enquanto o usuário o edita, bloqueie o registro somente depois que ele tiver sido editado. Usar buffer de linha otimista fornece o menor tempo em que os registros ficam bloqueados. Para obter mais informações, consulte Buffering Data.
