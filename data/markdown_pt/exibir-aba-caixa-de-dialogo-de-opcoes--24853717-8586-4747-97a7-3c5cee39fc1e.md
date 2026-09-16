# Exibir aba, caixa de diálogo de opções

Contém opções para controlar a exibição de recursos Visual FoxPro.

Quando você escolhe Definir como Padrão, que aparece em cada aba na caixa de diálogo, Visual FoxPro salva todas as opções em todas as abas.

Mostrar
** Barra de estado**
Especifica se Visual FoxPro exibe a barra de estado na parte inferior da janela principal. Corresponde ao SET STATUS BAR Comando.
** Clock **
Indica se o relógio do sistema aparece na barra de estado. Você deve escolher a opção StatusBar para que esta opção tenha efeito. Corresponde ao SET CLOCK Comando.
** Resultados do Comando **
Specifies that Visual FoxPro displays the results of certain commands including APPEND FROM, AVERAGE, CALCULATE, COUNT, INDEX, SUM, and TOTAL, in the main Visual FoxPro window, the system message window, the graphical status bar, or a user-defined window. Corresponds to the SET TALK Command .
** Mensagens do sistema **
Especifica que Visual FoxPro exibe certas mensagens do sistema na barra de status. Esta opção corresponde ao SET NOTIFY Comando.
** Abrir o último projeto na inicialização**
Abra o projeto mais recentemente usado ao iniciar Visual FoxPro. Esta opção não está disponível se existir alguma das seguintes condições: A configuração do Ficheiro de Recursos na página Localização do Ficheiro na janela Opções está vazia. Para obter mais informações, consulte Arquivo Localidades Página, Opções Caixa de diálogo . O comando SET RESOURCE é definido como OFF . Para mais informações, ver SET RESOURCE Comando. Em um computador executando Windows XP ou 2000, a política de sistemas para não manter um histórico de arquivos recentemente abertos foi definida.
** Lista mais recente usada contém **
Makes it possible for you to specify the number of files displayed in the most recently used (MRU) list. The default setting is 4. This option is unavailable if any of the following conditions exist: The Resource File setting on the File Locations tab in the Options dialog box is empty. For more information, see File Locations Tab, Options Dialog Box . The SET RESOURCE command is set to OFF . For more information, see SET RESOURCE Command . On a computer running Windows XP or 2000, the systems policy for not keeping a history of recently opened files has been set.
**Lista de contagem de exibição**
Especifica o número máximo de itens a serem exibidos inicialmente nas caixas da lista do IntelliSense. O valor padrão é 15. O valor mínimo é 5.

Veja também
- Options Dialog Box (Visual FoxPro)
- Visual FoxPro Environment Settings
