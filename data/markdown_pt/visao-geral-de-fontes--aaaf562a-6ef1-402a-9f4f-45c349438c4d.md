# Visão geral de fontes

O Visual FoxPro pode usar as fontes que você instalou. As fontes determinam a aparência do texto exibido ou impresso. Além disso, as fontes determinam a posição e o tamanho dos controles.

# Tamanho e posição do controle

No Visual FoxPro, a propriedade ScaleMode do Form no qual um controle está colocado determina o tamanho e a posição do controle. Se ScaleMode estiver definido como Pixels (3), o tamanho de um controle é especificado em pixels. Se ScaleMode estiver definido como Foxels (0), o tamanho de um controle é determinado pela fonte e tamanho de fonte atuais do Form.

Foxel é um termo do Visual FoxPro que corresponde à altura máxima e largura média de um caractere na fonte atual. A altura da linha corresponde à altura máxima de uma letra na fonte atual; a largura da coluna corresponde à largura média de uma letra na fonte atual.

No Visual FoxPro, você pode usar frações decimais para coordenadas de linha e coluna para facilitar o posicionamento preciso de controles e saída. No FoxPro para MS-DOS, porções fracionárias de coordenadas de linha e coluna são ignoradas.

No Visual FoxPro, para determinar ou alterar a fonte da janela principal do Visual FoxPro, pressione SHIFT enquanto exibe o menu Format, depois escolha a opção Screen Font. A fonte de uma janela definida pelo usuário pode ser especificada incluindo a cláusula FONT quando você cria a janela com DEFINE WINDOW.

# Substituição de fonte

Se você especificar uma fonte que não está disponível, o Windows substitui uma fonte com características de fonte semelhantes. O Windows considera o tamanho em pontos, características serif e o pitch da fonte que você solicita. Uma fonte TrueType é tipicamente substituída. Uma fonte raster ou vetorial só é substituída quando as características da fonte que você solicita correspondem de perto às da fonte raster ou vetorial.

# Funções de fonte

Várias funções podem ser usadas para retornar informações sobre fontes e texto em uma fonte específica.

A tabela a seguir descreve essas funções.

| Função | Descrição |
| --- | --- |
| AFONT( ) | Coloca informações sobre fontes disponíveis em um array. |
| FONTMETRIC( ) | Retorna atributos de fonte para fontes instaladas. |
| GETFONT( ) | Exibe a caixa de diálogo Font e retorna o nome da fonte que você escolhe. |
| SYSMETRIC( ) | Retorna o tamanho de um elemento de exibição. |
| SCOLS( ) | Retorna o número de colunas disponíveis na janela principal do Visual FoxPro. Útil ao centralizar texto ou controles na janela principal do Visual FoxPro. |
| SROWS( ) | Retorna o número de linhas disponíveis na janela principal do Visual FoxPro. Útil ao centralizar texto ou controles na janela principal do Visual FoxPro. |
| WCOLS( ) | Retorna o número de colunas dentro da janela especificada. Útil ao centralizar texto ou controles em uma janela definida pelo usuário. |
| WFONT( ) | Retorna o nome, tamanho ou estilo da fonte atual para uma janela. |
| WROWS( ) | Retorna o número de colunas dentro da janela especificada. Útil ao centralizar texto ou controles em uma janela definida pelo usuário. |
