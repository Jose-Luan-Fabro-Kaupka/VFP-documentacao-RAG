# Caixa de diálogo Pane Customization

A caixa de diálogo Pane Customization é usada para criar, modificar e excluir painéis no Task Pane Manager.
 **New**
Exibe a caixa de diálogo Pane para você inserir informações básicas sobre o novo painel a ser criado. The following options are displayed: Vendor Especifica o nome da empresa que está criando o novo painel. Unique ID Especifica um número de ID exclusivo para o conteúdo do painel. Recomenda-se aceitar o valor padrão. Name Especifica o nome do novo painel. Este nome aparece no topo do Task Pane Manager. Para especificar uma tecla de atalho para o link no topo do Task Pane Manager, inclua um caractere de escape na caixa Name. For example, \<My Pane would specify the letter M as the hot key in the panes link. Pane Type Especifica o tipo de painel que deseja criar. Os quatro tipos de painéis que você pode criar são explicados na tabela a seguir. Pane Type Description Web Page Exibe uma URL da Internet usando o controle ActiveX do Internet Explorer. HTML O painel e suas seções de conteúdo são exibidos como HTML no controle ActiveX do Internet Explorer. XML O painel e suas seções de conteúdo são exibidos como XML no controle ActiveX do Internet Explorer. Um arquivo Extensible Stylesheet Language (XSL) local deve ser distribuído com este tipo de painel. VFP Controls Especifique uma biblioteca de classes e classe Visual FoxPro para criar como o painel. Esta classe deve herdar da classe PaneContainer da biblioteca FoxPane. DEFINE CLASS MyPane AS PaneContainer OF FoxPane
**Delete**
Exclui um painel do Task Pane Manager. Quando selecionado, uma caixa de diálogo aparece solicitando que você exclua o painel selecionado.
**Publish**
Exibe a caixa de diálogo Publish Pane onde você pode publicar o painel selecionado encapsulando o conteúdo do painel e seus arquivos associados em um arquivo manifest XML para fácil distribuição. The following options are displayed: Publish all content in pane Especifica que todas as seções de conteúdo do painel são publicadas no arquivo manifest XML. Publish selected content Especifica que somente as seções de conteúdo selecionadas na lista são publicadas no arquivo manifest XML. Publish files associated with the pane Especifica que arquivos associados ao painel são publicados no arquivo manifest XML. Publish files common to all panes Especifica que arquivos comuns a todos os painéis são publicados no arquivo manifest XML. Esta opção deve ser selecionada somente se você precisar distribuir conteúdo na pasta raiz PaneCache.
**View Content**
Exibe a seção Pane Content no lado direito da caixa de diálogo Pane Customization.
**View Files**
Exibe a seção Pane Files no lado direito da caixa de diálogo Pane Customization.
**Pane List**
Lista todos os painéis instalados no Task Pane Manager. Selecionar um painel atualiza os controles das seções Pane Content e Pane Files com informações sobre o painel selecionado.
**Inactive**
Especifica que o painel selecionado está inativo. Painéis inativos não aparecem na barra de ferramentas Pane List no topo do Task Pane Manager ou na caixa de diálogo Task Pane Options.
**Save**
Salva quaisquer alterações no painel selecionado, aplica-as ao Task Pane Manager e fecha a caixa de diálogo Pane Customization.
**Apply**
Salva quaisquer alterações no painel selecionado e aplica-as ao Task Pane Manager.

# Pane Content

A seção Pane Content é exibida quando você seleciona View Content. Nesta seção, você pode especificar configurações para os painéis.
 **Add**
Adiciona uma nova seção de conteúdo, que é exibida em Content Sections List abaixo do botão.
**Remove**
Solicita que você exclua a seção de conteúdo selecionada.
**Up Arrow**
Move a seção selecionada para cima em Content Sections List .
**Down Arrow**
Move a seção selecionada para baixo em Content SectionsList .
**Content Sections List**
Lista as seções de conteúdo de um painel. Selecionar uma seção de conteúdo atualiza os controles da seção Pane Content com informações sobre o painel selecionado.

# Guia General

Exibe opções para o conteúdo raiz do painel ou conteúdo de seção em que você especifica informações gerais sobre o item selecionado. Para obter mais informações, consulte General Tab, Pane Customization Dialog Box.

# Guia Data

Exibe a URL para painéis baseados em páginas Web ou contém os dados XML usados para renderizar uma página para painéis baseados em HTML ou XML. Este painel está disponível somente quando o tipo de painel raiz é Web Page, HTML ou XML. Para obter mais informações, consulte Data Tab, Pane Customization Dialog Box.

# Guia Transform Data

Especifica a transformação XML usada para renderizar painéis baseados em HTML ou XML. This pane is available only when the root pane type is HTML or XML. Para obter mais informações, consulte Transform Data Tab, Pane Customization Dialog Box.

# Guia Default Data

Especifica os dados a serem usados quando o painel for renderizado se o conteúdo online do painel não puder ser baixado. This pane is available only when the root pane type is HTML or XML. Para obter mais informações, consulte Default Data Tab, Pane Customization Dialog Box.

# Guia Handler Code

Especifica código de handler para tratar entrada do usuário em painéis. This pane is available only when the root pane type is HTML or XML. Para obter mais informações, consulte Handler Code Tab, Pane Customization Dialog Box.

# Guia Options

Especifica opções personalizadas para uma seção de conteúdo. Para painéis baseados em XML e HTML, opções podem ser especificadas somente no conteúdo de subseção. Para painéis Web Page e VFP Control, opções podem ser especificadas somente na seção de conteúdo raiz. Para obter mais informações, consulte Options Tab, Pane Customization Dialog Box.

# Pane Files

A seção Pane Files é exibida quando você seleciona View Files. Nesta seção, você pode adicionar, editar e remover arquivos associados a um painel.
 **Add**
Solicita ao usuário que selecione um arquivo para adicionar a um painel.
**Edit**
Abre um arquivo e seu editor padrão associado para edição.
**Remove**
Solicita ao usuário que remova o arquivo selecionado do painel.
