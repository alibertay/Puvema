import SixTeenPersonalities as stp
import CV, Sectors, advice

# TODO: Kişilik testine, seçilen sektöre ve içerikteki yetkinliklere göre bir yol belirlenecek.

for i in range(len(stp.Personality.Questions)):
    print("Lütfen soruları aşağıdaki seçeneklerle cevaplayınız:\n"
          "1 - Kesinlikle evet\n "
          "2 - Evet\n "
          "3 - Nötr\n "
          "4 - Hayır\n "
          "5 - Kesinlikle hayır")
    print(stp.Personality.Questions[i])
    choice = input()
    if choice == "1":
        answer = -2
    elif choice == "2":
        answer = -1
    elif choice == "3":
        answer = 0
    elif choice == "4":
        answer = 1
    elif choice == "5":
        answer = 2

    if i in [0,1,4,5,6,9,10,16,17,18,19,20,21,22,24,25,26,32,34,35,36,37,44,47,50,51,53,54,55]:
        isPositive = False
    else:
        isPositive = True

    if i in [0,2,3,4,5,7,8,11,12,13,22,24,25,30,33,36,42,46,47,48,49,50,51,53,54,58,59]:
        cons1 = "E"
        cons2 = "I"
    elif i in [1,9,10,14,15,16,17,18,20,21,23,26,27,32,34,37,39,43,56,57]:
        cons1 = "T"
        cons2 = "F"
    elif i in [6,38,41,44,45]:
        cons1 = "J"
        cons2 = "P"
    elif i in [19,28,29,31,35,40,52,55]:
        cons1 = "S"
        cons2 = "N"

    stp.Personality.Score(answer,cons1,cons2,isPositive)
stp.Personality.CalculateCharacter()

print("Lütfen tercih ettiğiniz sektörü işaretleyin\n")
for i in range(len(Sectors.SectorList)):
    print("{sayi} - {sektor}".format(sayi = i+1, sektor = Sectors.SectorList[i]))
choice = int(input())
advice.Advice.SectorChoice = Sectors.SectorList[choice-1]

# Özgeçmiş için daha detaylı bir çıktı alınabilir fakat şimdilik yalnızca çıktı almak istiyoruz :)
print("Özgeçmiş şablonunu oluşturmamızda bize yardımcı ol.")
BI = input("Bold mu Italic mi? B/I (N - Normal)")
SN = input("Sıralı liste mi sırasız liste mi? S/N")

CV.CV.Isim = input("Adınız: ")
CV.CV.DogumTarihi = input("Doğum tarihiniz: ")
CV.CV.Mail = input("Mail adresiniz: ")

CV.CV.Deneyimler = input("Deneyimleriniz: ")
CV.CV.Diller = input("Yabancı dilleriniz: ")
CV.CV.Egitim = input("Eğitim bilgileriniz: ")
CV.CV.Organizasyonlar = input("Üye olduğunuz organizasyonlar: ")
CV.CV.Projeler = input("Projeleriniz: ")
CV.CV.Sertifikalar = input("Sertifikalarınız: ")
CV.CV.Oduller = input("Ödül ve onurlarınız: ")
CV.CV.Yayinlar = input("Yayınlarınız: ")
CV.CV.Referanslar = input("Referanslarınız: ")
CV.CV.Vizyon = input("Vizyonunuzu tanımlayan kısa bir yazı yazınız: ")
CV.CV.CvFill()

print("Özgeçmişin hazır!\n "
      "Senin kişilik tipin: {kisilik}\n "
      "Tercih ettiğin sektör: {sektor}\n "
      "Sen {advice1}\n "
      "Tercih ettiğin sektörde çalışanlar genellikle {sektordekiler}\n "
      "Ayrıca Udemy'deki bu kursu beğenebilirsin: {kurs}".format(kisilik=stp.Personality.CharacterType,
                                                                 sektor = advice.Advice.SectorChoice,
                                                                 advice1= advice.Advice.Compare(),
                                                                 sektordekiler = advice.Advice.SectorCharacteristicAdvices[Sectors.SectorList.index(advice.Advice.SectorChoice)],
                                                                 kurs = advice.Advice.Educate()))