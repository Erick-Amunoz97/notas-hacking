
# waves over lambda

## Descripcion
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 39894`.

## Pistas
1. Flag is not in the usual flag format

## Solucion
el puerto nos da un codigo encryptado:

-------------------------------------------------------------------------------
uoeqwzrx alwl px gojw ynzq - ywlvjleug_px_u_oslw_nzikmz_zqynuqrgjl
-------------------------------------------------------------------------------
klrflle jx ralwl fzx, zx p azsl znwlzmg xzpm xoilfalwl, ral koem oy ral xlz. klxpmlx aonmpeq ojw alzwrx roqlralw rawojqa noeq tlwpomx oy xltzwzrpoe, pr azm ral lyylur oy izhpeq jx ronlwzer oy lzua oralw'x gzwexzem lsle uoespurpoex. ral nzfglwral klxr oy onm ylnnofxazm, kluzjxl oy apx izeg glzwx zem izeg spwrjlx, ral oeng ujxapoe oe mluh, zem fzx ngpeq oe ral oeng wjq. ral zuuojerzer azm kwojqar ojr znwlzmg z koc oy moipeolx, zem fzx rogpeq zwuaprlurjwznng fpra ral koelx. izwnof xzr uwoxx-nlqqlm wpqar zyr, nlzepeq zqzpexr ral ipddle-izxr. al azm xjehle uallhx, z glnnof uoitnlcpoe, z xrwzpqar kzuh, ze zxulrpu zxtlur, zem, fpra apx zwix mwottlm, ral tznix oy azemx ojrfzwmx, wlxliknlm ze pmon. ral mpwlurow, xzrpxyplm ral zeuaow azm qoom aonm, izml apx fzg zyr zem xzr mofe zioeqxr jx. fl lcuazeqlm z ylf fowmx nzdpng. zyrlwfzwmx ralwl fzx xpnleul oe kozwm ral gzuar. yow xoil wlzxoe ow oralw fl mpm eor klqpe razr qzil oy moipeolx. fl ylnr ilmprzrpsl, zem ypr yow eorapeq kjr tnzupm xrzwpeq. ral mzg fzx lempeq pe z xlwleprg oy xrpnn zem lcvjpxprl kwpnnpzeul. ral fzrlw xaoel tzupypuznng; ral xhg, fpraojr z xtluh, fzx z klepqe piilexprg oy jexrzpelm npqar; ral slwg ipxr oe ral lxxlc izwxa fzx nphl z qzjdg zem wzmpzer yzkwpu, 

ocupamos usar una herramienta que decifre el codigo para desencriptarlo.


Despues de pasarlo por el programa nos da el texto decifrado y la llave: 
Decrypted text

------------------------------------------------------------------------------- CONGRATS HERE IS YOUR FLAG - FREQUENCY_IS_C_OVER_LAMBDA_AGFLCGTYUE ------------------------------------------------------------------------------- BETWEEN US THERE WAS, AS I HAVE ALREADY SAID SOMEWHERE, THE BOND OF THE SEA. BESIDES HOLDING OUR HEARTS TOGETHER THROUGH LONG PERIODS OF SEPARATION, IT HAD THE EFFECT OF MAKING US TOLERANT OF EACH OTHER'S YARNSAND EVEN CONVICTIONS. THE LAWYERTHE BEST OF OLD FELLOWSHAD, BECAUSE OF HIS MANY YEARS AND MANY VIRTUES, THE ONLY CUSHION ON DECK, AND WAS LYING ON THE ONLY RUG. THE ACCOUNTANT HAD BROUGHT OUT ALREADY A BOX OF DOMINOES, AND WAS TOYING ARCHITECTURALLY WITH THE BONES. MARLOW SAT CROSS-LEGGED RIGHT AFT, LEANING AGAINST THE MIZZEN-MAST. HE HAD SUNKEN CHEEKS, A YELLOW COMPLEXION, A STRAIGHT BACK, AN ASCETIC ASPECT, AND, WITH HIS ARMS DROPPED, THE PALMS OF HANDS OUTWARDS, RESEMBLED AN IDOL. THE DIRECTOR, SATISFIED THE ANCHOR HAD GOOD HOLD, MADE HIS WAY AFT AND SAT DOWN AMONGST US. WE EXCHANGED A FEW WORDS LAZILY. AFTERWARDS THERE WAS SILENCE ON BOARD THE YACHT. FOR SOME REASON OR OTHER WE DID NOT BEGIN THAT GAME OF DOMINOES. WE FELT MEDITATIVE, AND FIT FOR NOTHING BUT PLACID STARING. THE DAY WAS ENDING IN A SERENITY OF STILL AND EXQUISITE BRILLIANCE. THE WATER SHONE PACIFICALLY; THE SKY, WITHOUT A SPECK, WAS A BENIGN IMMENSITY OF UNSTAINED LIGHT; THE VERY MIST ON THE ESSEX MARSH WAS LIKE A GAUZY AND RADIANT FABRIC,

Key to decrypt the message

HJXZNWYKMUBEDLOIGTVPCQRSFA

Key used to encrypt the message

ZKUMLYQAPBHNIEOTVWXRJSFCGD
```bash()
```

## Bandera

FREQUENCY_IS_C_OVER_LAMBDA_AGFLCGTYUE


## Notas adicionales

| comando | descripcion

## Referencias
