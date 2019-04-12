import random
def generateurListeAdresse():
    listeAdresse=[]
    file = open('adresse.txt','r')
    while len(listeAdresse)<1000:
        a=str(file.readline())
        a=a[:-1]
        a+=str(file.readline())
        a=a[:-1]

        if "'" not in a:
            listeAdresse.append(a)
    return listeAdresse

def generateurListeNom():
    listeNom=[]
    file = open('nom.txt','r')
    while len(listeNom)<1000:
        a=str(file.readline())
        a=a[:-1]

        if "'" not in a:
            listeNom.append(a)
    return listeNom

def generateurListePrenom():
    listePrenom=[]
    file = open('prenom.txt','r')
    while len(listePrenom)<1000:
        a=str(file.readline())
        a=a[:-1]
        if "'" not in a:
            listePrenom.append(a)
    return listePrenom

def generateurEmail():
    char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",
    "z","1","2","3","4","5","6","7","8","9","0"]

    listeemail=[]

    while len(listeemail)<1000:
        email = ""
        nb = random.randrange(5,10)
        c = 0
        while c < nb:
            email+=random.choice(char)
            c += 1
        email+=random.choice(["@hotmail.com","@gmail.com","@yahoo.com"])
        if email not in listeemail:
            listeemail.append(email)
    return listeemail

def listeCarteCredit():
    listeCarteCredit=[]
    while len(listeCarteCredit)<1000:
        cc = ""
        while len(cc) < 16:
            cc += str(random.randrange(0,9))
        if cc not in listeCarteCredit:
            listeCarteCredit.append(cc)
    return listeCarteCredit

def generateurMDP():
    char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",
    "z","1","2","3","4","5","6","7","8","9","0"]

    listeMDP=[]

    while len(listeMDP)<1000:
        mdp = ""
        nb = random.randrange(5,10)
        c = 0
        while c < nb:
            mdp+=random.choice(char)
            c += 1

        listeMDP.append(mdp)
    return listeMDP

def creationScriptClient(listeAdresse,listeNom,listePrenom,listeemail,listeCarteCredit,listeMDP,):

    f = open("scriptClient.txt","+w")
    f.write("use Bibilunette \ninsert into Client \n(courriel,nom,prenom,adresse,numCarte,motPasse) \nVALUES \n")

    for i in range(1000):
        if i !=999:
            client = ("('"+listeemail[i]+"','"
            +listeNom[i]+"','"
            +listePrenom[i]+"','"
            +listeAdresse[i]+"','"
            +listeCarteCredit[i]+"','"
            +listeMDP[i]+"'),\n")
            f.write(client)


        else:
            client = ("('"+listeemail[i]+"','"
            +listeNom[i]+"','"
            +listePrenom[i]+"','"
            +listeAdresse[i]+"','"
            +listeCarteCredit[i]+"','"
            +listeMDP[i]+"');")
            f.write(client)

    f.close()


