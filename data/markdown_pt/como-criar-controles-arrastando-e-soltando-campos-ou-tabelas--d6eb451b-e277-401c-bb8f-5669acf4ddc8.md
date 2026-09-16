# Como: criar controles arrastando e soltando campos ou tabelas

Você pode especificar o tipo de controle criado quando arrasta um campo ou tabela para um formulário. Por exemplo, você pode criar um controle de caixa de texto sempre que um campo Character é arrastado para um formulário.

### Para mapear tipos de campo para classes
- No menu Tools, escolha Options.
- Selecione a guia Field Mapping.
- Para alterar um mapeamento de tipo de campo, selecione uma linha na área Map fields to classes for drag and drop e escolha Modify.
- Na caixa de diálogo Modify Field Mapping, selecione um tipo de campo na lista Type. Para definir a classe criada sempre que você arrasta uma tabela ou vários campos, selecione Multiple na lista Type.
- Para selecionar a biblioteca de classes (.vcx file) que contém o controle que deseja associar ao tipo de campo selecionado, escolha Browse.
- Selecione um nome de classe na lista Name. A classe que você especifica aqui será criada sempre que um campo do tipo selecionado é arrastado para um formulário.
- Escolha OK para aceitar o mapeamento.
- Defina opções na área Database options: Para... Selecione... Criar um rótulo além do controle vinculado quando você arrasta um campo ou tabela para um formulário ou contêiner Drag and drop field caption Definir a propriedade Comment do controle vinculado para o texto especificado na caixa Field Comment na guia Fields do Table Designer (Visual FoxPro) Copy field comment Definir a propriedade InputMask do controle vinculado para a máscara de entrada especificada na guia Fields do Table Designer Copy field input mask Definir a propriedade Format do controle vinculado para o formato especificado na guia Fields do Table Designer Copy field format

> **Observação:** Você também pode especificar classes para arrastar e soltar na caixa Display Class na guia Fields do Table Designer. As configurações no Table Designer substituem as configurações que você especifica aqui.

# Criando rapidamente um único controle

Você pode criar rapidamente um único controle baseado no mapeamento de tipo de campo que especificou na guia Field Mapping na Options Dialog Box (Visual FoxPro). Você também pode substituir o mapeamento padrão e criar um tipo de classe diferente.

### Para criar um único controle
- Clique em qualquer campo no Data Environment e arraste-o para um formulário. Observação A propriedade ControlSource do controle recém-criado é definida para a propriedade Name do campo.

### Para criar um único controle e substituir o mapeamento de campo atual
- Clique com o botão direito em qualquer campo no Data Environment e arraste-o para um formulário.
- No menu de atalho, selecione Create Other Control Here.
- Na caixa de diálogo Open, escolha um arquivo Visual Class Library (.vcx).
- Selecione o tipo de controle que deseja criar na caixa Class Name e escolha Open.

# Criando rapidamente vários controles

Você pode arrastar uma tabela inteira para um formulário. Por padrão, um controle de grade é criado quando você arrasta uma tabela para um formulário. Você pode substituir o padrão e criar vários controles correspondentes aos mapeamentos de tipo de campo padrão especificados para cada campo na tabela.

### Para criar um controle de grade
- Escolha qualquer tabela no Data Environment, Database Designer (Visual FoxPro) ou Project Manager Window e arraste-a para um formulário.

### Para criar vários controles
- Clique com o botão direito em qualquer tabela, ou em dois ou mais campos destacados em uma tabela, no Data Environment, Database Designer ou Project Manager, e arraste para um formulário.
- No menu de atalho, selecione Create Multiple Controls Here.
