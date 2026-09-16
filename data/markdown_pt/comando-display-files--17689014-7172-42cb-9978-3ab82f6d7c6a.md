# Comando DISPLAY FILES

Exibe informações sobre arquivos.

```foxpro
DISPLAY FILES [ON Drive] [LIKE FileSkeleton]
   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]
```

#### Parâmetros
 **ON Drive**
Especifica a unidade ou volume em que os arquivos residem.
**LIKE FileSkeleton**
Especifica uma condição pela qual o Visual FoxPro exibe informações somente sobre arquivos que correspondem ao padrão esqueleto FileSkeleton. O padrão esqueleto pode conter curingas como ? e *.
**TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY FILES para uma impressora. No Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo antes de iniciar a impressão. Nesta caixa de diálogo, você pode ajustar as configurações da impressora, incluindo o número de cópias e os números de página a imprimir. As configurações da impressora que você pode ajustar dependem do driver de impressora atualmente instalado. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY FILES para o arquivo especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, você será perguntado se deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.

# Observações

Use DISPLAY FILES para exibir informações sobre arquivos residentes em um disco. Você pode exibir informações sobre todos os arquivos em uma unidade, volume, diretório ou pasta especificada, ou somente arquivos que correspondam a um padrão esqueleto contendo curingas como ? e *.

Emitir DISPLAY FILES sem argumentos exibe informações sobre tabelas no diretório atual. As informações exibidas incluem o seguinte:
 - Nome da tabela.
- Número de registros na tabela.
- Data e hora da última atualização da tabela.
- O tamanho de cada tabela em bytes.
- Se cada tabela faz parte de um banco de dados.

# Exemplo

O exemplo a seguir exibe os nomes dos bancos de dados no diretório ...\Samples\Data.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CLEAR
DISPLAY FILES LIKE *.DBC
```
