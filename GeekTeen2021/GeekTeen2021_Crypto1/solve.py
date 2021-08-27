# 低加密指数广播攻击
import gmpy2
from functools import reduce
from Crypto.Util.number import *


def CRT(items):
    N = reduce(lambda x, y: x * y, (i[1] for i in items))
    result = 0
    for a, n in items:
        m = N // n
        d, r, s = gmpy2.gcdext(n, m)
        if d != 1:
            raise Exception("Input not pairwise co-prime")
        result += a * s * m
    return result % N, N


# e, n, c
e = 3
# n = [142782424368849674771976671955176187834932417027468006479038058385550042422280158726561712259205616626939123504489410624745195777853423961104590708231562726165590769610040722589287393102301338152085670464005026301781192671834390892019478189768725018303217559795377795540494239283891894830166363576205812991157, 153610425077816156109768509904751446801233412970601397035720458311275245730833227428213917577405780162151444202393431444812010569489900435979730559895340377469612234558042643742219128033827948585534761030527275423811282367831985007507137144308704413007806012914286105842311420933479771294576841956749281552971, 152540067782701001222493009941492423063369171831039847414320547494725020441901272486665728360741395415762864872737675660423920609681185809510355937534756399208661762715484879562585724584849261266873624875852300611683382543315580370484972470694466195837255994159609193239840228218925381488410059939975556977947, 125842716702134814646356078531900645012495638692517778270527426844383063904041812273637776798591687732598509470005151551320457132061693618473039437320011446697406190781306264437609046721508738109650829547010385875425097336266103994639126319889016342284747700714199556143378526590058467791687837422897022829661,
#      116144389285266462769913139639175922392318396923181100785008570884082681963637784423143843845816350379438789947802939701820129805341796427821894273985551331666719808355412080909245720551238149511778060242720419584504473490216670437024863860559347959698828131475160058721701582089480924088773887932997353631767, 127833907448946785858374094953899556339175475846831397383049660262333005992005484987913355932559627279178940862787593749842796469355336182379062826441222705075178971785791223706944120681105575965622931327112817747065200324610697178273898956820957640413744954233327851461318200323486469677469950386824833536523, 130561613227079478921314550968562766645507834694262831586725464124109153306162445639759476845681271537955934718244296904503168256991962908095007040044300188572466395275317838178325500238288302672390013747102961340256309124310478931896245221622317302428447389760864327859640573452084295225059466376349115703119, 115953389401040751013569404909249958538962411171147823610874077094621794755967854844224923689925397631692572916641171075740839099217316101334941033937183815345038898177087515909675028366437302462022970987947264115373697445950951595479758872029099661065186221250394358255523574834723958546450323357472451930993, 143437107845384843564651522639125300763388830136500260725097766445883003928355325003575359566631064630487365774344508496878731109174874449170057678821440711511966073934025028100604234445470976333825866939923998344367645612128590820812489407412175198698290167077116185959180877334222693344630253253476594907313]

n = [14447643252565777715864027833246970457644149205377077114557844194475351427602891434717210425761489397720768080804057681716878329775755736867275787090842342972747341989307768894823500496996775613553387006129396991308248383534027124304458858418272142277374195546642817466972257010498548703719857037562126864875309726037978176322675043436578560167240153963108730741,
     14065305138241653019388796033620985654344872570254349628087800523983030095068530755725116979263314303250478127056342308461281099856158859645844038934106881739232524756021030652006569887095508481889526525415268231172343427513042160771430081607295983468540271672389951882100887649557428947588071682994165813844808959646535650068447724168824415128560373107657807327,
     14010873209740800300684312375935492061920876881342349004610469290657051121488882809366891041879534163378791500190062839533527507469631225716976954903025528349856859843788182713777319610094774588945463215323571510783491373934016807174204289914087857971209627878790468079321441437412922836789644662742241393729814010578667933096115511831275664646781666371100775831]
c = [655211559830901881626626097152306719128388521516334109253550160043521245799947987489054867663109075767866438236801643617557912404772535692717188057470530665117139416687814086766636662376218400418270178467997319355411551852208736360216757822331892808300290948859787819982434071094236295277637146803036093821085776769606587252732290644161131676572954739122419002,
     1451096827187308092257461798788497359980882370087563598858659005441513963642268986129505978813632720616618261110590225983328290346904340868481157589349368878751642636235746965976318718510025688796415356307603321615034271450401038655811551775889557904151912135588169928694505788955763846671906402014887087028162763288140509516671034677655593845343739634875020090,
     1853441923361033603685710754520080375544251354487044118329680038538917316465766359224867975816575527977067835928253352867273074229093539391809037301206592544335048449659879811356822310243071554170780989815049744260329758728335075075478479348582229733418740278581140054825946065894298935680443960089114313940919866616075895298102221191351496616365265412249738063]


