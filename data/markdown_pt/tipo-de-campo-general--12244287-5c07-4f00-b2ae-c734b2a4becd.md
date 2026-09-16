# Tipo de campo General

Para armazenar objetos OLE, use o tipo de campo General.

O campo General contém uma referência de dez bytes ao conteúdo real do campo: uma planilha, um documento de processador de texto ou uma imagem, criada por outro aplicativo. Entretanto, o tipo e a quantidade reais de dados dependem do servidor de Automação que cria o objeto e de você vincular ou incorporar o objeto OLE.

Se você vincular um objeto OLE, a tabela conterá apenas a referência aos dados e ao aplicativo que os criou. Se incorporar um objeto OLE, a tabela conterá uma cópia dos dados e uma referência ao aplicativo que os criou. O tamanho de um campo General é limitado apenas pela quantidade de espaço disponível em disco. Para obter mais informações sobre como usar OLE no aplicativo, consulte Compartilhando informações e adicionando OLE.

Para obter as especificações do tipo de campo General, consulte Tipos de dados e campos do Visual FoxPro.
