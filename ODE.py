import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import functions as func

M = 1
B = 10
k = 20
u = 1
t = np.linspace(0, 10, 5000)
mengaT = np.linspace(0, 10, 500)
y0 = [0, 0]
mengaX = [0.0, 0.04803314124262707, 0.1799567872139412, 0.37957708734233236, 0.6331485576325565, 0.9290294325561672,
          1.1986391392662783, 1.3218778653196317, 1.3201594152830833, 1.2161881765693927, 1.0292892227739587,
          0.8493711307695423, 0.7874978560181448, 0.8240952410295624, 0.941015082077651, 1.0827214918514978,
          1.1091122170061691, 1.029680667610504, 0.9234920635220838, 0.9186965318884819, 1.0010425919266708,
          1.0564311155830683, 1.0011147791467225, 0.9496842448434178, 0.9936367525107198, 1.0322283698011538,
          0.977222512706093, 0.9828445646343731, 1.0218708874305025, 0.9802111340613476, 1.004927556544068,
          0.9992859198666193, 0.9928302993996799, 1.0038379373137674, 0.9956331233811136, 0.996930626700748,
          1.0053830037439204, 0.9922270691951626, 1.0013160505529066, 1.004709600050783, 0.998211226402027,
          0.9956051398452324, 0.9961364156035654, 0.9969604195289877, 0.9972046599240615, 0.9972941995763581,
          0.9984414859988463, 1.0013339069789993, 1.0004763129842225, 0.9985122250476595, 1.0011794238958887,
          0.9988671584357507, 1.0001651189127694, 1.0007008966662432, 0.999560749623802, 0.9992220097843493,
          0.9993354900146197, 0.99945452958971, 0.9994813224977305, 0.9994875055891473, 0.9996025599410399,
          0.9999094969432142, 1.0002328693238078, 1.0002040010031898, 0.9998462872482086, 0.9997224411564845,
          1.0000200209043821, 1.0001484696510392, 0.9998741399787079, 0.9998312030658779, 1.0000764325020748,
          1.0000138236960594, 0.9998412189884163, 0.9999832972980616, 1.0000462241488501, 0.9998914627649552,
          0.9999377550367734, 1.00003491925275, 0.9999316842431096, 0.9999234646329995, 1.000013931132157,
          0.999956453435218, 0.9999239354388336, 0.9999946677390225, 0.9999695933131213, 0.999930256337567,
          0.9999799440936079, 0.999975243661996, 0.999938118716302, 0.9999697732976408, 0.9999764442622527,
          0.9999455380621318, 0.9999633595010905, 0.9999752363997997, 0.9999516984947804, 0.999959764535438,
          0.9999729378466451, 0.9999563819909527, 0.9999581333779284, 0.9999703566396122, 0.9999596751081031,
          0.9999577656089075, 0.9999679513948546, 0.9999618012037395, 0.9999581294202524, 0.9999659420534307,
          0.9999630280671616, 0.999958846751168, 0.9999643982494317, 0.9999636120637513, 0.999959668197392,
          0.9999633001932987, 0.9999637729529033, 0.999960445565195, 0.99996258087003, 0.9999636830717689,
          0.9999611023325881, 0.9999621574601841, 0.9999634669241014, 0.999961612434997, 0.9999619481359727,
          0.9999632084493725, 0.9999619792278469, 0.9999618818971767, 0.9999629596087065, 0.9999622218819891,
          0.9999619013970152, 0.9999627457957599, 0.9999623674664718, 0.999961965719207, 0.9999625785805022,
          0.999962441478195, 0.9999620464527964, 0.9999624573406907, 0.9999624672923659, 0.9999621256429118,
          0.9999623766811189, 0.9999624636109549, 0.9999621938481502, 0.9999623280187966, 0.999962444861964,
          0.9999622479581742, 0.9999623027882535, 0.9999624201869265, 0.9999622868162346, 0.9999622931271568,
          0.9999623959094354, 0.9999623126547782, 0.9999622934488241, 0.9999623751807585, 0.9999623281163339,
          0.9999622982289966, 0.9999623589913841, 0.9999623363163599, 0.9999623053172644, 0.9999623471484628,
          0.9999623394323647, 0.9999623124437871, 0.9999623394499729, 0.9999623395354856, 0.9999623181863991,
          0.9999623351413846, 0.9999623382826102, 0.9999623223291274, 0.9999623326580744, 0.999962336844518,
          0.9999623255796172, 0.9999623315071176, 0.99996233512185, 0.9999623279472114, 0.9999623312071462,
          0.9999623339056232, 0.9999623284546292, 0.9999623314089592, 0.999962333502807, 0.9999623285468537,
          0.9999623317803135, 0.9999623332628677, 0.9999623285127708, 0.999962332213333, 0.9999623330493693,
          0.9999623283542637, 0.9999623322059681, 0.9999623324535589, 0.9999623289462537, 0.9999623326424449,
          0.9999623319836866, 0.9999623288546103, 0.9999623335289946, 0.9999623309808889, 0.9999623290372287,
          0.9999623338569446, 0.9999623305357841, 0.9999623291403293, 0.999962333909976, 0.9999623306447087,
          0.9999623298331954, 0.9999623333660529, 0.9999623302629959, 0.9999623301246315, 0.9999623337629806,
          0.9999623293778087, 0.9999623307716965, 0.9999623332889439, 0.9999623296337186, 0.9999623311684409,
          0.9999623330458003, 0.9999623289760676, 0.999962332187317, 0.9999623325344077, 0.9999623287080294,
          0.9999623325389952, 0.999962332181843, 0.9999623287949375, 0.9999623331293788, 0.9999623315025249,
          0.9999623288726514, 0.9999623334670175, 0.9999623310732546, 0.9999623291404934, 0.9999623335012319,
          0.9999623308206421, 0.9999623296882773, 0.9999623336598834, 0.9999623302268363, 0.9999623301262598,
          0.9999623334696552, 0.9999623299298143, 0.9999623304413832, 0.9999623331542348, 0.9999623295638584,
          0.9999623308124537, 0.9999623334736671, 0.9999623291924865, 0.9999623309772581, 0.9999623335320108,
          0.9999623288333993, 0.9999623313138674, 0.9999623332039056, 0.9999623294125777, 0.9999623313994959,
          0.9999623328206058, 0.9999623293177389, 0.9999623319655937, 0.9999623324861572, 0.9999623288884034,
          0.9999623324915543, 0.9999623321023806, 0.9999623291388214, 0.9999623329584276, 0.9999623314440591,
          0.9999623290521888, 0.9999623336399638, 0.9999623308301853, 0.9999623295107342, 0.9999623335923266,
          0.9999623302736673, 0.999962330010502, 0.9999623337740275, 0.9999623294165029, 0.9999623307960532,
          0.999962333351762, 0.9999623293778129, 0.9999623314883573, 0.999962333077127, 0.9999623287628436,
          0.9999623324467473, 0.999962332334901, 0.9999623286177434, 0.9999623328252677, 0.9999623319571114,
          0.9999623294164134, 0.9999623324066901, 0.9999623318780889, 0.9999623294564999, 0.9999623327479139,
          0.9999623313120761, 0.9999623295782798, 0.9999623333496903, 0.9999623304730146, 0.9999623299606307,
          0.9999623337325926, 0.9999623296184987, 0.9999623306627532, 0.9999623336339043, 0.9999623296207084,
          0.9999623309759882, 0.9999623333019942, 0.9999623289852504, 0.9999623317174975, 0.9999623331167324,
          0.9999623286518267, 0.9999623321660899, 0.999962332943719, 0.9999623284866295, 0.9999623326421376,
          0.9999623324071794, 0.9999623287107705, 0.9999623327877708, 0.9999623322553397, 0.9999623289262193,
          0.9999623325963087, 0.9999623317210264, 0.9999623299028387, 0.999962332260643, 0.9999623312839728,
          0.9999623300254856, 0.9999623324989255, 0.9999623313271845, 0.9999623298303871, 0.9999623329241841,
          0.9999623306287889, 0.9999623302193562, 0.9999623332451376, 0.9999623297534197, 0.9999623310461216,
          0.9999623330880149, 0.9999623290299815, 0.9999623319822616, 0.9999623326582651, 0.9999623287012066,
          0.9999623324303266, 0.9999623323077189, 0.9999623287090774, 0.9999623331982642, 0.9999623317041691,
          0.9999623287072448, 0.9999623332885806, 0.9999623314650238, 0.9999623292342917, 0.9999623334583014,
          0.9999623307727722, 0.9999623294945922, 0.9999623338029489, 0.9999623301223821, 0.999962329992285,
          0.9999623339177658, 0.9999623296445043, 0.9999623303932743, 0.9999623339494664, 0.9999623297577146,
          0.9999623307953295, 0.999962333384449, 0.9999623290690569, 0.9999623315732039, 0.9999623330991929,
          0.999962328636596, 0.9999623322514116, 0.999962332681083, 0.9999623292929357, 0.999962332035025,
          0.9999623321121129, 0.9999623294953042, 0.9999623327445558, 0.9999623313451522, 0.9999623293714875,
          0.9999623331953107, 0.9999623312371886, 0.9999623291864566, 0.999962333591556, 0.9999623305713725,
          0.9999623296245284, 0.9999623339137685, 0.9999623298057346, 0.9999623303121858, 0.9999623339151269,
          0.9999623294785419, 0.9999623305753973, 0.9999623337268595, 0.9999623291743014, 0.9999623308699671,
          0.999962333636772, 0.9999623293184042, 0.9999623312314009, 0.999962332990254, 0.9999623294071689,
          0.9999623315258003, 0.9999623328421312, 0.9999623289771539, 0.9999623323815862, 0.9999623323438571,
          0.9999623288071083, 0.9999623328091822, 0.999962331954463, 0.9999623288056081, 0.9999623333871465,
          0.9999623314339412, 0.9999623289321536, 0.9999623335466079, 0.9999623310064687, 0.9999623289636286,
          0.9999623335945063, 0.9999623305500877, 0.9999623296583051, 0.9999623338127784, 0.9999623300606466,
          0.9999623299980287, 0.9999623332788685, 0.999962330316944, 0.9999623306343873, 0.9999623329393961,
          0.9999623297148308, 0.9999623313431955, 0.9999623329118851, 0.9999623292004222, 0.9999623317959926,
          0.9999623329401149, 0.9999623291356122, 0.999962332045186, 0.9999623325188288, 0.9999623288104345,
          0.9999623327887908, 0.9999623318582743, 0.9999623288891644, 0.9999623335006927, 0.9999623309543392,
          0.9999623292639859, 0.9999623336914695, 0.9999623305388333, 0.9999623296150597, 0.9999623339159335,
          0.9999623302785995, 0.999962329928586, 0.9999623331379557, 0.9999623304779667, 0.999962330705053,
          0.9999623320681797, 0.9999623306148749, 0.9999623313876577, 0.9999623322029254, 0.9999623302355349,
          0.9999623306608476, 0.9999623325950334, 0.9999623302950982, 0.9999623307317628, 0.9999623329482376,
          0.9999623296819835, 0.9999623314274659, 0.9999623328017445, 0.9999623291841125, 0.99996233195724,
          0.9999623323742177, 0.999962329008783, 0.9999623328851229, 0.9999623316426794, 0.9999623290554427,
          0.9999623335417424, 0.9999623309983827, 0.9999623293101804, 0.9999623338857395, 0.9999623301910997,
          0.9999623296700876, 0.9999623339359122, 0.9999623298621507, 0.9999623301595217, 0.999962333907376,
          0.9999623291650738, 0.9999623309504424, 0.9999623337785885, 0.9999623288377132, 0.9999623312314938,
          0.9999623333992066, 0.9999623290314612, 0.9999623316992468, 0.9999623330192332, 0.9999623286223351,
          0.9999623323955024, 0.9999623326989391, 0.999962328609079, 0.9999623326865693, 0.9999623323179831,
          0.9999623288388754, 0.9999623327520856, 0.9999623321640515, 0.9999623287773316, 0.9999623330721584,
          0.9999623315513864, 0.999962329183663, 0.9999623330724028, 0.9999623312839306, 0.9999623295021163,
          0.9999623332939979, 0.9999623306080897, 0.9999623298381253, 0.9999623337372693, 0.9999623297342786,
          0.9999623305271248, 0.9999623337879058, 0.99996232898363, 0.9999623310934057, 0.9999623336244476,
          0.9999623287312572, 0.9999623315142246, 0.9999623334179838, 0.9999623287934007, 0.9999623316739666,
          0.9999623333324671, 0.9999623285905855, 0.9999623318546514, 0.9999623332724124]

