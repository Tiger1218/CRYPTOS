

# This file was *autogenerated* from the file crypto1_solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_50630448182626893495464810670525602771527685838257974610483435332349728792396826591558947027657819590790590829841808151825744184405725893984330719835572507419517069974612006826542638447886105625739026433810851259760829112944769101557865474935245672310638931107468523492780934936765177674292815155262435831801499197874311121773797041186075024766460977392150443756520782067581277504082923534736776769428755807994035936082391356053079235986552374148782993815118221184577434597115748782910244569004818550079464590913826457003648367784164127206743005342001738754989548942975587267990706541155643222851974488533666334645686774107285018775831028090338485586011974337654011592698463713316522811656340001557779270632991105803230612916547576906583473846558419296181503108603192226769399675726201078322763163049259981181392937623116600712403297821389573627700886912737873588300406211047759637045071918185425658854059386338495534747471846997768166929630988406668430381834420429162324755162023168406793544828390933856260762963763336528787421503582319435368755435181752783296341241853932276334886271511786779019664786845658323166852266264286516275919963650402345264649287569303300048733672208950281055894539145902913252578285197293 = Integer(50630448182626893495464810670525602771527685838257974610483435332349728792396826591558947027657819590790590829841808151825744184405725893984330719835572507419517069974612006826542638447886105625739026433810851259760829112944769101557865474935245672310638931107468523492780934936765177674292815155262435831801499197874311121773797041186075024766460977392150443756520782067581277504082923534736776769428755807994035936082391356053079235986552374148782993815118221184577434597115748782910244569004818550079464590913826457003648367784164127206743005342001738754989548942975587267990706541155643222851974488533666334645686774107285018775831028090338485586011974337654011592698463713316522811656340001557779270632991105803230612916547576906583473846558419296181503108603192226769399675726201078322763163049259981181392937623116600712403297821389573627700886912737873588300406211047759637045071918185425658854059386338495534747471846997768166929630988406668430381834420429162324755162023168406793544828390933856260762963763336528787421503582319435368755435181752783296341241853932276334886271511786779019664786845658323166852266264286516275919963650402345264649287569303300048733672208950281055894539145902913252578285197293); _sage_const_15640629897212089539145769625632189125456455778939633021487666539864477884226491831177051620671080345905237001384943044362508550274499601386018436774667054082051013986880044122234840762034425906802733285008515019104201964058459074727958015931524254616901569333808897189148422139163755426336008738228206905929505993240834181441728434782721945966055987934053102520300610949003828413057299830995512963516437591775582556040505553674525293788223483574494286570201177694289787659662521910225641898762643794474678297891552856073420478752076393386273627970575228665003851968484998550564390747988844710818619836079384152470450659391941581654509659766292902961171668168368723759124230712832393447719252348647172524453163783833358048230752476923663730556409340711188698221222770394308685941050292404627088273158846156984693358388590950279445736394513497524120008211955634017212917792675498853686681402944487402749561864649175474956913910853930952329280207751998559039169086898605565528308806524495500398924972480453453358088625940892246551961178561037313833306804342494449584581485895266308393917067830433039476096285467849735814999851855709235986958845331235439845410800486470278105793922000390078444089105955677711315740050638 = Integer(15640629897212089539145769625632189125456455778939633021487666539864477884226491831177051620671080345905237001384943044362508550274499601386018436774667054082051013986880044122234840762034425906802733285008515019104201964058459074727958015931524254616901569333808897189148422139163755426336008738228206905929505993240834181441728434782721945966055987934053102520300610949003828413057299830995512963516437591775582556040505553674525293788223483574494286570201177694289787659662521910225641898762643794474678297891552856073420478752076393386273627970575228665003851968484998550564390747988844710818619836079384152470450659391941581654509659766292902961171668168368723759124230712832393447719252348647172524453163783833358048230752476923663730556409340711188698221222770394308685941050292404627088273158846156984693358388590950279445736394513497524120008211955634017212917792675498853686681402944487402749561864649175474956913910853930952329280207751998559039169086898605565528308806524495500398924972480453453358088625940892246551961178561037313833306804342494449584581485895266308393917067830433039476096285467849735814999851855709235986958845331235439845410800486470278105793922000390078444089105955677711315740050638); _sage_const_1 = Integer(1); _sage_const_65537 = Integer(65537); _sage_const_10 = Integer(10); _sage_const_54372504422578163821842661820992519574720094743792971271580036722643401901785509893350887232430564989 = Integer(54372504422578163821842661820992519574720094743792971271580036722643401901785509893350887232430564989)
n = _sage_const_50630448182626893495464810670525602771527685838257974610483435332349728792396826591558947027657819590790590829841808151825744184405725893984330719835572507419517069974612006826542638447886105625739026433810851259760829112944769101557865474935245672310638931107468523492780934936765177674292815155262435831801499197874311121773797041186075024766460977392150443756520782067581277504082923534736776769428755807994035936082391356053079235986552374148782993815118221184577434597115748782910244569004818550079464590913826457003648367784164127206743005342001738754989548942975587267990706541155643222851974488533666334645686774107285018775831028090338485586011974337654011592698463713316522811656340001557779270632991105803230612916547576906583473846558419296181503108603192226769399675726201078322763163049259981181392937623116600712403297821389573627700886912737873588300406211047759637045071918185425658854059386338495534747471846997768166929630988406668430381834420429162324755162023168406793544828390933856260762963763336528787421503582319435368755435181752783296341241853932276334886271511786779019664786845658323166852266264286516275919963650402345264649287569303300048733672208950281055894539145902913252578285197293 
c = _sage_const_15640629897212089539145769625632189125456455778939633021487666539864477884226491831177051620671080345905237001384943044362508550274499601386018436774667054082051013986880044122234840762034425906802733285008515019104201964058459074727958015931524254616901569333808897189148422139163755426336008738228206905929505993240834181441728434782721945966055987934053102520300610949003828413057299830995512963516437591775582556040505553674525293788223483574494286570201177694289787659662521910225641898762643794474678297891552856073420478752076393386273627970575228665003851968484998550564390747988844710818619836079384152470450659391941581654509659766292902961171668168368723759124230712832393447719252348647172524453163783833358048230752476923663730556409340711188698221222770394308685941050292404627088273158846156984693358388590950279445736394513497524120008211955634017212917792675498853686681402944487402749561864649175474956913910853930952329280207751998559039169086898605565528308806524495500398924972480453453358088625940892246551961178561037313833306804342494449584581485895266308393917067830433039476096285467849735814999851855709235986958845331235439845410800486470278105793922000390078444089105955677711315740050638 
# print(factor(n))
primes = "2148630611 * 2157385673 * 2216411683 * 2223202649 * 2230630973 * 2240170147 * 2278427881 * 2293226687 * 2322142411 * 2365186141 * 2371079143 * 2388797093 * 2424270803 * 2436598001 * 2444333767 * 2459187103 * 2491570349 * 2510750149 * 2525697263 * 2572542211 * 2575495753 * 2602521199 * 2636069911 * 2647129697 * 2657405087 * 2661720221 * 2672301743 * 2682518317 * 2695978183 * 2703629041 * 2707095227 * 2710524571 * 2719924183 * 2724658201 * 2733527227 * 2746638019 * 2752963847 * 2753147143 * 2772696307 * 2824169389 * 2841115943 * 2854321391 * 2858807113 * 2932152359 * 2944722127 * 2944751701 * 2949007619 * 2959325459 * 2963383867 * 3012495907 * 3013564231 * 3035438359 * 3056689019 * 3057815377 * 3083881387 * 3130133681 * 3174322859 * 3177943303 * 3180301633 * 3200434847 * 3228764447 * 3238771411 * 3278196319 * 3279018511 * 3285444073 * 3291377941 * 3303691121 * 3319529377 * 3335574511 * 3346647649 * 3359249393 * 3380851417 * 3398567593 * 3411506629 * 3417563069 * 3453863503 * 3464370241 * 3487902133 * 3488338697 * 3522596999 * 3539958743 * 3589083991 * 3623581037 * 3625437121 * 3638373857 * 3646337561 * 3648309311 * 3684423151 * 3686523713 * 3716991893 * 3721186793 * 3760232953 * 3789253133 * 3789746923 * 3811207403 * 3833706949 * 3833824031 * 3854175641 * 3860554891 * 3861767519 * 3865448239 * 3923208001 * 3941016503 * 3943871257 * 3959814431 * 3961738709 * 3978832967 * 3986329331 * 3991834969 * 3994425601 * 4006267823 * 4045323871 * 4056085883 * 4073647147 * 4091945483 * 4098491081 * 4135004413 * 4140261491 * 4141964923 * 4152726959 * 4198942673 * 4205028467 * 4218138251 * 4227099257 * 4235456317 * 4252196909 * 4270521797 * 4276173893"
primes = primes.split(' * ')
# print(primes)
# primees = []
phi = _sage_const_1 
e = _sage_const_65537 
for prime in primes:
    phi = phi * (int(prime , _sage_const_10 ) - _sage_const_1 )
from gmpy2 import invert
from libnum import *
# from Crypto.Util.number import long_to_bytes
d = invert(e , phi)
print((pow(c, d, n)))
# 54372504422578163821842661820992519574720094743792971271580036722643401901785509893350887232430564989
print(n2s(_sage_const_54372504422578163821842661820992519574720094743792971271580036722643401901785509893350887232430564989 ))

