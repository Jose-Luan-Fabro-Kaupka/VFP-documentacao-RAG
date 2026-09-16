# Como: criar um arquivo de configuração

Para criar um arquivo de configuração, use o editor do Visual FoxPro ou qualquer editor que possa criar arquivos de texto para criar um arquivo de texto no diretório onde o Visual FoxPro está instalado. Versões anteriores do Visual FoxPro criaram o arquivo Config.fpw no diretório de inicialização. Config.fpw tornou-se o arquivo de configuração padrão. Você pode criar qualquer arquivo de programa e usá-lo para estabelecer configurações e comportamentos padrão iniciando o Visual FoxPro usando esse arquivo, clicando duas vezes no arquivo ou usando uma referência na linha de comando.

Se você estiver criando um novo arquivo de configuração, pode salvá-lo com qualquer nome que desejar. Por convenção, arquivos de configuração têm a extensão .fpw.

Quando você inicia o Visual FoxPro, pode usar um arquivo de configuração padrão dos seguintes locais, nesta ordem:
 - Diretório de trabalho atual
- Diretório onde o Visual FoxPro está instalado
- Diretórios listados no caminho do DOS

Se o Visual FoxPro não encontrar um arquivo de configuração nesses locais, o Visual FoxPro usa apenas as configurações padrão estabelecidas na caixa de diálogo Options.

> **Observação:** Para detalhes sobre como especificar uma alternativa ao nome ou local padrão do arquivo de configuração, consulte How to: Specify the Configuration File .

Insira configurações usando um destes métodos:
 - Faça configurações com o comando SET.
- Defina variáveis de sistema.
- Chame programas ou funções.
- Inclua termos especiais usados somente em arquivos de configuração.

### Para inserir comandos SET em um arquivo de configuração
- Insira comandos SET sem a palavra-chave SET e com um sinal de igual. Por exemplo, para definir um caminho padrão, use este formato: DEFAULT = HOME()+"\VFP" Para adicionar um relógio à barra de status, use este comando: CLOCK = ON

Para inserir uma configuração para uma variável de sistema, use a mesma sintaxe que você usaria na janela Command ou em um programa.

### Para definir variáveis de sistema em um arquivo de configuração
- Insira o nome da variável de sistema, um sinal de igual ( = ) e o valor para definir a variável. Por exemplo, o comando a seguir especifica um programa alternativo de verificação ortográfica: _SPELLCHK = "SPLLCHK.EXE"

Você também pode chamar funções ou executar programas de um arquivo de configuração usando o comando COMMAND. Por exemplo, você pode iniciar um programa de inicialização como parte do processo de inicialização.

### Para chamar funções ou executar comandos em um arquivo de configuração
- Insira COMMAND , um sinal de igual ( = ) e o comando a executar ou função a chamar. Por exemplo, para incluir o número da versão do Visual FoxPro na legenda da janela principal do Visual FoxPro, use este comando: COMMAND =_SCREEN.Caption="Visual FoxPro " + VERS(4) O comando a seguir inicia um aplicativo específico quando o Visual FoxPro é iniciado: COMMAND = DO MYAPP.APP

Você também pode usar termos especiais em um arquivo de configuração que não correspondem a valores SET, variáveis de sistema ou comandos.

### Para usar termos especiais em um arquivo de configuração
- Insira o termo especial, um sinal de igual ( = ) e a configuração. Por exemplo, para definir o número máximo de variáveis disponíveis no Visual FoxPro, use este comando: MVCOUNT = 2048

Para uma lista completa de termos especiais para arquivos de configuração, consulte Special Terms for Configuration Files.

# Iniciando aplicativos ou programas automaticamente

Você pode inserir comandos em um arquivo de configuração que iniciam programas automaticamente quando o Visual FoxPro é iniciado. Você pode usar esses comandos para iniciar um aplicativo inteiro ou apenas um programa, como um que inicializa variáveis de sistema.

### Para iniciar aplicativos de um arquivo de configuração
- Atribua o nome do seu aplicativo à variável de sistema _STARTUP em qualquer lugar do arquivo de configuração: _STARTUP = MYAPP.APP -ou-
- Use o comando COMMAND, que deve ser a última linha do seu arquivo de configuração: COMMAND = DO MYAPP.APP
