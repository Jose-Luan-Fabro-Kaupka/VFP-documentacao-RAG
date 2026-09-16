# Como: acoplar formulários

Você pode acoplar formulários definidos pelo usuário a certas janelas IDE do Visual FoxPro ou a outros formulários.

### Para acoplar um formulário
- Abra o formulário no Form Designer .
- Na janela Properties, defina a propriedade Dockable do formulário como 1.
- Salve e execute o formulário.
- Arraste o formulário para a área de acoplamento da janela ou formulário de destino. Um contorno do formulário aparece e altera de forma quando o formulário é movido sobre uma área de acoplamento elegível.

Para obter mais informações, consulte Form Designer e Propriedade Dockable.

### Para acoplar um formulário programaticamente
- No código, defina a propriedade Dockable do formulário como 1.
- Defina a propriedade Visible do formulário como .T. (True).
- Chame o método Dock do formulário com os valores apropriados.

Para obter mais informações, consulte Propriedade Visible (Visual FoxPro) e Método Dock.

### Para desacoplar um formulário
- Escolha uma das seguintes opções: Arraste o formulário da janela ou formulário ao qual está acoplado. -OU- Chame o método Dock do formulário com os valores apropriados. -OU- Defina a propriedade Dockable do formulário como 2 ou 0.
