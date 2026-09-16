# Como: Adicionar Chamadas de API do Visual FoxPro

Para integrar seu programa ao Visual FoxPro, você pode chamar rotinas de API do Visual FoxPro. Essas rotinas de API são funções que você pode chamar de qualquer programa C ou C++, incluindo um arquivo .ocx ou .fll, que dão acesso a variáveis, gerenciam operações de banco de dados e realizam muitas outras tarefas específicas do Visual FoxPro.

A tabela a seguir lista as categorias gerais de chamadas de API disponíveis no Visual FoxPro. Para obter detalhes sobre funções de API individuais, consulte Rotinas de Biblioteca de API A-Z ou Rotinas de Biblioteca de API por Categoria.

Para usar as rotinas de API do Visual FoxPro, você deve incluir o arquivo Pro_ext.h, disponível no diretório de API do Visual FoxPro. Este arquivo inclui os protótipos das funções e estruturas que permitem compartilhar informações com o Visual FoxPro.

Se você estiver escrevendo um controle ActiveX, também deve adicionar chamadas para inicializar e limpar a API.

### Para adicionar rotinas de API do Visual FoxPro ao seu objeto ActiveX
- Use #INCLUDE para incluir o arquivo Pro_ext.h junto com quaisquer outros arquivos de cabeçalho necessários.
- No Construtor (método Init) do controle, chame _OCXAPI( ) para inicializar a interface com o Visual FoxPro usando este código: _OCXAPI(AfxGetInstanceHandle(),DLL_PROCESS_ATTACH);
- Inclua chamadas à API do Visual FoxPro conforme necessário em seu objeto.
- No Destrutor (método Destroy) do objeto, chame _OCXAPI( ) novamente para liberar o processo criado no Construtor, usando este código: _OCXAPI(AfxGetInstanceHandle(),DLL_PROCESS_DETACH);

Para um exemplo de uma biblioteca .fll que inclui chamadas à API do Visual FoxPro, consulte os programas de exemplo no diretório \Api\Samples que possuem a extensão C: EVENT.C, HELLO.C e assim por diante.

Se você usar chamadas de API do Visual FoxPro em seu controle ActiveX, objeto COM ou biblioteca .fll, o código que contém as chamadas é incompatível com outros aplicativos. Portanto, você pode querer construir um ou mais testes no programa para determinar se o objeto está sendo chamado do Visual FoxPro.

Por exemplo, se você estiver criando um controle ActiveX usando o Microsoft Foundation Classes, pode alterar o código do construtor do controle para incluir um teste e, em seguida, alertar o usuário se o controle foi chamado de um programa diferente do Visual FoxPro:

```foxpro
if (!_OCXAPI(AfxGetInstanceHandle(),DLL_PROCESS_ATTACH))
{
   ::MessageBox(0,"This OCX can only be hosted by Visual Foxpro","",0);
      //Here you can do whatever you want when the host isn't VFP:
      // you might want to reject loading or you
      // might want to set a property
      // saying that the host isn't VFP and the control will use other
      // means to achieve it's purpose.
}
```

Se você estiver criando um controle ActiveX usando o Microsoft ActiveX Template Library, use o seguinte código:

```foxpro
if (!_OCXAPI(_Module.GetModuleInstance(),DLL_PROCESS_ATTACH))
{
   ::MessageBox(0,"This OCX can only be hosted by Visual Foxpro","",0);
      //Here you can do whatever you want when the host isn't VFP:
      // you might want to reject loading or you
      // might want to set a property
      // saying that the host isn't VFP and the control will use other
      // means to achieve it's purpose.
}
```

Neste exemplo, o controle não sai e continuará em execução após o usuário ter confirmado a mensagem. A estratégia que você escolher depende de como você antecipa que o controle será usado. Por exemplo, se você detectar que o controle está sendo usado fora do Visual FoxPro, pode definir um sinalizador que você testa em cada ponto do controle onde chama a API do Visual FoxPro. Se o sinalizador indicar que o controle está fora do Visual FoxPro, você pode desviar em torno da chamada de API para um meio alternativo de realizar a mesma tarefa.
