class Personality:
    # Alttaki değişkenleri her inputtan sonra puanlamaya göre arttır ya da azalt
    def __init__(self):
        self.Introver = 0
        self.Extraver = 0
        self.Sensing = 0
        self.Intuition = 0
        self.Thinking = 0
        self.Feelings = 0
        self.Judgement = 0
        self.Perception = 0
        self.CharacterType = ""
        self.Questions = [
            "1)Kendinizi başka kişilere tanıtmayı zor buluyorsunuz.",
            "2)E-postalarınıza mümkün olduğu kadar çabuk yanıt vermeye çalışıyor ve dağınık bir gelen kutusuna tahammül edemiyorsunuz.",
            "3)Çoğunlukla düşüncelerinizde öyle kayboluyorsunuz ki, etrafınızdakileri görmezden geliyor veya unutuyorsunuz.",
            "4)Biraz baskı olan durumlarda bile, kolay şekilde rahat ve odaklı kalabiliyorsunuz.",
            "5)Genellikle konuşmaları başlatan taraf siz değilsiniz.",
            "6)Nadiren sırf meraktan bir şey yapıyorsunuz.",
            "7)Kendinizi başka kişilere tanıtmayı zor buluyorsunuz.",
            "8)Kendinizi diğer insanlardan üstün hissediyorsunuz.",
            "9)Sizin için düzenli olmak uyum sağlamaktan daha önemli.",
            "10)Genellikle yüksek motivasyona sahip ve enerjiksiniz.",
            "11)Bir tartışmayı kazanmak, kimsenin üzülmemesini sağlamaktan daha önemsiz.",
            "12)Çoğunlukla kendinizi diğer insanlara karşı haklı göstermek zorunda olduğunuzu hissediyorsunuz.",
            "13)Ev ve iş ortamlarınız oldukça düzenli.",
"14)İlgi merkezi olmaktan çekinmiyorsunuz."
,"15)Yaratıcı olmaktan çok pratik olduğunuzu düşünüyorsunuz."
,"16)İnsanlar sizi nadiren üzebilir."
,"17)Seyahat planlarınız genellikle iyi düşünülmüştür."
,"18)Sizin için diğer insanların duygularıyla bağ kurmak çoğunlukla zordur."
,"19)Ruh haliniz çok hızlı değişebiliyor."
,"20)İlgi merkezi olmaktan çekinmiyorsunuz."
,"21)Yaratıcı olmaktan çok pratik olduğunuzu düşünüyorsunuz."
,"22)İnsanlar sizi nadiren üzebilir."
,"23)Seyahat planlarınız genellikle iyi düşünülmüştür."
,"24)Sizin için diğer insanların duygularıyla bağ kurmak çoğunlukla zordur."
,"25)Ruh haliniz çok hızlı değişebiliyor."
,"26)Eylemlerinizin diğer insanları nasıl etkilediği konusunda nadiren endişe duyuyorsunuz."
,"27)Çalışma tarzınız yöntemsel ve organize bir yaklaşımdan çok, rastgele enerji patlamalarına daha yakın."
,"28)Çoğunlukla başkalarına imreniyorsunuz."
,"29)İlginç bir kitap veya video oyunu, çoğunlukla sosyal bir etkinlikten daha iyi."
,"30)Her projenin en önemli kısmı, bir plan geliştirmek ve buna bağlı kalabilmektir."
,"31)Doğada yürürken kendinizi çoğunlukla düşüncelerinizde kaybolmuş şekilde buluyorsunuz."
,"32)Eğer birisi e-postanıza hızlı şekilde yanıt vermezse, söylediğiniz bir şeyin yanlış olup olmadığı hakkında endişelenmeye başlıyorsunuz."
,"33)Bir ebeveyn olarak, çocuğunuzun zekiden çok nazik olarak büyümesini tercih ediyorsunuz."
,"34)Başkalarının eylemlerinizi etkilemesine izin vermiyorsunuz."
,"35)Hayalleriniz gerçek dünyaya ve içindeki olaylara odaklanma eğiliminde."
,"36)Yeni işyerinizde, sosyal etkinliklere katılmaya başlamanız uzun sürmüyor."
,"37)Dikkatli planlamacıdan çok, doğuştan doğaçlama yapan birisiniz."
,"38)Duygularınız, onları kontrol ettiğinizden daha çok sizi kontrol ediyor."
,"39)Kıyafet giyme ve rol oynama etkinlikleri içeren sosyal etkinliklere gitmekten zevk alıyorsunuz."
,"40)Çoğunlukla gerçek dışı ve mantıksız, ancak ilginç olan fikirleri keşfetmek için vakit harcıyorsunuz."
,"41)Detaylı bir plan oluşturmak için vakit harcamak yerine doğaçlama yapmayı tercih ediyorsunuz."
,"42)Nispeten ketum ve sessiz birisiniz."
,"43)Bir işletme sahibi olsaydınız, sadık ama düşük performanslı çalışanları işten çıkarmanız çok zor olurdu."
,"44)Çoğunlukla, insanın varoluşunun nedenlerini düşünüyorsunuz."
,"45)Önemli kararlar verirken, mantık genellikle kalpten daha önemli."
,"46)Seçeneklerinizi açık tutmak, bir yapılacaklar listesine sahip olmaktan daha önemli."
,"47)Eğer arkadaşınız bir şey hakkında üzgünse, sorunu çözmek için yöntemler önermek yerine duygusal destek sunmanız daha muhtemel."
,"48)Kendinizi nadiren güvensiz hissediyorsunuz."
,"49)Kişisel bir zaman çizelgesi oluşturma ve buna bağlı kalma konusunda herhangi bir zorluk yaşamıyorsunuz."
,"50)Konu ekip çalışması olduğunda, haklı olmak işbirlikçi olmaktan daha önemli."
,"51)Gerçeklerle desteklensin veya desteklenmesin, herkesin görüşlerine saygı duyulması gerektiğini düşünüyorsunuz."
,"52)Bir grup insanla birlikte vakit geçirdikten sonra, kendinizi daha enerjik hissediyorsunuz."
,"53)Eşyalarınızı sık sık yanlış yerlere koyuyorsunuz."
,"54)Kendinizi duygusal açıdan çok kararlı görüyorsunuz."
,"55)Zihniniz daima keşfedilmemiş fikirler ve planlarla meşgul."
,"56)Kendinize bir hayalperest demezsiniz."
,"57)Genellikle birçok kişi önünde konuşurken rahat olmakta zorluk çekiyorsunuz."
,"58)Genel anlamda, hayal gücünüzden çok deneyiminize güveniyorsunuz."
,"59)Başkalarının ne düşündüğü hakkında çok fazla endişe ediyorsunuz."
,"60)Eğer oda doluysa, duvarlara daha yakın duruyor ve ortada durmaktan kaçınıyorsunuz."
        ]

    def Score(self, answer, cons1,cons2,isPositive):
        if cons1 == "E" and cons2 == "I" and isPositive == False:
            if answer <= 0:
                self.Introver -= answer
            else:
                self.Extraver += answer
        elif cons1 == "E" and cons2 == "I" and isPositive == True:
            if answer <= 0:
                self.Extraver -= answer
            else:
                self.Introver += answer

        if cons1 == "S" and cons2 == "N" and isPositive == False:
            if answer <= 0:
                self.Intuition -= answer
            else:
                self.Sensing += answer
        elif cons1 == "S" and cons2 == "N" and isPositive == True:
            if answer <= 0:
                self.Sensing -= answer
            else:
                self.Intuition += answer

        if cons1 == "T" and cons2 == "F" and isPositive == False:
            if answer <= 0:
                self.Feelings -= answer
            else:
                self.Thinking += answer
        elif cons1 == "S" and cons2 == "N" and isPositive == True:
            if answer <= 0:
                self.Thinking -= answer
            else:
                self.Feelings += answer

        if cons1 == "J" and cons2 == "P" and isPositive == False:
            if answer <= 0:
                self.Perception -= answer
            else:
                self.Judgement += answer
        elif cons1 == "S" and cons2 == "N" and isPositive == True:
            if answer <= 0:
                self.Judgement -= answer
            else:
                self.Perception += answer

    def CalculateCharacter(self):
        if self.Introver > self.Extraver:
            self.CharacterType = self.CharacterType + "I"

        elif self.Extraver > self.Introver:
            self.CharacterType = self.CharacterType + "E"

        else:
            pass

        if self.Sensing > self.Intuition:
            self.CharacterType = self.CharacterType + "S"

        elif self.Intuition > self.Sensing:
            self.CharacterType = self.CharacterType + "N"

        else:
            pass

        if self.Thinking > self.Feelings:
            self.CharacterType = self.CharacterType + "T"

        elif self.Feelings > self.Thinking:
            self.CharacterType = self.CharacterType + "F"

        else:
            pass

        if self.Judgement > self.Perception:
            self.CharacterType = self.CharacterType + "J"

        elif self.Perception > self.Judgement:
            self.CharacterType = self.CharacterType + "P"

        else:
            pass

Personality = Personality()