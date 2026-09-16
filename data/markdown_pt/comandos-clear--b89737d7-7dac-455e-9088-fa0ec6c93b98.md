# Comandos CLEAR

Libera o item ou itens especificados da memória.

```foxpro
CLEAR [ALL | CLASS ClassName | CLASSLIB ClassLibraryName | DEBUG | DLLS
   [cAliasNameList]| EVENTS | ERROR |FIELDS | GETS | MACROS | MEMORY
   | MENUS | POPUPS | PROGRAM | PROMPT | READ [ALL] | RESOURCES
   [FileName] | TYPEAHEAD | WINDOWS]
```

#### Parâmetros
 **ALL**
Libera da memória todas as variáveis e matrizes e as definições de todas as barras de menu, menus e janelas definidas pelo usuário. CLEAR ALL também fecha quaisquer tabelas, incluindo todos os arquivos de índice, formato e memo associados, e seleciona a área de trabalho 1. CLEAR ALL também libera da memória todas as funções de biblioteca compartilhada externa registradas com DECLARE - DLL. CLEAR ALL não libera variáveis de sistema e não limpa o buffer de programa compilado. Use CLEAR PROGRAM para limpar o buffer de programa compilado. Emitir CLEAR ALL dentro de um evento ou método para um controle ou objeto ativo gera uma mensagem de erro do Visual FoxPro. Uma variável de tipo objeto não pode ser liberada da memória quando seu controle ou objeto associado está ativo.
**CLASS ClassName**
Limpa uma definição de classe da memória. Quando uma instância de uma classe é criada, o Visual FoxPro mantém a definição da classe na memória após a instância ser liberada. Use CLEAR CLASS para limpar uma definição de classe da memória após sua instância ser liberada.
**CLASSLIB ClassLibraryName**
Limpa da memória todas as definições de classe contidas em uma biblioteca de classes visual. Se instâncias de classes na biblioteca de classes existirem, as definições de classe não são limpas da memória. No entanto, todas as definições de classe que não têm instâncias são limpas da memória.
**DEBUG**
Limpa todos os pontos de interrupção no Debugger e restaura as janelas do Debugger (Call Stack, Trace, Watch, etc.) às suas posições padrão. Se Clear Debug for emitido quando o Debugger estiver fechado, o Debugger é aberto com as janelas do Debugger em suas posições padrão. Funciona no modo fox ou debugger frame.
**DLLS cAliasNameList**
Limpa da memória bibliotecas compartilhadas externas registradas com DECLARE - DLL. cAliasNameList é uma lista separada por vírgulas de aliases de função a serem removidos da memória, como no exemplo a seguir: CLEAR DLLS "RegCloseKey","RegOpenKey" Se você não usou alias na declaração, cAliasNameList é o mesmo que o nome da função. Se você não especificar cAliasNameList , todas as DLLS são removidas da memória. Você pode usar a função ADLLS( ) para determinar quais DLLs estão carregadas. Consulte DECLARE - DLL Command para obter mais informações sobre o registro de funções de biblioteca compartilhada externa.
**ERROR**
Redefine as estruturas de erro do Visual FoxPro como se nenhum erro tivesse ocorrido. As seguintes funções são redefinidas para seus valores padrão: AERROR( ) Function (redefinida para zero). ERROR( ) Function (redefinida para zero). MESSAGE( ) Function (redefinida para a cadeia de caracteres vazia). MESSAGE( ) Function (redefinida para a cadeia de caracteres vazia). SYS(2018) - Error Message Parameter (redefinido para a cadeia de caracteres vazia). Evite usar CLEAR ERROR dentro de um comando TRY...CATCH...FINALLY Command , particularmente se você está usando TRY...CATCH...FINALLY Command para relançar um erro. O objeto Exception pode não ser mais válido.
**EVENTS**
Interrompe o processamento de eventos iniciado com READ EVENTS. Quando CLEAR EVENTS é executado, a execução do programa continua na linha do programa imediatamente após READ EVENTS.
**FIELDS**
Libera uma lista criada com SET FIELDS e executa SET FIELDS OFF. CLEAR FIELDS difere de SET FIELDS TO porque libera todas as listas de campos para todas as áreas de trabalho, não apenas a lista de campos da área de trabalho atual. Além disso, SET FIELDS TO não emite implicitamente SET FIELDS OFF.
**GETS**
Libera todos os controles @ ... GET pendentes. Emitir CLEAR também libera todos os controles @ ... GET pendentes. Observação GETS está incluído para compatibilidade com versões anteriores.
**MACROS**
Libera da memória todas as macros de teclado, incluindo quaisquer atribuições de tecla SET FUNCTION. As macros podem ser salvas em um arquivo de macro ou em um campo memo com SAVE MACROS e restauradas depois com RESTORE MACROS. Você também pode restaurar as macros padrão com RESTORE MACROS.
**MEMORY**
Libera da memória todas as variáveis de memória públicas e privadas e matrizes. Variáveis de sistema não são liberadas.
**MENUS**
Libera todas as definições de barra de menu da memória.
**POPUPS**
Libera da memória todas as definições de menu criadas com DEFINE POPUP.
**PROGRAM**
Limpa o buffer de programa compilado. O Visual FoxPro mantém um buffer dos programas executados mais recentemente. Em casos raros, o Visual FoxPro pode não reconhecer alterações feitas em arquivos de programa no disco. CLEAR PROGRAM força o Visual FoxPro a ler os programas do disco, em vez do buffer de programa. O motivo mais comum para o Visual FoxPro não reconhecer alterações feitas em arquivos de programa é o uso de um editor externo ou terminate-and-stay-resident (TSR) para modificar um arquivo de programa. Com esta exceção, você não deve precisar usar CLEAR PROGRAM.
**PROMPT**
Libera itens de menu criados com @ ... PROMPT.
**READ [ALL]**
Incluído para compatibilidade com versões anteriores. Use CLEAR EVENTS em vez disso.
**RESOURCES [ FileName ]**
Especifica o nome de um arquivo de bitmap, imagem, fonte, cursor ou ícone em cache a ser limpo da memória. Se nenhum nome de arquivo for especificado, todos os arquivos de bitmap, imagem, fonte, cursor e ícone são removidos da memória. Quando o Visual FoxPro exibe um recurso de bitmap, imagem, cursor, ícone ou fonte, o recurso é armazenado em cache para otimizar o desempenho. Se um recurso com o mesmo nome é usado (por exemplo, um bitmap diferente com o mesmo nome de um já em cache), o Visual FoxPro não recarrega o recurso. Limpar um arquivo de recurso é portanto particularmente útil para remover uma imagem gráfica da memória e forçar o Visual FoxPro a recarregar uma imagem com o mesmo nome do disco. Por exemplo, um relatório pode exibir imagens gráficas de um banco de dados, todas nomeadas TEMP; no entanto, como todas têm o mesmo nome, o Visual FoxPro não recarregará cada nova imagem gráfica a menos que a existente tenha sido limpa da memória usando o comando CLEAR RESOURCES. Se um recurso específico ainda estiver em uso pelo Visual FoxPro, ele pode não ser possível limpá-lo usando o comando CLEAR RESOURCES.
**TYPEAHEAD**
Limpa o buffer de digitação antecipada do teclado. CLEAR TYPEAHEAD é útil quando você deseja impedir entrada em um campo ou impedir uma resposta a um prompt antes que o campo ou prompt seja exibido.
**WINDOWS**
Libera da memória todas as definições de janela definidas pelo usuário e limpa as janelas da janela principal do Visual FoxPro ou da janela definida pelo usuário ativa. Use SAVE WINDOW para salvar definições de janela em um arquivo ou campo memo para uso posterior. Emitir CLEAR WINDOWS libera quaisquer referências de variável de sistema a formulários. Por exemplo, os seguintes comandos criam uma referência de variável de sistema para um formulário e depois exibem informações sobre a variável: goMyForm = CREATEOBJECT('FORM') DISPLAY MEMORY LIKE goMyForm && Displays GOMYFORM O FORM Emitir CLEAR WINDOWS libera a referência de variável de sistema e a variável agora contém o valor nulo: CLEAR WINDOWS DISPLAY MEMORY LIKE goMyForm && Displays GOMYFORM O .NULL.

# Observações

CLEAR apaga a janela principal do Visual FoxPro ou a janela definida pelo usuário atual e libera da memória todos os controles @ ... GET pendentes. Você pode incluir CLEAR em arquivos de formato.
