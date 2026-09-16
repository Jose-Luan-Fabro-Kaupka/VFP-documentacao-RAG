# Como: especificar o arquivo de configuração

Quando o Visual FoxPro inicia, você pode especificar um arquivo de configuração ou ignorar todos os arquivos de configuração, permitindo que o Visual FoxPro use suas configurações padrão.

Quando o Visual FoxPro carrega um arquivo de configuração, as configurações desse arquivo têm precedência sobre as configurações padrão correspondentes feitas na caixa de diálogo Options.

### Para especificar um arquivo de configuração
- Na linha de comando que inicia o Visual FoxPro, especifique a opção -C e o nome do arquivo de configuração que deseja usar (incluindo um caminho, se necessário). Não coloque espaço entre a opção e o nome do arquivo. -ou-
- No Windows, clique duas vezes no nome do arquivo de configuração a ser usado. O Visual FoxPro será iniciado usando o arquivo de configuração selecionado.

Se você deseja evitar o uso de qualquer arquivo de configuração, incluindo o arquivo padrão Config.fpw, você pode suprimir todos os arquivos de configuração. Isso faz com que o Visual FoxPro use apenas as configurações padrão estabelecidas na caixa de diálogo Options.

### Para suprimir um arquivo de configuração
- Na linha de comando que inicia o Visual FoxPro, adicione a opção -C sem nada depois dela. Por exemplo, para evitar qualquer arquivo de configuração encontrado no diretório de inicialização ou no caminho do sistema, use esta linha de comando: VFP VersionNumber .exe -C

### Especificando um arquivo de configuração externo

Você pode usar um arquivo de configuração externo além de um arquivo de configuração interno em circunstâncias em que precise configurar opções separadamente. Por exemplo, definir `SCREEN=OFF` deve ser feito em um arquivo de configuração interno.

Você pode configurar o Visual FoxPro para ler um arquivo de configuração externo após um arquivo de configuração interno usando a nova diretiva ALLOWEXTERNAL no arquivo de configuração interno. Quando você inclui a configuração `ALLOWEXTERNAL=ON` no arquivo de configuração interno, o Visual FoxPro procura um arquivo de configuração externo, geralmente Config.fpw, e lê suas configurações. Você também pode especificar um arquivo de configuração diferente usando a opção de linha de comando `-C` ao iniciar o Visual FoxPro.

> **Observação:** Para servidores de arquivo .exe e .dll, o Visual FoxPro suporta apenas os arquivos de configuração incorporados no servidor. Portanto, o Visual FoxPro ignora a configuração ALLOWEXTERNAL.

### Para ler um arquivo de configuração externo após um interno
- No arquivo de configuração interno, defina o termo especial ALLOWEXTERNAL como ativado. ALLOWEXTERNAL = ON
- Ao iniciar seu programa, especifique um segundo arquivo de configuração usando a opção de linha de comando -C ou tenha um segundo arquivo de configuração no caminho padrão do programa.

Para obter mais informações sobre opções de linha de comando, consulte How to: Use Command-Line Options When Starting Visual FoxPro.

As configurações em um arquivo de configuração externo têm precedência sobre as do arquivo de configuração interno, se existirem configurações duplicadas, porque o arquivo de configuração externo é lido após o arquivo interno. O Visual FoxPro não inicia a inicialização até ler ambos os arquivos.

Se você deseja especificar o arquivo de configuração como somente leitura, coloque o arquivo em seu projeto e marque-o como Included. Se você deseja especificar que o arquivo pode ser modificado, coloque o arquivo em seu projeto e marque-o como Excluded. Você pode então distribuir o arquivo separadamente com seu aplicativo ou arquivo executável. Por convenção, arquivos de configuração usam a extensão .fpw.
