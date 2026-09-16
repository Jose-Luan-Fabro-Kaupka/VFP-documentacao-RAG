# Guia Optional Bands, caixa de diálogo Report Properties (Report Builder)

Permite incluir bandas Title, Summary ou Detail adicionais no layout de página do relatório ou etiqueta e especificar configurações para elas.

Esta guia é pré-selecionada quando você escolhe Optional Bands no menu Report ou no menu de contexto do layout do relatório.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa Optional Bands do Visual FoxPro quando o Report Builder está ativo.
 - Como: adicionar bandas a relatórios
- Como: alterar a ordem das bandas Detail
- Como: configurar saída para bandas de relatório
- Como: excluir bandas de relatórios

# Title

Contém opções para a banda Title.
 **Report has title band**
Especifica se o layout inclui uma banda Title para exibir informações uma vez no início do relatório.
**New page after title has printed**
Especifica que uma quebra de página será enviada à impressora após as informações da banda Title serem renderizadas. Disponível apenas quando a caixa de seleção Report has title band está selecionada.

# Summary

Contém opções para a banda Summary.
 **Report has summary band**
Especifica se o layout inclui uma banda Summary para exibir informações uma vez no final do relatório.
**Summary prints as new page**
Especifica que uma quebra de página será enviada à impressora antes das informações da banda Summary serem renderizadas. Disponível apenas quando a caixa de seleção Report has summary band está selecionada.
**Include page header with summary**
Especifica que as informações da banda Page Header serão renderizadas na página separada junto com as informações da banda Summary.
**Include page footer with summary**
Especifica que as informações da banda Page Footer serão renderizadas na página separada junto com as informações da banda Summary.

# Detail bands

Contém opções para bandas Detail no layout. A caixa de lista mostra as bandas Detail no layout de página e permite alterar sua ordem, adicioná-las ou removê-las.
 **Detail Bands List**
Permite alterar a ordem das bandas Detail.
**Add**
Adiciona uma nova banda Detail ao layout de página. Você pode incluir no máximo 20 bandas detail separadas no layout.
**Remove**
Remove a banda Detail selecionada do layout de página. Você não poderá excluir a primeira banda na lista. O layout deve conter pelo menos uma banda Detail.
