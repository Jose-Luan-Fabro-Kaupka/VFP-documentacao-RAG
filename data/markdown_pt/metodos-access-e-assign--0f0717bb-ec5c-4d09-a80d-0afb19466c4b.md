# Métodos Access e Assign

O Visual FoxPro oferece suporte aos métodos Access e Assign, que são procedimentos ou funções definidos pelo usuário com o mesmo nome de uma propriedade de classe e com o sufixo _ACCESS ou _ASSIGN acrescentado ao nome do procedimento ou função. Você pode usar os métodos Access e Assign para executar código ao consultar o valor de uma propriedade ou tentar alterar esse valor. O Visual FoxPro executa os métodos Access e Assign somente ao consultar ou alterar valores de propriedades em tempo de execução, não em tempo de design. É possível criar os métodos Access e Assign de forma separada e independente.

Os métodos Access e Assign oferecem os seguintes benefícios:
 - Você pode criar uma interface pública para uma classe ou objeto que separe a interface da implementação.
- Pode implementar facilmente a validação de propriedades.
- Pode proteger facilmente propriedades em controles ActiveX derivados.

O Visual FoxPro executa o código de um método Access ao consultar o valor de uma propriedade, normalmente usando a propriedade em uma referência de objeto, armazenando seu valor em uma variável ou exibindo-o com o comando de ponto de interrogação (?).

O Visual FoxPro executa o código de um método Assign quando você tenta alterar o valor da propriedade, normalmente usando o comando STORE ou o operador = para atribuir um novo valor à propriedade.

> **Observação:** Você pode criar métodos Access e Assign para a maioria das propriedades nativas do Visual FoxPro. É possível criar métodos Assign para propriedades somente leitura; contudo, o método nunca é executado. O Visual FoxPro não oferece suporte ao método Assign para a propriedade Value de controles, nem aos métodos Access e Assign para propriedades, eventos ou métodos nativos de controles ActiveX. Contudo, oferece suporte a métodos Access e Assign para propriedades, eventos e métodos do OLE Container do Visual FoxPro que contém um controle ActiveX.

> **Observação:** Os métodos Access e Assign de matrizes de membros não são disparados ao acessar a matriz usando uma função nativa de matriz, como ASCAN().

> **Observação:** O método Assign será disparado para certas propriedades nativas quando seu valor for consultado, mas não alterado. Entre elas estão propriedades dimensionais como Top, Left, Height e Width, além de algumas outras, como Visible. Isso ocorre devido à maneira como o Visual FoxPro trata internamente essas propriedades.

O Visual FoxPro trata os métodos Access e Assign como Protected em tempo de execução, portanto eles não podem ser acessados fora da definição da classe. Contudo, no Designer de Classes, o Visual FoxPro trata esses métodos de uma maneira especial. Quando você solta um objeto em um contêiner, como um botão de comando em um formulário, o Visual FoxPro geralmente marca os métodos Protected desses objetos como somente leitura e não modificáveis no designer. Contudo, você pode editar os métodos Access e Assign desses objetos no Designer de Classes.

# Métodos THIS_ACCESS

Você pode criar métodos THIS_ACCESS para executar código ao alterar o valor de um membro do objeto ou consultá-lo. O método THIS_ACCESS deve sempre retornar uma referência de objeto; caso contrário, o Visual FoxPro gera um erro. Normalmente, o método retorna a referência de objeto, THIS. O método THIS_ACCESS também deve incluir um parâmetro para aceitar o nome do membro do objeto alterado ou consultado.

> **Observação:** THIS_ACCESS não se destina a substituir globalmente os métodos Access e Assign. Ele fornece apenas informações sobre o membro do objeto acessado ou consultado. Ao contrário de um método Access ou Assign, THIS_ACCESS não oferece controle sobre os valores retornados a membros específicos do objeto.
