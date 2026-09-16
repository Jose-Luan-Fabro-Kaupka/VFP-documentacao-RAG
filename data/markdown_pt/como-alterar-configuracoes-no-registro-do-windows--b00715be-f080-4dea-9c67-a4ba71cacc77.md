# Como: alterar configurações no Registro do Windows

Você pode definir a configuração do Visual FoxPro fazendo alterações diretamente no Registro do Windows. Para alterar o Registro do Windows, use o Registry Editor, um utilitário fornecido com o Windows.

> **Observação:** Use cautela ao alterar o Registro do Windows. Alterar a entrada de registro errada ou fazer uma entrada incorreta para uma configuração pode introduzir um erro que impede o Visual FoxPro, ou até mesmo o Windows, de iniciar ou funcionar corretamente.

### Para alterar configurações no registro
- No Windows, inicie o Registry Editor.
- No nó HKEY_CURRENT_USER, navegue até o diretório Software\Microsoft\Visual FoxPro e abra a pasta da versão atual do Visual FoxPro.
- Na pasta Options, clique duas vezes no nome da configuração a ser alterada e insira um novo valor.
- Feche o Registry Editor. Sua alteração terá efeito na próxima vez que você iniciar o Visual FoxPro.

Você também pode fazer alterações no registro chamando APIs do Windows de um programa Visual FoxPro.
