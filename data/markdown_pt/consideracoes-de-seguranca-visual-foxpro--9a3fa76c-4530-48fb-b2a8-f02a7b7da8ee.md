# Considerações de segurança (Visual FoxPro)

Ao projetar um aplicativo servidor, sua especificação de design deve abordar questões de segurança. Você deve considerar e pode abordar os seguintes itens na especificação funcional do aplicativo:
 - Objetivos de segurança Defina o que você precisa proteger.
- Riscos de segurança Entenda as vulnerabilidades do seu aplicativo. Você também deve entender a importância das ameaças potenciais em relação ao seu negócio.
- Autenticação Descreve o processo de aceitar credenciais de um usuário e validar essas credenciais contra uma autoridade designada. A identidade do usuário, ou possivelmente de um aplicativo ou computador, é referida como principal de segurança. O cliente deve fornecer credenciais para permitir que o servidor verifique a identidade do principal. Depois que a identidade é conhecida, o aplicativo pode autorizar o principal a acessar recursos no sistema.
- Autorização Descreve o processo de determinar se a identidade comprovada tem permissão para acessar um recurso específico.
- Proteção da transmissão de dados Garanta que os dados não possam ser visualizados ou adulterados durante a transmissão usando criptografia quando cruzam a rede. Você deve considerar o nível de segurança que seus dados precisam durante a transmissão.
- Representação Permite que um processo servidor seja executado usando as credenciais de segurança do cliente. Quando o servidor representa o cliente, quaisquer operações realizadas pelo servidor usam as credenciais do cliente. A representação não permite que o servidor acessa recursos remotos em nome do cliente e requer delegação.
- Delegação Permite que um processo servidor seja executado usando as credenciais de segurança do cliente, semelhante à representação. No entanto, a delegação é mais poderosa e permite que o processo servidor faça chamadas a outros computadores agindo como o cliente.
- Segurança do sistema operacional Refere-se ao estabelecimento de Listas de Controle de Acesso (ACLs) apropriadas e segurança de rede para impedir que invasores acessam recursos protegidos. Você deve definir as ACLs apropriadas nos recursos apropriados para permitir acesso somente pelos principais relevantes.
- Proteção do acesso físico Refere-se ao armazenamento do computador servidor em uma sala segura. Você não deve negligenciar essa questão fundamental.
- Segurança de acesso a código Permite que o código seja confiável em graus variados dependendo de onde se origina e de outros aspectos da identidade do código. Você deve estar ciente de como criar suas próprias permissões de acesso.
