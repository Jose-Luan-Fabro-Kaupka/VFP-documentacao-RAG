# Como: manipular objetos com OLE Container Control e OLE Bound Control

Você adiciona um objeto OLE a um formulário clicando na ferramenta OLE Container Control e arrastando para dimensionar na janela Form. Esta ferramenta pode representar um objeto servidor como Microsoft Excel ou Word, ou pode representar um controle ActiveX se o diretório SYSTEM do Windows contiver controles ActiveX (arquivos com extensão .ocx). Para informações gerais sobre controles ActiveX, consulte Sharing Information and Adding OLE.

# OLE Bound Control

Você pode criar um objeto OLE vinculado em um formulário clicando nesta ferramenta e arrastando para dimensionar na janela Form. Depois de criar o objeto, você o conecta a um campo General em uma tabela. Em seguida, você usa o objeto para exibir o conteúdo do campo. Por exemplo, se você armazena documentos Word em um campo General, pode exibir o conteúdo desses documentos usando um objeto OLE vinculado em um formulário.

### Para criar um objeto OLE vinculado
- Crie ou abra um formulário.
- Na barra de ferramentas Form Controls, escolha o botão OLE Bound Control e arraste para dimensionar no formulário.
- Vincule o objeto OLE a um campo General definindo a propriedade ControlSource do objeto.

Para um exemplo de uso do controle OLE Bound, consulte Sharing Information and Adding OLE.
