# Comando SET EVENTTRACKING

Ativa ou desativa o rastreamento de eventos ou especifica um arquivo de texto para o qual as informações de rastreamento de eventos são direcionadas.

```foxpro
SET EVENTTRACKING ON | OFF | PROMPT | TO [FileName [ADDITIVE]]
```

#### Parâmetros
 **ON**
Ativa o rastreamento de eventos e direciona as informações de rastreamento de eventos para o arquivo de texto especificado com FileName .
**OFF**
Desativa o rastreamento de eventos e interrompe o direcionamento das informações de rastreamento de eventos para o arquivo de texto.
**PROMPT**
Exibe a caixa de diálogo Event Tracking, permitindo que o usuário especifique quais eventos são rastreados.
**TO FileName**
Especifica o nome de um arquivo de texto para o qual as informações de rastreamento de eventos são direcionadas. SET EVENTTRACKING deve estar ON para direcionar informações de rastreamento de eventos para um arquivo de texto. Emita SET EVENTTRACKING TO sem um nome de arquivo para fechar o arquivo de texto. Se o arquivo que você especificar não existir, o Microsoft Visual FoxPro cria e abre automaticamente.
**ADDITIVE**
Anexa as informações de rastreamento de eventos ao final do arquivo de texto especificado com FileName . Se você omitir ADDITIVE, as informações de rastreamento de eventos substituem o conteúdo do arquivo de texto.

# Observações

Use o comando SET EVENTLIST Command ou a caixa de diálogo Event Tracking Dialog Box para especificar os eventos que são rastreados.

A partir do Visual FoxPro 7, o formato do log de eventos difere das versões anteriores. O novo formato adiciona um carimbo de data/hora (para permitir profiling) às informações de evento já exibidas em cada linha.
