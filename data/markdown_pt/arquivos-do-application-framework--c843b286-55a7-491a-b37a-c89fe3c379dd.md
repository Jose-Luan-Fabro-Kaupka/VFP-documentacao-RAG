# Arquivos do Application Framework

Um application framework inclui o arquivo de projeto e uma biblioteca de classes inicial derivada das classes base do Visual FoxPro, pronta para você preencher com tabelas e documentos novos ou existentes.
 **Master Include File**
Este arquivo #INCLUDE comum é usado por componentes com configurações e cadeias de caracteres. O arquivo também inclui o valor APP_GLOBAL, o nome usado pelos componentes para referência.
**Configuration File**
Um Config.fpw opcional usado para aplicações como formulários de nível superior para implementar configurações como SCREEN=OFF.
**Project Hook Class**
Controla eventos relacionados ao projeto, como adicionar novos arquivos. Também pode acessar o Application Builder para definir ações e propriedades de interação de arquivos na aplicação.
**Application Meta Table**
Contém informações como configurações de projeto feitas ou usadas pelo Application Builder e Project Hooks.
**Application Builder**
Facilita a adição de componentes ao projeto e a definição de propriedades como opções de navegação.

O framework permite especificar se deseja criar uma aplicação completa ou apenas um application framework. Se escolher criar uma aplicação completa, pode incluir na aplicação um banco de dados e formulários ou relatórios que já criou, ou pode criar uma nova aplicação do zero usando um modelo de banco de dados. Se escolher criar um framework, pode voltar depois e adicionar componentes ao framework.
