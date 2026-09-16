# Criação de aplicações com precisão e integridade de dados

Você pode combinar o poder das regras de validação de dados e stored procedures do Visual FoxPro com as regras de validação de dados e stored procedures da fonte de dados para construir aplicações cliente/servidor que protegem a integridade dos dados.

# Mantendo a integridade dos dados

Você pode criar versões locais das regras de validação do servidor remoto para fornecer mensagens amigáveis ao usuário; por exemplo, fornecer mensagens sobre atualizações que não seriam permitidas quando enviadas ao servidor remoto porque os dados inseridos violaram alguma regra de integridade relacional ou validação de dados do servidor.

### Usando regras do Visual FoxPro em uma view remota ou offline

Você pode criar regras em nível de campo e de registro em views remotas e offline para validar dados inseridos localmente antes que os dados sejam enviados à fonte de dados remota. Como o propósito dessas regras de view é impedir o envio de dados à fonte de dados que serão rejeitados pelas regras de integridade de dados do servidor, você deseja replicar as regras da fonte de dados nas regras que cria para sua view remota. Você usa a função DBSETPROP( ) Function para criar regras para views.

> **Dica:** Você pode criar uma regra de validação local em uma view remota que chama uma stored procedure em um servidor remoto e envia o valor que deseja validar ao servidor como um parâmetro. No entanto, usar uma stored procedure em um servidor remoto aumenta o tempo de processamento durante a entrada de dados.

### Usando regras do servidor

Você pode optar por confiar nas regras estabelecidas no servidor para validação de dados. Se ocorrer um erro, sua rotina de tratamento de erros pode chamar a função AERROR( ) Function para obter informações, incluindo o número da mensagem de erro, o texto da mensagem de erro remota e o identificador de conexão associado ao erro.

### Usando triggers do servidor

Embora você possa criar triggers do Visual FoxPro em tabelas locais, não pode criá-las em views. Você pode, no entanto, usar triggers na fonte de dados remota. Triggers do servidor podem ser usados para processar atualizações secundárias de dados, como atualizações ou exclusões em cascata. Usar triggers do servidor para processar atualizações secundárias é mais eficiente do que enviar vários comandos ao servidor remoto da sua aplicação Visual FoxPro.

# Protegendo contra perda de dados

Tanto o Visual FoxPro quanto a maioria das fontes de dados remotas fornecem capacidades de registro de transações para proteger contra perda de dados. Para obter mais informações, consulte Programming for Shared Access.

Você pode usar transações do Visual FoxPro para protótipos locais e para processar dados locais. Use transações do servidor para atualizações, inserções e exclusões de dados remotos. Para obter mais informações, consulte Optimizing Client/Server Performance.
