# Rotinas de gerenciamento de memória

Essas rotinas de API permitem manipular e alocar memória para suas funções de API.
 **_Alloca( ) API Library Routine**
Aloca um bloco de espaço na pilha para a rotina chamadora. A memória é liberada automaticamente quando a rotina termina.
**_AllocHand( ) API Library Routine**
Retorna um novo MHANDLE de tamanho hsize. Um valor zero é retornado quando não há memória suficiente para atender à solicitação. A memória alocada com _AllocHand( ) não é inicializada.
**_FreeHand( ) API Library Routine**
Libera um MHANDLE previamente alocado por meio de rotinas como _AllocHand( ).
**_GetHandSize( ) API Library Routine**
Retorna o número utilizável de bytes associados a um MHANDLE.
**_HandToPtr( ) API Library Routine**
Traduz um MHANDLE em um ponteiro FAR (32 bits), que aponta para a memória alocada a esse MHANDLE.
**_HLock( ) API Library Routine**
Bloqueia um MHANDLE para impedir que ele se mova se o Visual FoxPro exigir reorganização de memória.
**_HUnLock( ) API Library Routine**
Desbloqueia um MHANDLE, permitindo que ele participe da reorganização de memória do Visual FoxPro.
**_MemAvail( ) API Library Routine**
Retorna True se uma solicitação para alocar um handle de tamanho bytes for bem-sucedida. Caso contrário, _MemAvail( ) retorna False.
**_MemCmp( ) API Library Routine**
Compara duas áreas de memória de length bytes.
**_MemFill( ) API Library Routine**
Preenche uma área de memória começando no local apontado por ptr com length cópias do byte em character.
**_MemMove( ) API Library Routine**
Copia length bytes de src para dest.
**_SetHandSize( ) API Library Routine**
Altera a quantidade de memória alocada a um MHANDLE. A rotina retorna True se a realocação for bem-sucedida ou False se a realocação falhar.