mengaControllingEffort = [255.61698963089353, 255.61698963089353, 255.61698963089353, 255.61698963089353,
                          255.61698963089353, 255.6169896305083, -255.61698963089353, -255.61698963089353,
                          -255.61698963089353, -255.61698963089353, -255.61698924245454, 255.61698963089353,
                          255.61698963089353, 255.61698963089353, 255.61698962818608, -255.61698963083634,
                          -255.61698963089273, -255.61698926939155, 255.6169896307368, 255.6169896308216,
                          -244.7743977487596, -255.61698962678864, -246.7474976322393, 255.6169896197535,
                          255.6115183537394, -255.61698940192463, 255.61698818571452, 255.61698294179917,
                          -255.61698784639694, 255.61698660386895, -255.59156954325655, 226.03705694297147,
                          255.61450461006692, -255.52511713317423, 255.56845038937166, 255.36933169016334,
                          -255.60165662631414, 255.6155638434066, -250.35145224332777, -255.58441071847537,
                          253.7380613368292, 255.57002425728953, 255.52797882365445, 255.35908970273405,
                          255.25461809038075, 255.20486218119132, 252.60555933431303, -250.57618245457806,
                          -190.5627282031402, 252.09769316557217, -248.16091690822222, 247.17245120201707,
                          -84.27261795456263, -224.74017891264398, 182.05144948097282, 231.53483522106112,
                          220.8318632613678, 203.96662805690482, 199.13227022390785, 197.95422683194536,
                          171.21132926742186, 47.54495020161178, -114.32691648762128, -101.95939974257749,
                          78.87706496498879, 132.0921323585057, -10.64664227007247, -76.36756297820949,
                          65.34747515827178, 85.99328358623723, -40.29985419291653, -7.3535468703089775,
                          81.28549806648631, 8.883808544669666, -24.513832104217347, 56.704242463273815,
                          32.92026714706485, -18.545294500875766, 36.08626892990382, 40.353102014931444,
                          -7.4106628757592885, 23.10256605932273, 40.10935823597265, 2.837236854060619,
                          16.156211012156806, 36.82919123553549, 10.66523191029915, 13.160432259878693,
                          32.73023504901068, 16.060854629001664, 12.523340208228612, 28.844967682943476,
                          19.45566002602888, 13.16428536874592, 25.60760800848762, 21.355255406468274,
                          14.383490878172385, 23.14024256617431, 22.21632439069358, 15.751764585705821,
                          21.402477077953673, 22.410389427347333, 17.02587317337913, 20.279374954928045,
                          22.218412935090473, 18.089554673500313, 19.630893627133077, 21.83981004518673,
                          18.906330268301705, 19.322113220175083, 21.406126178618766, 19.48701834024305,
                          19.237034289650488, 20.995588543723223, 19.86730060956265, 19.28456442987064,
                          20.64864845718381, 20.091098204577353, 19.398859703119715, 20.379126905451407,
                          20.201726161596596, 19.535525617339804, 20.185294614911193, 20.236731668634043,
                          19.66708601599449, 20.05704957802461, 20.226426590112823, 19.780118343993227,
                          19.980101449342133, 20.1924337325689, 19.868510853275634, 19.94098130424269,
                          20.149766702068764, 19.932596780740845, 19.92733654685297, 20.10791418468829,
                          19.97523094823469, 19.929282460908926, 20.071866299101075, 20.000951763232006,
                          19.93919273150175, 20.043267402357134, 20.01428737009262, 19.952235268835963,
                          20.022729320849947, 20.019393712293404, 19.965067562731218, 20.009072431430067,
                          20.019223696307595, 19.97602398099362, 20.000900209640765, 20.016697153121488,
                          19.98458103431324, 19.996566058887453, 20.01295066645849, 19.990840695834358,
                          19.99491908097481, 20.00918395069742, 19.994909774053287, 19.994864575912697,
                          20.006148692439545, 19.997187096750395, 19.9955267889473, 20.00395904908399,
                          19.99849965927849, 19.996286898764435, 20.002240997061527, 19.999108001303195,
                          19.997197421836265, 20.000989599758906, 19.99926655211645, 19.99784026303653,
                          20.00072140280579, 19.99915988321921, 19.998053172933332, 20.000672657274528,
                          19.998963602734147, 19.99817999374723, 20.000690671910984, 19.99873472886386,
                          19.998292839030753, 20.00077445124617, 19.998738621598857, 19.998607756641128,
                          20.000461553371817, 19.99850792030226, 19.998856109226942, 20.000509991714274,
                          19.998039331439312, 19.999386141075746, 20.00041346828823, 19.997865992295,
                          19.999621402584264, 20.000358974166403, 19.997837962321192, 19.999563830136513,
                          19.999992757863474, 19.998125454828358, 19.999765585612124, 19.999838718476667,
                          19.99791565727732, 20.000233453795374, 19.999496710376985, 19.99816621105299,
                          20.000098191932135, 19.999287009902293, 19.998294725455963, 20.000445795139626,
                          19.998748479688935, 19.998565023752036, 20.00058746747395, 19.99856259898574,
                          19.998751372965653, 20.000541531943, 19.99825054976264, 19.999110428767928, 20.00050045608873,
                          19.99807208964943, 19.999337320916876, 20.000358887435677, 19.998054005502627,
                          19.99947084001854, 20.00006935478254, 19.997970149669683, 19.999784697832045,
                          19.999837857858772, 19.99807069544209, 19.99994168970814, 19.999671298476947,
                          19.99823741203438, 20.000135116693098, 19.999475168048555, 19.99806857493716,
                          20.00033140635362, 19.99938806018499, 19.998037737187623, 20.00052120286216,
                          19.999210144300413, 19.99821115834824, 20.000215076562572, 19.99916488508621,
                          19.99841375279692, 20.000265203873735, 19.998865672267176, 19.998590526723216,
                          20.000492130292066, 19.998587674053578, 19.998793373097218, 20.00035977117364,
                          19.998340906578647, 19.999141331044502, 20.000405561063634, 19.99798067825663,
                          19.9994657959608, 20.000163195680994, 19.99800585708271, 19.99975994517873,
                          19.999899041945117, 19.997909818376957, 20.000213001890682, 19.999483836548983,
                          19.998133008334648, 20.000233451565492, 19.999117917074418, 19.99827816761045,
                          20.000558495249898, 19.998611356968002, 19.9986704737073, 20.000635188376826,
                          19.998411288713964, 19.998870155628094, 20.000213049187685, 19.998632529323935,
                          19.998911923202716, 20.000191861362453, 19.998452174322832, 19.99921109106265,
                          20.000127494246634, 19.998134103326354, 19.99965457956698, 19.999925401579592,
                          19.99793171897703, 20.000106236413572, 19.999554292685776, 19.99798388101967,
                          20.000105068482657, 19.999388731380304, 19.998159313250884, 20.00044094156417,
                          19.998996804318974, 19.99825723402336, 20.000617173563654, 19.998759699358892,
                          19.998348680901273, 20.000704488968942, 19.998508082731856, 19.998632270715856,
                          20.00058601863684, 19.99843110782524, 19.998712526067425, 20.000472142617397,
                          19.998532305749425, 19.99899493907856, 19.99995594770327, 19.998709722983644,
                          19.99922594514826, 19.999891122336052, 19.998583777973348, 19.999203105492267,
                          19.999994242203268, 19.99835900609643, 19.999572244605634, 19.999788651475342,
                          19.998189365021574, 20.000034923558143, 19.99935166212772, 19.998272412801708,
                          20.000417298816828, 19.998856862400135, 19.998499558522845, 20.00059107366414,
                          19.998620036153444, 19.99868484086167, 20.00058691352408, 19.99821414011729,
                          19.999003849054898, 20.000587882173498, 19.99816640305796, 19.999130250099768,
                          20.000309310087335, 19.998076696536735, 19.999496141815097, 20.00017172756769,
                          19.99789453191483, 19.999839907415648, 19.999908670642842, 19.997833845010724,
                          20.0000924911171, 19.999696726551957, 19.997817089521657, 20.000032653477767,
                          19.999484219091556, 19.998115731524926, 20.00039664540364, 19.99907307114903,
                          19.998266504600227, 20.000625223793033, 19.998714602267125, 19.998487498007815,
                          20.000278313651837, 19.998828974101436, 19.998788229044415, 20.000171351245495,
                          19.998453949253534, 19.999193608587913, 20.00023679486501, 19.998215701213898,
                          19.999250673105696, 20.00033459350241, 19.998006264389147, 19.99960259221818,
                          20.000103049440344, 19.997835957770064, 20.000007272353432, 19.999739586101114,
                          19.9978352398051, 20.00018021098371, 19.99960046490843, 19.997934749217336,
                          20.000341018148376, 19.999444769146063, 19.99798236528342, 20.000264852197635,
                          19.999253732214463, 19.998324084609468, 20.000217935390598, 19.99909812649137,
                          19.998402375447924, 20.000445221003393, 19.998645798083842, 19.99866573989439,
                          20.000535099023853, 19.99841979074198, 19.998871555409394, 20.000535891982,
                          19.998114305747126, 19.99914667889584, 20.00046900599336, 19.998030021838005,
                          19.99937262081493, 20.000452369832775, 19.99800470499408, 19.999613842395885,
                          20.000085196639365, 19.99788933645415, 19.999872537895847, 19.999905634773167,
                          19.99817153643293, 19.999737071143787, 19.999569285548926, 19.99835096577189,
                          20.000055319835557, 19.999194642843808, 19.998365506801804, 20.000327211943052,
                          19.998955315482412, 19.998350585811, 20.000361467410652, 19.998823603480645,
                          19.998573258016812, 20.00053334099581, 19.99843056872091, 19.998922396270576,
                          20.000491728091575, 19.998054290458683, 19.999400174033894, 20.000293615170477,
                          19.997953454741186, 19.999619790905975, 20.00010805412086, 19.997834813485895,
                          19.99975733826805, 19.99994233889777, 19.998246016403453, 19.99965196215219,
                          19.99953193498331, 19.998811450075912, 19.999579598881997, 19.999171142202457,
                          19.99874022981593, 19.999780100162983, 19.999555299889398, 19.9985329798205, 19.9997486178364,
                          19.999517817466835, 19.998346292575658, 20.0000726813583, 19.99915010141742,
                          19.99842372197269, 20.00033583243733, 19.998870087616588, 19.998649692696876,
                          20.000428503334437, 19.99837965202676, 19.99903634963331, 20.000403841236842,
                          19.998032593542977, 19.999376894682513, 20.00026919894464, 19.997850772611677,
                          19.999803586535172, 20.000078968984916, 19.9978242536795, 19.99997745346636,
                          19.999820277159145, 19.997839336577133, 20.00034589543133, 19.999402233684535,
                          19.997907407693088, 20.00051892274805, 19.99925368309831, 19.99810793132266,
                          20.000416516714626, 19.99900645080295, 19.998308767578692, 20.00063276138403,
                          19.998638442629222, 19.998478060132186, 20.000639767969457, 19.99848459821697,
                          19.998679415666835, 20.000518308473946, 19.998449969376185, 19.998760776745765,
                          20.000550837596926, 19.998280793771162, 19.999084602883098, 20.000336070037264,
                          19.99828066461379, 19.99922596744711, 20.00016775068768, 19.99816353976621,
                          19.999583185240397, 19.999990152185514, 19.99792924708867, 20.000045040658215,
                          19.99962597948069, 19.997902482987683, 20.000441798015355, 19.999326669989284,
                          19.997988879369757, 20.000575190325147, 19.999104244826874, 19.99809800656646,
                          20.00054234420723, 19.99901981268657, 19.998143206721178, 20.000649542719707,
                          19.998924311155367, 19.99817494886358]

