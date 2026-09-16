# Classe básica GoTo Dialog Box

Esta classe cria uma caixa de diálogo GoTo Record.

| Categoria | Data Navigation |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Navigatio n |
| Classe | _gotodialog |
| Biblioteca de classes | _table.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\datanav.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item da Galeria de Componentes, selecione Create Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você solta a classe em um projeto ou escolhe Create a new form from the selected class no menu de atalho, o Visual FoxPro abre um construtor para que você possa especificar o nome do formulário e, em seguida, cria e abre o formulário no Form Designer.

_GoToDialog é uma caixa de diálogo modal com um membro _TableNav e um spinner para permitir que o usuário especifique um número de registro. Quando você clica em OK, o método GoToRecord navega até o registro especificado e, em seguida, executa o método RefreshLastWindowAfterChange para atualizar a exibição. Observe que GoToRecord( ) atualiza a exibição mesmo se a tabela não permitir navegação, caso você reverta uma alteração.

_GoToDialog usa _TableNav para determinar o alias atual na inicialização. Em seguida, define SpinnerLowValue e KeyboardLowValue do spinner como 1 e SpinnerHighValue e KeyboardHighValue como RECCOUNT( ). Também define a propriedade Value do spinner adequadamente.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| método RefreshUIAfterChange | Interno à classe. |
