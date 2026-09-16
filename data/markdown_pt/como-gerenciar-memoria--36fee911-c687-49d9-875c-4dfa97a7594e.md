# Como: gerenciar memória

Você pode alocar e gerenciar memória usando a API do Visual FoxPro.

> **Observação:** As técnicas descritas se aplicam tanto a controles ActiveX quanto a bibliotecas FLL.

### Para alocar e usar memória
- Aloque um handle com _AllocHand( ) .
- Bloqueie o handle com _HLock( ) .
- Converta o handle em um ponteiro com _HandToPtr( ) .
- Referencie a memória usando o ponteiro.
- Desbloqueie o handle com _HUnLock( ) . Observação Para evitar corrupção de arquivo memo, não grave em um arquivo memo antes de chamar _AllocMemo( ) .

Para endereçar a memória alocada, suas rotinas de API devem converter o handle em um ponteiro chamando a rotina _HandToPtr( ) da API Library Routine. Mesmo que o gerenciador de memória do Visual FoxPro precise reorganizar a memória para obter mais memória contígua para solicitações subsequentes de memória, o handle permanece o mesmo. Rotinas que aumentam, reduzem, liberam e bloqueiam alocações de memória também são fornecidas.

Ao criar rotinas externas, tente minimizar o uso de memória. Se você criar uma rotina externa que aloca memória dinamicamente, tente usar a menor quantidade de memória possível. Tenha especial cuidado ao bloquear grandes alocações de memória por longos períodos de tempo. Lembre-se de desbloquear handles de memória com _HUnLock( ) API Library Routine quando eles não precisarem mais estar bloqueados, porque o desempenho do Visual FoxPro pode ser afetado adversamente por handles de memória bloqueados.

> **Cuidado:** O uso excessivo de memória dinâmica priva o Visual FoxPro de memória para buffers, janelas, menus e assim por diante, e degrada o desempenho, porque a memória fornecida para atender solicitações de API é gerenciada pelo gerenciador de memória do Visual FoxPro. Alocar handles grandes e retê-los pode fazer com que o Visual FoxPro fique sem memória e encerre anormalmente. O ambiente Visual FoxPro não tem proteção de memória. A rotina externa de API não pode fornecer toda a validação inerente a um programa Visual FoxPro padrão. Se você corromper a memória, receberá mensagens como "Transgressed handle," "Internal consistency error," e "Transgressed node during compaction."

A função a seguir de uma biblioteca FLL ilustra a alocação de memória. O exemplo usa _RetDateStr( ) API Library Routine para retornar um tipo Date do Visual FoxPro (supondo que o parâmetro Character seja uma data válida):

```foxpro
#include <Pro_ext.h>
void dates(ParamBlk  *parm)
{
   MHANDLE mh;
   char *instring;
   if ((mh = _AllocHand(parm->p[0].val.ev_length + 1)) == 0) {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   instring = _HandToPtr(parm->p[0].val.ev_handle);
   instring[parm->p[0].val.ev_length] = '\0';
   _RetDateStr(instring);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"DATES", (FPFI) dates, 1, "C"}
};
FoxTable _FoxTable = {
   (FoxTable *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
