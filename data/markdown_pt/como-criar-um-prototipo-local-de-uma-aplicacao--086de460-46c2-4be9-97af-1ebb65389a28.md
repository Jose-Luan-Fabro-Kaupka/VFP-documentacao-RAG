# Como: criar um protótipo local de uma aplicação

Ao criar um protótipo local da sua aplicação, você pode estar começando do zero ou convertendo uma aplicação existente do Visual FoxPro em uma aplicação cliente/servidor. A principal diferença entre criar um protótipo local de uma aplicação cliente/servidor e desenvolver qualquer outra aplicação do Visual FoxPro está no uso de exibições e tabelas locais para representar os dados que posteriormente serão migrados.

### Para criar e migrar um protótipo local
- Crie sua aplicação usando exibições e tabelas locais para representar os dados que você deseja mover para um servidor remoto.
- Use exibições locais no ambiente de dados da aplicação para formulários e relatórios.
- Migre exibições e tabelas locais usando o Assistente de Migração do SQL Server: na etapa Set Upsizing Options, na área Changes to make locally, selecione Redirect views to remote data. Ao selecionar essa opção, o Assistente de Migração copia para o servidor remoto as tabelas locais selecionadas e redireciona as exibições locais para usar dados remotos, quando aplicável.

Para obter mais informações, consulte Trabalhando com exibições (Visual FoxPro) e Criando formulários.
