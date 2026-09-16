# Como: definir características de entrada do usuário

Você pode definir as características da entrada que os usuários podem digitar em um controle usando a propriedade InputMask.

Por exemplo, suponha que você deseja limitar a entrada do usuário em uma caixa de texto a valores numéricos menores que 1.000.000 com duas casas decimais. Você pode definir a propriedade InputMask da caixa de texto como 999,999.99. A vírgula (,) e o ponto (.) são exibidos na caixa de texto antes do usuário inserir quaisquer valores. Se o usuário pressionar uma tecla de caractere, o caractere não é exibido na caixa de texto. Como outro exemplo, suponha que você tenha um campo em uma tabela que aceita tipos de dados Logical e deseja que o usuário digite "Y" ou "N", mas não "T" ou "F". Você pode definir a propriedade InputMask da coluna como "Y".

# Ocultando valores de entrada do usuário

Quando você deseja obter informações confidenciais de um usuário, por exemplo, quando o usuário digita uma senha em uma caixa de texto, você pode impedir que as informações digitadas pelo usuário sejam exibidas na tela.

### Para ocultar a entrada do usuário em uma caixa de texto
- Defina a propriedade PasswordChar do TextBox como o asterisco (*) ou outro caractere genérico.

Se você definir a propriedade PasswordChar como qualquer coisa diferente de uma cadeia de caracteres vazia, as propriedades Value e Text (Visual FoxPro) da caixa de texto contêm o valor real que o usuário digitou na caixa de texto, mas a caixa de texto exibe um caractere genérico para cada tecla que o usuário pressionou.
