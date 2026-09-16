# Como: exibir definições de código

Ao realizar uma pesquisa de referência de código, você pode localizar a definição de um elemento de código que encontrou no arquivo de programa atual, se a definição existir. Para obter mais informações, consulte Como: pesquisar referências de código.

### Para exibir a definição de um elemento de código
- Abra o arquivo de programa na localização do elemento de código.
- Clique duas vezes no texto do elemento de código para selecioná-lo.
- Clique com o botão direito para exibir o menu de atalho e selecione View Definition .

Você também pode chamar View Definition usando o comando DO (_FOXREF) WITH... Para obter mais informações, consulte Variável de sistema _FOXREF.

View Definition primeiro pesquisa outras referências de arquivos externos que estão no arquivo de origem, seguidas por arquivos no projeto ativo. Se existirem várias definições de elementos de código, a janela Go To Definition aparece para que você possa selecionar uma definição.

Se a definição não puder ser encontrada em um arquivo do projeto ativo, View Definition pesquisa outros projetos ou pastas abertos. Se a definição for encontrada em uma dessas localizações, a janela Go To Definition abre para você selecionar a localização correta. Para obter mais informações, consulte Janela Go To Definition.

Se o elemento de código for definido pelo usuário e a definição for encontrada, o Visual FoxPro abre uma janela de edição na localização da definição. Se o item que você selecionar for um comando ou função nativo do Visual FoxPro, a Ajuda do Visual FoxPro abre o tópico de ajuda desse item. Se o item que você selecionar for um nome de arquivo, como para uma instrução #INCLUDE ou comando SET PROCEDURE, o Visual FoxPro abre o arquivo.
