# Vinculando bibliotecas de tipos

O Visual FoxPro oferece suporte a propriedades, eventos e métodos intrínsecos (do Visual FoxPro) em uma biblioteca de tipos de servidor Automation. Somente propriedades cuja visibilidade está definida como PUBLIC são incluídas na biblioteca de tipos.

Tanto propriedades personalizadas definidas pelo usuário quanto métodos definidos pelo usuário aparecem nas bibliotecas de tipos do Visual FoxPro, desde que estejam marcados como PUBLIC. Para métodos, o Visual FoxPro também inclui um tipo de valor de retorno (variant) e uma lista de parâmetros (variants) analisados da definição original do método. Descrições de propriedades de arquivos de classe .vcx também aparecerão na biblioteca de tipos.

Bibliotecas de tipos geradas pelo processo Build são armazenadas em arquivos .tlb criados junto com o servidor .dll ou .exe. As bibliotecas de tipos também são incluídas no arquivo .dll ou .exe como um recurso vinculado. Isso elimina a necessidade de enviar o arquivo .tlb extra, embora ele ainda seja criado, junto com o arquivo .vbr, para uso com implantação remota.

> **Observação:** O método Release do Visual FoxPro não é incluído na biblioteca de tipos porque ele já existe como um método COM.
