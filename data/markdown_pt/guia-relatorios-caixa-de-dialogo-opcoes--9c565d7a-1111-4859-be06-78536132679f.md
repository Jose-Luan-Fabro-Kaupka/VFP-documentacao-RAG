# Guia Relatórios, Caixa de diálogo Opções

Contém opções iniciais padrão e configurações globais para o Report Designer usar ao criar relatórios.

Quando você escolhe Definir como padrão, que aparece em cada guia na caixa de diálogo Opções, o Visual FoxPro salva todas as opções em todas as guias.

# Padrões de dados e saída
 **Usar sessões de dados privadas**
Executa o relatório usando uma sessão de dados privada. Você também pode selecionar Private Data Session no menu Relatório. Para obter mais informações sobre sessões de dados privadas, consulte Como: usar sessões de dados .
**Salvar ambiente da impressora**
Salva a configuração atual do ambiente da impressora com um relatório. Em versões anteriores do Visual FoxPro, o ambiente da impressora era salvo com o relatório por padrão. No Visual FoxPro 9, não é salvo por padrão. Para obter mais informações, consulte Como: salvar o ambiente da impressora para relatórios .
**Usar legendas de campos do DBC**
Usa legendas de campos do contêiner de banco de dados (DBC) quando você solta campos em um relatório.

# Expression Builder
 **Sempre adicionar alias**
Especifica que o nome da tabela ou view é sempre incluído com os campos usados na expressão.
**Adicionar alias não selecionado somente**
Especifica que, quando mais de uma tabela ou view está aberta, o Visual FoxPro inclui somente o nome de qualquer tabela ou view que não esteja selecionada na lista Aliases da Janela de Sessão de Dados com qualquer um de seus campos na expressão. Nomes de tabelas ou views não são adicionados para tabelas selecionadas na lista Aliases.
**Nunca adicionar alias**
Especifica que nomes de tabelas ou views não são incluídos com nenhum campo quando você cria a expressão.

# Comportamento do mecanismo de relatório

Especifica a configuração inicial de SET REPORTBEHAVIOR quando o Visual FoxPro é iniciado.

Consulte Comando SET REPORTBEHAVIOR para obter mais informações.
 **80 (Compatível com versões anteriores)**
Define REPORTBEHAVIOR como 80
**90 (Assistido por objetos)**
Define REPORTBEHAVIOR como 90

# Padrões do designer

### Escala da régua

Especifica as unidades de medida para a régua nas bordas superior e esquerda da janela do Report Designer ou Label Designer.
 **Nenhuma**
As réguas não são exibidas. As unidades de medida exibidas em várias caixas de diálogo serão em polegadas.
**Polegadas**
A régua de medida e outras dimensões são exibidas em polegadas.
**Centímetros**
A régua de medida e outras dimensões são exibidas em centímetros.
**Pixels**
A régua de medida e outras dimensões são exibidas em pixels.
**Padrão do sistema**
Especifica polegadas ou centímetros como a unidade de medida exibida na régua, dependendo da configuração de idioma.

### Mostrar posição na barra de status

Especifica se deve mostrar a posição do cursor do mouse ou a posição do controle atualmente selecionado (em unidades da régua) na barra de status.

### Grade
 **Ajustar à grade**
Alinha as bordas dos controles recém-desenhados com as linhas de grade mais próximas no Report Designer. Você também pode selecionar Snap to Grid no menu Formatar para habilitar esta opção quando estiver no Designer.
**Mostrar linhas de grade**
Especifica se deve exibir linhas visíveis de ajuste à grade no Designer. A resolução da grade visível é metade da grade real de ajuste. (Por exemplo, se o espaçamento horizontal estiver definido como 12 pixels, as linhas de grade verticais serão desenhadas a cada 24 pixels.) Você também pode selecionar Grid Lines no menu Exibir quando estiver no Designer.
**Espaçamento horizontal (pixels)**
Especifica o número de pixels para espaçar horizontalmente cada seção da grade. Você também pode definir o espaçamento horizontal selecionando Set Grid Scale no menu Formatar.
**Espaçamento vertical (pixels)**
Especifica o número de pixels para espaçar verticalmente cada seção da grade. Você também pode definir o espaçamento vertical selecionando Set Grid Scale no menu Formatar.

### Fonte padrão

Exibe as configurações de fonte padrão para novos relatórios ou layouts de etiqueta. Clicar no botão de reticências (…) abre a caixa de diálogo Fonte para que você possa selecionar uma fonte padrão diferente.
 **Usar script de fonte**
Indica que o conjunto de caracteres do idioma deve ser habilitado na caixa de diálogo Fonte e salvo com o relatório. Você pode optar por não salvar a seleção específica de script de fonte com o layout desmarcando esta caixa de seleção. Para obter mais informações, consulte Caixa de diálogo Fonte .
