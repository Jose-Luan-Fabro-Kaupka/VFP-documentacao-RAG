# Integração de objetos e dados

Na maioria dos aplicativos, você pode melhor utilizar o poder do Visual FoxPro integrando objetos e dados. A maioria das classes do Visual FoxPro possui propriedades e métodos que permitem integrar o poder de um gerenciador de banco de dados relacional e um sistema totalmente orientado a objetos.
 Propriedades para integrar classes do Visual FoxPro e dados de banco de dados
| Classe | Propriedades de dados |
| --- | --- |
| Grid | RecordSource , ChildOrder , LinkMaster |
| Todos os outros controles | ControlSource |
| Caixa de listagem e caixa de combinação | ControlSource , RowSource |
| Formulário e conjunto de formulários | DataSession |

Como essas propriedades de dados podem ser alteradas em tempo de design ou de execução, você pode criar controles genéricos com funcionalidade encapsulada que operam em dados diversos.

Para obter mais informações sobre integração de dados e objetos, consulte Criando formulários e Usando controles
