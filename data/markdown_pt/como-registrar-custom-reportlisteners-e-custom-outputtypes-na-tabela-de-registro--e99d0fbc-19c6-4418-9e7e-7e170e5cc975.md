# Como: registrar Custom ReportListeners e Custom OutputTypes na tabela de registro Report Output Registry

Quando procura um ReportListener registrado, ReportOutput.app verifica os registros em sua tabela de registro com o valor 100 no campo Objtype e um valor no campo ObjCode correspondente ao primeiro parâmetro que recebeu. Ele ignora registros excluídos na tabela e usa registros de registro com o valor 110 no campo ObjType para aplicar filtros adicionais que limitam os registros a serem considerados.

Quando identifica o registro correto, ReportOutput.app usa os outros campos no registro para instanciar uma referência à sua classe derivada de ReportListener designada.

Neste tópico você aprende como criar registros na tabela de registro para que ReportOutput.app possa usá-los neste processo.

> **Observação:** Para obter mais informações sobre a estrutura e o uso da tabela de registro, consulte Understanding the Report Output Application . Para obter informações sobre como criar e especificar uma tabela de registro, consulte How to: Specify an Alternate Report Output Registry Table .

### Para adicionar um novo valor OBJECT TYPE à tabela de registro
- Emita o seguinte comando para criar a tabela de registro padrão de ReportOutput.app em disco: DO (_REPORTOUTPUT) WITH -100 && Write registry file Observação Se a variável de sistema _REPORTOUTPUT contém o nome de um Report Output Application diferente do ReportOutput.app padrão no seu ambiente, substitua HOME() + ReportOutput.app , ou código similar, para invocar o Report Output Application padrão.
- Uma janela BROWSE aparece com registros de registro para diferentes componentes usando esta tabela.
- Examine o registro atual na tabela. Este registro é uma entrada excluída mostrando como criar um registro de registro para novas entradas de ReportListener. Observe que seu valor Objtype é 100 , indicando que fornece informações de classe derivada de ReportListener, e que seu valor Objcode é 999 , significando que ReportOutput.app deve usar este registro quando solicitado um ReportListener do tipo 999 . Observe também o nome da classe no campo Objname ( DebugListener ).
- No menu popup Table, escolha a opção Recall Records…. Na caixa de diálogo que aparece, clique no botão Recall. O registro DebugListener agora está ativo.
- Altere o valor Objcode para um número diferente, como 55 .
- Feche a janela BROWSE.
- Emita o seguinte comando: REPORT FORM ? OBJECT TYPE 55 * substitua o número que você usou na tabela se não foi 55
- O comando REPORT FORM gera saída de depuração.
- Salve o nome da tabela de registro atual para uso posterior, usando o seguinte comando. Para obter mais informações, consulte How to: Use the Report Output Application's Reference Collection . lcOutputRegistry = _oReportOutput["-200"] && current registry

### Para adicionar uma nova definição de classe à tabela de registro
- Abra a tabela de registro que você criou anteriormente e abra uma janela BROWSE. USE (lcOutputRegistry) SHARED ALIAS MyRegistry BROWSE
- No menu popup Table, escolha Append New Record . O novo registro aparece na parte inferior da janela Browse.
- Altere o valor Objtype do novo registro para 100 , indicando seu uso. Altere seu valor Objcode para um valor diferente do que você usou anteriormente, por exemplo 77 .
- No campo Objname, use o nome de uma classe diferente derivada de ReportListener. Por exemplo, você poderia usar " XMLDisplayListener ", uma classe entregue na pasta Foundation Class (FFC).
- No campo Objvalue, use o nome da biblioteca de classes da classe. A extensão de arquivo é opcional se a biblioteca de classes for uma biblioteca de classes visual (.vcx), mas obrigatória se a biblioteca de classes for um programa (.prg). Se você usou " XMLDisplayListener " acima, deve usar " _ReportListener " aqui. Observação Para este exemplo, você pode usar o caminho completo da biblioteca neste campo ou pode SET PATH TO (HOME() + "FFC") quando estiver pronto para invocar ReportOutput.app. No entanto, ao distribuir aplicações, você pode compilar _ReportListener.VCX no seu arquivo de aplicação e ele será encontrado sem um caminho.
- Deixe o campo Objinfo em branco, a menos que a biblioteca de classes que você usou na última etapa esteja compilada em uma aplicação (.app ou .exe) fora do seu próprio código. Por exemplo, no registro DebugListener, o nome Objinfo contém o nome com caminho completo do Report Output Application, porque o campo Objvalue contém o nome da biblioteca compilada em ReportOutput.app. Se você usou "_ReportListener " ou " _ReportListener.vcx " da pasta FFC em Objvalue, este valor deve ficar em branco.
- Feche a tabela de registro. (Embora você a tenha aberto SHARED , em certos casos ReportOutput.app exigirá uso exclusivo da tabela.) Na janela Command: USE IN MyRegistry
- Certifique-se de que a biblioteca de classes que você especificou esteja disponível no seu path, se você não usou seu caminho completo no campo Objvalue anteriormente. Depois use sua classe designada com ReportOutput.app: REPORT FORM ? OBJECT TYPE 77
- O comando REPORT FORM gera saída usando a classe que você especificou.

