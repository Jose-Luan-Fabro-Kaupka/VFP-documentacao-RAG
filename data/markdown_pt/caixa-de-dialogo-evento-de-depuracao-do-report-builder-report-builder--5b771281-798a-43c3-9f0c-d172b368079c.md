# Caixa de diálogo Evento de depuração do Report Builder (Report Builder)

Trata eventos do Label ou Report Designer com uma caixa de diálogo abrangente que permite explorar o conteúdo do cursor FRX e decidir como definir os sinalizadores de retorno para controlar a resposta do designer.

O formulário Debug Handler exibe o conteúdo do cursor FRX usando o mesmo layout básico da caixa de diálogo FRX Cursor Browser, mas com alguns controles adicionais:
 **Detalhes do evento**
Exibe uma caixa de diálogo MESSAGEBOX() contendo o conteúdo dos parâmetros passados ao Report Builder pelo designer. Consulte Compreendendo eventos do Report Builder para obter mais informações sobre parâmetros do report builder.
**Opções**
Exibe a caixa de diálogo Options do report builder.
**Alterações FRX**
Controla a configuração do Bit 1 do parâmetro ReturnFlags: Save instruirá o designer a recarregar as alterações no cursor FRX no layout do relatório. Discard instruirá o designer a descartar quaisquer alterações.
**Comportamento nativo**
Controla a configuração do Bit 0 do parâmetro ReturnFlags: Allow instruirá o designer a continuar respondendo ao evento como se o Report Builder não estivesse ativo. Suppress instruirá o designer a ignorar o evento.
**Continuar**
Dispensa a caixa de diálogo Debug Handler e retorna o controle ao designer.
