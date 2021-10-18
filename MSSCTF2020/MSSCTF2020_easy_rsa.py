from FLAG import flag
from Crypto.Util.number import getPrime , GCD , inverse , long_to_bytes , bytes_to_long

def getPhi(n):
    phi = (p-1)*(q-1)
    # 1~n
    res = 0
    for i in range(1 , n):
        if GCD(i , n) == 1:
            res += 1 
    return res

def encrypt(m , e , n):
    return pow(m , e , n)

def decrypt(c , e , n):
    d = inverse(e , n)
    return long_to_bytes(pow(c , d , n))
assert flag[:7] == b'mssctf{'
assert flag[-1:] == b'}'
assert len(flag) == 16
mssctf{XXXXXXXX}
n = 1
for k in range(36):
    p = getPrime(512) * 4
    n *= p
m = bytes_to_long(flag)

e = 65537
f = open('./cipher.txt' , 'w')
f.write('c = '+str(encrypt(m , e , n)) + '\n')
f.write('n = '+str(n))

# (n,c,e)
## cipher.txt:

# c = 636878814757207888179251661312243322922440654777015371544677720932520889108716969297562698196956434817343971084693767514772474354601076787230217446051237633152894187947980508386214523362602488220104067703692100432411236841354556515644213342350092977455431262495395736469885775821776688336547880415337867842631654888208261651581054930244721113674672463495656269400319955609793930751686803239891916403356235419000554555891865032753436460858757148836900169945621835301385201743967395743732822576027834591541817699112720626967326509810718759979505560062957622845337709368495677639750622019834168720221596220346017818223996147503889927547584662688350488760218002197787360480054314837787390889077585239389502507383206487878833764411064999710141177412620680112097551900619082143298485734177448450905337277899312852814571057009650354526288507899922902481692906783961978621569079579216201614995420537010784346270222591142486434239109060568146460246027088859646485892396038131337934639280401612638126588605679596735157833454389681162431315572386410935747996161083982546763576762501372542181489112485938952302329130618947110370481740479247148032710218958696816828925703854978724662215247389836430478905037211532276223786801493323165304370701964885961867732377488951720245051343996635559484131841242194359978975780678030112866863913174731005206127968142161530123779331426868562865658329205606086228862761368762143552470881756204763892792628572390232153361587581173259953679711772577257129538540077864117235276686083519141993906860868169404807095254001368967509055076326270572934934639348726035075492553320944783242539692348973389257639974525153691744235603318221510840763344457925244289786502218935651206717182147386308070864616445119357812106978965974878219831456913307142973592492484539244791693463782183745401219408703620723710535593765498963232192216100030845416790537931516626050485075324844973684610578492904756047790320665611453691134950231219860916087418754231986312277844456654094643390088683046791946811051393020382451166925560493345197435739737425872248579291264670555293262249210246971217486356125663627145087359661741528167507896329099636774838153403670259253076054262378949755019182531642511838553285078096307652273210283288949647437995965369013037270828723983940103618326923455081025001524548494019775522384206717276421476910746373261330366150459698384949054653666026462491113925552903188495448872741038646580130340533779893633684762118399230733469981102313082962163717853011364290671142436011361412194968139732838774247283133932610355197979124240687647449379201693172552775370518417475138285273656925832177886463132335227240628804380106493609844036710544240320535076382403646746161125321262738824485626282192116330245914504339937114852015944017882926656381889510803910454543781927852968021979565455654221119731315897791552443948323780191161127289943324236415293256787874090793070989025580481755121429710475858488406500941410721504359987580721999982131759761410732275174891893453270182891657514643871214379056525865733002854235563582577875369846489032299069694627594244350603531634937662136958215623014633080197454249366745498069419552251678524102084510922970121544892978445129723706558219330348303409559351204692028018245331824336022772473556782375345475410560978613938288699363999094014443554292190256777570231542617526847666289877791502729592158949069871165125664054665796426472573822735250282874558004398583053641448701475777397604147106604781832850999493647071483945427346408179852557772747073203066002775053141204498970959675773077788221954357515413930694878816199488840339861105031661660222825599413108516048672646631386912042008528795765820266740760078744601951064936940489671650708943664905952353545452765630969960395239631714589042432113624339811706074990085086376214183864354151775350869548955497612692497511714260451744891986675795166457334323496104293836905127874399576971339302717080071781682042267599037626361315674113799570578399219966060707464229173035904345752140500164609614849169123793123888992013546878839688676541544672592390059336237904363977528862908525145522127186995913211847747870004039295254849159273949302138212335352825938515294119428709317049994924132571015679046891514712183547436838209035675317544092629270673443672661647645111395484749029934034476957277206323351347251666664001950387198556565183100065642287214428556401403117927289097751274092852942788459386216272587108128528849731041314457992656785738732161590362246547375077991502685490265414298934403512383990624094412378546635099924939300108258532708761386177012163166421458195993135423825837085512067699484147825485079236156275542022394381441227621438182272306541332034365477078377165032889421750939523647032298824736485450649048951968115271332533319156225142307358740676669686726512608503991941068440501223802419836206989344220764072802904190749090157304820922952825654452956412368786001136618260988709780775701781943226618206292647326494911568347721351880940222892660630574167935616174677279396673231479860620020537419813173486022074138476422814764994122430581202044162622344124431665717366539293260792079559963692345219270608786295234377265269169764042015273142340536349540071784663493561319041426782180872837422489918246141723627133520988855455217704377659245143253024865378563306313857069919223322255822254922633576761231088247906677171998343557416895785649795569881654318323492717235354704308053986526589074627716934582323728270077785395761575408552228365761832766790769608619052824493785106199367471912697043342392816030419572770984515136628486046626492731159241853
# n = 731042195242201639816089154897391564146671687523530397365946920332517917436603539637215215680190646597601797836351163582773677312331127241087839921807725419107948624182529991800730323788012519583674811094025535023342692206435125194627309393339424819364015887067700956734284038352816142257353317584289346614014857773150122277679947856967573768186643683846184833335685616285826348267946850639385260220889692893909478929580438163809456293894570557543801605351981968971317238853881088910485533690664950094884932753533118114754736786629828703432480084043603055249429234464590769016666543988193265527867295911304956488957991812680160810658906837545692920180074867965109733583589041862846843917132429359568641267411009424002167630449594570076826905868730018221987526813909090106010777955868303503370431116260495909261465698434711826149284307974519954058885921840185349196839639349648856419812843986063622096942371618141322862558805352136694703870662320745155055945697577789292276505596023738608205039366103180377768214765309749112781277188096763910313429182987045052395156294053375414408585410256547845241072506820550843804869124707677391177045432510219685704771906884060311105382145240837044949251906431570106016029910135851864245077326545757121203095607916198621611665827464980989104913873148175991268538316754240904466177587722303879660836013018905170336184577051439760575466259434759590735119275297011180014915193710531014681639589553990753942088818649074503373064805197318250356835283960733070712081203436133905622993350719027384937703090425239510255387859414062587955270739394997641962377143700493374448139536828072509692839439229125389838196854419330364747176371626844839965720817277879737481922851683419689147229245053361191106479645800339499984241290427294030688210764773115220829513983826635873196347097319219441977401808929363274014661536012050762708807765600157732094521199224045827416861076357098611341450067299812078825510919613312585652693147926261089993418039192918878884792250988181155835687714678604776363343039667475250757456323195655907069976807636722861860918201058882508169218329645212833392178937681251783633322070433881259996236121874305361361198746680831975361943444519458798132347347024824111642640516087478109489371439531016401943342364546321791160716168382043695993595586091871659977668637331065432526609819124152448303791325992088597890699879145082669759853530564637372809471231450298007727765798517422565634391515859528492606957729315677963120963772979368264164871884631703272092520839319279947230150756179346914447114018279978763621272744958235872149743773553697227187632036626021958851497591656042043110153257476417111308828851618861990283928517221075685578768329698273802729039144348460021294029938184702848427532869729475079701178093701550166837635818215610280849054739347754904705955002108251696313401856225541677149185597174854610028749556838382838687688838145093413693076218703194604969642247303876368499441475695996388752081368112506161138605111073995347299608345550429847241938150207109196422298139030512488499754378642212398446641146523229434357303850917736053512234846176624401606491572046593322339971318700281758493581900413477994459141876438453934091458142917034114545211335011056365897011788747863968124902440143485533617969801823329455350319519573825129626795448453240275121268056799376662180982226434471679291153031768324083458814443373923136015807128816283299038835715279859616575980186936297158183972782374257928396501179870979637599316609526674392031469864088776638409643745989338009464418757253125096386351752827169464852775209358015668451045946706521665964591086329887682907814658858379358736256321514201937434954426551977083423920449720010647722701940894142083495825537432178767307656423368622353442128470776053782658747946079499739864799034097059899807436091722319620929839189842604472392777587033526145879413856002971635373039163339795019908630601870651945215927841197367055887678082692486311706160946282364948062311848173636141699945734562675308766776536901327903911404759552174140720572137897563448866439040898435688257424084965680026702753190361312273010027525741982138745687036364116011265615347323022166389331145737694326158540375856086861815271631332941241550127534676679901585754898290395293666042030596466125177284503453544974784080640657937593703082668778239244294384626476398381657640839686715650713945975291753953350369678735642953728438961783837723819475191239138456616427219132847157322619347312277124883645805245342875862154544423945618575130208490308094413244333336820916445126839709501629253184171081780121489727038223347537458513908697151776751616040732917450138348033912922500892139452337472892740615820931148680160567385953448125484119615810979685944204198570790284253389134274846612072565409324453975470627890748538201237572075160504383472480157604773775810315457360817357356865202736605835413227722729241241012323280028355667572685947973185897524490080084054258003646839033945033448973332384212269482028589207577464027896594540617945236224044675038150993370170306823130832711058407800989255769408694927694373377894900825330747623529939107054129553114471391393052514593287785063920119964456688479719123429027093841999138899194285917139034817489006148788677180617767184732931999874376444528674680476971826711885460223293886392718767543616160845315959226338576460268458339801178684792446076358974335340657009025512887427372808457438915255190533243978299717732396466132430299017071942810093125809343630553150946773766706967617574287642876897028496526984101990023376780720317984187852918667748371857408