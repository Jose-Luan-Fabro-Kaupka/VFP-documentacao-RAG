# Função AGETFILEVERSION( )

Cria um array contendo informações sobre arquivos com recursos de versão do Windows, como arquivos .exe, .dll e .fll, ou servidores de automation criados no Visual FoxPro.

> **Observação:** Para que um servidor de automation do Visual FoxPro tenha recursos de versão do Windows, você deve especificar um valor para pelo menos um item na caixa de diálogo Versão EXE. Para obter mais informações, consulte Caixa de diálogo Versão EXE .

```foxpro
AGETFILEVERSION(ArrayName, cFileName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array no qual as informações do arquivo são colocadas. Se o array que você especifica não existir, o Visual FoxPro cria automaticamente o array. Se o array existir e não for grande o suficiente para conter as informações do arquivo, o Visual FoxPro aumenta automaticamente o tamanho do array. Se o array for maior que o necessário, o Visual FoxPro trunca o array. A tabela a seguir lista o conteúdo de cada elemento do array. Elemento Conteúdo 1 Comentários 2 Nome da empresa 3 Descrição do arquivo 4 Versão do arquivo 5 Nome interno 6 Copyright legal 7 Marcas registradas legais 8 Nome original do arquivo 9 Compilação privada 10 Nome do produto 11 Versão do produto O formato deste valor depende da versão do Visual FoxPro. Para detalhes, consulte a função VERSION( ) . 12 Compilação especial 13 Auto-registro OLE (contém "OLESelfRegister" se o arquivo suporta auto-registro; caso contrário, contém a cadeia de caracteres vazia) 14 Idioma (derivado do Código de tradução) 15 Código de tradução Por exemplo, você pode usar o código a seguir para determinar o Locale ID para o arquivo executável do Visual FoxPro: DIMENSION aFiles[1] AGETFILEVERSION(aFiles,"VFP9.EXE") ? EVAL("0x"+LEFT(aFiles[15],4)) ** Retorna 1033 para a versão dos EUA
**cFileName**
Especifica o nome e, opcionalmente, o caminho do arquivo de destino.

# Valor de retorno

Numérico. AGETFILEVERSION( ) retorna o número de elementos no array. Se o arquivo que você especifica não existir ou não contiver recursos de versão do Windows, AGETFILEVERSION( ) retorna zero, e o array, se já criado, permanece inalterado.

# Observações

AGETFILEVERSION( ) pode ser abreviado para um número mínimo de 5 caracteres.