mengaV = [0.0, 4.635728850540582, 8.39590336185174, 11.412171933833928, 13.797686801511166, 15.649639942124947,
          9.692432440891642, 2.8277541105637702, -2.8108848959840174, -7.405116928173031, -11.111186952522008,
          -5.884293224567003, -0.4673814965391523, 3.9692330554717956, 7.571299702775502, 4.328151121354407,
          -1.5014862758270375, -6.261555890343362, -2.7216306852917, 2.082947707182877, 5.90937060973464,
          -0.18268054591620175, -5.166975715695516, -0.0282054293674594, 4.268283813340395, -0.9116658208827397,
          -2.136063555673981, 2.540630450038882, -0.5566043482531143, -1.039051705163047, 2.544418500842944,
          -2.793545487260721, 1.9936290463861, -2.063627404195858, 1.8806183193371635, -1.8110858172222,
          1.075186906434676, 0.1718458166207859, -1.5859252526404795, 0.4393098396272853, 1.2851591684564139,
          0.3278281104222387, -0.24215919517251552, -0.4550487439352459, -0.35081478203797534, 0.026136496934952982,
          0.628419553179395, 0.48593790113083196, -0.752430300801827, 0.2547087799065919, -0.14722248247657999,
          0.24930125387422508, -0.576632051362797, 0.2595595937335816, 0.42085231993776534, 0.07152220350074216,
          -0.12576495729316867, -0.1800506028183228, -0.13384948287170748, -0.01469557112744672, 0.14759087549110342,
          0.25656730847103937, 0.13103181218027174, -0.12426097227512896, -0.1739131258332483, 0.04972988914988683,
          0.15287731443738592, -0.05067361520553701, -0.11325126929662882, 0.07194996368905651, 0.06650616465330728,
          -0.0893388764673688, -0.009138860511247337, 0.07758511739879417, -0.03779017693614622, -0.039399611396261684,
          0.05600587017160027, -0.004769344904223509, -0.04240702488449913, 0.0332625520944352, 0.011219212469092644,
          -0.035268161112635324, 0.016313258569557388, 0.016938501581199316, -0.02582484400032541,
          0.0052410421097509804, 0.017226726702679093, -0.017137667908486334, -0.001264885782693389,
          0.014962481691475545, -0.010202012537162308, -0.0045567220006974595, 0.011774305999143224,
          -0.005148167371631813, -0.005743159959254101, 0.008547392419406497, -0.0017589188063300287,
          -0.005661555933006437, 0.005720543087110908, 0.00030443370962315375, -0.004910395104116752,
          0.003468570353622393, 0.0013913243020270613, -0.0038915440657730656, 0.0018095761390079872,
          0.0018126312566310702, -0.0028535397490430207, 0.000679602380920033, 0.0018187696445931343,
          -0.001934367001870589, -2.141298011946625e-05, 0.0015977846485917854, -0.0011932729951414209,
          -0.00040186618245798136, 0.0012800645972210593, -0.0006415310044379216, -0.0005600273496559219,
          0.0009486883302983752, -0.00026127690136234144, -0.0005770692355735208, 0.0006505276386593264,
          -2.1719896617402435e-05, -0.0005147473933996503, 0.0004078103437147551, 0.00011107228605699497,
          -0.00041739441325124884, 0.00022554661324738004, 0.00016942978138440813, -0.0003121782353494679,
          9.850446159801294e-05, 0.000179814333367197, -0.00021639839420792636, 1.753343708013425e-05,
          0.00016278772420578232, -0.000137558715953645, -2.793806485412238e-05, 0.00013289341418838121,
          -7.812210969451834e-05, -4.858514168899456e-05, 0.00010020632852463247, -3.6601775829150446e-05,
          -5.319910953810484e-05, 6.971051768652343e-05, -9.962876010492489e-06, -4.883252989880588e-05,
          4.510547558109439e-05, 5.143183386112983e-06, -4.012063804037204e-05, 2.6536298819970163e-05,
          1.2010050004803687e-05, -3.0701635261599167e-05, 1.3773092657107012e-05, 1.4030377979822085e-05,
          -2.1650936243830223e-05, 5.495025231394147e-06, 1.2942231847994996e-05, -1.4283034236642278e-05,
          8.401650261739306e-07, 1.0463022957951701e-05, -8.898946495686369e-06, -1.0319399794910933e-06,
          7.940264354871849e-06, -5.317281133675826e-06, -1.8926924100410975e-06, 5.741752734382761e-06,
          -3.168875288208474e-06, -1.8410295715422168e-06, 3.8167696514334544e-06, -1.6830109343690663e-06,
          -1.4593176081365613e-06, 2.4208599861039935e-06, -1.2189618238335471e-06, -9.936726128805692e-07,
          1.9616116787652055e-06, -1.180866960938972e-06, -7.988934952749258e-07, 2.0297135151082786e-06,
          -1.5388135759300547e-06, -4.6899282595474287e-07, 1.9392904008287643e-06, -1.6477895619530392e-06,
          -2.475932365608009e-07, 1.6443799019010424e-06, -1.3350795845773112e-06, 7.640830050261522e-08,
          1.4317343921683734e-06, -1.6983512665267011e-06, 6.779672447980914e-07, 9.915255830581394e-07,
          -1.965463163984515e-06, 1.2153096997965603e-06, 5.765698991121795e-07, -1.976051750772047e-06,
          1.5240357780070241e-06, 4.7216683333282664e-07, -1.657430773841751e-06, 1.0794977043563865e-06,
          1.9365902356619203e-07, -1.5047494029990656e-06, 1.5690177358652117e-06, -2.9853255104343236e-07,
          -1.2616899520688071e-06, 1.726091323982984e-06, -5.444973236922998e-07, -9.081399558058439e-07,
          1.5634731149564544e-06, -9.998345408178578e-07, -4.454143578353981e-07, 1.65710972677186e-06,
          -1.568451647055559e-06, 8.331072027277895e-08, 1.4104732633914258e-06, -1.6300885908363385e-06,
          3.92650542309869e-07, 1.273846733905723e-06, -1.8915625007503411e-06, 8.083987401516076e-07,
          1.0229330467726357e-06, -1.9503767979227166e-06, 1.1632947821554698e-06, 6.869677636896947e-07,
          -1.640364147613519e-06, 1.3011539011227403e-06, 8.470610726859852e-08, -1.5571019320804712e-06,
          1.3160807022557972e-06, -9.298221440293115e-08, -1.3454921106718484e-06, 1.4207421756212385e-06,
          -3.644079562570327e-07, -9.101341291455163e-07, 1.6279820377890814e-06, -6.37375930491237e-07,
          -1.0932652201175163e-06, 1.913659624975891e-06, -1.0073191288364419e-06, -9.141939217192134e-07,
          1.963894751851605e-06, -9.608295211806357e-07, -5.844229130596622e-07, 1.4410385590879968e-06,
          -8.243447169216636e-07, -3.9866057088158776e-07, 1.4446580205190022e-06, -1.3631045081236509e-06,
          1.3472209462377942e-07, 1.40866279939557e-06, -1.366781348947853e-06, 3.2298034773340865e-07,
          1.0691088666063276e-06, -1.7286398607381086e-06, 9.502347405004265e-07, 6.844081619765176e-07,
          -1.890882312629353e-06, 1.159645383584843e-06, 3.4925609904879384e-07, -1.666275855569181e-06,
          1.6187787409224261e-06, -2.8878621027709555e-07, -1.3240235225147088e-06, 1.862759617555741e-06,
          -5.894402413447212e-07, -8.213178919191047e-07, 1.6787819150063081e-06, -1.2047043030853146e-06,
          -2.7060776957324e-07, 1.6329659209490398e-06, -1.7325474001669707e-06, 3.17666390817051e-07,
          1.4106607193608043e-06, -1.5086227302247588e-06, 3.0418346025196437e-07, 7.636285419334806e-07,
          -1.104002227749042e-06, 3.222363473214562e-07, 8.396748693954832e-07, -1.437422631845742e-06,
          8.957205812768728e-07, 4.039000334430381e-07, -1.585115985379185e-06, 1.4778888967999737e-06,
          -1.0660803085100953e-07, -1.38871148823417e-06, 1.8085748059028284e-06, -4.983028582095549e-07,
          -1.0715534379866837e-06, 1.6848362718577531e-06, -9.120262032905306e-07, -7.461711289821972e-07,
          1.8329899019217994e-06, -1.3573688538409308e-06, -3.594664188479277e-07, 1.8193114672710792e-06,
          -1.5579833377813057e-06, -2.7914275398989562e-08, 1.750368567762655e-06, -1.544424124300677e-06,
          1.1674203888537305e-07, 1.5786238491040447e-06, -1.7085249861620607e-06, 3.339570731807086e-07,
          1.094476093155819e-06, -1.212013463492042e-06, 3.6908002837588677e-07, 5.442450174602362e-07,
          -1.0159273867081106e-06, 4.1141336022267105e-07, 6.238556704867861e-07, -1.1862048450969593e-06,
          7.002220310246559e-07, 4.024018533747677e-07, -1.2667063961187174e-06, 1.1996540968003812e-06,
          -1.7977053995727563e-07, -1.0439922546051141e-06, 1.5724801709684757e-06, -9.314519682925817e-07,
          -6.089504492581865e-07, 1.6916697252884035e-06, -1.4908520818504972e-06, -1.0420644767119016e-07,
          1.5959465715705244e-06, -1.703785176527059e-06, 4.1454800774451304e-07, 1.2559397835347939e-06,
          -1.942227235735327e-06, 7.726214989680908e-07, 1.157134922363706e-06, -1.6266608756558452e-06,
          8.70314157220051e-07, 6.914833672276115e-07, -1.7940940647270882e-06, 1.38306417944189e-06,
          3.492976257707067e-07, -1.7240756995821445e-06, 1.717729531656638e-06, -2.7363330811185804e-07,
          -1.502466733117424e-06, 1.8634949947397497e-06, -2.9573675397946274e-07, -1.2377380219878193e-06,
          1.679811534366056e-06, -7.950886676054792e-07, -7.728684566079757e-07, 1.782796878810872e-06,
          -1.2969358718022059e-06, -4.4010320834239377e-07, 1.8116259616460483e-06, -1.332545892264546e-06,
          -1.5228601211459126e-07, 1.182651932227968e-06, -1.0279507739877935e-06, 2.7899482887659374e-07,
          8.84502977648922e-07, -1.4549508699085494e-06, 7.384239718834897e-07, 8.355342306477695e-07,
          -1.7354913475484996e-06, 9.750663699420648e-07, 6.568831833854828e-07, -1.7830394873266933e-06,
          1.4872165439481004e-06, 1.2131032829807687e-07, -1.6000503768182767e-06, 1.8309353517103294e-06,
          -4.3275851270875796e-07, -1.4364559624173548e-06, 1.698083142789893e-06, -5.406746629150831e-07,
          -1.3138148235175385e-06, 1.9827532066886054e-06, -8.711128736038924e-07, -9.222144675890577e-07,
          1.3761214713698492e-06, -7.771570137480121e-07, -6.081576209162662e-07, 1.4995681096365963e-06,
          -1.1280229674852438e-06, -2.3192145539634097e-07, 1.569715089455125e-06, -1.6508518901098726e-06,
          1.5173131825265443e-07, 1.3739297976932995e-06, -1.7616669642629311e-06, 6.60224610527342e-07,
          1.1622543380166523e-06, -1.8906576043646705e-06, 9.865934648888364e-07, 8.772371910231777e-07,
          -2.0008518717025035e-06, 1.2058326542023983e-06, 6.875541798894356e-07, -1.799852752812421e-06,
          1.5071826033003615e-06, 1.8693748106346275e-07, -1.6743015248521514e-06, 1.4196156267089565e-06,
          -6.8415444737787895e-09, -1.0948164732648812e-06, 1.1654118658218537e-06, -4.033842482045946e-07,
          -7.505969687588544e-07, 1.39285530535598e-06, -8.822739505456931e-07, -5.387372158764431e-07,
          1.6425789021775788e-06, -1.2257726987238037e-06, -3.1513726132889285e-07, 1.5073770724609039e-06,
          -1.4247703839656285e-06, 2.9674855000216903e-08, 1.3967193502356801e-06, -1.782055015496404e-06,
          7.464765879599133e-07, 9.297641626840553e-07, -1.905697969640909e-06, 1.3047901946164977e-06,
          4.7147888287211667e-07, -1.6353735057463866e-06, 1.4090883001400176e-06, 2.5396669294217053e-07,
          -1.723163234915871e-06, 1.2939677907520959e-06, 9.849745512678037e-08, -8.812369740449297e-07,
          8.412188236826297e-07, -1.8017515089686723e-07, -2.1477346380558784e-07, 6.173738636210265e-07,
          -3.966402272506463e-07, -4.773641171260036e-07, 7.66707915325116e-07, -1.0555255638998069e-07,
          -8.720353557595657e-07, 1.1721237289888678e-06, -4.4459451827256114e-07, -7.328745944841231e-07,
          1.41577009700668e-06, -9.658257291553822e-07, -3.2101896989346747e-07, 1.4209769534136962e-06,
          -1.3455836985784492e-06, 2.2427868832407983e-07, 1.2601198778678928e-06, -1.7915279533667754e-06,
          9.018236897904074e-07, 8.484610672884911e-07, -1.8873984481201984e-06, 1.3238487994676471e-06,
          3.566240655627497e-07, -1.8070554894772046e-06, 1.5501650182285155e-06, 2.999219046236688e-08,
          -1.7028056448033565e-06, 1.8241269525860013e-06, -4.4897086077233674e-07, -1.2930430362104707e-06,
          2.041579961953175e-06, -9.519571330635053e-07, -1.0906700031217052e-06, 1.8797160883181406e-06,
          -9.931194131689008e-07, -8.025475021857257e-07, 1.7966421432934103e-06, -1.3752353449205104e-06,
          -2.39170739567716e-07, 1.7516172939534133e-06, -1.6810097173643642e-06, -5.237766082751596e-08,
          1.6723060195065757e-06, -1.751940868112032e-06, 1.8596256986273679e-07, 1.4313002109986244e-06,
          -1.7605051724433693e-06, 5.753847804522484e-07, 1.145144014361546e-06, -1.6193599842415348e-06,
          7.578771676672786e-07, 8.563975806597316e-07, -1.4263414845085977e-06, 8.476631431959979e-07,
          4.779542811387732e-07, -1.6199492541347635e-06, 1.4198993878597272e-06, 3.424109008131559e-09,
          -1.4548661214692512e-06, 1.7962971006065738e-06, -6.639104660546079e-07, -1.1296143248783247e-06,
          2.0821874436618783e-06, -1.0414638700681865e-06, -8.280163687864879e-07, 1.95933640337039e-06,
          -1.2269962634249435e-06, -7.221303327804779e-07, 1.9536975863485337e-06, -1.3174901245624545e-06,
          -6.585457387435892e-07, 2.028428403296496e-06, -1.3655535343787829e-06]


def solveAndPlot(sstring):
    finalString = sstring

    def ode(y, t):
        x2, x3 = y  # x2 == possition , x3 == velocity
        error = u - x2
        funcError = func.evalFunction(error, finalString)
        dydt = [x3, (-B * x3 - k * x2 + funcError) / M]
        return dydt

    sol = odeint(ode, y0, t)
    controlingEffort = []

    for i in sol[:, 0]:
        error = u - i
        funcError = func.evalFunction(error, finalString)
        controlingEffort.append(funcError)

    plt.plot(t, sol[:, 0], 'b', label='x(t) - rasa')
    plt.plot(mengaT, mengaX, 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("0001plot_Position.png")
    plt.close()

    plt.plot(t, sol[:, 1], 'b', label='x(t) - rasa')
    plt.plot(mengaT, mengaV, 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("001plot_Velocity.png")
    plt.close()

    plt.plot(t, controlingEffort, 'b', label='x(t) - rasa')
    plt.plot(mengaT, mengaControllingEffort, 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("01plot_CotrollingEffort.png")
    plt.close()

# menga = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
# solveAndPlot(menga)
