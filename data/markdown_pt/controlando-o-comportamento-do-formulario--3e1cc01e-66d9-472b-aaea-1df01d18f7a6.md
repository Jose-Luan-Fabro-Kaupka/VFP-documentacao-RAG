# Controlando o comportamento do formulário

Quando você está criando um formulário no Form Designer, o formulário está ativo: exceto ao definir a propriedade Visible Property (Visual FoxPro) como false (.F.), as alterações visuais e comportamentais que você faz são imediatamente refletidas no formulário. Se você definir a propriedade WindowState Property (Visual FoxPro) como 1 – Minimized ou 2 – Maximized, o formulário no Form Designer reflete imediatamente essa configuração. Se você definir a propriedade Movable Property como false (.F.), um usuário não poderá mover o formulário em tempo de execução e você também não poderá mover o formulário em tempo de design. Você pode querer projetar a funcionalidade do seu formulário e adicionar todos os controles apropriados antes de definir algumas das propriedades que determinam o comportamento do formulário.

As seguintes propriedades de formulário são comumente definidas em tempo de design para definir a aparência e o comportamento do formulário.

| Propriedade | Descrição | Padrão |
| --- | --- | --- |
| AlwaysOnTop | Controla se um formulário está sempre acima de outras janelas abertas. | False (.F.) |
| AutoCenter | Controla se o formulário é centralizado automaticamente na janela principal do Visual FoxPro ou na área de trabalho quando o formulário é inicializado. | False (.F.) |
| BackColor | Determina a cor da janela do formulário. | 255,255,255 |
| BorderStyle | Controla se o formulário não tem borda, tem borda de linha única, borda dupla ou borda do sistema. Se BorderStyle for 3 - System, o usuário poderá redimensionar o formulário. | 3 |
| Caption | Determina o texto exibido na barra de título do formulário. | Form1 |
| Closable | Controla se o usuário pode fechar o formulário clicando duas vezes na caixa de fechamento. | True (.T.) |
| DataSession | Controla se as tabelas no formulário são abertas em áreas de trabalho globalmente acessíveis ou privadas ao formulário. | 1 |
| MaxButton | Controla se o formulário tem ou não um botão de maximizar. | True (.T.) |
| MinButton | Controla se o formulário tem ou não um botão de minimizar. | True (.T.) |
| Movable | Controla se o formulário pode ou não ser movido para um novo local na tela. | True (.T.) |
| ScaleMode | Controla se a unidade de medida nas propriedades de tamanho e posição do objeto é foxels ou pixels. | Determinado pelas configurações na caixa de diálogo Options. |
| Scrollbars | Controla o tipo de barras de rolagem que um formulário possui. | 0 - None |
| TitleBar | Controla se uma barra de título aparece na parte superior do formulário. | 1 - On |
| ShowWindow | Controla se a janela é filha (in screen), flutuante ou janela de nível superior. | 0 - In Screen |
| WindowState | Controla se o formulário está minimizado (somente no Windows), maximizado ou normal. | 0 - Normal |
| WindowType | Controla se o formulário é modeless (o padrão) ou modal. Se o formulário for modal, o usuário deve fechar o formulário antes de acessar qualquer outro elemento da interface do usuário do seu aplicativo. | 0 – Modeless |

Você pode usar a propriedade LockScreen Property para tornar mais limpa a aparência do ajuste em tempo de execução das propriedades de layout dos controles.
