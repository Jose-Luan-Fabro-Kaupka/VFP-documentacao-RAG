# Exemplo Set VFP Shell Open Commands

Arquivo: ...\Samples\Solution\Winapi\Shellopen.scx

Este exemplo é um utilitário que você pode usar para alterar as configurações Shell Open de vários tipos de arquivo (extensões) e usa a Registry Access Foundation Class. As configurações Shell Open controlam como um arquivo é aberto quando você clica duas vezes no arquivo no Windows Explorer.

Antes do Visual FoxPro 7.0, o Visual FoxPro abria um arquivo em uma instância em execução do Visual FoxPro. A partir do Visual FoxPro 7.0, o Visual FoxPro abre esse arquivo em uma nova instância do Visual FoxPro. Este exemplo permite que você controle como deseja que os arquivos sejam abertos em nível de tipo de arquivo.
 Este exemplo contém as seguintes classes
| Classe | Biblioteca | Descrição |
| --- | --- | --- |
| registry | registry.vcx | Contém rotinas para acessar o Registro do Windows. |
