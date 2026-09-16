# Como: especificar a página de código de um arquivo .dbf

Quando você cria arquivos .dbf, o Visual FoxPro automaticamente atribui marcas de página de código para que você possa identificar quais páginas de código eles usam. No entanto, se você usar arquivos .dbf de versões anteriores do FoxPro, eles podem não ter marcas de página de código.

Você pode determinar se um arquivo .dbf tem uma marca de página de código usando a função CPDBF( ) depois de abrir o arquivo ou fazendo o Visual FoxPro verificar quando você abrir o arquivo.

### Para verificar marcas de página de código automaticamente
- No menu Tools, escolha Options.
- Selecione a guia Data.
- Defina a caixa de seleção Prompt for code page, se ainda não estiver definida. Para salvar essa configuração para sessões futuras do Visual FoxPro, escolha Set as Default. Dica Em vez de definir a caixa de seleção Prompt for code page, você pode usar o comando SET CPDIALOG para verificar páginas de código.

Se um arquivo não tiver uma marca de página de código, você deve adicionar uma marca, conforme descrito na seção a seguir.

# Adicionando marcas de página de código

Se você usar um arquivo .dbf de uma versão anterior do FoxPro, o arquivo pode não ter uma marca de página de código; sem essa marca, o arquivo pode não ser exibido corretamente. Se a verificação automática de página de código estiver habilitada, ao abrir o arquivo você poderá saber se ele tem uma marca de página de código. Se não tiver, você pode adicionar uma.

### Para adicionar manualmente uma marca de página de código a um arquivo .dbf
- Certifique-se de que a verificação automática de página de código esteja em vigor (consulte o procedimento anterior).
- Abra o arquivo. Se o arquivo não tiver uma marca de página de código, a caixa de diálogo Code Page aparece.
- Escolha a página de código apropriada.
- Visualize o arquivo para ver se você atribuiu a página de código correta. Se não conseguir ver alguns dos dados, ou se não reconhecer alguns deles, a página de código não está correta.
- Se a página de código estiver incorreta, remova a marca de página de código usando o programa CPZERO no diretório Visual FoxPro Tools\Cpzero.
- Repita este procedimento até que a página de código esteja correta. Observação Arquivos de texto como programas (.prg) e consultas (.qpr) não têm marcas de página de código. Isso significa que você não pode identificar quais páginas de código os arquivos usam. No entanto, se você incluir esses arquivos em um projeto, o projeto pode manter um registro das páginas de código usadas. Para obter mais informações, consulte Como: especificar a página de código de um arquivo de texto.

# Removendo marcas de página de código

Se um arquivo .dbf não for exibido corretamente, ele pode ter a marca de página de código errada. Você pode remover a marca de página de código com o programa CPZERO localizado em Tools\Cpzero. Executar CPZERO define a página de código como 0, ou seja, nenhuma.

### Para remover uma marca de página de código
- Execute CPZERO usando a seguinte sintaxe: DO CPZERO WITH " filename ", 0 Observação Ao remover a marca de página de código de um arquivo .dbf, os dados no arquivo não mudam. Para alterar a página de código dos dados, você deve marcar o arquivo com a página de código correta.

# Alterando marcas de página de código

Você pode alterar a página de código de um arquivo .dbf removendo sua marca de página de código e, em seguida, adicionando uma nova, copiando o arquivo para outro arquivo ou usando o programa CPZERO.

### Para alterar a página de código de um arquivo .dbf copiando o arquivo
- Use o comando COPY TO, especificando a página de código de destino com a cláusula AS. (Para definir a página de código como a página de código do sistema atual, omita a cláusula AS.) Por exemplo, para copiar Test.dbf para Test866.dbf, alterando a página de código para 866, use os seguintes comandos: USE TEST.DBF COPY TO TEST866.DBF AS 866

Quando COPY TO for concluído, os dados no arquivo resultante terão a nova página de código.

### Para alterar uma marca de página de código usando CPZERO
- Execute CPZERO usando a seguinte sintaxe: DO CPZERO WITH " filename ", newCodePage Observação Alguns caracteres não podem ser traduzidos entre páginas de código com sucesso. Além disso, o Visual FoxPro não suporta algumas traduções de página de código. Sempre verifique os resultados de uma alteração de página de código para ter certeza de que seus dados foram traduzidos com sucesso.
