# Como: instalar o Visual FoxPro

Você pode instalar esta versão do Visual FoxPro de um CD-ROM ou de uma rede em um disco rígido local. É necessário instalar o Visual FoxPro em uma unidade local, não em uma unidade mapeada. Nenhuma outra preparação é necessária antes de instalar o Visual FoxPro. Você deve ter privilégios de administrador para instalá-lo. Recomenda-se usar privilégios de usuário avançado para utilizar com eficiência todas as ferramentas fornecidas.

Você pode instalar ou desinstalar com segurança usando a Instalação do Visual FoxPro. Se estiver atualizando o Visual FoxPro, primeiro desinstale a versão anterior do programa. Embora as duas versões do Visual FoxPro possam existir no mesmo computador, não é possível instalar a versão atual no mesmo diretório da versão anterior.

Se pretende publicar serviços Web XML usando o Visual FoxPro, talvez seja conveniente configurar os Serviços de Informações da Internet (IIS) em um computador com Windows 2000, Windows XP ou Windows Server 2003. Consulte a documentação do sistema operacional para obter instruções sobre como instalar e configurar o IIS.

> **Observação:** A instalação do Visual FoxPro não instala mais Service Packs do sistema operacional Windows nem versões do Internet Explorer. É altamente recomendável instalar as versões mais recentes desses componentes antes de instalar o Visual FoxPro. Além disso, o Visual FoxPro 9.0 é compatível somente com Windows 2000 Service Pack 3 ou posterior. Para obter detalhes sobre a instalação do Service Pack mais recente, visite a página da Microsoft em http://www.microsoft.com/windows2000/ .

A instalação completa inclui todos os arquivos de programa do Visual FoxPro, a ajuda online e os arquivos de exemplos.

### Para instalar o Visual FoxPro
- Feche todos os aplicativos abertos. Observação: se você usa um programa antivírus no computador, desative-o ou suspenda-o antes de executar o Assistente de Instalação. O assistente pode não funcionar corretamente com a proteção antivírus ativada. Após a instalação, lembre-se de reiniciar o programa antivírus.
- Insira o CD do Visual FoxPro. A página inicial da Instalação do Visual FoxPro aparecerá automaticamente.
- Clique em Install Visual FoxPro para iniciar a Instalação do Visual FoxPro.
- Para determinar se você precisa de componentes adicionais, clique em Prerequisites para exibir os componentes necessários.
- Clique em Install Now! para instalar os novos componentes. Se os Pré-requisitos do Visual FoxPro precisarem apenas atualizar componentes, clique em Update Now!
- Talvez seja necessário reiniciar o computador. Ao terminar, clique em Done. A Instalação do Visual FoxPro reaparecerá.
- Para continuar a instalação, clique em Visual FoxPro.
- Depois de aceitar o Contrato de Licença de Usuário Final e inserir a chave do produto e seu nome, clique em Continue. Observação: o Visual FoxPro não pode ser instalado em uma unidade mapeada. É necessário instalá-lo em uma unidade local. Não tente usar a funcionalidade Map Network Drive da Instalação.
- Na página Options, selecione os recursos que deseja instalar e clique em Install Now! para continuar.
- Ao terminar, clique em Done para retornar à Instalação do Visual FoxPro. Clique em Exit para voltar à página inicial da Instalação do Visual FoxPro.

Se você desinstalar o Visual FoxPro enquanto a versão anterior ainda existir no computador, determinadas chaves compartilhadas do Registro usadas pela versão anterior serão removidas. Será necessário reinstalar essas chaves críticas compartilhadas do Registro.

Se você executar o Visual FoxPro pelo menu Start, a Instalação do Visual FoxPro reinstalará automaticamente essas chaves. Se iniciar o Visual FoxPro de outra maneira, como executando diretamente o arquivo executável do aplicativo, o programa de instalação não será iniciado automaticamente. Use Add/Remove Programs no Control Panel e siga estas etapas para reinstalar manualmente as chaves do Registro:

### Para reinstalar manualmente as chaves do Registro do Visual FoxPro 9.0
- No menu Start, clique em Control Panel.
- Clique em Add/Remove Programs.
- Clique em Change/Remove para Microsoft Visual FoxPro 9.0.
- Clique em Visual FoxPro e em Repair/Reinstall.
