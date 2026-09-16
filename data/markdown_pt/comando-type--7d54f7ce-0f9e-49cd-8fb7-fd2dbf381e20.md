# Comando TYPE

Exibe o conteúdo de um arquivo.

```foxpro
TYPE FileName1   [AUTO]   [WRAP]
   [TO PRINTER [PROMPT] | TO FILE FileName2]   [NUMBER]
```

#### Parâmetros
 **FileName1**
Especifica o nome do arquivo a exibir. O nome deve incluir uma extensão de arquivo.
**AUTO**
Ativa a indentação automática. Quando você também inclui WRAP, TYPE indenta automaticamente o texto com quebra de linha em cada parágrafo na mesma quantidade em que indenta a primeira linha do parágrafo. Por exemplo: Linhas com quebra de linha são alinhadas com a tabulação quando um parágrafo começa com uma tabulação. Linhas com quebra de linha são alinhadas com a tabulação quando um parágrafo começa com um número (ou outro texto) seguido de uma tabulação e texto. Linhas com quebra de linha são indentadas na mesma quantidade que a primeira linha quando a primeira linha de um parágrafo é indentada com espaços.
**WRAP**
Habilita a quebra de palavras para que uma palavra muito longa para caber no final de uma linha seja movida automaticamente para a próxima linha.
**TO PRINTER [PROMPT]**
Direciona a saída para a impressora. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo de impressão antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName2**
Direciona a saída para o arquivo especificado com FileName2.
**NUMBER**
Coloca números de linha no início de cada linha na saída.

# Observações

TYPE exibe o conteúdo de arquivos. Esta exibição pode ser direcionada para a janela principal do Visual FoxPro, a janela definida pelo usuário ativa, uma impressora ou outro arquivo.

Quando SET HEADINGS está ON, o Visual FoxPro insere uma quebra de página, o caminho e o nome do arquivo e a data no início da saída produzida com TYPE. Se SET HEADINGS estiver OFF, essas informações não são incluídas.

No FoxPro para MS-DOS, se uma configuração de driver de impressora estiver carregada e você direcionar a saída de TYPE para um arquivo ou impressora, TYPE exibe o conteúdo do arquivo usando as configurações da configuração do driver de impressora.
