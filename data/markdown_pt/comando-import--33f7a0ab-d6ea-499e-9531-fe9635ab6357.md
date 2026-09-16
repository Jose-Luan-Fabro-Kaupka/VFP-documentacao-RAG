# Comando IMPORT

Importa dados de um formato de arquivo externo para criar uma nova tabela Visual FoxPro.

```foxpro
IMPORT FROM FileName   [DATABASE DatabaseName [NAME LongTableName]]
   [TYPE] FW2 | MOD | PDOX | RPD | WK1    | WK3 | WKS | WR1 | WRK | XLS
    | XL5 [SHEET cSheetName]   | XL8 [SHEET cSheetName]   [AS nCodePage]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo do qual importar dados. Se você não incluir uma extensão com o nome do arquivo, a extensão padrão para o tipo de arquivo especificado é assumida.
**DATABASE DatabaseName**
Especifica um banco de dados ao qual a nova tabela é adicionada.
**NAME LongTableName**
Especifica um nome longo para a nova tabela. Nomes longos podem conter até 128 caracteres e podem ser usados no lugar de nomes de arquivo curtos no banco de dados.
**TYPE**
A palavra-chave TYPE é opcional, mas você deve incluir um dos seguintes tipos de arquivo: Tipo de arquivo Descrição FW2 Inclua FW2 para importar arquivos FW2, criados pelo Framework II. MOD Inclua MOD para importar arquivos MOD, criados pelo Microsoft Multiplan versão 4.1. PDOX Inclua PDOX para importar arquivos Paradox. Arquivos de banco de dados nas versões 3.5 e 4.0 do Paradox da Borland podem ser importados incluindo a opção PDOX. RPD Inclua RPD para importar arquivos RPD, criados pelo RapidFile. WK1 | WK3 | WKS Inclua WK1 para importar dados de uma planilha Lotus 1-2-3. As colunas da planilha tornam-se campos na tabela e as linhas da planilha tornam-se registros na tabela. Uma extensão WK1 é atribuída a planilhas criadas no Lotus 1-2-3 revisão 2.x; uma extensão WK3 é atribuída a planilhas criadas no Lotus 1-2-3 revisão 3.x; e uma extensão .wks é atribuída a planilhas criadas no Lotus 1-2-3 revisão 1-A. WR1 | WRK Inclua WR1 para importar dados de uma planilha Lotus Symphony. As colunas da planilha tornam-se campos na tabela e as linhas da planilha tornam-se registros na tabela. Uma extensão WR1 é atribuída a planilhas criadas no Symphony versão 1.10, e uma extensão .wrk é atribuída a planilhas criadas no Symphony versão 1.1. XLS Inclua XLS para importar dados de planilhas do Microsoft Excel versões 2.0, 3.0 e 4.0. As colunas da planilha tornam-se campos na tabela e as linhas da planilha tornam-se registros na tabela. Arquivos de planilha criados no Microsoft Excel têm extensão .xls. XL5 [SHEET cSheetName ] Inclua XL5 para importar dados do Microsoft Excel versão 5.0. As colunas da planilha tornam-se campos na tabela e as linhas da planilha tornam-se registros na tabela. Arquivos de planilha criados no Microsoft Excel têm extensão .xls. Se você omitir a cláusula SHEET, os dados em Sheet1 são importados. Para importar dados de uma planilha específica, inclua a palavra-chave SHEET e especifique o nome da planilha com cSheetName. XL8 [SHEET cSheetName ] Inclua XL8 para importar dados do Microsoft Excel 97. As colunas da planilha tornam-se campos na tabela e as linhas da planilha tornam-se registros na tabela. Arquivos de planilha criados no Microsoft Excel têm extensão .xls. Se você omitir a cláusula SHEET, os dados em Sheet1 são importados. Para importar dados de uma planilha específica, inclua a palavra-chave SHEET e especifique o nome da planilha com cSheetName.
**AS nCodePage**
Especifica a página de código do arquivo importado. O Visual FoxPro copia o conteúdo do arquivo importado e, ao copiar os dados, converte automaticamente os dados para a página de código atual do Visual FoxPro. Se você especificar um valor para nCodePage que não é suportado, o Visual FoxPro exibe uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para o arquivo importado. Se você omitir AS nCodePage e o Visual FoxPro não puder determinar a página de código do arquivo importado, o Visual FoxPro copia o conteúdo do arquivo importado e, ao copiar os dados, converte automaticamente os dados para a página de código atual do Visual FoxPro. Se você omitir AS nCodePage e o Visual FoxPro puder determinar a página de código do arquivo importado, o Visual FoxPro converte automaticamente os dados no arquivo importado da página de código dos dados para a página de código atual do Visual FoxPro. Use CPCURRENT( ) para determinar a página de código atual do Visual FoxPro. Se nCodePage for 0, o Visual FoxPro assume que a página de código do arquivo importado é a mesma da página de código atual do Visual FoxPro e nenhuma conversão de página de código ocorre.

# Observações

A maioria dos pacotes de software armazena seus dados em formatos de arquivo que não podem ser abertos diretamente no Visual FoxPro. IMPORT cria uma nova tabela Visual FoxPro a partir de dados armazenados em formatos de arquivo que o Visual FoxPro não pode ler diretamente.

Uma nova tabela é criada com o mesmo nome do arquivo do qual os dados são importados. Uma extensão .dbf é atribuída à tabela recém-criada.
