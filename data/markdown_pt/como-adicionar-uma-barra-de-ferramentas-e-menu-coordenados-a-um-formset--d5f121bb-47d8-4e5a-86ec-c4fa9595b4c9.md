# Como: adicionar uma barra de ferramentas e menu coordenados a um FormSet

Quando você criou uma classe de barra de ferramentas e um menu projetados para funcionar juntos, é fácil incorporá-los em um form set.

### Para incorporar uma barra de ferramentas e menu coordenados em um form set
- Adicione a barra de ferramentas ao form set de uma das três formas: Arraste a classe de barra de ferramentas da Project Manager Window para o Form Designer. Registre a biblioteca de classes da barra de ferramentas e adicione a barra de ferramentas ao form set na Form Controls toolbar. No evento Init do form set, inclua código com o método AddObject para adicionar a barra de ferramentas.
- No evento Load do form set, salve o menu existente e execute seu programa de menu. Por exemplo, se o nome do seu menu é mymenu, inclua as seguintes linhas de código usando o comando PUSH MENU e o comando DO: PUSH MENU _MSYSMENU DO mymenu.mpr
- No evento Unload do form set, restaure o menu original com o comando POP MENU: POP MENU _MSYSMENU

Se alguns comandos de menu são usados com mais frequência, você pode criar barras de ferramentas personalizadas contendo botões para esses comandos. Então, os usuários podem simplesmente pressionar os botões sempre que precisarem dos comandos. No entanto, se você criar uma barra de ferramentas, deve sincronizar os comandos de menu com seus botões correspondentes. Por exemplo, se você habilitar um botão, deve habilitar o comando de menu correspondente.
