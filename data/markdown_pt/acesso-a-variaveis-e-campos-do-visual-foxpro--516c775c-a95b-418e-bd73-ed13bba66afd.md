# Acesso a variáveis e campos do Visual FoxPro

Você pode acessar variáveis do Visual FoxPro ou valores de campos em seu controle ActiveX ou função FLL, tanto para leitura quanto para definição. Além disso, você pode criar novas variáveis que podem ser acessadas dentro do Visual FoxPro.

Variáveis e campos são disponibilizados no Visual FoxPro em uma tabela de nomes, que é uma matriz contendo os nomes de todas as variáveis e campos atualmente definidos. Você pode acessar um elemento individual na matriz usando um índice de tabela de nomes (NTI). Uma função especial da API, _NameTableIndex( ) API Library Routine, retorna o índice de uma variável ou campo existente com base em um nome que você fornece. Depois de determinar o NTI para uma determinada variável, você pode lê-la usando a função da API _Load( ) API Library Routine ou defini-la usando a função da API _Store( ) API Library Routine. Para criar uma nova variável, você pode chamar a função da API _NewVar( ) API Library Routine.

Para acessar variáveis ou campos do Visual FoxPro, você usa as estruturas Value e Locator definidas em Pro_ext.h. Se você estiver criando uma biblioteca FLL, pode usar a mesma técnica que usou para acessar parâmetros passados para suas funções. Para obter detalhes sobre as estruturas Value e Locator, consulte Parâmetros em bibliotecas externas.

O exemplo a seguir ilustra como você pode usar as estruturas Value e Locator em um controle ActiveX para acessar variáveis do Visual FoxPro.

```foxpro
long CFoxtlibCtrl::TLGetTypeAttr(long pTypeInfo, LPCTSTR szArrName)
{
  int nResult = 1;
  TYPEATTR *lpTypeAttr;
  Locator loc;
  Value val;
  OLECHAR szGuid[128];
  char *szBuff;
__try {
   if (_FindVar(_NameTableIndex(( char *)szArrName),-1,&loc)) {
      ((ITypeInfo *)pTypeInfo)->GetTypeAttr(&lpTypeAttr);
      if (_ALen(loc.l_NTI, AL_ELEMENTS) < 16) {
         _Error(631); //Array argument not of proper size.
      }
      //1 = Guid
      StringFromGUID2(lpTypeAttr->guid, (LPOLESTR )&szGuid,sizeof(szGuid));
      OLEOleToAnsiString(szGuid,&szBuff);
      val.ev_type = 'C';
      val.ev_length = strlen(szBuff);
      val.ev_handle = _AllocHand(val.ev_length);
      _HLock(val.ev_handle);
      _MemMove((char *) _HandToPtr( val.ev_handle ), szBuff, val.ev_length);
      OLEFreeString((void **)&szBuff);
      _HUnLock(val.ev_handle);
      loc.l_sub1 = 1;
      _Store(&loc,&val);
      _FreeHand(val.ev_handle);
      //2 = LCID
      loc.l_sub1 = 2;
      val.ev_type = 'I';
      val.ev_long = lpTypeAttr->lcid;
      _Store(&loc,&val);
      // code for values 3 - 16 here
      ((ITypeInfo *)pTypeInfo) -> ReleaseTypeAttr(lpTypeAttr);
      }
   } __except  (EXCEPTION_EXECUTE_HANDLER) {
      nResult = 0;
   }
return nResult;
```
