# Comando SET PRINTER

Habilita ou desabilita a saída para a impressora ou direciona a saída para um arquivo, porta ou impressora de rede. Há várias versões da sintaxe.

> **Dica:** Para direcionar a saída para um arquivo, uma porta para uma impressora local diferente ou uma impressora de rede, use SET PRINTER TO com os argumentos especificados. Para redefinir a saída para o utilitário de impressão MS-DOS PRN padrão, use SET PRINTER TO sem argumentos.

```foxpro
SET PRINTER ON [PROMPT] | OFF
```

```foxpro
SET PRINTER FONT cFontName [, nFontSize [, nFontCharSet]] [STYLE cFontStyle]
```

```foxpro
SET PRINTER TO [FileName [ADDITIVE] | PortName]
```

```foxpro
SET PRINTER TO [DEFAULT | NAME WindowsPrinterName]
```

```foxpro
SET PRINTER TO NAME \\ServerName\PrinterName
```

#### Parâmetros
 **ON [PROMPT]**
Habilita a saída para a impressora. PROMPT exibe a caixa de diálogo Print antes de a impressão começar. Na caixa de diálogo Print, você pode ajustar as configurações da impressora. O driver de impressora instalado atualmente determina quais configurações da impressora você pode ajustar. Observação Quando SET PRINTER estiver definido como ON , a saída formatada com o comando @ ... SAY não é direcionada para a impressora. Para direcionar a saída de @ ... SAY para a impressora, use o comando SET DEVICE TO PRINTER. Para obter mais informações, consulte SET DEVICE Command .
**OFF**
Desabilita a saída para a impressora. (Padrão)
**FONT cFontName [, cFontSize [, nFontCharSet ]]**
Especifica uma fonte padrão para a saída da impressora. cFontName especifica o nome da fonte e cFontSize especifica o tamanho em pontos. Você pode especificar um script de idioma com nFontCharSet . Consulte a função GETFONT( ) para obter uma lista dos valores de script de idioma disponíveis. Por exemplo, o comando a seguir especifica a fonte Courier de 16 pontos como fonte padrão da impressora: SET PRINTER FONT 'Courier', 16 Se a fonte que você especificar não estiver disponível, uma fonte com características semelhantes é substituída.
**STYLE cFontStyle**
Especifica um estilo de fonte padrão para a saída da impressora. Se você omitir a cláusula STYLE, o estilo de fonte normal é usado. Se o estilo de fonte que você especificar não estiver disponível, um estilo de fonte com características semelhantes é substituído. A tabela a seguir lista os estilos de fonte que você pode especificar com cFontStyle . cFontStyle Estilo de fonte B Bold I Italic N Normal O Outline Q Opaque S Shadow – Strikeout T Transparent U Underline Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o comando a seguir especifica Courier Bold Italic de 16 pontos: SET PRINTER FONT 'Courier', 16 STYLE 'BI'
**TO [ FileName [ADDITIVE] | PortName ]**
Especifica um arquivo ou porta para o qual a saída é direcionada. FileName especifica um nome de arquivo para o qual a saída é direcionada. ADDITIVE anexa a saída ao conteúdo existente do arquivo. Omitir ADDITIVE sobrescreve o conteúdo existente do arquivo. PortName envia a saída para uma impressora local diferente.
**TO [DEFAULT | NAME WindowsPrinterName ]**
Envia a saída da impressora para a impressora Windows padrão ou para uma impressora Windows específica. Observação Os nomes de impressora Windows são armazenados no arquivo Win.ini.
**TO NAME \\ ServerName \ PrinterName**
Coloca a saída da impressora em spool em uma impressora de rede. Observação Esta cláusula é suportada somente para versões do Visual FoxPro executadas no Windows 2000 ou posterior. ServerName é o nome de rede atribuído ao servidor de impressão. Esse nome é atribuído pelo administrador de rede e deve ser exclusivo. PrinterName é um nome atribuído à impressora pelo administrador de rede.

# Observações

Quando você direciona a saída para uma impressora de rede, a saída é impressa ou coletada em um spooler de impressão até que um novo comando SET PRINTER seja emitido. Para obter informações adicionais sobre impressão na sua rede, consulte a documentação da rede.

> **Observação:** Este comando não funciona no Unattended Server Mode.

Você pode usar as funções GETPRINTER( ) ou APRINTERS( ) para determinar os nomes das impressoras instaladas atualmente. Por exemplo, o comando a seguir exibe a caixa de diálogo Windows Printer e faz com que a impressora que você selecionar seja a impressora para a qual a saída impressa é direcionada:

```foxpro
SET PRINTER TO NAME GETPRINTER()
```

Para obter mais informações, consulte APRINTERS( ) Function e GETPRINTER( ) Function.
