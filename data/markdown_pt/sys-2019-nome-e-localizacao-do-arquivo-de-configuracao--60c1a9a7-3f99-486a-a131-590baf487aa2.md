# SYS(2019) - Nome e localização do arquivo de configuração

Retorna o nome e a localização dos arquivos de configuração interno e externo do Visual FoxPro.

```foxpro
SYS(2019 [, 1 | 2])
```

#### Parâmetros

| Parâmetro | Descrição |
| --- | --- |
| 1 | (Padrão) Inclua este parâmetro para retornar o nome e a localização de Config.fpw, o arquivo de configuração externo do Visual FoxPro. Emitir SYS(2019,1) é equivalente a emitir SYS(2019) sem parâmetros. |
| 2 | Inclua este parâmetro para retornar o nome e a localização do arquivo de configuração interno. |

# Valor de retorno

Character

# Observações

O arquivo de configuração externo do Visual FoxPro é chamado Config.fpw e não é instalado por padrão. Você pode criar seu próprio arquivo de configuração Config.fpw com MODIFY FILE.

Se um arquivo de configuração interno ou externo não puder ser localizado, SYS(2019) retorna uma cadeia de caracteres vazia.

O arquivo de configuração externo do Visual FoxPro normalmente está localizado no diretório onde o Visual FoxPro ou um aplicativo do Visual FoxPro é iniciado, mas pode estar em outro local. O Visual FoxPro primeiro procura no diretório de inicialização. Se o arquivo de configuração não estiver localizado no diretório de inicialização, o caminho do MS-DOS é pesquisado. Ao iniciar o Visual FoxPro ou um aplicativo do Visual FoxPro, você também pode usar a opção -C para designar um arquivo de configuração externo. Inclua a localização e o nome do arquivo de configuração imediatamente após -C.

Para aplicativos do Visual FoxPro, você também pode criar um arquivo de configuração interno, que é incorporado ao arquivo executável do aplicativo. O arquivo de configuração interno deve ser chamado Config.fpw. Quando um arquivo de configuração interno é usado, ele será lido por padrão e qualquer arquivo de configuração externo que possa existir será ignorado. Você pode permitir que seu aplicativo do Visual FoxPro leia um arquivo de configuração externo após ler o arquivo de configuração interno usando a diretiva ALLOWEXTERNAL no arquivo de configuração interno. Quando você inclui a configuração ALLOWEXTERNAL=ON no arquivo de configuração interno, o Visual FoxPro pesquisa um arquivo de configuração externo usando os critérios de pesquisa listados acima e lê suas configurações. A opção de inicialização -C é ignorada quando usada com um aplicativo que inclui um arquivo de configuração interno, a menos que a configuração ALLOWEXTERNAL=ON esteja incluída no arquivo de configuração interno.

> **Observação:** Para servidores .exe e .dll, o Visual FoxPro suporta apenas arquivos de configuração vinculados dentro do servidor. Portanto, o Visual FoxPro ignora a configuração ALLOWEXTERNAL.

Para obter mais informações sobre opções de linha de comando, consulte Como: usar opções de linha de comando ao iniciar o Visual FoxPro.

As configurações em um arquivo de configuração externo têm precedência sobre as do arquivo de configuração interno, se existirem configurações duplicadas, porque o arquivo de configuração externo é lido após o arquivo interno. O Visual FoxPro não inicia a inicialização até ler os dois arquivos.

Se você deseja especificar o arquivo de configuração como somente leitura, coloque o arquivo em seu projeto e marque-o como Included. Se você deseja especificar que o arquivo pode ser modificado, coloque o arquivo em seu projeto e marque-o como Excluded. Você pode então distribuir o arquivo separadamente com seu aplicativo ou arquivo executável. Por convenção, os arquivos de configuração usam a extensão .fpw.

Para obter mais informações, consulte Termos especiais para arquivos de configuração e Definindo opções de configuração na inicialização.

Para obter mais informações sobre o arquivo de configuração do Visual FoxPro, consulte Personalizando o ambiente do Visual FoxPro.
