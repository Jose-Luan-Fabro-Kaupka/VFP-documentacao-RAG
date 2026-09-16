# Rotinas de manipulação do editor de texto e da área de transferência

Essas rotinas de API permitem manipular o editor de texto do Visual FoxPro, o arquivo aberto no editor de texto e a área de transferência.
 **_EdActive( ) API Library Routine**
Oculta ou mostra o intervalo de seleção ou o ponto de inserção.
**_EdCloseFile( ) API Library Routine**
Fecha o arquivo especificado salvando sem perguntar, solicitando confirmação antes de salvar ou salvando como outro arquivo.
**_EdCopy( ) API Library Routine**
Copia a área selecionada para a área de transferência.
**_EdCut( ) API Library Routine**
Copia a área selecionada para a área de transferência e a exclui do editor.
**_EdDelete( ) API Library Routine**
Exclui a área selecionada. Se não houver seleção, exclui o caractere na posição atual.
**_EdGetChar( ) API Library Routine**
Obtém o caractere em EDPOS.
**_EdGetEnv( ) API Library Routine**
Lê várias configurações do editor.
**_EdGetLineNum( ) API Library Routine**
Retorna o número da linha para a posição EDPOS.
**_EdGetLinePos( ) API Library Routine**
Retorna o EDPOS para o início da linha EDLINE.
**_EdGetPos( ) API Library Routine )**
Retorna a POS atual do editor ou retorna o ponto de ancoragem se houver uma seleção.
**_EdGetStr( ) API Library Routine**
Obtém o texto entre EDPOS e EDPOS inclusive e o coloca em TEXT.
**_EdIndent( ) API Library Routine**
Recua o texto selecionado por int tab stops. Int pode ser negativo para formatar um recuo suspenso.
**_EdInsert( ) API Library Routine**
Insere BYTES de TEXT.
**_EdLastError( ) API Library Routine**
Retorna o número do erro do último erro do editor.
**_EdOpenFile( ) API Library Routine**
Inicia uma sessão de editor neste arquivo.
**_EdPaste( ) API Library Routine**
Copia o texto da área de transferência para o editor na posição atual.
**_EdPosInView( ) API Library Routine**
Retorna TRUE se a posição do editor estiver visível.
**_EdRedo( ) API Library Routine**
Refaz o desfazer mais recente.
**_EdRevert( ) API Library Routine**
Reverte para um arquivo salvo.
**_EdSave( ) API Library Routine**
Salva o arquivo sem fechar a janela de edição.
**_EdScrollToPos( ) API Library Routine**
Garante que o EDPOS passado esteja na tela, mas não move o ponto de inserção. BOOL significa centralizar EDPOS verticalmente.
**_EdScrollToSel( ) API Library Routine**
Garante que o ponto de ancoragem da seleção esteja na tela. BOOL significa centralizar o ponto de ancoragem verticalmente.
**_EdSelect( ) API Library Routine**
Seleciona o intervalo de EDPOS a EDPOS. Para mover o ponto de inserção, defina ambos os EDPOS iguais.
**_EdSendKey( ) API Library Routine**
Simula a pressão de tecla dada por int .
**_EdSetEnv( ) API Library Routine**
Define várias configurações do editor.
**_EdSetPos( ) API Library Routine**
Move o ponto de inserção e tem o efeito colateral de desmarcar qualquer coisa atualmente selecionada.
**_EdSkipLines( ) API Library Routine**
Move o ponto de inserção de EDPOS para o início da linha int .
**_EdUndo( ) API Library Routine**
Desfaz as alterações mais recentes.
**_EdUndoOn( ) API Library Routine**
Agrupa as ações realizadas após _EdUndoOn( ) ser passado até ser passado novamente como uma única ação para fins de desfazer.
