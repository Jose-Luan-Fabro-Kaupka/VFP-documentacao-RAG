# Como: fazer check-out de arquivos

Quando você trabalha em um projeto com controle de código-fonte, o Visual FoxPro pode solicitar que você faça check-out de arquivos quando os modifica abrindo o editor apropriado. Por exemplo, se você selecionar um formulário e escolher Modify para abrir o Form Designer, o Visual FoxPro pode primeiro solicitar que você faça check-out dos arquivos do formulário. (Se você não fizer check-out dos arquivos, o formulário é exibido no Form Designer, mas é somente leitura.)

No entanto, você também pode fazer check-out de arquivos manualmente, o que é útil se deseja acesso exclusivo ao arquivo, mas não quer abrir o editor do arquivo no momento. Você pode fazer isso, por exemplo, se pretende trabalhar com um arquivo fora do local.

### Para especificar que o Visual FoxPro solicite check-out de arquivos sendo modificados
- Na guia Projects da caixa de diálogo Options, certifique-se de que a opção Check out files upon modify está marcada e escolha OK . Para tornar esta configuração o padrão, escolha Set as Default e depois OK .

### Para fazer check-out de um arquivo manualmente
- No Project Manager , selecione o arquivo com o qual deseja trabalhar.
- No menu Project, escolha Source Control e depois Check Out .
- Na caixa de diálogo Check Out Files , selecione o arquivo ou arquivos com os quais deseja trabalhar e clique em OK .
