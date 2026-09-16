# Caixa de diálogo Import

Permite importar dados para uma tabela do Visual FoxPro a partir de uma planilha ou de outro formato de tabela. Você também pode usar o Import Wizard para importar arquivos.

> **Observação:** Não é possível importar arquivos de texto com este comando de menu. Para isso, use o Import Wizard ou crie uma tabela e acrescente o arquivo de texto à nova tabela.

Esta caixa de diálogo é exibida quando você seleciona Import no menu File.
 **Type**
Especifica o tipo de arquivo a importar. Selecione um tipo na lista.
**From**
Especifica o caminho e o nome do arquivo de origem. Digite-os ou clique no botão de diálogo para localizar o arquivo.
**Sheet**
Especifica uma planilha do Microsoft Excel a importar. Esta caixa aparece somente se Microsoft Excel estiver selecionado em Type.
**To**
Exibe o caminho, conforme definido na guia File Locations da caixa de diálogo Options, e o nome do arquivo importado. O nome é o mesmo do arquivo de origem, mas com extensão .dbf.
**Import Wizard**
Inicia o Import Wizard, que apresenta perguntas simples em uma breve série de etapas. É necessário usá-lo para importar arquivos de texto, ou criar uma tabela e então acrescentar o arquivo de texto à nova tabela.

A tabela a seguir mostra os tipos de arquivo que podem ser importados com este comando e os equivalentes a digitar na janela Command.

| Tipos de arquivo | Comando equivalente |
| --- | --- |
| FrameWork II (FW2) | IMPORT FROM FileName TYPE FW2 |
| Lotus 1-2-3 1-A (WKS) | IMPORT FROM FileName TYPE WKS |
| Lotus 1-2-3 2. x (WK1) | IMPORT FROM FileName TYPE WK1 |
| Lotus 1-2-3 3. x (WK3) | IMPORT FROM FileName TYPE WK3 |
| Microsoft Excel 2.0, 3.0 e 4.0 (XLS) | IMPORT FROM FileName TYPE XLS |
| MultiPlan 4.01 (MOD) | IMPORT FROM FileName TYPE MOD |
| Paradox 3.5, 4.0, 4.5 (DB) | IMPORT FROM FileName TYPE PDOX |
| RapidFile (RPD) | IMPORT FROM FileName TYPE RPD |
| Symphony 1.01 (WRK) | IMPORT FROM FileName TYPE WRK |
| Symphony 1.10 (WR1) | IMPORT FROM FileName TYPE WR1 |
