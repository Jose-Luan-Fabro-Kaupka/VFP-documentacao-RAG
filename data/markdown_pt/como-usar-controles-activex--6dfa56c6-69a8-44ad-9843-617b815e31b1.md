# Como: usar controles ActiveX

Controles ActiveX são objetos com funcionalidade encapsulada e propriedades, eventos e métodos expostos. Controles ActiveX fornecem uma ampla gama de funcionalidades que você pode facilmente aproveitar. Controles ActiveX que acompanham o Visual FoxPro incluem:
 - Controles do Windows, como os controles RichText e TreeView.
- Controles do sistema, como os controles Communications e MAPI.

Controles ActiveX são versáteis porque você pode subclassificá-los para criar outros controles e pode controlá-los usando os eventos, métodos e propriedades associados aos controles. Você não pode criar controles ActiveX com o Visual FoxPro; no entanto, pode criá-los usando o Microsoft OLE Custom Control Developer's Kit fornecido com o Microsoft Visual C++® 4.0 e com o Microsoft Visual Basic® Control Creation Edition versão 5.0.

Para obter mais informações sobre o acesso a controles ActiveX, consulte Extending Visual FoxPro with External Libraries. Para obter mais informações sobre a criação de controles ActiveX específicos para o Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Adicionando controles ActiveX a um formulário

Controles ActiveX no Visual FoxPro devem estar contidos em um controle OLE Container (a classe base é OLEControl). Quando você adiciona um controle OLE Container a um formulário, pode escolher o controle ActiveX que deseja adicionar ao formulário.

### Para adicionar um controle ActiveX a um formulário
- Na barra de ferramentas Form Controls, escolha OLE Container Control e arraste para dimensionar no formulário.
- Na caixa de diálogo Insert Object, escolha Insert Control .
- Na lista Control Type, selecione o controle ActiveX desejado.
- Escolha OK .

Se um controle ActiveX suporta vinculação de dados simples, o Visual FoxPro exporá uma propriedade ControlSource para o controle. Tudo o que você precisa fazer é definir a propriedade ControlSource para um campo de tabela e o valor exibido no controle ActiveX reflete esse valor no campo subjacente. Alterações no valor no controle são salvas no campo.

Para exemplos de uso de controles ActiveX, execute Solution.app no diretório Visual FoxPro ...\Samples\Solution.

> **Observação:** Para garantir que todos os eventos de controle ActiveX sejam processados, defina a propriedade AutoYield do objeto Application do Visual FoxPro como falso (.F.).
