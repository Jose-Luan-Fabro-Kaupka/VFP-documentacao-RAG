# Comando DIR ou DIRECTORY

Exibe informações sobre os arquivos em um diretório.

```foxpro
DIR | DIRECTORY [ON Drive] [[LIKE] [Path] [FileSkeleton]]
   [TO PRINTER [PROMPT] | TO FILE FileName]
```

#### Parâmetros
 **ON Drive**
Especifica o nome da unidade em que o diretório está localizado.
**[[LIKE] [ Path ] [ FileSkeleton ]]**
Especifica o caminho para o diretório que contém os arquivos. O caminho pode incluir o nome da unidade se você omitir ON Drive . Inclua FileSkeleton para exibir informações sobre tipos de arquivo diferentes de tabelas. FileSkeleton é um esqueleto de especificação de arquivo que suporta curingas. Por exemplo, para listar todos os arquivos de programa no diretório atual, execute o comando a seguir: DIR *.PRG No Visual FoxPro, você pode executar o comando a seguir para listar todos os arquivos sem extensões: DIR *.
**TO PRINTER [PROMPT]**
Direciona a saída de DIRECTORY para uma impressora. No Microsoft Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo de impressão antes do início da impressão. Nesta caixa de diálogo você pode ajustar as configurações da impressora, incluindo o número de cópias e as páginas a imprimir. As configurações da impressora que você pode ajustar dependem do driver de impressora instalado atualmente. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DIRECTORY para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, você será perguntado se deseja sobrescrever o arquivo.

# Observações

Use DIR para exibir informações sobre arquivos.

DIR sem a cláusula LIKE ou um esqueleto exibe o seguinte:
 - Nomes de todas as tabelas no diretório.
- Número de registros em cada tabela.
- Data em que cada tabela foi atualizada pela última vez.
- Tamanho de cada tabela em bytes (tabelas no formato original Microsoft FoxBASE são indicadas como tal).
- Se cada tabela faz parte de um banco de dados.
- O tamanho total em bytes que as tabelas ocupam no disco (não incluindo arquivos de memo .fpt associados).
- Número de tabelas exibidas.
- Número total de bytes restantes no disco.

As informações da tabela para a unidade e diretório padrão são exibidas, salvo especificação contrária com Drive ou Path ou ambos.

# Exemplo

```foxpro
CLEAR
DIR  && Display tables in the current directory
DIR *.CDX && Display index files in the current directory
DIR A*.DBF  && Display tables that begin with A
DIR *.*  && Display all files, including those without extensions
```
