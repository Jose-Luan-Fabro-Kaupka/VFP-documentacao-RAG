# Como: definir a área de design de um formulário

Você pode definir a área máxima de design para o Form Designer na caixa de diálogo Options.

### Para definir a área máxima de design de um formulário
- No menu Tools, escolha Options.
- Na caixa de diálogo Options, escolha a guia Forms.
- Na caixa Maximum design area, escolha as coordenadas em pixels para a área máxima de design. Dica Se você selecionar None, o Form Designer não impõe um limite ao tamanho do formulário que você projeta.

Para obter mais informações, consulte Guia Forms, caixa de diálogo Options.

Quando você define a área máxima de design, o fundo do Form Designer é branco dentro dos limites da área de design e cinza nas áreas além da área máxima de design. Se você desenvolve aplicações em um monitor com resolução de 1024 x 768, por exemplo, pode definir sua resolução de design para 640 x 480 e saber que os formulários que você projeta sempre caberão em telas de 640 x 480.

Na área de design, certifique-se de considerar atributos padrão de janela, como barras de ferramentas. Por exemplo, em uma tela de 640 x 480, um formulário com barra de status e uma barra de ferramentas encaixada na parte superior ou inferior da tela pode ter altura máxima de 390 pixels.

| Atributo da janela principal do Visual FoxPro | Pixels necessários (Windows sem tema) |
| --- | --- |
| Título e menu | 38 |
| Barra de status | 23 |
| Barra de ferramentas encaixada | 29 |

Observação As quantidades de pixels necessárias acima variarão se janelas com tema forem usadas.
