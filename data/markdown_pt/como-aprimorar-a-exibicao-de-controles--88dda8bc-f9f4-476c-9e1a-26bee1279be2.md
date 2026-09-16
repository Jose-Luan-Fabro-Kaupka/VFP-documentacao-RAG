# Como: aprimorar a exibição de controles

CommandButton Control, CheckBox Control e OptionButton Control podem exibir imagens além de legendas. Esses controles têm propriedades que permitem especificar imagens a serem exibidas nos controles.

| Propriedade | Descrição |
| --- | --- |
| DisabledPicture | Exibe imagem no botão quando o botão está desabilitado. Se você não especificar um valor, o Visual FoxPro exibe uma imagem esmaecida quando o controle está desabilitado. |
| DownPicture | Exibe imagem no botão quando o botão é pressionado. Se você não especificar valor, o Visual FoxPro exibe a imagem com as cores de fundo alteradas para que o botão pareça pressionado quando o botão é pressionado. |
| Picture | Exibe imagem no botão quando o botão está habilitado e não pressionado. |
| PicturePosition | Exibe imagem em relação à sua legenda. |
| PictureSelectionDisplay | Exibe imagem na caixa de texto de uma combo box. |

Se você não deseja que uma legenda seja exibida com a imagem, defina a propriedade Caption como uma cadeia vazia excluindo a legenda padrão na caixa de configurações de propriedades da Janela Properties (Visual FoxPro).

# Usando máscaras de imagem

Frequentemente, uma imagem .bmp contém espaço em branco que você não deseja que apareça em seus controles. Uma borda branca ao redor de uma imagem de forma irregular pode fazer seu controle parecer ruim. Para evitar este problema, o Visual FoxPro cria uma máscara padrão temporária para sua imagem. Áreas brancas recebem um atributo transparente para que a cor subjacente do botão ou fundo apareça. Para manter certas áreas brancas de seu .bmp brancas, crie uma máscara que substituirá a padrão.

### Para criar uma máscara para um .bmp
- Abra o arquivo .bmp no Paint ou outro utilitário de bitmap.
- Escureça todas as áreas da imagem que você deseja que sejam exibidas exatamente como estão no arquivo .bmp. Deixe as áreas que você deseja que sejam transparentes em branco.
- Salve o arquivo no mesmo diretório e com o mesmo nome do arquivo .bmp, mas com extensão .msk.

Quando o Visual FoxPro carrega um arquivo .bmp especificado pela propriedade Picture (Visual FoxPro) para um command button, option button ou check box, ele procura no mesmo diretório por um arquivo .msk correspondente. Se um arquivo .msk com o mesmo nome do .bmp estiver no diretório, o Visual FoxPro o usa como máscara para a imagem. Todas as áreas brancas na imagem .msk são tornadas transparentes no .bmp. Todas as áreas pretas na imagem .msk são exibidas exatamente como estão no .bmp.

> **Observação:** A imagem .bmp e a imagem .msk devem ter as mesmas dimensões para que a máscara possa representar a área do .bmp.
