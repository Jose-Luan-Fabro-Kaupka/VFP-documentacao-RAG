# Otimizando a velocidade de inicialização do Visual FoxPro

Embora o Visual FoxPro seja sempre rápido, você pode otimizar a velocidade de inicialização e de operação. Esta seção descreve como melhorar o desempenho do Visual FoxPro gerenciando a velocidade de inicialização e otimizando comandos SET.

# Gerenciando a velocidade de inicialização

O tempo necessário para carregar e iniciar o Visual FoxPro está relacionado ao tamanho físico do Visual FoxPro, ao comprimento da instrução PATH em vigor, ao número de itens a serem encontrados na inicialização e a outros fatores. Você pode controlar o tamanho da carga, o caminho de pesquisa, os locais dos arquivos de componentes e os valores dos comandos SET de inicialização do Visual FoxPro.

### Gerenciando locais de arquivos

O Visual FoxPro armazena o arquivo FoxUser.dbf, que contém as configurações do usuário, no diretório Application Data do usuário por padrão. Você pode exibir esse local digitando `? HOME(7)` na janela Command. O Visual FoxPro pesquisa os arquivos FoxUser.dbf e Config.fpw nos seguintes locais:
 - No aplicativo ou arquivo executável de inicialização, se houver. Por exemplo, você pode iniciar um aplicativo Visual FoxPro digitando o seguinte código na linha de comando: VFPversionNumber .exe MyApp .app – ou – VFP versionNumber .exe MyApp .exe Se o aplicativo ou arquivo executável de inicialização contiver um arquivo Config.fpw, o arquivo de configuração será sempre usado. Você pode substituir configurações em um arquivo Config.fpw que esteja vinculado dentro de um aplicativo especificando um arquivo Config.fpw externo, usando a opção de linha de comando -C ao iniciar um aplicativo ou o Visual FoxPro.
- No diretório de trabalho.
- No caminho estabelecido com a variável de ambiente PATH.
- No diretório que contém o Visual FoxPro.

### Controlando o carregamento de arquivos

Você também pode acelerar a inicialização impedindo que o Visual FoxPro carregue arquivos que não pretende usar. Se o seu aplicativo não usa o arquivo FoxUser ou FoxHelp, desabilite-os no arquivo Config.fpw usando os seguintes comandos:

```foxpro
RESOURCE = OFF
HELP = OFF
```

O Visual FoxPro busca todos os outros componentes do Visual FoxPro (GENXTAB, CONVERT e assim por diante) somente no diretório do Visual FoxPro. Se você colocar componentes em outro local, deve identificar explicitamente o caminho para esses componentes no arquivo Config.fpw. Por exemplo, você pode especificar estes locais:

```foxpro
_TRANSPORT = c:\migrate\transport.prg
_GENXTAB = c:\crosstab\genxtab.prg
_FOXREF = c:\coderefs\foxref.app
```

Você pode usar a variável de ambiente FOXPROWCFG para especificar explicitamente o local do Config.fpw. Para obter detalhes sobre a variável FOXPROWCFG, consulte Personalizando o ambiente do Visual FoxPro.

# Otimizando o tamanho da carga do Visual FoxPro

Se você não pretende usar nenhum dos componentes do Visual FoxPro listados anteriormente, defina-os como cadeia de caracteres vazia para acelerar a inicialização.

Para otimizar o tamanho da carga do Visual FoxPro, use a seguinte sintaxe:

```foxpro
        cFileVariable = ""
```

Substitua cFileVariable por _TRANSPORT, _CONVERT ou outras variáveis, conforme apropriado.

# Otimizando comandos SET principais

Você pode otimizar a operação do Visual FoxPro ajustando os valores de determinados comandos SET.

A tabela a seguir mostra os comandos SET que têm o maior efeito no desempenho e suas configurações para desempenho máximo. Você pode especificar valores de comandos SET incluindo-os no arquivo Config.fpw, digitando-os na janela Command ou definindo-os na caixa de diálogo Options.
 Configurações de comando para desempenho máximo
| Comando SET | Configuração de desempenho |
| --- | --- |
| Comando SET ESCAPE | ON |
| Comando SET OPTIMIZE | ON |
| Comando SET REFRESH | 0,0 |
| Comando SET SYSMENU | DEFAULT |
| Comando SET TALK | OFF |
| Comando SET VIEW | OFF |
