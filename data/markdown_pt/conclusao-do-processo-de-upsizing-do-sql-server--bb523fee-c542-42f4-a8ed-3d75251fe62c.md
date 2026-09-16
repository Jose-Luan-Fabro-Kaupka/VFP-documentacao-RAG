# Conclusão do processo de upsizing do SQL Server

Agora você pode executar etapas adicionais, tanto no servidor quanto em sua aplicação Visual FoxPro, para garantir que sua aplicação e dados estejam seguros e funcionando corretamente.

Você também pode usar as informações nesta seção ao construir uma aplicação a partir de views remotas em vez de fazer upsizing. Independentemente de como você criou tabelas remotas, você executa certas etapas para garantir que o servidor e o cliente estejam preparados para trabalhar juntos em sua aplicação cliente/servidor.

# Etapas do SQL Server

Você pode concluir o processo de upsizing em seu servidor:
 - Garantindo que as tabelas que deseja editar do Visual FoxPro sejam atualizáveis.
- Definindo permissões no banco de dados para que os usuários possam acessar os objetos que precisam.
- Protegendo seu trabalho tornando seu novo banco de dados recuperável, caso seja danificado ou perdido.

### Adicionando índices exclusivos para atualizabilidade

Uma tabela remota deve ter um índice exclusivo para ser atualizável no Visual FoxPro. O SQL Server Upsizing Wizard pode exportar um índice exclusivo existente, mas não cria um onde nenhum existe. Certifique-se de que as tabelas que deseja editar do Visual FoxPro sejam atualizáveis.

### Definindo permissões

O novo banco de dados SQL Server e seus objetos recebem um conjunto de permissões padrão do SQL Server. Defina permissões no banco de dados remoto para que seus usuários tenham acesso aos objetos que precisam.

### Permissões de logon do banco de dados

As permissões padrão de um novo banco de dados tornam-o acessível apenas a administradores de sistema e ao proprietário do banco de dados.

Você pode adicionar novos usuários e grupos usando o SQL Server Security Manager ou os procedimentos de sistema `sp_adduser` e `sp_addgroup`.

Para obter mais informações sobre adicionar usuários e grupos, consulte a Ajuda do SQL Server Security Manager e a documentação dos procedimentos de sistema `sp_adduser` e `sp_addgroup` no Microsoft SQL Server Transact-SQL Reference.

### Permissões de objeto

Todos os objetos criados pelo Visual FoxPro-to-SQL Server Upsizing Wizard, incluindo tabelas, triggers e defaults, são acessíveis inicialmente apenas ao proprietário do banco de dados e administradores de sistema. Isso é verdade quer você faça upsizing para um banco de dados novo ou existente. Se você sobrescrever objetos existentes, também sobrescreve todas as permissões de objeto.

### Garantindo recuperabilidade

Proteja seu trabalho tornando seu novo banco de dados recuperável caso seja danificado ou perdido.

### Fazendo dump do banco de dados Master

Quando um banco de dados é criado em um SQL Server, novos registros são adicionados às tabelas de sistema no banco de dados Master. Fazer dump do banco de dados Master também fornece uma cópia de backup, incluindo todas as alterações mais recentes.

### Agendando backups

Agende backups regulares de seu banco de dados, para que possa restaurar seu banco de dados desta cópia de backup em caso de problema grave.

### Espelhamento de dispositivo

Espelhar um dispositivo duplica continuamente as informações de um dispositivo SQL Server para outro. No caso de falha de um dispositivo, o outro contém uma cópia atualizada de todas as transações.

Se você antecipa que muitas alterações serão feitas em um banco de dados entre backups e não pode perder essas alterações, considere o espelhamento de dispositivo. O espelhamento de dispositivo é mais eficaz quando os dispositivos estão localizados em discos separados, pois ambos os dispositivos podem ser perdidos se estiverem no mesmo disco e o disco falhar.

# Etapas do cliente Visual FoxPro

