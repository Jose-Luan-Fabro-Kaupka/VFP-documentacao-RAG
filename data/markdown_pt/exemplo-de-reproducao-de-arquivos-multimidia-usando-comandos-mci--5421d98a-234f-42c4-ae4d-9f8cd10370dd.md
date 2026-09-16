# Exemplo de reprodução de arquivos multimídia usando comandos MCI

Arquivo: ...\Samples\Solution\Forms\Mci_play.scx

Este formulário de exemplo usa a Media Control Interface (MCI) para reproduzir arquivos multimídia e pode reproduzir qualquer mídia visual ou não visual instalada no seu sistema. No entanto, a função GETFILE( ) solicita os arquivos de mídia mais comuns de .avi, .wav, .mov e .mid. Para escolher outro arquivo, selecione All Files e escolha o arquivo desejado. Para localizar documentação dos comandos MCI, consulte a MSDN Library.

As três funções da API do Windows a seguir são declaradas no evento Init do formulário:
 - mciSendString
- mciGetErrorString
- SetWindowPos

O método DoMCI do formulário executa um comando MCI que é passado como parâmetro.

# Classes

Você pode abrir o formulário para ver todo o código necessário para executar arquivos multimídia, mas a funcionalidade também foi extraída em classes que você pode incorporar facilmente em suas próprias aplicações.

### Classe VideoFrame

A classe VideoFrame na biblioteca de classes ...\Samples\Classes\Samples.vcx do Visual FoxPro pode ser usada para reproduzir um arquivo multimídia visual, como um arquivo Video for Windows. A classe permite posicionar e dimensionar o vídeo a ser reproduzido e depois fornece métodos integrados para reproduzir facilmente o arquivo de mídia.

Para um exemplo de uso desta classe, consulte Video.scx no diretório ...\Samples\Solution\Forms do Visual FoxPro.

| Propriedade | Descrição |
| --- | --- |
| AutoOpen | Especifica se o arquivo de vídeo deve abrir e exibir automaticamente quando o objeto é instanciado. O valor padrão é true (.T.). |
| AutoPlay | Especifica se o arquivo de vídeo deve reproduzir automaticamente quando é aberto. O valor padrão é true (.T.). |
| AutoRepeat | Especifica se o arquivo de vídeo fará loop do vídeo. Definir isso como .T. fará o vídeo reproduzir continuamente. O valor padrão é false (.F.). |
| ControlSource | Especifica um Field que contém a referência do arquivo de vídeo. Se vazio, a classe espera um nome de arquivo estático na propriedade VideoFile. |
| MCIalias | Especifica o alias a ser usado pelo MCI. Se deixado vazio, o alias tem como padrão a propriedade Name da classe. Normalmente isso pode ser deixado vazio, mas se o usuário deseja reproduzir o mesmo arquivo de vídeo duas vezes ao mesmo tempo, um alias diferente precisaria ser especificado para cada um. |
| VideoFile | Contém o nome de um arquivo de vídeo a reproduzir, por exemplo: "D:\...\Samples\Solution\FORMS\FOX.AVI" |

| Método | Descrição |
| --- | --- |
| CloseVideo | Fecha o arquivo de vídeo e libera todos os recursos associados a ele. |
| DoMCI | Chamado pelos outros métodos para executar comandos MCI. Também pode ser chamado por um usuário para executar um comando MCI específico. |
| OpenVideo | Abre o arquivo de vídeo e mostra o primeiro quadro. |
| PauseVideo | Pausa um vídeo em reprodução. O vídeo pode ser reiniciado usando o método PlayVideo. |
| PlayVideo | Reproduz o arquivo de vídeo. O arquivo de vídeo deve ser aberto no método OpenVideo antes de poder ser reproduzido. |
| SetPosition | Permite que o usuário especifique a posição do arquivo de mídia. Pode ser executado a qualquer momento depois que o arquivo de vídeo foi aberto. Valores válidos são "Start", "End" ou um milissegundo específico no vídeo. |

### Classe Sound Player

Esta classe também está contida na biblioteca de classes ...\Samples\Classes\Samples.vcx. Pode ser usada para reproduzir um arquivo multimídia não visual, como um arquivo waveaudio. A classe permite especificar o arquivo a ser reproduzido e depois fornece métodos integrados para reproduzir facilmente o arquivo de mídia.

| Propriedade | Descrição |
| --- | --- |
| AutoOpen | Especifica se o arquivo de som deve abrir e exibir automaticamente quando o objeto é instanciado. O valor padrão é true (.T.). |
| AutoPlay | Especifica se o arquivo de som deve reproduzir automaticamente quando é aberto. O valor padrão é true (.T.). |
| AutoRepeat | Especifica se o arquivo de som reproduz continuamente. O valor padrão é false (.F.). |
| ControlSource | Especifica a coluna que contém a referência do arquivo de som. Se vazio, a classe espera um nome de arquivo estático na propriedade SoundFile. |
| MCIAlias | Especifica o alias a ser usado pelo MCI. Se deixado vazio, o alias tem como padrão a propriedade Name da classe. Normalmente isso pode ser deixado vazio, mas se o usuário deseja reproduzir o mesmo arquivo de som duas vezes ao mesmo tempo, um alias diferente precisaria ser especificado para cada um. |
| SoundFile | Contém o nome de um arquivo de som a reproduzir, por exemplo: "C:\WINDOWS\CHIMES.WAV" |

| Método | Descrição |
| --- | --- |
| OpenSound | Abre o arquivo de som. |
| PlaySound | Reproduz o arquivo de som. O arquivo deve ser aberto com o método OpenSound antes de poder ser reproduzido. |
| PauseSound | Pausa a reprodução de um arquivo de som. A reprodução pode ser continuada chamando o método PlaySound. |
| SetPosition | Permite que o usuário especifique a posição do arquivo de mídia. Pode ser executado a qualquer momento depois que o arquivo foi aberto. Valores válidos são "Start", "End" ou um milissegundo específico no som. |
| CloseSound | Fecha o arquivo de som e libera todos os recursos associados a ele. |
