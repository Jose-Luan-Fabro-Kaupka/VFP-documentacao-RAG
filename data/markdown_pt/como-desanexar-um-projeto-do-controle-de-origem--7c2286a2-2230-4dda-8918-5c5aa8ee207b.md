# Como: desanexar um projeto do controle de origem

Se você não deseja mais controlar os arquivos em um projeto, pode desanexar o projeto do controle de origem. Ao fazer isso, os arquivos permanecem no projeto de controle de origem para que outros desenvolvedores possam continuar a usá-los e para que você possa examinar o histórico ou usá-los com outros projetos.

Se você tem arquivos de projeto no seu computador marcados como somente leitura — ou seja, você tem cópias dos arquivos, mas eles não estão em check-out — pode remover o atributo somente leitura quando o projeto for desanexado do controle de origem.

> **Observação:** Quando você desanexa um projeto do controle de origem, você rompe o vínculo entre seus arquivos de projeto locais e o projeto controlado por origem, e seus arquivos locais passam a ser leitura/gravação. Certifique-se de instituir procedimentos manuais de controle de versão após desanexar o projeto, ou você corre os riscos inerentes ao trabalhar com arquivos que não estão sob controle de origem.

### Para desanexar um projeto do controle de origem
- Faça check-in de todos os arquivos sob controle de origem.
- No menu Project, escolha Detach Project from Source Control.
