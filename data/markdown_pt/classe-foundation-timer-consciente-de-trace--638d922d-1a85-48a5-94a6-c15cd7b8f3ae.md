# Classe Foundation Timer Consciente de Trace

Este é um utilitário de aplicativo que detecta se a janela de trace está aberta e trata o tempo de depuração adequadamente.

| Categoria | Application |
| --- | --- |
| Catálogo Padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _traceawaretimer |
| Classe Base | Timer |
| Biblioteca de Classes | _app.vcx |
| Classe Pai | _timer |
| Exemplo | ...\Samples\Solution\Ffc\environ.scx |

# Observações

Embora o Visual FoxPro permita ignorar completamente o rastreamento de eventos de timer durante a depuração, isso nem sempre é uma solução apropriada porque às vezes o código em eventos de timer é pertinente ao que você está tentando depurar. Em vez disso, este timer determina se alguma das janelas de depuração está visível e, se estiver, define um intervalo especial lento.

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item da Galeria de Componentes, selecione Adicionar ao Formulário. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca um ícone no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| Propriedade iRegularInterval | Especifica o período de intervalo padrão. Armazenado durante o evento Init e restaurado durante eventos Timer se você alterou o Interval. Padrão: 0 |
| Propriedade iTraceInterval | Especifica um período de intervalo mais lento para usar durante a depuração. Padrão: 10000 |
