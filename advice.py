import SixTeenPersonalities as stp
import Sectors

class Advice:
    def __init__(self):
        self.SectorChoice = ""
        self.SectorCharacteristicAdvices = [
            # Bu kısım, projenin geliştirilmesiyle beraber LinkedIn ve Kariyer.net'teki verilerle eğitilmiş bir NLP algoritmasıyla hazırlanacaktır.
            "Sonuç odaklı ve analitik düşünebilen, Raporlama ve yazışma diline hakim, Güçlü iletişim becerilerine sahip, ekip çalışmasına yatkın.",
            "Analitik ve Algoritmik düşünce yeteneğine sahip, Yoğun çalışma temposuna ayak uydurabilen.",
            "İnsan ilişkilerinde başarılı, Dinamik, motivasyonu yüksek ve güler yüzlü, Bilgilerini, hobilerini ve yetkinliklerini öğrencilerle paylaşmaya açık, Sabırlı.",
            "Sistemli çalışan ve raporlama becerisine sahip, İnsan ilişkilerinde başarılı ve iletişim becerisi yüksek, analitik düşünebilen.",
            "Yoğun iş temposuna ayak uydurabilecek, Ekip çalışmasına yatkın,  Etkin iletişim becerisine sahip,  İnsan ilişkilerinde başarılı, müzakere yeteneği gelişmiş,  Analitik düşünebilme yeteneğine sahip.",
            "Dinamik ve Girişimci ruhlu,  Fikir ve konsept geliştirme konusunda tecrübeli, Sorumluluk alan, organizasyon ve planlama yeteneği olan.",
            "Raporlama yapabilen, Yoğun tempoda çalışabilecek, Dikkatli ve titiz.",
            "Takım çalışmasına uygun, Gelişime açık olan, Sorumluluk bilinci gelişmiş, Analatik düşünme yeteneğine sahip.",
            "Çalışkan, insan ilişkilerinde başarılı, esnek çalışma saatlerine uyabilen, Hareketli ve neşeli.",
            "Problem çözme becerisi gelişmiş, sonuç odaklı düşünebilen, pratik çözümler üretenbilen.",
            "Hedef odaklı çalışabilecek, İletişimi güçlü, güleryüzlü, ekip çalışmasına yatkın, İkna kabiliyeti yüksek.",
            "Diksiyonu düzgün,sorumluluk alabilen, analitik düşünebilen.",
            "İletişimi kuvvetli, diksiyonu düzgün, Uyumlu, takım çalışmasına yatkın."]

        self.AdviceList = [
 # Bu kısım, projenin geliştirilmesiyle beraber sixteenpersonalities'teki verilerle eğitilmiş bir NLP algoritmasıyla hazırlanacaktır.
            "Konuşkan, Keskin gözlemci, bildiğinden şaşmayan, rutine karşı, alternatif arayan birisin.",
                           "Sessiz, Çevreyi anında kavrayan, sabitleyen, Objektif, doğrucu, Anı değerlendiren birisin.",
                           "Katılımcı, Bugüne ve şimdiye odaklı, Samimi, Deneye açık, keşifçi birisin.",
                           "Olaylara ve kişilere derinlemesine bakan, Bugüne ve şimdiye odaklı, Yardımlaşmacı,yakınlık kuran, Açık fikirli birisin.",
                           "Dışa odaklı, Uyanık ve meraklı, Kişisel yargılarıyla hareket etmeyen, Programlı, kurallar koyan birisin.",
                           "Bire bir yakınlık kuran, Pratik, Eşit paylaştıran, Sürelere uyan birisin.",
                           "Dışarı etkinlikleriyle ilgili, İkna eden, Kendini adayan, geçimli, Planlayan, emreden birisin.",
                           "Kendi başına harekete geçebilen, Gerçekçi, Değerlere ve bağlılığa odaklı, Sistematik, düzenli, yöntemli birisin.",
                           "Etrafa sosyal enerji saçan, Kurguya açık, Kendi yargılarından emin, Konuları karara bağlayan birisin.",
                           "Enerjisini kendine saklayan, Hayatı, dünyayı yaşamak isteyen, Yardımlaşmacı,yakınlık kuran, İyi organize, planlı birisin.",
                           "Girişken, Açıksözlü, Gelecekteki olasılıkları kurabilen, Soruların arkasındaki itkileri gören, Parçaları birbirinden ayrı tutan birisin.",
                           "Bire bir yakınlık kuran, İçine doğanlara göre hareket eden, Samimi, Daha fazla veri toplayan, alternatif arayan birisin.",
                           "Sosyal, İç gözlemi kuvvetli, kendini tahlil edebilen, Tarafsız ve mantıklı, Geleceği dikkatle planlayan birisin.",
                           "Kendine dönük, Hayal gücü kuvvetli, kafası karışık, Siyah beyaz , test ederek düşünen, Hemen bitiren birisin.",
                           "Birçok yüzeysel ilişkisi olan, İçine doğanlara göre hareket eden, Prensiplere ve kurallara odaklı, Fikirlerle dolu, yeni fikirlerle hareket eden birisin.",
                           "Koruyucu, dışa kapalı, Fantastik, Eşit paylaştıran, Hayatın akışına açık birisin."]

    def Compare(self):
        if stp.Personality.CharacterType == "ESTP" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "ESTP" and self.SectorChoice != Sectors.SectorList[6] and stp.Personality.CharacterType == "ESTP" and self.SectorChoice != Sectors.SectorList[10] and stp.Personality.CharacterType == "ESTP" and self.SectorChoice != Sectors.SectorList[11]:
            return self.AdviceList[0]
        else:
            pass

        if stp.Personality.CharacterType == "ISTP" and self.SectorChoice != Sectors.SectorList[1] and stp.Personality.CharacterType == "ISTP" and self.SectorChoice != Sectors.SectorList[4] and stp.Personality.CharacterType == "ISTP" and self.SectorChoice != Sectors.SectorList[9] and stp.Personality.CharacterType == "ISTP" and self.SectorChoice != Sectors.SectorList[12]:
            return self.AdviceList[1]
        else:
            pass

        if stp.Personality.CharacterType == "ESFP" and self.SectorChoice != Sectors.SectorList[5] and stp.Personality.CharacterType == "ESFP" and self.SectorChoice != Sectors.SectorList[6] and stp.Personality.CharacterType == "ESFP" and self.SectorChoice != Sectors.SectorList[8]:
            return self.AdviceList[2]
        else:
            pass

        if stp.Personality.CharacterType == "ISFP" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "ISFP" and self.SectorChoice != Sectors.SectorList[5] and stp.Personality.CharacterType == "ISFP" and self.SectorChoice != Sectors.SectorList[9]:
            return self.AdviceList[3]
        else:
            pass

        if stp.Personality.CharacterType == "ESTJ" and self.SectorChoice != Sectors.SectorList[0] and stp.Personality.CharacterType == "ESTJ" and self.SectorChoice != Sectors.SectorList[3] and stp.Personality.CharacterType == "ESTJ" and self.SectorChoice != Sectors.SectorList[10] and stp.Personality.CharacterType == "ESTJ" and self.SectorChoice != Sectors.SectorList[7]:
            return self.AdviceList[4]
        else:
            pass

        if stp.Personality.CharacterType == "ISTJ" and self.SectorChoice != Sectors.SectorList[7] and stp.Personality.CharacterType == "ISTJ" and self.SectorChoice != Sectors.SectorList[0] and stp.Personality.CharacterType == "ISTJ" and self.SectorChoice != Sectors.SectorList[3] and stp.Personality.CharacterType == "ISTJ" and self.SectorChoice != Sectors.SectorList[4]:
            return self.AdviceList[5]
        else:
            pass

        if stp.Personality.CharacterType == "ESFJ" and self.SectorChoice != Sectors.SectorList[6] and stp.Personality.CharacterType == "ESFJ" and self.SectorChoice != Sectors.SectorList[8] and stp.Personality.CharacterType == "ESFJ" and self.SectorChoice != Sectors.SectorList[10] and stp.Personality.CharacterType == "ESFJ" and self.SectorChoice != Sectors.SectorList[11]:
            return self.AdviceList[6]
        else:
            pass

        if stp.Personality.CharacterType == "ISFJ" and self.SectorChoice != Sectors.SectorList[0] and stp.Personality.CharacterType == "ISFJ" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "ISFJ" and self.SectorChoice != Sectors.SectorList[7] and stp.Personality.CharacterType == "ISFJ" and self.SectorChoice != Sectors.SectorList[11] and stp.Personality.CharacterType == "ISFJ" and self.SectorChoice != Sectors.SectorList[12]:
            return self.AdviceList[7]
        else:
            pass

        if stp.Personality.CharacterType == "ENFJ" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "ENFJ" and self.SectorChoice != Sectors.SectorList[5] and stp.Personality.CharacterType == "ENFJ" and self.SectorChoice != Sectors.SectorList[6]:
            return self.AdviceList[8]
        else:
            pass

        if stp.Personality.CharacterType == "INFJ" and self.SectorChoice != Sectors.SectorList[5] and stp.Personality.CharacterType == "INFJ" and self.SectorChoice != Sectors.SectorList[7]:
            return self.AdviceList[9]
        else:
            pass

        if stp.Personality.CharacterType == "ENFP" and self.SectorChoice != Sectors.SectorList[6] and stp.Personality.CharacterType == "ENFP" and self.SectorChoice != Sectors.SectorList[8] and stp.Personality.CharacterType == "ENFP" and self.SectorChoice != Sectors.SectorList[10]:
            return self.AdviceList[10]
        else:
            pass

        if stp.Personality.CharacterType == "INFP" and self.SectorChoice != Sectors.SectorList[0] and stp.Personality.CharacterType == "INFP" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "INFP" and self.SectorChoice != Sectors.SectorList[3] and stp.Personality.CharacterType == "INFP" and self.SectorChoice != Sectors.SectorList[7]:
            return self.AdviceList[11]
        else:
            pass

        if stp.Personality.CharacterType == "ENTJ" and self.SectorChoice != Sectors.SectorList[2] and stp.Personality.CharacterType == "ENTJ" and self.SectorChoice != Sectors.SectorList[6] and stp.Personality.CharacterType == "ENTJ" and self.SectorChoice != Sectors.SectorList[10]:
            return self.AdviceList[12]
        else:
            pass

        if stp.Personality.CharacterType == "INTJ" and self.SectorChoice != Sectors.SectorList[0] and stp.Personality.CharacterType == "INTJ" and self.SectorChoice != Sectors.SectorList[1] and stp.Personality.CharacterType == "INTJ" and self.SectorChoice != Sectors.SectorList[7] and stp.Personality.CharacterType == "INTJ" and self.SectorChoice != Sectors.SectorList[12]:
            return self.AdviceList[13]
        else:
            pass

        if stp.Personality.CharacterType == "ENTP" and self.SectorChoice != Sectors.SectorList[1] and stp.Personality.CharacterType == "ENTP" and self.SectorChoice != Sectors.SectorList[3] and stp.Personality.CharacterType == "ENTP" and self.SectorChoice != Sectors.SectorList[8] and stp.Personality.CharacterType == "ENTP" and self.SectorChoice != Sectors.SectorList[11] and stp.Personality.CharacterType == "ENTP" and self.SectorChoice != Sectors.SectorList[9]:
            return self.AdviceList[14]
        else:
            pass

        if stp.Personality.CharacterType == "INTP" and self.SectorChoice != Sectors.SectorList[1] and stp.Personality.CharacterType == "INTP" and self.SectorChoice != Sectors.SectorList[3] and self.SectorChoice != Sectors.SectorList[12]:
            return self.AdviceList[15]
        else:
            pass

    def Educate(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import time
        from bs4 import BeautifulSoup

        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)

        self.SectorChoice = self.SectorChoice.replace(" ","+")
        self.SectorChoice = self.SectorChoice.replace("ı","i")
        self.SectorChoice = self.SectorChoice.replace("ş","s")
        self.SectorChoice = self.SectorChoice.replace("ü","u")
        self.SectorChoice = self.SectorChoice.replace("ö","u")
        self.SectorChoice = self.SectorChoice.replace("ğ","g")
        self.SectorChoice = self.SectorChoice.replace("ç","c")

        browser.get("https://www.udemy.com/courses/search/?src=ukw&q={sektor}".format(sektor = self.SectorChoice.lower()))
        time.sleep(2)

        source = browser.page_source
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find_all("div", {"class": "course-list--container--3zXPS"})

        for table in table:
            certificate = table.find("a", {"class": "udlite-custom-focus-visible browse-course-card--link--3KIkQ"})
        return certificate.text
        time.sleep(3)
        browser.close()
Advice = Advice()