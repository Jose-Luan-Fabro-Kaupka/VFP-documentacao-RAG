# Como: obter as versões mais recentes dos arquivos

Se você deseja visualizar a versão mais recente de um arquivo, pode fazer check-out. No entanto, se o arquivo já estiver com check-out ou se você deseja apenas visualizar o arquivo (não modificá-lo), pode obter a versão mais recente de um arquivo. Ao fazer isso, o Visual FoxPro copia a versão mais atual com check-in de um arquivo para o seu computador, mas o mantém como arquivo somente leitura. Você pode obter a versão mais recente de um arquivo mesmo se ele estiver com check-out no momento.

Se o arquivo que você está obtendo é um arquivo de texto, o software de controle de origem mesclará a versão mais atual com a sua versão em vez de simplesmente substituí-la.

> **Observação:** Para mesclar arquivos ao obter a versão mais recente, pode ser necessário habilitar isso como uma opção no seu software de controle de origem. Para detalhes, consulte a documentação do seu software de controle de origem.

### Para obter a versão mais recente de um arquivo
- Na Janela do Gerenciador de projetos , selecione o arquivo para o qual deseja a versão mais recente.
- No menu Projeto, escolha Controle de origem e, em seguida, escolha Obter versão mais recente . Se o arquivo estiver com check-out no momento, você será solicitado a substituir ou mesclar sua versão com check-out com a versão atual do projeto de controle de origem. Observação Se você já tiver o arquivo com check-out, o Visual FoxPro solicitará que você o substitua. Se você fez alterações no arquivo desde o último check-out, escolha No quando solicitado a substituir o arquivo.
