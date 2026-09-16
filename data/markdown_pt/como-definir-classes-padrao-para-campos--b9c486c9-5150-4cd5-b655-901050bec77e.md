# Como: definir classes padrão para campos

Você pode definir ou alterar a classe padrão de um campo em uma tabela de banco de dados para que, ao arrastar ou adicionar o campo a um formulário, um objeto seja instanciado da classe padrão e apareça no formulário.

Por exemplo, campos de caractere aparecem como controles text box quando você os adiciona a um formulário. Suponha que você deseja adicionar o campo como um controle combo box em vez de um text box. Você pode alterar a classe padrão do campo para a classe base ComboBox. Você também pode especificar bibliotecas de classes que você criar.

### Para definir uma classe padrão para um campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer.
- Na guia Fields, selecione o campo desejado.
- Na lista Display class da área Map field type to classes, selecione a classe padrão para o campo.
- Para especificar uma biblioteca de classes, na caixa Display library, digite o nome da biblioteca de classes. Para procurar e selecionar uma biblioteca de classes, clique no botão de reticências (...).

Para obter mais informações, consulte Guia Fields, Table Designer.

> **Dica:** Se você alterar frequentemente a classe e a biblioteca de classes para campos, pode mapear tipos de dados para a classe e as bibliotecas de classes desejadas usando a guia Field Mapping na caixa de diálogo Options. Para obter mais informações, consulte Guia Field Mapping, caixa de diálogo Options e Como: criar controles arrastando e soltando campos ou tabelas.
