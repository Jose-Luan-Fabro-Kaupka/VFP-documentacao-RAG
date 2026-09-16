# Como: adicionar um menu a um formulário de nível superior

Menus em formulários de nível superior não apenas fornecem navegação no formulário, mas também podem dar pistas iniciais sobre o design do seu aplicativo.

### Para adicionar um menu a um formulário de nível superior
- Crie um menu de formulário de nível superior. Para obter mais informações sobre como criar menus para formulários de nível superior, consulte Designing Menus and Toolbars .
- Defina a propriedade ShowWindow do formulário como 2 – As Top-Level Form .
- No evento Init do formulário, execute o programa de menu e passe dois parâmetros: DO menuname.mpr WITH oForm, lAutoRename oForm é uma referência de objeto ao formulário. No evento Init do formulário, passe THIS como o primeiro parâmetro. lAutoRename especifica se um novo nome exclusivo é gerado para o menu. Se você planeja executar várias instâncias do formulário, passe .T. para lAutoRename. Por exemplo, você pode chamar um menu chamado mySDImenu com este código: DO mySDImenu.mpr WITH THIS, .T.
