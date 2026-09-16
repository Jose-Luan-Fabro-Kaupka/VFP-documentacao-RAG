# Como: configurar o tratamento de eventos do Report Builder

O Report Builder pode ser configurado para responder a eventos no Report Designer de várias maneiras diferentes. Ele pode:
 - Usar uma tabela de consulta que mapeia eventos do Report Designer com classes de manipulador específicas. Este é o modo de manipulação padrão.
- Usar uma classe de manipulador de "debug" para todos os eventos.
- Notificá-lo de cada evento conforme ocorre com um alerta MESSAGEBOX() contendo informações sobre os parâmetros que seriam passados ao builder. O Report Designer então processa o evento como se o builder não estivesse ativo.
- Ignorar os eventos completamente.

Essa configuração é ajustada na caixa de diálogo Options do Report Builder ou usando os parâmetros de linha de comando do Report Builder.

> **Importante:** Diferentemente das configurações na caixa de diálogo Options do Visual FoxPro (Visual FoxPro), essa preferência não persiste entre sessões do Visual FoxPro.

# Definir o modo de tratamento de eventos do builder usando a caixa de diálogo Options

Consulte Como: exibir a caixa de diálogo Report Builder Options para obter etapas detalhadas sobre como exibir essa caixa de diálogo.

### Para usar a tabela de consulta de manipuladores de eventos (padrão)
- Abra a caixa de diálogo Report Builder Options.
- Defina a opção de tratamento de eventos do Report Designer como Search for a handler class in the handler registry table.
- Selecione Close para fechar a caixa de diálogo.

Para obter mais informações, consulte Como: especificar uma tabela alternativa de manipuladores de eventos de relatório.

### Para usar a classe de manipulador de eventos Debug
- Abra a caixa de diálogo Report Builder Options.
- Defina a opção de tratamento de eventos do Report Designer como Use the debug handler for all events.
- Selecione Close para fechar a caixa de diálogo.

Consulte Report Builder Debug Event Dialog Box (Report Builder) para obter mais informações.

### Para sinalizar cada evento com um alerta MESSAGEBOX()
- Abra a caixa de diálogo Report Builder Options.
- Defina a opção de tratamento de eventos do Report Designer como Use the event inspector for all events.
- Selecione Close para fechar a caixa de diálogo.

Nesse modo, o report builder alerta sobre a ocorrência do evento, mas não trata o evento, devolvendo-o ao Report Designer para tratamento normal.

### Para ignorar todos os eventos do report builder
- Abra a caixa de diálogo Report Builder Options.
- Defina a opção de tratamento de eventos do Report Designer como Ignore builder events completely.
- Selecione Close para fechar a caixa de diálogo.

O Report ou Label Designer responderá ao evento normalmente como se _REPORTBUILDER estivesse vazio. Consulte a variável de sistema _REPORTBUILDER para obter mais informações.

# Definir o modo de tratamento de eventos do builder usando a linha de comando

O Report Builder também expõe essa configuração por meio de um parâmetro de linha de comando:

### Para definir o modo de manipulação de eventos na Janela de Comando
- Digite o seguinte comando: DO (_REPORTBUILDER) WITH 4, iHandleMode - OU - DO (HOME()+"reportbuilder.app") WITH 4, iHandleMode

O iHandleMode deve ser um inteiro de 1 a 4, representando os quatro modos possíveis de tratamento de eventos descritos acima.