# c = [85033868418784308573673709960700777350314426427677627319697346811123742342359072170220428874952996988431950989321281905284522596263957356289624365171732095210045916218066135140320107686084053271623461104022705353814233772164502775939590711842361956121603943483040254727995655776263673058788416722141673409688, 66065963470666895005407449599703926269325406456711861190876894466341571726360462706664546294453572319565476664348345756905411939632955966517708138047546806602828064213238537646393524578984547577761559965654539771172357089802682793169968961304179886652390277814477825753096636750388350662980872556701402397564, 116011740820520887443111656288411611070614127688662643257265381793048354928820176624229624692124188995846076431510548507016903260774215950803926107831505634778278712070141663189086436127990584944132764896694777031370995058271038329228336417590284517922855284619653301817355115583540545182119702335431334401666, 97640420284096094887471273365295984332267897927392169402918423863919914002451127544715668846623138003564829254309568918651163254043205129883843425179687841236818720463784828905460885026290909768599562386370732119591181513319548915478512030197629196018254041500662654260834562708620760373487652389789200792120,
#      8112507653841374573057048967617108909055624101437903775740427861003476480616929517639719198652146909660899632120639789106782550275648578142883715280547602249589837441805676364041484345030575130408744621981440093280624046635769338568542048839419939250444929802135605724150484414516536378791500915047844188300, 36792148360808115566234645242678223867680969786675055638670907933041180936164293809961667801099516457636164692292891528415720085345494773373966277807505798679784807614784581861287048096977968620964436947452527540958289441390882589051225367658014709290392321808926567572528170531844664734909469690750971883323, 53043093283305492238903255767698153246673671181809989362223466090875767705978690531154079519999671834688647277179370374802495005937892824566602423646978168777735383632928274082669949750078161820002768640908750005814934158829006019656592134357897586040866207754535586785064545866404380204728594863102313407789, 88499407133762624445946519155722583633934260410706930537441122463087556094734626189377091740335667052378955691250910459790202385799502439716173363179773811920751410726795431402796346647688144853156900427797933862087074385441977254140336390678022955770879265490567987868532251217565094093318626424653599450992, 138337520305048557335599940473834485492131424901034295018189264168040969172072024612859307499682986987325414798210700710891033749119834960687318156171051379643844580970963540418974136891389303624057726575516576726845229494107327508855516437230240365759885913142671816868762838801720492804671259709458388192984]
data = list(zip(c, n))
x, n = CRT(data)
p = gmpy2.iroot(gmpy2.mpz(x), e)
print(p)
n = 9268365774880703391442727909575765427797075427451511529595496691163237049525133788965261716909405603845314783550122799589366982296802469163382370555818305282640258091443322302637596677934166554221101764915837609843260146565192516689400630889416102239771317014391907670780065078005197071222914754451153669022244069896636339261981139783224044474469686856105005842068010061834060619043866982130239845784980885446597457288485656817720389360622457941147295646045631025849063883110722217015655254582331888201457735202485530216190054977883059642108637163834310120937686480140674874547683513243469709006493746278572825903527
c = 693332343170160519673454723171047887414505975503036113355778145914917873346915691272534953852966333737944390200425607168968652743930269614282060927729137503247045783993719753800493329194410182353122413742118531672166811765491984151380946564347831562918772440125408762187949870567504545707100336055688808987710499013778118610992351046714255619883612191260346561356558241413680106422736485715067182414121219009392029455080305055589612076035694920467703079913206953026763057115933540071906726871235161316367013001665727865458781748868434073571946280260683097988895302130357840906597822748291691210644430303613675959004
breaks = 7406413397889594819729124655996446805274089058403997531172097174743789607749214262645845515849507186738393885455235301567067826056015531748179023283379262574076077687681132602668567800919308891406503891057505703870530996216846919029038937493423905841638283094795463952829946842095027698108329020862087760987798683786469717224736752276576938673519759410918963207097597232761533320116452660531623609181750754583340190542963682680193544820711164355151659298443161283771646518723239767335061327076063035999588657451372739274968126924948246784634501688827275520242392732098397952387682626075221441989977163646799969426210
# for e in range(100000):
#     if pow(203 , e , n) == breaks:
#         print(e)
e = 64033
q = n // p[0]
phi = (p[0] - 1) * (q - 1)
d = gmpy2.invert(e , phi)
print(long_to_bytes(pow(c,d,n)))