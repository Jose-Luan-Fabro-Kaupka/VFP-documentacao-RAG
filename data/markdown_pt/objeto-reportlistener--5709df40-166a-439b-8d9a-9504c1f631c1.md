# Objeto ReportListener

Fornece assistência de objeto aos comandos REPORT FORM e LABEL FORM.

```foxpro
ReportListener
```

# Observações

Enquanto o Report Engine processa os dados e o layout do seu relatório ou etiqueta, ele envia informações para um objeto ReportListener, em vez de enviar a saída diretamente para uma impressora ou dispositivo de visualização. O ReportListener "escuta" essas instruções e trata da responsabilidade de avaliar e renderizar o conteúdo do seu relatório de forma apropriada para o seu dispositivo de saída.

A classe ReportListener foi projetada especificamente para comunicação bidirecional com o Report Engine durante todo o processo de geração de saída. Usando um ReportListener, você pode:
 - Escrever código para cada evento de renderização de elemento e banda conforme o processo de geração de relatório avança pelo escopo de registros do relatório.
- Alterar a posição dos elementos de layout sendo renderizados ou seu conteúdo.
- Fornecer feedback ao usuário sobre a execução do relatório.
- Fazer solicitações ao report engine para imagens de página, para serem exibidas na tela ou salvas em disco.
- Gerenciar uma sessão de dados privada, mantendo informações da tabela de definição de relatório ou etiqueta (.frx ou .lbx), para investigar atributos de objetos e bandas de relatório.
- Comunicar-se diretamente com o dispositivo para o qual o Report System renderiza a saída.
- Investigar todas as cláusulas do comando REPORT FORM e alterar algumas dessas cláusulas dinamicamente.

O Visual FoxPro oferece várias formas diferentes de anexar um ReportListener aos comandos REPORT FORM ou LABEL FORM:
 - Use a cláusula OBJECT no comando. Para obter mais informações, consulte REPORT FORM Command .
- Use a cláusula OBJECT TYPE <N>, especificando um ListenerType numérico para o tipo de saída que você deseja criar. O Report Engine solicita um ReportListener do ListenerType apropriado ao Report Output Application. Para obter mais informações, consulte ListenerType Property e Report Output Application .
- Use SET REPORTBEHAVIOR 90 para habilitar assistência de objeto em todos os comandos REPORT FORM e LABEL FORM. Para obter mais informações, consulte SET REPORTBEHAVIOR Command .

Usando ReportListeners, você pode enviar saída para vários dispositivos de saída em uma execução de relatório e pode adicionar tipos de saída, como HTML, que os relatórios do Visual FoxPro não suportam nativamente. Para obter mais informações, consulte ReportListener Foundation Classes e Extending Reports at Run Time.
