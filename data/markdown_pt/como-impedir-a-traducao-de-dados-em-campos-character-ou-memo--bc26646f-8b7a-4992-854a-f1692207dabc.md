# Como: impedir a tradução de dados em campos Character ou Memo

Em alguns casos, você não deseja a tradução automática de página de código. Por exemplo, se um campo Character contém uma senha criptografada, você não deseja que o Visual FoxPro traduza automaticamente a senha, pois isso a alteraria.

### Para impedir a tradução de dados em um campo Character ou Memo
- Abra o projeto que contém a tabela.
- Selecione a tabela.
- Escolha o botão Modify. O Table Designer (Visual FoxPro) é exibido.
- Selecione o campo cujos dados você deseja proteger.
- Na lista Type, selecione Character (Binary) para um campo Character ou Memo (Binary) para um campo memo.
- Escolha OK e, em seguida, escolha Yes para tornar as alterações permanentes.
- Verifique as alterações exibindo a estrutura da tabela com o comando DISPLAY STRUCTURE. Como alternativa, use o comando MODIFY STRUCTURE para proteger os campos apropriados.

Você também pode impedir a tradução de caracteres selecionados em arquivos de texto usando a função CHR( ).
