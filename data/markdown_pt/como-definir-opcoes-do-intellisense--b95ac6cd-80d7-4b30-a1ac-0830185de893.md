# Como: definir opções do IntelliSense

Você pode definir opções do IntelliSense que afetam sua disponibilidade e aparência conforme descrito nas seções a seguir:
 - Definindo níveis de disponibilidade para Quick Info e List Members
- Especificando o número de arquivos na lista Most Recently Used (MRU)
- Definindo o número de itens a exibir nas caixas de listagem do IntelliSense

Para personalizar a funcionalidade do IntelliSense para elementos de linguagem do Visual FoxPro e definidos pelo usuário, incluindo comandos e funções que exibem listas semelhantes ao IntelliSense, como comandos SET, modifique os registros na tabela IntelliSense. Para obter mais informações, consulte Customizing IntelliSense in Visual FoxPro.

# Definindo níveis de disponibilidade para Quick Info e List Members

Você pode alterar o nível de disponibilidade para Quick Info e List Members para Auto, Manual ou Disabled. Definir estas opções permite ativar ou desabilitar Quick Info e List Members das seguintes maneiras:
 - Quando definido como Automatic (padrão), Quick Info ou List Members aparece onde apropriado quando a tecla ativadora correspondente é pressionada. Para obter mais informações sobre o uso de teclas ativadoras, consulte How to: View IntelliSense When Writing Code .
- Quando definido como Manual, Quick Info ou List Members está disponível quando você escolhe Quick Info ou List Members, respectivamente, no menu Edit, um menu de atalho ou pressionando o atalho de teclado apropriado quando o cursor está posicionado em um local onde Quick Info ou List Members está disponível.
- Quando definido como Disabled, Quick Info ou List Members não está disponível e não aparece. Observação Para comandos, informações de sintaxe que aparecem em janelas Tip aparecem automaticamente, a menos que Quick Info e List Members estejam definidos como Disabled.

Para obter mais informações, consulte Visual FoxPro IntelliSense Manager Window.

### Para definir disponibilidade para Quick Info e List Members
- No menu Tools, clique em IntelliSense Manager .
- Na caixa de diálogo IntelliSense Manager, clique na guia General.
- Para tornar opções disponíveis para Quick Info ou List Members, certifique-se de que a caixa de seleção Enable IntelliSense está selecionada. Se a caixa de seleção Enable IntelliSense estiver desmarcada, Quick Info e List Members estão ambos desabilitados.
- Selecione as opções desejadas nas caixas de listagem List members ou Quick info tips .
- Quando terminar, clique em OK .

Você também pode ativar ou desabilitar List Members e Quick Info programaticamente definindo as opções apropriadas na propriedade EditorOptions usando a variável de sistema _VFP. Para obter mais informações, consulte EditorOptions Property.

# Especificando o número de arquivos na lista Most Recently Used (MRU)

Você pode especificar o número de arquivos exibidos na lista MRU usando a caixa de diálogo Options.

### Para especificar o número de arquivos na lista MRU
- No menu Tools, clique em Options .
- Na caixa de diálogo Options, clique na guia View.
- Na caixa Most Recently Used list contains , selecione ou digite o número de arquivos que deseja exibir.
- Quando terminar, clique em OK .

Para obter mais informações, consulte View Tab, Options Dialog Box.

# Definindo o número de itens a exibir nas caixas de listagem do IntelliSense

Você pode definir o número de itens a exibir inicialmente nas caixas de listagem do IntelliSense usando a caixa de diálogo Options.

### Para definir o número de itens a exibir nas caixas de listagem do IntelliSense
- No menu Tools, clique em Options .
- Na caixa de diálogo Options, clique na guia View.
- Na caixa List display count , selecione ou digite o número de itens que deseja exibir inicialmente nas caixas de listagem do IntelliSense.
- Quando terminar, clique em OK .

Para obter mais informações, consulte View Tab, Options Dialog Box.
