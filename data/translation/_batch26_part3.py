PART3 = {
    "4a1e906b-5565-4edf-9727-e921ffabc367.md": """# Janela Accessibility Browser

Você pode usar o Accessibility Browser para ajudá-lo a explorar vários elementos da interface do usuário de uma aplicação por meio de sua interface IAccessible e desenvolver aplicações mais acessíveis para pessoas com deficiências. O código-fonte do browser está incluído para que você possa aprimorar a funcionalidade desta ferramenta.

Para obter mais informações, consulte How to: Use the Accessibility Browser.
 **This VFP session**
Quando clicado, a caixa de listagem de elementos da interface do usuário é preenchida com a instância atual do Visual FoxPro.
**Separate VFP session**
Quando clicado, a caixa de listagem de elementos da interface do usuário é preenchida com uma nova instância do Visual FoxPro.
**Refresh**
Atualiza a caixa de listagem de elementos da interface do usuário com base nas opções Session e na caixa de seleção Forms only.
**Forms only**
Quando selecionado, apenas formulários Visual FoxPro (aqueles da coleção _VFP.Forms) são exibidos. Caso contrário, todos os elementos da interface do usuário na aplicação Visual FoxPro são incluídos.
**+**
Expande a caixa de listagem de elementos da interface do usuário.
**-**
Recolhe a caixa de listagem de elementos da interface do usuário.
**UI element list**
Contém uma listagem hierárquica (baseada na contenção pai) de todos os elementos acessíveis da interface do usuário. A lista é preenchida quando o botão Refresh é clicado. Quando você clica em um item na lista, as propriedades IAccessible desse item são exibidas na seção Member detail.

# Member detail

Esta seção lista propriedades IAccessible e seus valores para o item selecionado na caixa de listagem de elementos da interface do usuário. Para obter mais informações sobre propriedades e métodos IAccessible, visite o site da Web Microsoft Accessibility em http://www.microsoft.com/enable/.
 **Go (accParent)**
Seleciona o pai do item atual na caixa de listagem de elementos da interface do usuário.
**Go (accChild)**
Seleciona o filho do item atual na caixa de listagem de elementos da interface do usuário. O filho selecionado é aquele selecionado na lista suspensa accChild que precede o botão Go.
**Do It**
Executa a ação padrão do item selecionado.
**<- (accNavigate)**
Navega para o elemento da interface do usuário anterior.
**-> (accNavigate)**
Navega para o próximo elemento da interface do usuário.
**Select**
Seleciona o elemento da interface do usuário atual na caixa de listagem.
**Focus**
Coloca o foco no elemento da interface do usuário atual na caixa de listagem.
**Click**
Clica no elemento da interface do usuário atual na caixa de listagem.
**Flash**
Exibe uma borda amarela ao redor do elemento real da interface do usuário selecionado na caixa de listagem de elementos da interface do usuário.
**Highlight**
Quando selecionado, mostra automaticamente uma borda amarela ao redor do elemento real da interface do usuário conforme você altera o item selecionado na caixa de listagem de elementos da interface do usuário.

# Plataformas Suportadas

Windows 2000 e posteriores incluem todo o suporte principal para Accessibility. Versões anteriores do Windows suportam Accessibility em vários graus.

| Plataforma | Descrição do suporte |
| --- | --- |
| Windows 98 | Inclui Active Accessibility versão 1.1 na versão inicial do Windows 98; no entanto, você pode executar msaardk.exe para atualizar para uma versão posterior do Active Accessibility. Todas as versões de idioma do Windows 98 são suportadas, e futuros Service Packs do Windows 98 conterão versões atualizadas e localizadas do Active Accessibility. |
| Windows 2000 | Inclui os arquivos do sistema principal do Active Accessibility para todas as versões de idioma do sistema operacional. O suporte para processadores Intel e Alpha é fornecido no Windows 2000. |
| Windows Me | As opções de acessibilidade são instaladas por padrão durante a configuração do Windows Me, tornando o Accessibility Wizard e os utilitários de acessibilidade instantaneamente disponíveis. A maior integração do Microsoft Active Accessibility no Windows Me ajuda muitos recursos de acessibilidade a funcionar de forma mais suave e eficaz com o sistema operacional e outras aplicações. |

# Consulte também
- How to: Use the Accessibility Browser
- Windows (Visual FoxPro)
- Development Productivity Tools
- Accessibility for People with Disabilities (Visual FoxPro)
""",
}
