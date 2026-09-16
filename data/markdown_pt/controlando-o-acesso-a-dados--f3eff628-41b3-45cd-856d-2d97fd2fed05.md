# Controlando o acesso a dados

Como você acessa dados em arquivos, o gerenciamento eficaz de dados começa com o controle sobre o ambiente desses arquivos. Você deve escolher como acessar os dados e como e quando limitar esse acesso.

# Nesta seção
 **Como: definir o acesso a dados**
Explica como especificar o tipo de acesso, exclusivo ou compartilhado, ao usar uma tabela.
**Bloqueando dados**
Discute métodos para bloquear manualmente ou automaticamente o acesso a tabelas e registros para gerenciar o acesso em um ambiente compartilhado.
**Atualizando dados usando várias instâncias de formulário**
Discute como os dados são atualizados e como bloqueios em registros podem afetar outras instâncias de um formulário.
**Como: usar sessões de dados**
Descreve como usar sessões de dados para garantir que cada usuário em um ambiente compartilhado tenha uma duplicata exata e segura do ambiente de trabalho, e para garantir que várias instâncias de um formulário possam operar de forma independente.
**Personalizando o ambiente de uma sessão de dados**
Discute como você pode usar sessões de dados privadas para estabelecer configurações personalizadas de comandos SET dentro de uma única sessão do Visual FoxPro.
**Armazenamento em buffer de dados**
Descreve o armazenamento em buffer de dados e como usá-lo para proteger dados durante atualizações.
**Como: habilitar armazenamento em buffer**
Explica como habilitar o armazenamento em buffer de registro e de tabela para proteger dados durante atualizações.
**Como: acrescentar e excluir registros em buffers de tabela**
Explica como acrescentar e excluir registros com o armazenamento em buffer de tabela habilitado.

# Referência
 **Função CURSORSETPROP( )**
Especifica configurações de propriedade para uma tabela ou cursor do Visual FoxPro.
**Função TABLEUPDATE( )**
Confirma alterações feitas em uma linha em buffer, uma tabela em buffer, cursor ou cursor adapter.
**Função TABLEREVERT( )**
Descarta alterações feitas em uma linha em buffer ou em uma tabela ou cursor em buffer e restaura os dados OLDVAL( ) para cursores remotos e os valores atuais do disco para tabelas e cursores locais.
**Função LOCK( )**
Tenta bloquear um ou mais registros em uma tabela.
**Janela Data Session**
Use a janela Data Session para abrir e exibir tabelas ou exibições, estabelecer relacionamentos temporários e definir propriedades de área de trabalho.

# Seções relacionadas
 **Programação para acesso compartilhado**
Explica como a programação para acesso compartilhado torna possível criar um aplicativo que será executado em várias máquinas em um ambiente de rede.
**Atualizando dados**
Explica como atualizar dados usando buffers, transações ou exibições.
**Gerenciando conflitos ao atualizar dados**
Discute como você pode antecipar e gerenciar os conflitos inevitáveis que resultam de operações de atualização de dados.
**Armazenamento em buffer de dados**
Explica como armazenar dados em buffer para proteger dados durante atualizações.
