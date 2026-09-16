# Classe base Sort Dialog Box

Esta caixa de diálogo permite realizar uma classificação de dados ascendente ou descendente em um campo específico.

| Categoria | Data Query |
| --- | --- |
| Catálogo padrão | Visual FoxPro\Foundation Classes\ Data Query |
| Classe | _sortdialog |
| Classe base | Form |
| Biblioteca de classes | _table2.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item do Component Gallery, selecione Add to Project. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Se você escolher Create a new form from the selected class, o Visual FoxPro abre um builder para que você possa especificar o nome do formulário e, em seguida, cria e abre o formulário no Form Designer. Você precisa fornecer uma tabela indexada para a caixa de diálogo Sort.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método DoSort | Permite classificar no campo atual ou especificar o campo pelo qual ordenar uma tabela. Sintaxe: DoSort( ) Retorno: nenhum Argumentos: nenhum |
