# Classe Foundation Pool Manager

A Classe Foundation Pool Manager gerencia um pool, ou coleção, de objetos de uma única classe. Quando você precisa usar um objeto repetidamente por um curto período, use a classe Pool Manager.

| Categoria | Informações da classe |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _poolmanager |
| Classe base | Custom |
| Biblioteca de classes | _poolmanager.vcx |
| Classe pai | Custom |
| Exemplo | ...\Samples\Solution\Ffc\_PoolManager.scx |

# Observações

Esta classe funciona melhor se criar uma instância do objeto leva mais tempo do que obter uma instância existente. Este é comumente o caso para os seguintes tipos de classes:
 - Classes não leves como a classe Form do Visual FoxPro.
- Classes que contêm código intensivo em recursos no evento Init do formulário.
- Classes que fazem uso de recursos externos, como uma conexão de banco de dados, servidor de automação ou serviço Web XML.

Você pode adicionar a classe Pool Manager aos designers Form ou Class a partir da Toolbox ou a um projeto. Quando você adiciona a classe Pool Manager a um projeto, pode adicionar a classe ou criar uma subclasse.

A classe Pool Manager usa a classe base Collection do Visual FoxPro para armazenar referências de objetos. Para obter mais informações, consulte Classe Collection.

Para obter mais informações sobre o uso de classes foundation, consulte Guidelines for Using Visual FoxPro Foundation Classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cClass | Nome da classe em pool. Você também pode definir esta propriedade passando-a como o primeiro parâmetro ao criar o objeto pool manager. Padrão: None |
| Propriedade cClassLibrary | Biblioteca que contém a classe em pool. A propriedade cClassLibrary pode apontar para uma biblioteca de classes visuais ou um arquivo de programa. Você pode alterar esta propriedade passando-a como o segundo parâmetro ao criar o objeto pool manager. Padrão: None |
| Propriedade lRaiseEvent | Se True (.T.), dispara os eventos ObjectRequested e ObjectReturned. Se você não precisa desses eventos para aumentar o desempenho, defina esta propriedade como False (.F.). Padrão: .T. |
| Propriedade nObjectsCreated | Incrementada cada vez que um objeto é criado Padrão: 0 |
| Método Get | Retorna uma referência de objeto a um objeto em pool. Todos os parâmetros são passados ao evento Init de um objeto recém-criado e ao evento ObjectRequested. Sintaxe : Get( Param1, Param2, ...) Retorno : Object Argumentos : Deve passar parâmetros por valor e não pode passar matrizes a um objeto em pool. |
| Método Free | Retorna um objeto ao pool, tornando-o disponível para a próxima chamada do método Get. Sintaxe: Free(@oObject) Retorno: None Argumentos: oObject é uma referência de objeto obtida anteriormente do método Get. O objeto pode ser passado por referência. |
| Evento ObjectRequested | Disparado quando um objeto é solicitado. Você pode usar este evento para inicializar um objeto baseado nos parâmetros atuais. Quando um objeto em pool se vincula a este evento, o evento é disparado para cada objeto, não apenas para o objeto em si. Sintaxe: ObjectRequested( oObject, Param1, Param2, ...) Retorno: None Argumentos: oObject é uma referência ao objeto em pool que é retornado ao chamador. Todos os parâmetros do método Get são passados a este evento como parâmetros adicionais. |
| Evento ObjectReturned | Disparado quando um objeto é retornado ao pool chamando o método Free. Quando um objeto em pool se vincula a este evento, o evento é disparado para cada objeto, não apenas para o objeto em si. Sintaxe: ObjectReturned(oObject) Retorno: None Argumentos: oObject é uma referência ao objeto em pool. |
