# Controles e objetos criados em versões anteriores

Este tópico descreve o suporte a controles e objetos criados em versões anteriores do FoxPro. Alguns controles se comportam de forma ligeiramente diferente conforme você use o Visual FoxPro para Windows ou para Macintosh; por padrão, os controles no Visual FoxPro para Macintosh seguem as convenções de interface do usuário comuns aos aplicativos Macintosh. Por exemplo, por padrão, os controles CheckBox, ComboBox e OptionButton não podem receber o foco no Visual FoxPro para Macintosh. Para obter mais detalhes sobre diferenças no comportamento dos controles, consulte o tópico do comando SET KEYCOMP.

No Visual FoxPro, uma cláusula NAME está disponível para cada um dos controles criados em versões anteriores do FoxPro. A cláusula NAME cria uma referência de objeto para controles criados com @ ... GET e @ ... EDIT e permite manipulá-los com propriedades, eventos e métodos do Visual FoxPro. A cláusula NAME fornece uma etapa intermediária para atualizar seus aplicativos usando técnicas de programação orientada a objetos do Visual FoxPro.

# Compatibilidade com controles do FoxPro 2.x

A tabela a seguir lista os controles disponíveis em versões anteriores do FoxPro e a classe base que você pode usar para criar programaticamente o mesmo controle no Visual FoxPro.

| Controles do FoxPro 2.x | Controles equivalentes do Visual FoxPro | Nomes de classes base do Visual FoxPro |
| --- | --- | --- |
| @ ... GET - Caixas de seleção | Controle CheckBox | CheckBox |
| @ ... GET - Listas | Controle ListBox | ListBox |
| @ ... GET - Pop-ups | Controle ComboBox | ComboBox |
| @ ... GET - Botões de comando | Controle CommandButton | CommandButton |
| @ ... GET - Botões de opção | Controle OptionButton | OptionButton |
| @ ... GET - Seletores numéricos | Controle Spinner | Spinner |
| @ ... GET - Caixas de texto | Controle TextBox | TextBox |
| @ ... EDIT - Regiões de edição de texto | Controle EditBox | EditBox |

Para obter uma lista completa das classes base no Visual FoxPro, consulte Classes base no Visual FoxPro.
