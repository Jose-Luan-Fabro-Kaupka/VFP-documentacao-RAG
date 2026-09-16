# Caixa de diálogo Export

Permite exportar dados de tabelas do Visual FoxPro para um arquivo de texto, planilha ou formato de tabela comum.

Esta caixa de diálogo aparece quando você seleciona Export no menu File.
 **Type**
Especifica o tipo de arquivo a exportar. Selecione um tipo de arquivo na lista.
**To**
Especifica o caminho e o nome do arquivo de destino. Digite o caminho e o nome ou clique no botão de diálogo para localizar o arquivo de destino.
**Text delimiter**
Permite delimitar cadeias de caracteres de texto no arquivo de saída. O delimitador de texto padrão é o caractere de aspas duplas ("). Esta opção aparece somente se você escolher Delimited Text na lista suspensa Type.
**Field separator**
Torna possível separar campos de dados no arquivo de saída. O separador de campo padrão é o caractere vírgula (,). Esta opção aparece somente se você escolher Delimited Text na lista suspensa Type.
**From**
Especifica o caminho e o nome do arquivo de origem. Digite o caminho e o nome ou clique no botão de diálogo para localizar o arquivo de origem.
**Options**
Exibe a caixa de diálogo Export Options, onde você especifica quais registros e campos exportar.

A tabela a seguir mostra os tipos de arquivo que você pode exportar com este comando e seus equivalentes que você digitaria na janela Command.

| Tipos de arquivo | Equivalente de comando |
| --- | --- |
| Data Interchange Format (DIF) | COPY TO FileName TYPE DIF |
| DBASE IV (DBF) | COPY TO FileName FOX2X |
| Delimited Text | COPY TO FileName TYPE DELIMITED |
| FoxBASE+ (DBF) | COPY TO FileName FOXPLUS |
| FoxPro for Windows 2.x (DBF) | COPY TO FileName FOX2X |
| Lotus 1-2-3 1-A (WKS) | COPY TO FileName TYPE WKS |
| Lotus 1-2-3 2. x (WK1) | COPY TO FileName TYPE WK1 |
| Microsoft Excel 2.0, 3.0, and 4.0 (XLS) | COPY TO FileName TYPE XLS |
| MultiPlan 4.01 (MOD) | COPY TO FileName TYPE MOD |
| Symbolic Link Format | COPY TO FileName TYPE SYLK |
| Symphony 1.01 (WRK) | COPY TO FileName TYPE WRK |
| Symphony 1.10 (WR1) | COPY TO FileName TYPE WR1 |
| System Data Format (SDF) | COPY TO FileName TYPE SDF |
| Visual FoxPro (DBF) | COPY TO FileName |