def creationScriptLunette():
        listeItem=[]
        listeItemrejete=[]

        f = open("scriptLunette.txt","+w")
        f.write("use Bibilunette \ninsert into Lunette \n(sku,collection ,forme ,materiel ,largeVerre ,longBranche ,largePont ,quantite ,prix ,lightWeight ,springHinge ,adjustNosePad ,image) \nVALUES \n")
        for i in range(1000):
            c = 0
            while c == 0:
                collection = random.choice(["Aqua","Oceana","Rif","HighTide","Tsunamit","SummerLove"])
                forme = random.choice(["Ronde","Rectangle","Aviateur","Oval"])
                materiel = random.choice(["Metal","Bois","Ivoire","Plastique"])
                largeVerre = random.choice(["55mm","60mm","65mm"])
                longbranche = random.choice(["135mm","140mm","145mm"])
                largePont = random.choice(["18mm","20mm","22mm"])
                quantite = str(random.randrange(5,20))
                prix = (str(random.randrange(399,1299,50))+".99")
                lightWeight =  str(random.randrange(0,2))
                springHinge = str(random.randrange(0,2))
                adjustNosePad = str(random.randrange(0,2))

                if forme =="Ronde" and materiel == "Metal":
                        image = "rond_metal.jpg"
                if forme =="Ronde" and materiel == "Bois":
                        image = "rond_Bois.jpg"
                if forme =="Ronde" and materiel == "Ivoir":
                        image = "rond_Ivoire.jpg"
                if forme =="Ronde" and materiel == "Plastique":
                        image = "rond_Plastique.jpeg"


                if forme =="Rectangle" and materiel == "Metal":
                    image = "rectangle_metal.jpg"
                if forme =="Rectangle" and materiel == "Bois":
                    image = "rectangle_Bois.jpg"
                if forme =="Rectangle" and materiel == "Ivoir":
                    image = "rectangle_Ivoire.png"
                if forme =="Rectangle" and materiel == "Plastique":
                    image = "rectangle_Plastique.png"



                if forme =="Aviateur" and materiel == "Metal":
                    image = "aviateur_metal.jpg"
                if forme =="Aviateur" and materiel == "Bois":
                    image = "aviateur_Bois.jpg"
                if forme =="Aviateur" and materiel == "Ivoir":
                    image = "aviateur_Ivoire.jpg"
                if forme =="Aviateur" and materiel == "Plastique":
                    image = "aviateur_Plastique.jpg"





                if forme == "Oval" and materiel == "Metal":
                    image = "oval_metal.jpg"
                if forme == "Oval" and materiel == "Bois":
                    image = "oval_Bois.jpg"
                if forme == "Oval" and materiel == "Ivoir":
                    image = "oval_Ivoire.jpg"
                if forme == "Oval" and materiel == "Plastique":
                    image = "oval_Plastique.png"


                sku = ""
                sku =( "1-"+collection[:2]
                    +materiel[:2]
                    +largeVerre[:2]
                    +longbranche[:3]
                    +largePont[:2]
                    +lightWeight[0]
                    +springHinge[0]
                    +adjustNosePad[0])
                if sku not in listeItem:

                    listeItem.append(sku)
                    c = 1
                else:

                    listeItemrejete.append(sku)



            if i !=999:
                lunette = ("('"+sku+"','"
                +collection+"','"
                +forme+"','"
                +materiel+"','"
                +largeVerre+"','"
                +longbranche+"','"
                +largePont+"','"
                +quantite+"','"
                +prix+"','"
                +lightWeight+"','"
                +springHinge+"','"
                +adjustNosePad+"','"
                +image+"'),\n")
                f.write(lunette)

            else:
                lunette = ("('"+sku+"','"
                +collection+"','"
                +forme+"','"
                +materiel+"','"
                +largeVerre+"','"
                +longbranche+"','"
                +largePont+"','"
                +quantite+"','"
                +prix+"','"
                +lightWeight+"','"
                +springHinge+"','"
                +adjustNosePad+"','"
                +image+"');")
                f.write(lunette)
                print(lunette)
        f.close()
        print (len(listeItem))
        print (len(listeItemrejete))

if __name__=="__main__":

    listeAdresse = generateurListeAdresse()
    listeNom = generateurListeNom()
    listePrenom = generateurListePrenom()
    listeemail = generateurEmail()
    listeCarteCredit = listeCarteCredit()
    listeMDP = generateurMDP ()
    print ("nb d'adresse : ",len(listeAdresse),
    "\n","nb de nom : ",len(listeNom),
    "\n","nb de email : ",len(listeemail),
    "\n","nb de prenom : ",len(listePrenom),
    "\n","nb de cc : ",len(listeCarteCredit),
    "\n","nb de mdp : ",len(listeMDP))

    creationScriptClient(listeAdresse, listeNom, listePrenom, listeemail, listeCarteCredit, listeMDP)
    creationScriptLunette()
