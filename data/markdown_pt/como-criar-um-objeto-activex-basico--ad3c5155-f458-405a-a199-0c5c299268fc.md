# Como: criar um objeto ActiveX básico

Você pode criar objetos COM com a ActiveX Template Library fornecida com o Microsoft® Visual C++.

Você cria controles Microsoft ActiveX específicos para o Visual FoxPro como faria com qualquer controle semelhante. A maioria dos compiladores C++ permite criar esboços do controle, e eles podem ser criados com o Microsoft Visual Basic Control Creation Edition.

As seções a seguir descrevem as etapas para criar um controle ActiveX com o Microsoft Visual C++ 6.0 para uso no Visual FoxPro.

### Para criar um projeto para o controle ActiveX
- Inicie o Microsoft Visual C++.
- No menu File, escolha New .
- Na caixa de diálogo New, escolha Project Workspace .
- Na caixa de diálogo New Project Workspace, especifique um nome de projeto.
- Na lista Type, escolha OLE ControlWizard .
- Escolha Create e siga as etapas do assistente.

Quando o assistente terminar, você pode compilar o controle ActiveX imediatamente. No entanto, também precisará definir propriedades e métodos para o controle.

### Para adicionar propriedades e métodos ao controle ActiveX
- No menu View, escolha ClassWizard .
- Escolha a guia OLEAutomation.
- Escolha Add Method ou Add Property .
- Preencha o nome, parâmetro e outras informações exigidas pelo elemento que está criando e escolha OK .
- Escolha Edit Code para exibir o editor e insira o código que define a propriedade ou método que está criando.

Por exemplo, para criar uma propriedade Version que retorna a versão do arquivo .ocx como um inteiro (como 101), você cria a propriedade com um tipo de retorno `long` e adiciona código semelhante ao seguinte:

```foxpro
#define VERSION 101
long CPyCtrl::GetVersion()
{
   // set the version number here
   return VERSION;
}
```

Como o número de versão geralmente é somente leitura, você não criaria uma função SetVersion( ).
