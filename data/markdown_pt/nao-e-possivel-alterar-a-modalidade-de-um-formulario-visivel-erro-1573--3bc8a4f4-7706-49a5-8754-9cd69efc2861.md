# Não é possível alterar a modalidade de um formulário visível (Erro 1573)

O parâmetro nStyle do método Show não pode ser alterado enquanto um formulário estiver visível.
 - Você está chamando o método Show de um formulário com um parâmetro enquanto o formulário está visível. Altere a modalidade do formulário quando ele não estiver visível, usando código semelhante ao seguinte: Form1.Hide Form1.Show(nStyle)