Depois de transferir objetos do Visual FoxPro para um SQL Server, você provavelmente precisa modificar o código no banco de dados Visual FoxPro original para que funcione corretamente com o novo banco de dados SQL Server.

### Otimizando views

Views criadas pelo SQL Server Upsizing Wizard não são parametrizadas e, portanto, não são otimizadas. Para processamento mais eficiente, adicione parâmetros a views criadas pelo SQL Server Upsizing Wizard para baixar apenas os dados necessários. Para obter informações sobre adicionar um parâmetro a uma view, consulte Como: criar views parametrizadas.

O SQL Server não suporta algumas funções do Visual FoxPro. Se a view remota criada pelo SQL Server Upsizing Wizard usa funções que não puderam ser mapeadas para funções Transact-SQL, a view não funcionará. Para obter mais informações sobre mapeamento de expressões Visual FoxPro para expressões Transact-SQL, consulte Mapeando bancos de dados Visual FoxPro para bancos de dados SQL Server.

### Criando stored procedures e triggers

O SQL Server Upsizing Wizard não faz upsizing de stored procedures e triggers do Visual FoxPro. Se deseja criar stored procedures ou triggers do SQL Server, pode usar Transact-SQL no servidor ou usar SQL pass-through no Visual FoxPro. Para obter mais informações sobre o uso de Transact-SQL, consulte a documentação do SQL Server. Para obter informações sobre o uso de SQL pass-through, consulte Aprimorando aplicações usando tecnologia SQL Pass-Through.

### Comparando ordem de eventos

No Visual FoxPro, alguns eventos ocorrem em ordem diferente, dependendo se sua aplicação está usando dados do SQL Server ou dados do Visual FoxPro. Essas diferenças podem exigir alterações em seu código.

### Valores padrão

Valores padrão de campo do Visual FoxPro aparecem quando você começa a editar um novo registro. Valores padrão gerados por defaults do SQL Server aparecem apenas depois que um registro foi inserido. Você precisa alterar qualquer código que dependa de ter valores antes que o registro seja confirmado, como o código para lookups.

### Regras de validação

No Visual FoxPro, a validação de campo ocorre quando o foco sai de um campo. Quando você edita dados do SQL Server em tabelas anexadas, triggers e regras não são disparados até que você saia do registro. Você pode precisar modificar quaisquer regras de validação de registro que dependam de validação de campo ocorrendo quando um campo é abandonado.

### Tratando expressões não convertidas

O relatório de upsizing indica se cada regra de validação de tabela Visual FoxPro, regra de validação de campo e expressão padrão foi convertida com sucesso. Se uma expressão padrão ou regra de validação não foi traduzida, você deve reescrevê-la em Transact-SQL.

Você também pode realizar validação no nível do formulário no Visual FoxPro. No entanto, se dados do servidor são então modificados sem usar um formulário particular, a validação não será aplicada e dados inválidos podem ser inseridos.

Para obter mais informações, consulte Como o SQL Server Upsizing Wizard funciona. Para obter mais informações sobre funções Transact-SQL, consulte a documentação do SQL Server.

### Bloqueio de registro

O Visual FoxPro usa bloqueio otimista internamente ao acessar tabelas em um servidor SQL. Bloqueio otimista significa que a linha é bloqueada apenas quando o valor editado é confirmado e o processo de atualização ocorre — geralmente um intervalo muito breve.

Bloqueio otimista é usado em vez de bloqueio pessimista no SQL Server porque bloqueio pessimista no SQL Server é fornecido por bloqueio de página, potencialmente bloqueando muitos registros de uma vez. Enquanto o bloqueio de página impede que outros usuários façam alterações no mesmo registro que você está editando, também pode impedir que usuários acessem muitos outros registros na mesma página (bloqueada). Bloqueio otimista fornece o melhor acesso multiusuário para uma aplicação cliente/servidor Visual FoxPro.

Você pode otimizar atualizações e controlar como conflitos de atualização são tratados com a propriedade SQL WhereType. Para obter mais informações sobre controle de conflitos de atualização, consulte Gerenciando conflitos ao atualizar dados.