### Para filtrar registros na tabela de registro
- Abra a tabela de registro que você criou anteriormente e abra uma janela BROWSE. USE (lcOutputRegistry) SHARED ALIAS MyRegistry BROWSE
- Altere o valor Objcode para a classe que você especificou na última seção para corresponder ao valor que você usou para DebugListener anteriormente. Por exemplo: GO BOTTOM REPLACE Objcode WITH 55 Observação Agora você tem duas classes registradas com o mesmo valor de tipo de saída ( 55 ). Por padrão, ReportOutput.app usará a primeira que encontrar (neste caso, DebugListener ). Neste procedimento, você usa um filtro para controlar qual registro ReportOutput.app usa.
- No menu popup Table, escolha Append New Record . O novo registro aparece na parte inferior da janela Browse.
- Altere o valor Objtype do novo registro para 110 , o valor específico para registros de configuração do Report Output Application, e seu valor Objcode para 1 , o valor específico para registros de filtro.
- Registros de filtro não usam os campos Objname e Objvalue. Use a seguinte expressão no campo Objinfo. Esta expressão indica que você não deseja usar nenhuma classe compilada no arquivo ReportOutput.app, você só deseja usar classes externas: ATC("ReportOutput.APP",Objinfo) = 0
- Feche a tabela de registro.
- Solicite ao Report Output Application uma referência a ReportListener usando este tipo. O terceiro parâmetro abaixo garante que qualquer referência em cache deste tipo de tentativas anteriores será liberada e você obterá uma nova avaliação da classe apropriada: oRL = NULL DO (_REPORTOUTPUT) WITH 55, oRL, 2 && reload
- Verifique se a referência da classe é a segunda classe que você adicionou à tabela (no exemplo, XMLDisplayListener): ? oRL.Class
- Abra a tabela de registro novamente e altere o valor Objcode ou faça alguma outra alteração para que o registro não se qualifique mais como filtro: USE (lcOutputRegistry) SHARED ALIAS MyRegistry GO BOTTOM REPLACE Objcode WITH 2 USE && close the table again
- Emita os mesmos comandos que você usou anteriormente e observe que você recebe uma referência a DebugListener desta vez: DO (_REPORTOUTPUT) WITH 55, oRL, 2 && reload ? oRL.Class Dica Filtros podem ser baseados em valores em campos adicionais da tabela de registro, porque campos definidos pelo usuário são permitidos na tabela. Por exemplo, você poderia ter um campo lógico chamado CustPref e filtrar pelo valor CustPref , indicando qual classe o usuário final da sua aplicação prefere usar. Para funcionar como filtro, uma expressão precisa ser algo apropriado para uma instrução LOCATE aplicada à tabela de registro. O Report Output Application usa o filtro em uma instrução LOCATE quando pesquisa a tabela de registro por um registro para um ReportListener do tipo de saída apropriado. Para obter mais informações sobre como o Report Output Application usa o campo Objinfo para aplicar um filtro e sobre como usa o restante das colunas da tabela de registro, consulte Understanding the Report Output Application .
