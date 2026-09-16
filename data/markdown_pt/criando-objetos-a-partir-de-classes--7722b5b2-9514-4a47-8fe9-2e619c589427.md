# Criando objetos a partir de classes

Depois de salvar uma classe visual, você pode criar um objeto baseado nela com a função CREATEOBJECT( ). O exemplo a seguir demonstra a execução de um formulário salvo como definição de classe no arquivo de biblioteca de classes Forms.vcx:
 Criando e exibindo um objeto Form cuja classe foi criada no Form Designer
| Código | Comentários |
| --- | --- |
| SET CLASSLIB TO Forms ADDITIVE | Define a biblioteca de classes para o arquivo .vcx no qual a definição do formulário foi salva. A palavra-chave ADDITIVE impede que este comando feche outras bibliotecas de classes que possam estar abertas. |
| frmTest = CREATEOBJECT("TestForm") | Este código assume que o nome da classe de formulário salva na biblioteca de classes é TestForm. |
| frmTest.Show | Exibe o formulário. |
