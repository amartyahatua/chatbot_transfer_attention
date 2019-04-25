import random
import pandas as pd

class GenerateData(object):
    def __init__(self):

        #common
        self.len = 0
        self.zip = [[99501,99950],[35004,36925],[71601,72959,75502,75502],[85001,86556],[90001,96162],[80001,81658],[6001,6389,6401,6928],[19701,19980],[32004,34997],[30001,31999,39901,39901],[96701,96898],[50001,52809,68119,68120],[83201,83876],[60001,62999],[46001,47997],[66002,67954],[40003,42788],[70001,71232,71234,71497],[1001,2791,5501,5544],[20331,20331,20335,20797,20812,21930],[3901,4992],[48001,49971],[55001,56763],[63001,65899],[38601,39776,71233,71233],[59001,59937],[27006,28909],[58001,58856],[68001,68118,68122,69367],[3031,3897],[7001,8989],[87001,88441],[88901,89883],[6390,6390,10001,14975],[43001,45999],[73001,73199,73401,74966],[97001,97920],[15001,19640],[2801,2940],[29001,29948],[57001,57799],[37010,38589],[73301,73301,75001,75501,75503,79999],[84001,84784],[20040,20041,20040,20167,20042,20042],[5001,5495,5601,5907],[98001,99403],[53001,54990],[24701,26886],[82001,83128]]
        self.ziptxc = [[35233,35205,35243],[91010,92037,92354,90027,90048,90057,90095,90033,92868,39402,94304,92501,95816,95817,92123,92093,92024,94109,94158,94143,94305,90509,91010,92037,92354,90027,90048,90057,90095,90033,92868,39402,4304,92501,95816,95817,92123,92093,92024,94109,94158,94143,94305,90509],[85016,85006,85054],[72205,72202,72762,72401,72209],[91010,92037,92354,90027,90048,90057,90095,90033,92868,39402,94304,92501,95816,95817,92123,92093,92024,94109,94158,94143,94305,90509,91010,92037,92354,90027,90048,90057,90095,90033,92868,39402,4304,92501,95816,95817,92123,92093,92024,94109,94158,94143,94305,90509],[80045,80206,80210,80218],[6102,6510],[19702,19803],[32114,33316,32608,33021,32224,33770,33136,32819,32504,33701,33606,33331,32803],[30322,30309,30912,30322],[96813,98105,98122,98195,98101,99204],[60611,60612,60637,60153,60453,61637,62781,60611,60612],[46804,46260,47432],[50309,52246,52242,50309],[66160],[40536,40202,40202],[70118,70121,70112,71103],[4102],[21287,21207],[20889],[2215,2114,2111,2115,2118,2115,1805,1199,1605],[48109,48201,48202,48201,48236,49503,49503,49503,48304],[55407,55404,55415,55454,55902,55902],[39216],[65212,64108,64111,64132,63110,63110,63110,63104],[58501,58104],[68114,68198],[89102],[3766],[8103,7601,7039,8901,7103,7112],[87131,87106],[12208,10467,10468,11203,14215,11030,11040,10032,10065,33140,10016,14642,11794,13421,10595],[27514,28203,27710,27834,27157],[58501,58104],[45229,45219,45219,44106,44109,43205,43210,43614],[73104,73104,74137,73104],[97210,97239,97239],[18103,17822,16550,17110,17033,19141,19102,19134,19107,19140,19104,19104,15213,16148,15212,15224,19013,19096],[2905],[29425,29425],[57105,57117],[37403,37920,38103,38120,37203,37205,37232,37212,37212],[78705,78758,78411,75235,75235,75203,75203,75203,75246,78539,79902,76104,76104,76104,76104,77555,77030,77030,77030,77030,77030,78207,78229,77030,76508],[84107,84132,84113],[5401],[22908,22042,23507,23507,23229,23298,23249],[98105,98122,98195,98101,99204],[25526],[53792,53226,53226,53215],[57105,57117]]
        self.ziptxcdict = {35233:"ALCH - Children's of Alabama:Birmingham",35205:"ALUA - University of Alabama Hospital	Birmingham",35243:"ALVA - Birmingham VA Medical Center	Birmingham",91010:"CAHP - City of Hope National Medical Center	Duarte",92037:"CAGH - Scripps Green Hospital	La Jolla",92354:"CALL - Loma Linda University Medical Center	Loma Linda",90027:"CACL - Childrens Hospital Los Angeles	Los Angeles",90048:"CACS - Cedars-Sinai Medical Center	Los Angeles",90057:"CASV - St. Vincent Medical Center	Los Angeles",90095:"CAUC - University of California at Los Angeles Medical Center	Los Angeles",90033:"CAUH - Keck Hospital of USC	Los Angeles",92868:"CAIM - University of California Irvine Medical Center	Orange",39402:"CASJ - Saint Joseph Hospital	Orange",94304:"CAPC - Lucile Salter Packard Children's Hospital at Stanford	Palo Alto",92501:"CARC - Riverside Community Hospital  *	Riverside",95816:"CASG - Sutter Medical Center Sacramento	Sacramento",95817:"CASM - University of California Davis Medical Center	Sacramento",92123:"CASH - Sharp Memorial Hospital	San Diego",92093:"CASD - University of California San Diego Medical Center	San Diego",92024:"CACH - Rady Children's Hospital and Health Center	San Diego",94109:"CAPM - California Pacific Medical Center-Van Ness Campus	San Francisco",94158:"CAMB - UCSF Medical Center at Mission Bay	San Francisco",94143:"CASF - University of California San Francisco Medical Center	San Francisco",94305:"CASU - Stanford Health Care	Stanford",90509:"CALA - Harbor UCLA Medical Center	Torrance",91010:"CAHP - City of Hope National Medical Center	Duarte",92037:"CAGH - Scripps Green Hospital	La Jolla",92354:"CALL - Loma Linda University Medical Center	Loma Linda",90027:"CACL - Childrens Hospital Los Angeles	Los Angeles",90048:"CACS - Cedars-Sinai Medical Center	Los Angeles",90057:"CASV - St. Vincent Medical Center	Los Angeles",90095:"CAUC - University of California at Los Angeles Medical Center	Los Angeles",90033:"CAUH - Keck Hospital of USC	Los Angeles",92868:"CAIM - University of California Irvine Medical Center	Orange",39402:"CASJ - Saint Joseph Hospital	Orange",94304:"CAPC - Lucile Salter Packard Children's Hospital at Stanford	Palo Alto",92501:"CARC - Riverside Community Hospital  *	Riverside",95816:"CASG - Sutter Medical Center Sacramento	Sacramento",95817:"CASM - University of California Davis Medical Center	Sacramento",92123:"CASH - Sharp Memorial Hospital	San Diego",92093:"CASD - University of California San Diego Medical Center	San Diego",92024:"CACH - Rady Children's Hospital and Health Center	San Diego",94109:"CAPM - California Pacific Medical Center-Van Ness Campus	San Francisco",94158:"CAMB - UCSF Medical Center at Mission Bay	San Francisco",94143:"CASF - University of California San Francisco Medical Center	San Francisco",94305:"CASU - Stanford Health Care	Stanford",90509:"CALA - Harbor UCLA Medical Center	Torrance",85016:"ARBH - Baptist Medical Center	Little Rock",85006:"ARCH - Arkansas Children's Hospital	Little Rock",85054:"ARUA - UAMS Medical Center	Little Rock",72205:"AZCH - Phoenix Children's Hospital	Phoenix",72202:"AZGS - Banner-University Medical Center Phoenix	Phoenix",72762:"AZMC - Mayo Clinic Hospital	Phoenix",72401:"AZSJ - St. Joseph's Hospital and Medical Center	Phoenix",72209:"AZUA - Banner University Medical Center-Tucson	Tucson",91010:"CAHP - City of Hope National Medical Center	Duarte",92037:"CAGH - Scripps Green Hospital	La Jolla",92354:"CALL - Loma Linda University Medical Center	Loma Linda",90027:"CACL - Childrens Hospital Los Angeles	Los Angeles",90048:"CACS - Cedars-Sinai Medical Center	Los Angeles",90057:"CASV - St. Vincent Medical Center	Los Angeles",90095:"CAUC - University of California at Los Angeles Medical Center	Los Angeles",90033:"CAUH - Keck Hospital of USC	Los Angeles",92868:"CAIM - University of California Irvine Medical Center	Orange",39402:"CASJ - Saint Joseph Hospital	Orange",94304:"CAPC - Lucile Salter Packard Children's Hospital at Stanford	Palo Alto",92501:"CARC - Riverside Community Hospital  *	Riverside",95816:"CASG - Sutter Medical Center Sacramento	Sacramento",95817:"CASM - University of California Davis Medical Center	Sacramento",92123:"CASH - Sharp Memorial Hospital	San Diego",92093:"CASD - University of California San Diego Medical Center	San Diego",92024:"CACH - Rady Children's Hospital and Health Center	San Diego",94109:"CAPM - California Pacific Medical Center-Van Ness Campus	San Francisco",94158:"CAMB - UCSF Medical Center at Mission Bay	San Francisco",94143:"CASF - University of California San Francisco Medical Center	San Francisco",94305:"CASU - Stanford Health Care	Stanford",90509:"CALA - Harbor UCLA Medical Center	Torrance",91010:"CAHP - City of Hope National Medical Center	Duarte",92037:"CAGH - Scripps Green Hospital	La Jolla",92354:"CALL - Loma Linda University Medical Center	Loma Linda",90027:"CACL - Childrens Hospital Los Angeles	Los Angeles",90048:"CACS - Cedars-Sinai Medical Center	Los Angeles",90057:"CASV - St. Vincent Medical Center	Los Angeles",90095:"CAUC - University of California at Los Angeles Medical Center	Los Angeles",90033:"CAUH - Keck Hospital of USC	Los Angeles",92868:"CAIM - University of California Irvine Medical Center	Orange",39402:"CASJ - Saint Joseph Hospital	Orange",94304:"CAPC - Lucile Salter Packard Children's Hospital at Stanford	Palo Alto",92501:"CARC - Riverside Community Hospital  *	Riverside",95816:"CASG - Sutter Medical Center Sacramento	Sacramento",95817:"CASM - University of California Davis Medical Center	Sacramento",92123:"CASH - Sharp Memorial Hospital	San Diego",92093:"CASD - University of California San Diego Medical Center	San Diego",92024:"CACH - Rady Children's Hospital and Health Center	San Diego",94109:"CAPM - California Pacific Medical Center-Van Ness Campus	San Francisco",94158:"CAMB - UCSF Medical Center at Mission Bay	San Francisco",94143:"CASF - University of California San Francisco Medical Center	San Francisco",94305:"CASU - Stanford Health Care	Stanford",90509:"CALA - Harbor UCLA Medical Center	Torrance",80045:"COCH - Children's Hospital Colorado	Aurora",80206:"COUC - University of Colorado Hospital/Health Science Center	Aurora",80210:"COPM - Centura Porter Adventist Hospital  *	Denver",80218:"COSL - Presbyterian/St Luke's Medical Center	Denver",6102:"CTHH - Hartford Hospital	Hartford",6510:"CTYN - Yale New Haven Hospital	New Haven",19702:"DECC - Christiana Care Health Services	Newark",19803:"DEAI - Alfred I duPont Hospital for Children	Wilmington",32114:"FLHM - Halifax Medical Center	Daytona Beach",33316:"FLBC - Broward Health Medical Center	Ft. Lauderdale",32608:"FLUF - UF Health Shands Hospital	Gainesville",33021:"FLJD - Memorial Regional Hospital/Joe DiMaggio Children's Hospital	Hollywood",32224:"FLMR - Memorial Regional Hospital	Hollywood",33770:"FLSL - Mayo Clinic Florida	Jacksonville",33136:"FLLM - Largo Medical Center	Largo",32819:"FLJM - Jackson Memorial Hospital University of Miami School of Medicine	Miami",32504:"FLFH - AdventHealth Orlando	Orlando",33701:"FLSH - Sacred Heart Hospital Pensacola	Pensacola",33606:"FLAC - Johns Hopkins All Children's Hospital  *	St. Petersburg",33331:"FLTG - Tampa General Hospital	Tampa",32803:"FLCC - Cleveland Clinic Florida Weston	Weston",30322:"GAEH - Children's Healthcare of Atlanta at Egleston	Atlanta",30309:"GAEM - Emory University Hospital	Atlanta",30912:"GAPH - Piedmont Hospital	Atlanta",30322:"GAMC - AU Medical Center",96813:"HIQM - The Queen Medical Center	Honolulu",98105:"WACH - Seattle Childrens Hospital	Seattle",98122:"WASM - Swedish Medical Center	Seattle",98195:"WAUW - University of Washington Medical Center	Seattle",98101:"WAVM - Virginia Mason Medical Center	Seattle",99204:"WASH - Providence Sacred Heart Medical Center & Children's Hospital	Spokane",60611:"ILCM - Ann & Robert H. Lurie Children's Hospital of Chicago	Chicago",60612:"ILNM - Northwestern Memorial Hospital	Chicago",60637:"ILPL - Rush University Medical Center	Chicago",60153:"ILUC - University of Chicago Medical Center	Chicago",60453:"ILUI - University of Illinois Medical Center	Chicago",61637:"ILLU - Loyola University Medical Center	Maywood",62781:"ILCH - Advocate Christ Medical Center	Oak Lawn",60611:"ILSF - OSF Saint Francis Medical Center	Peoria",60612:"ILMM - Memorial Medical Center	Springfield",46804:"INLH - Lutheran Hospital of Fort Wayne	Ft Wayne",46260:"INSV - St Vincent Hospital and Health Care Center	Indianapolis",47432:"INIM - Indiana University Health	Indianapolis",50309:"IAIM - Iowa Methodist Medical Center	Des Moines",52246:"IAMH - MercyOne Des Moines Transplant Center	Des Moines",52242:"IAVA - The Iowa City VA Health Care System	Iowa City",50309:"IAIV - University of Iowa Hospitals and Clinics Transplant Programs	Iowa City",66160:"KSUK - University of Kansas Hospital	Kansas City",40536:"KYUK - University of Kentucky Medical Center	Lexington",40202:"KYJH - Jewish Hospital	Louisville",40202:"KYKC - Norton Children's Hospital	Louisville",70118:"LACH - Children's Hospital	New Orleans",70121:"LAOF - Ochsner Foundation Hospital	New Orleans",70112:"LATU - Tulane Medical Center	New Orleans",71103:"LAWK - Willis-Knighton Medical Center	Shreveport",4102:"MEMC - Maine Medical Center	Portland",21287:"MDJH - Johns Hopkins Hospital	Baltimore",21207:"MDUM - University of Maryland Medical System	Baltimore",20889:"DCWR - Walter Reed National Military Medical Center at Bethesda	Bethesda",2215:"MABI - Beth Israel Deaconess Medical Center	Boston",2114:"MAMG - Massachusetts General Hospital	Boston",2111:"MANM - Tufts Medical Center	Boston",2115:"MAPB - Brigham and Women's Hospital	Boston",2118:"MABU - Boston Medical Center	Boston",2115:"MACH - Boston Children's Hospital	Boston",1805:"MALC - Lahey Clinic Medical Center	Burlington",1199:"MABS - Baystate Medical Center	Springfield",1605:"MAUM - UMass Memorial Medical Center	Worcester",48109:"MIUM - University of Michigan Medical Center	Ann Arbor",48201:"MICH - Children's Hospital of Michigan	Detroit",48202:"MIHF - Henry Ford Hospital	Detroit",48201:"MIHH - Harper University Hospital Detroit Medical Center	Detroit",48236:"MISJ - Ascension St. John Hospital	Detroit",49503:"MISM - Mercy Health Saint Maryâ€™s	Grand Rapids",49503:"MISH - Spectrum Health	Grand Rapids",49503:"MIDV - Helen DeVos Children's Hospital	Grand Rapids",48304:"MIBH - William Beaumont Hospital	Royal Oak",55407:"MNAN - Abbott Northwestern Hospital	Minneapolis",55404:"MNCM - Children's Minnesota	Minneapolis",55415:"MNHC - Hennepin County Medical Center	Minneapolis",55454:"MNUM - University of Minnesota Medical Center",55902:"MNMC - Rochester Methodist Hospital (Mayo Clinic)	Rochester",55902:"MNSM - Saint Marys Hospital (Mayo Clinic)	Rochester",39216:"MSUM - University of Mississippi Medical Center	Jackson",65212:"MOUM - University of Missouri Hospital and Clinics	Columbia",64108:"MOCM - Children's Mercy Hospital	Kansas City",64111:"MOLH - St Luke's Hospital of Kansas City	Kansas City",64132:"MORH - Research Medical Center	Kansas City",63110:"MOSL - SSM Health Saint Louis University Hospital	St Louis",63110:"MOCH - St. Louis Children's Hospital at Washington University Medical Center	St Louis",63110:"MOBH - Barnes-Jewish Hospital	St. Louis",63104:"MOCG - Cardinal Glennon Children's Hospital	St. Louis",58501:"NDMC - Sanford Bismarck Medical Center	Bismarck",58104:"NDSL - Sanford Medical Center Fargo	Fargo",68114:"NECH - Children's Hospital & Medical Center	Omaha",68198:"NEUN - The Nebraska Medical Center	Omaha",89102:"NVUM - University Medical Center of Southern Nevada	Las Vegas",3766:"NHDH - Mary Hitchcock Memorial Hospital	Lebanon",8103:"NJLL - Our Lady of Lourdes Medical Center	Camden",7601:"NJHK - Hackensack University Medical Center	Hackensack",7039:"NJSB - Saint Barnabas Medical Center	Livingston",8901:"NJRW - Robert Wood Johnson University Hospital	New Brunswick",7103:"NJUH - University Hospital	Newark",7112:"NJBI - Newark Beth Israel Medical Center	Newark",87131:"NMAQ - University Hospital",87106:"NMPH - Presbyterian Hospital	Albuquerque",12208:"NYAM - Albany Medical Center Hospital	Albany",10467:"NYMA - Montefiore Medical Center	Bronx",10468:"NYVA - James J. Peters VA Medical Center	Bronx",11203:"NYDS - State University of New York",14215:"NYEC - Erie County Medical Center	Buffalo",11030:"NYNS - North Shore University Hospital/Northwell Health	Manhasset",11040:"NYCC - Long Island Jewish Medical Center-Cohen Childrens Medical Center	New Hyde Park",10032:"NYCP - NY Presbyterian Hospital/Columbia Univ. Medical Center	New York",10065:"NYNY - New York-Presbyterian Hospital/Weill Cornell Medical Center	New York",33140:"NYMS - Mount Sinai Medical Center	New York",10016:"NYUC - New York University Medical Center	New York",14642:"NYFL - Strong Memorial Hospital",11794:"NYSB - University Hospital of State University of New York at Stony Brook	Stony Brook",13421:"NYUM - State University of New York Upstate Medical University	Syracuse",10595:"NYWC - Westchester Medical Center	Valhalla",27514:"NCMH - University of North Carolina Hospitals	Chapel Hill",28203:"NCCM - Carolinas Medical Center	Charlotte",27710:"NCDU - Duke University Hospital	Durham",27834:"NCEC - Vidant Medical Center	Greenville",27157:"NCBG - Wake Forest Baptist Medical Center	Winston Salem",58501:"NDMC - Sanford Bismarck Medical Center	Bismarck",58104:"NDSL - Sanford Medical Center Fargo	Fargo",45229:"OHCM - Children's Hospital Medical Center	Cincinnati",45219:"OHTC - The Christ Hospital	Cincinnati",45219:"OHUC - University of Cincinnati Medical Center	Cincinnati",44106:"OHUH - University Hospitals of Cleveland	Cleveland",44109:"OHCC - The Cleveland Clinic Foundation	Cleveland",43205:"OHCH - Nationwide Children's Hospital	Columbus",43210:"OHOU - Ohio State University Medical Center	Columbus",43614:"OHCO - University of Toledo Medical Center	Toledo",73104:"OKBC - Integris Baptist Medical Center	Oklahoma City",73104:"OKCM - Children's Hospital of Oklahoma	Oklahoma City",74137:"OKMD - OU Medical Center	Oklahoma City",73104:"OKSJ - St John Medical Center	Tulsa",97210:"ORGS - Legacy Good Samaritan Hospital and Medical Center	Portland",97239:"ORUO - Oregon Health and Science University	Portland",97239:"ORVA - VA Portland Health Care System	Portland",18103:"PALV - Lehigh Valley Hospital	Allentown",17822:"PAGM - Geisinger Medical Center	Danville",16550:"PAPH - UPMC Hamot	Erie",17110:"PAHH - Pinnacle Health System at Harrisburg Hospital	Harrisburg",17033:"PAHE - Penn State Milton S Hershey Medical Center	Hershey",19141:"PAAE - Albert Einstein Medical Center	Philadelphia",19102:"PAHM - Hahnemann University Hospital	Philadelphia",19134:"PASC - St. Christopher's Hospital for Children	Philadelphia",19107:"PATJ - Thomas Jefferson University Hospital	Philadelphia",19140:"PATU - Temple University Hospital	Philadelphia",19104:"PAUP - Hospital of the University of Pennsylvania	Philadelphia",19104:"PACP - Children's Hospital of Philadelphia	Philadelphia",15213:"PAVA - VA Pittsburgh Healthcare System	Pittsburgh",16148:"PAPT - University of Pittsburgh Medical Center	Pittsburgh",15212:"PAAG - Allegheny General Hospital	Pittsburgh",15224:"PACH - UPMC Children's Hospital of Pittsburgh	Pittsburgh",19013:"PACC - Crozer-Chester Medical Center	Upland",19096:"PALH - The Lankenau Hospital	Wynnewood",2905:"RIRH - Rhode Island Hospital	Providence",29425:"SCCH - MUSC Children's Hospital	Charleston",29425:"SCMU - Medical University of South Carolina	Charleston",57105:"SDMK - Avera McKennan Hospital	Sioux Falls",57117:"SDSV - Sanford Health/USD Medical Center	Sioux Falls",37403:"TNEM - Erlanger Medical Center	Chattanooga",37920:"TNUK - University of Tennessee Medical Center at Knoxville	Knoxville",38103:"TNLB - Le Bonheur Children's Medical Center	Memphis",38120:"TNMH - Methodist University Hospital	Memphis",37203:"TNBM - Baptist Memorial Hospital	Memphis",37205:"TNPV - Centennial Medical Center	Nashville",37232:"TNST - Saint Thomas Hospital	Nashville",37212:"TNVU - Vanderbilt University Medical Center and Nashville VA Medical Center	Nashville",37212:"TNVU - Nashville Veterans Administration Hospital	Nashville",78705:"TXCT - Seton Medical Center Austin	Austin",78758:"TXDM - North Austin Medical Center	Austin",78411:"TXDC - Driscoll Children's Hospital	Corpus Christi",75235:"TXCM - Children's Medical Center of Dallas	Dallas",75235:"TXHD - Medical City Dallas Hospital	Dallas",75203:"TXMC - Methodist Dallas Medical Center	Dallas",75203:"TXPM - Parkland Health and Hospital System	Dallas",75203:"TXSP - UT Southwestern Medical Center/William P. Clements Jr. University Hospital	Dallas",75246:"TXTX - Baylor University Medical Center	Dallas",78539:"TXDR - Doctor's Hospital at Renaissance	Edinburg",79902:"TXLP - Las Palmas Medical Center	El Paso",76104:"TXPL - Medical City Fort Worth	Fort Worth",76104:"TXFW - Texas Health Harris Methodist Fort Worth Hospital	Fort Worth",76104:"TXCF - Cook Children's Medical Center	Fort Worth",76104:"TXAS - Baylor Scott and White All Saints Medical Center-Fort Worth	Fort Worth",77555:"TXJS - University of Texas Medical Branch at Galveston	Galveston",77030:"TXHH - Memorial Hermann Hospital",77030:"TXHI - CHI St. Lukes Health Baylor College of Medicine Medical Center	Houston",77030:"TXMH - Houston Methodist Hospital	Houston",77030:"TXVA - Michael E. DeBakey VA Medical Center	Houston",77030:"TXTC - Texas Children's Hospital	Houston",78207:"TXUC - University Childrens Health	San Antonio",78229:"TXHS - Methodist Specialty and Transplant Hospital	San Antonio",77030:"TXBC - University Hospital",76508:"TXSW - Scott and White Memorial Hospital	Temple",84107:"UTLD - Intermountain Medical Center	Murray",84132:"UTMC - University of Utah Medical Center	Salt Lake City",84113:"UTPC - Primary Children's Hospital	Salt Lake City",5401:"VTMC - The University of Vermont Medical Center	Burlington",22908:"VAUV - University of Virginia Health Sciences Center	Charlottesville",22042:"VAFH - Inova Fairfax Hospital	Falls Church",23507:"VACH - Children's Hospital of the King's Daughters	Norfolk",23507:"VANG - Sentara Norfolk General Hospital	Norfolk",23229:"VAHD - Henrico Doctors' Hospital	Richmond",23298:"VAMC - Medical College of Virginia Hospitals	Richmond",23249:"VAMV - Hunter Holmes McGuire Veterans Administration Medical Center	Richmond",98105:"WACH - Seattle Children's Hospital	Seattle",98122:"WASM - Swedish Medical Center	Seattle",98195:"WAUW - University of Washington Medical Center	Seattle",98101:"WAVM - Virginia Mason Medical Center	Seattle",99204:"WASH - Providence Sacred Heart Medical Center & Children's Hospital	Spokane",25526:"WVCA - Charleston Area Medical Center	Charleston",53792:"WIUW - University of Wisconsin Hospital and Clinics	Madison",53226:"WICH - Children's Hospital of Wisconsin	Milwaukee",53226:"WISE - Froedtert Memorial Lutheran Hospital	Milwaukee",53215:"WISL - Aurora St. Lukes Medical Center	Milwaukee",57105:"SDMK - Avera McKennan Hospital	Sioux Falls",57117:"SDSV - Sanford Health/USD Medical Center	Sioux Falls"}
        self.gender = [0,1]
        self.state = [0,49]
        self.organ = [0,4]
        self.height = [121,201]
        self.weight = [40,111]
        self.autoimmune_disease = [0,1]
        self.hiv = [0,1]
        self.malignancies = [0,1]
        self.other_problem = [0,1]

        ##insulin
        self.on_insulin = [0,1]
        self.no_insulin = [0,5]
        self.time_insulin = [0,10]

        ##heart
        self.storke = [0,1]
        self.pacemaker = [0,1]

        #kidney
        self.on_dialysis = [0,1]
        self.serum_creatinine = [74,107]

        #liver
        self.life_support = [0,1]
        self.hepatitis = [0,1]
        self.fatty_liver = [0,1]

        #lung
        self.smoker = [0,1]
        self.ventilation = [0,1]
        self.pneumonia = [0,1]
        self.asthamatic = [0,1]

        self.datalist = list()


    def countIndices(self,stateCount):
        indexrange=0
        start=0
        end=0

        for i in range(0,len(self.zip[2]),2):
            #temp = self.zip[2][i]
            indexrange = indexrange + (self.zip[2][i+1] - self.zip[2][i])
        return indexrange

    def generateNumber(self,begin,end):
        return random.randrange(begin,end)

    def findthezip(self,stateCount):

        indexrange=self.countIndices(stateCount)
        randnum = self.generateNumber(0,indexrange)
        result=0
        dist = 0
        for i in range(0, len(self.zip[stateCount]), 2):
            dist = dist+(self.zip[stateCount][i+1] - self.zip[stateCount][i])
            if(randnum > dist):
                randnum=randnum-dist
            else:
                result=self.zip[stateCount][i]+randnum

        return result

    def findClosest(self,ziphospital,zip):
        mindist=99999
        minzip=0
        for i in range(len(ziphospital)):
            tempDiff=abs(ziphospital[i]-zip)
            if(tempDiff<mindist):
                minzip=ziphospital[i]
                mindist=tempDiff
        print("===")
        print(ziphospital)
        print(zip)
        print(minzip)
        return  minzip







    def findtxczip(self,state,zip):

        ziphospital=self.ziptxc[state]
        txczip=self.findClosest(ziphospital,zip)

        return txczip

    def createSingleData(self):
        gender=self.generateNumber(0,2)
        state=self.generateNumber(0,49)
        zip=self.findthezip(state)
        organ=self.generateNumber(0,4)
        height=self.generateNumber(121,201)
        weight=self.generateNumber(40,111)
        autoimmune_disease=self.generateNumber(0,2)
        hiv=self.generateNumber(0,2)
        malignancies=self.generateNumber(0,2)
        other_problem=self.generateNumber(0,2)
        txczip=self.findtxczip(state,zip)
        address=self.ziptxcdict[txczip]
        waiting=self.generateNumber(200,500)
        # print(gender)
        # print(state)
        # print(zip)
        # print(organ)
        # print(height)
        # print(weight)
        # print(autoimmune_disease)
        # print(hiv)
        # print(malignancies)
        # print(other_problem)

        ##Pancreas
        on_insulin=self.generateNumber(0,2)
        no_insulin=self.generateNumber(0,2)
        time_insulin=self.generateNumber(0,2)
        # print(on_insulin)
        # print(no_insulin)
        # print(time_insulin)

        ##Heart
        storke=self.generateNumber(0,2)
        pacemaker=self.generateNumber(0,2)
        # print(storke)
        # print(pacemaker)

        ##Kidney
        on_dialysis=self.generateNumber(0,2)
        serum_creatinine=self.generateNumber(74, 107)
        # print(on_dialysis)
        # print(serum_creatinine)


        ##Liver
        life_support=self.generateNumber(0,2)
        hepatitis=self.generateNumber(0,2)
        fatty_liver=self.generateNumber(0,2)
        # print(life_support)
        # print(hepatitis)
        # print(fatty_liver)


        ##Lung
        smoker=self.generateNumber(0,2)
        ventilation=self.generateNumber(0,2)
        pneumonia=self.generateNumber(0,2)
        asthamatic=self.generateNumber(0,2)

        # print(smoker)
        # print(ventilation)
        # print(pneumonia)
        # print(asthamatic)

        infolist=[gender,state,zip,organ,height,weight,autoimmune_disease,hiv,malignancies,other_problem,on_insulin,no_insulin,time_insulin,storke,pacemaker,on_dialysis,serum_creatinine,life_support,hepatitis,fatty_liver,smoker,ventilation,pneumonia,asthamatic,address,waiting]
        #print(infolist)
        return  infolist

    def createData(self):
        dataPoints=4

        #self.createSingleData()
        # datalist.append(self.createSingleData())
        # datalist.append(self.createSingleData())
        self.datalist.append(["gender", "state", "zip", "organ", "height", "weight", "autoimmune_disease", "hiv", "malignancies", "other_problem", "on_insulin", "no_insulin", "time_insulin", "storke", "pacemaker", "on_dialysis", "serum_creatinine", "life_support", "hepatitis", "fatty_liver", "smoker", "ventilation", "pneumonia", "asthamatic", "address", "waiting"])

        for i in range(dataPoints):
            self.datalist.append(self.createSingleData())

        df = pd.DataFrame(self.datalist)
        df.to_csv("data.csv",index=False)
        print("File created")
        #print(df)

genData = GenerateData()
genData.createData()
