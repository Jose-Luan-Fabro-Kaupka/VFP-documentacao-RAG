# Como: atualizar uma tabela em uma view

Você pode usar views locais ou remotas para atualizar as tabelas base na fonte de dados remota. Na guia Update Criteria, View Designer, a guia Update Criteria permite controlar como as alterações feitas nos dados remotos (atualizações, exclusões e inserções) são enviadas de volta à fonte de dados remota. Você também pode habilitar e desabilitar a atualização de campos específicos nas tabelas e definir o método de atualização SQL apropriado para o seu servidor.

> **Observação:** As tabelas base locais que são abertas automaticamente quando você usa uma view não são fechadas automaticamente quando você fecha uma view; você deve fechá-las explicitamente. Isso é consistente com o comando SQL SELECT.

# Tornando uma tabela atualizável

Se desejar que as alterações feitas na versão local de uma tabela sejam enviadas de volta à tabela de origem, é necessário definir a opção Send SQL Updates. Você deve definir pelo menos um campo chave para usar esta opção. Se a tabela selecionada tem um campo de chave primária definido e você o selecionou na guia Fields, o View Designer usa automaticamente o campo de chave primária da tabela como campo chave da view.

### Para habilitar a atualização de tabelas de origem
- Na guia Update Criteria, defina a opção Send SQL updates.

# Definindo campos chave

Quando você abre uma tabela no View Designer pela primeira vez, a guia Update Criteria mostra quais campos da tabela estão definidos como campos chave. O Visual FoxPro usa campos chave para identificar exclusivamente os registros de atualização em tabelas remotas que você modificou localmente.

### Para definir um campo chave
- Na guia Update Criteria, clique na coluna key ao lado do nome do campo.

Se você alterou os campos chave e deseja restaurá-los à configuração original na tabela de origem, escolha Reset Key. O Visual FoxPro verificará as tabelas remotas e usará os campos chave dessas tabelas.

# Atualizando campos específicos

Você pode especificar que apenas determinados campos em qualquer tabela sejam atualizáveis. É necessário ter um campo chave definido para uma tabela para tornar quaisquer campos dessa tabela atualizáveis. Se os campos não estiverem marcados como atualizáveis, os usuários podem fazer alterações no campo em um formulário ou janela Browse, mas essas alterações não são enviadas à tabela remota.

### Para tornar um campo atualizável
- Na guia Update Criteria, clique na coluna atualizável ("lápis") ao lado do nome do campo.

# Atualizando todos os campos

Se desejar poder fazer alterações em todos os campos de uma tabela, pode definir todos os campos de uma tabela como atualizáveis.

### Para tornar todos os campos atualizáveis
- Na guia Update Criteria, escolha Update All . Observação Você deve ter um campo chave definido em uma tabela para usar Update All. Update All não afeta campos chave.
