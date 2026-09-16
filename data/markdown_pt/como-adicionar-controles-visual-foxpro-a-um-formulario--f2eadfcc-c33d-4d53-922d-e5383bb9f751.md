# Como: adicionar controles Visual FoxPro a um formulário

Você pode adicionar qualquer um dos controles Visual FoxPro padrão ao seu formulário. Por exemplo, você pode adicionar rótulos para campos no formulário, adicionar controles como botões, caixas de edição ou caixas de listagem, ou adicionar imagens ou linhas e formas para melhorar a aparência do seu formulário.

### Para adicionar um controle a um formulário
- Abra o formulário no Form Designer.
- Na barra de ferramentas Form Controls, clique no controle que deseja adicionar.
- No Form Designer, clique no formulário na localização em que deseja posicionar o controle em seu tamanho padrão. O novo controle aparece onde você o posicionou. Você pode então movê-lo para sua localização final no formulário e redimensioná-lo conforme necessário.

Você também pode clicar e arrastar o cursor para desenhar o controle com as dimensões desejadas. Para obter mais informações, consulte Form Designer.

Agora você pode definir propriedades para o controle clicando em Properties no menu View para abrir a janela Properties. A janela Properties exibe todas as propriedades dos controles que você adiciona a um formulário. Para obter mais informações, consulte Properties Window (Visual FoxPro).

Você pode adicionar vários controles do mesmo tipo sem escolher o controle cada vez que desejar adicionar um controle.

### Para adicionar vários controles a um formulário
- Abra o formulário no Form Designer.
- Na barra de ferramentas Form Controls, clique no controle que deseja adicionar.
- Na barra de ferramentas Form Controls, clique em Button Lock. Dica Você também pode clicar duas vezes no controle que deseja adicionar.

Agora você pode adicionar vários controles do mesmo tipo sem clicar no controle na barra de ferramentas Form Controls várias vezes.

# Adicionando controles com um builder

Assim como você pode usar wizards para criar formulários rapidamente, você pode usar um builder para adicionar certos controles a um formulário. O builder define as propriedades apropriadas no controle usando suas respostas a uma série de perguntas.

### Para adicionar um controle com um builder
- Abra o formulário no Form Designer.
- Na barra de ferramentas Form Controls, clique em Builder Lock.
- Adicione o controle desejado ao formulário. Se disponível, um builder é aberto para o controle.
- Siga as instruções nas guias do builder. Observação Para definir propriedades de controle na janela Properties, desative o Builder Lock.

Para obter mais informações sobre a escolha de controles, consulte Using Controls. Para detalhes sobre fontes válidas de controle de imagem, consulte Graphics Support in Visual FoxPro.

# Adicionando controles vinculados a dados a um formulário

Você pode vincular controles a dados em uma tabela, view, campo de tabela ou campo de view.

### Para vincular um controle a dados em uma tabela, view ou campo de tabela ou view
- Defina a propriedade ControlSource de um controle para um campo ou a propriedade RecordSource de uma grade para uma tabela ou view.

Para obter mais informações, consulte ControlSource Property ou RecordSource Property.

Você também pode criar controles vinculados a dados arrastando campos ou tabelas para o formulário a partir dos seguintes locais:
 - Project Manager Window
- Database Designer (Visual FoxPro)
- Data Environment Designer

O tipo de controle criado ao arrastar um campo ou tabela depende das configurações Field Mappings na guia Properties do Table Designer ou na guia Field Mapping da caixa de diálogo Options.

> **Dica:** Você pode facilitar a vinculação de novos controles a campos em tabelas ou views colocando as tabelas ou views associadas ao seu formulário no data environment do formulário. A propriedade ControlSource na janela Properties exibe uma lista dos campos disponíveis no Data Environment designer para que você possa selecionar aquele que deseja vincular a um controle.
