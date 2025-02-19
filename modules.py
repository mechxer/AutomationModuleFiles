import random
from faker import Faker
from wonderwords import RandomWord
import string
from datetime import datetime, timedelta
import os

BASE_PATH = str(os.getcwd())


class BDNames():
    def __init__(self) -> None:
        try:
            self.BOY_FIRST_NAME = open('names/Boy-FirstNames.txt', 'r').read().split("\n")
            self.BOY_LAST_NAME = open('names/Boy-LastNames.txt', 'r').read().split("\n")
            self.GIRL_FIRST_NAME = open('names/Girl-FirstNames.txt', 'r').read().split("\n")
            self.GIRL_LAST_NAME = open('names/Girl-LastNames.txt', 'r').read().split("\n")
        except:
            self.BOY_FIRST_NAME = ['Aaban', 'Aabid', 'Aadil', 'Aahil', 'Aalam', 'Aalee', 'Aalim', 'Aamil', 'Aamir', 'Aaqib', 'Aaqil', 'Aaradhaya', 'Aarav', 'Aarif', 'Aarit', 'Aariz', 'Aarman', 'Aarnav', 'Aaron', 'Aarpit', 'Aarth', 'Aarush', 'Aarya', 'Aaryan', 'Aashank', 'Aashif', 'Aashir', 'Aashish', 'Aashka', 'Aasif', 'Aasim', 'Aatif', 'Aaus', 'Aayan', 'Aazim', 'Abaan', 'Abbas', 'Abd Al-Ala', 'Abdul Aalee', 'Abdul Adl', 'Abdul Afuw', 'Abdul Ahad', 'Abdul Aleem', 'Abdul Ali', 'Abdul Alim', 'Abdul Awwal', 'Abdul Azeez', 'Abdul Azim', 'Abdul Aziz', 'Abdul Baari', 'Abdul Baasit', 'Abdul Badee', 'Abdul Baith', 'Abdul Baqi', 'Abdul Bari', 'Abdul Baseer', 'Abdul Batin', 'Abdul Fattah', 'Abdul Ghafaar', 'Abdul Ghafoor', 'Abdul Hafeez', 'Abdul Hafiz', 'Abdul Hakam', 'Abdul Hakeem', 'Abdul Haleem', 'Abdul Halim', 'Abdul Hameed', 'Abdul Hamid', 'Abdul Hannan', 'Abdul Haq', 'Abdul Haseeb', 'Abdul Hasib', 'Abdul Hayy', 'Abdul Jabaar', 'Abdul Jaleel', 'Abdul Jawwad', 'Abdul Kabir', 'Abdul Kareem', 'Abdul Karim', 'Abdul Khabir', 'Abdul Lateef', 'Abdul Maajid', 'Abdul Maalik', 'Abdul Majeed', 'Abdul Mani', 'Abdul Mannan', 'Abdul Mateen', 'Abdul Mubdee', 'Abdul Mueed', 'Abdul Muhaimin', 'Abdul Muhaymin', 'Abdul Muhsin', 'Abdul Muhyee', 'Abdul Muiz', 'Abdul Mujeeb', 'Abdul Munim', 'Abdul Muntaqim', 'Abdul Muqeet', 'Abdul Muqsit', 'Abdul Musawwir', 'Abdul Mutaal', 'Abdul Muti', 'Abdul Muzanni', 'Abdul Nafi', 'Abdul Naseer', 'Abdul Noor', 'Abdul Qaadir', 'Abdul Qadeer', 'Abdul Qadir', 'Abdul Qahaar', 'Abdul Qayyum', 'Abdul Qudoos', 'Abdul Raafi', 'Abdul Rabb', 'Abdul Rafi', 'Abdul Raheem', 'Abdul Rahim', 'Abdul Rahman', 'Abdul Raqib', 'Abdul Rauf', 'Abdul Tawwab', 'Abdul Waali', 'Abdul Wahid', 'Abdul Wajid', 'Abdul Wakil', 'Abdul Waliy', 'Abdul Wasi', 'Abdul-Aalee', 'Abdul-Adheem', 'Abdul-Aleem', 'Abdul-Baaqi', 'Abdul-Baari', 'Abdul-Baasit', 'Abdul-Barr', 'Abdul-Dhahir', 'Abdul-Ghaffar', 'Abdul-Ghafur', 'Abdul-Ghani', 'Abdul-Hadi', 'Abdul-Hafeedh', 'Abdul-Hakeem', 'Abdul-Haleem', 'Abdul-Hameed', 'Abdul-Haqq', 'Abdul-Haseeb', 'Abdul-Jabbar', 'Abdul-Jaleel', 'Abdul-Kareem', 'Abdul-Khaliq', 'Abdul-Lateef', 'Abdul-Majeed', 'Abdul-Majid', 'Abdul-Malik', "Abdul-Mu'eid", "Abdul-Mu'izz", 'Abdul-Mughni', 'Abdul-Mujeeb', 'Abdul-Mumin', 'Abdul-Muqtadir', "Abdul-Muta'alee", 'Abdul-Nur', 'Abdul-Qaadir', 'Abdul-Qahhar', 'Abdul-Qaiyoum', 'Abdul-Quddus', 'Abdul-Rasheed', 'Abdul-Rashid', 'Abdul-Waajid', 'Abdul-Wadood', 'Abdul-Wahhab', 'Abdul-Warith', 'Abdullah', 'Abdur Rahman', 'Abdur Rashid', 'Abdur Razzaq', 'Abdur-Raheem', 'Abdur-Rahman', 'Abdur-Raqeeb', 'Abdur-Rasheed', 'Abdur-Rauf', 'Abdur-Razzaq', 'Abdus', 'Abdus Sabur', 'Abdus Salaam', 'Abdus Samad', 'Abdus Sami', 'Abdus Sattar', 'Abdus Shafi', 'Abdus Subbooh', 'Abdus-Sabour', 'Abdus-Salaam', 'Abdus-Samad', 'Abdus-Sameei', 'Abdus-Shaheed', 'Abdus-Shakur', 'Abdush Shahid', 'Abhijit', 'Abid', 'Abisali', 'Abrad', 'Abrar', 'Abrash', 'Absi', 'Abul-Hassan', 'Abyad', 'Abyan', 'Abzari', 'Adam', 'Adawi', 'Adbul-Qawi', 'Adeeb', 'Adeel', 'Adeem', 'Adel', 'Adham', 'Adheem', 'Adib', 'Adil', 'Adiy', 'Adl', 'Adnan', 'Aduz', 'Adyan', 'Afaaq', 'Afeef', 'Affan', 'Afham', 'Afif', 'Afiq', 'Aflah', 'Afraz', 'Afruz', 'Aftaab', 'Aftab', 'Afzal', 'Agharr', 'Ahab', 'Ahad', 'Ahmad', 'Ahmar', 'Ahnaf', 'Ahsan', 'Ahwas', 'Ahyan', 'Ahzab', 'Aidan', 'Aidh', 'Aijaz', 'Aiman', 'Ainal', 'Aizat', 'Ajer', 'Ajlah', 'Ajmal', 'Akbar', 'Akdas', 'Akeem', 'Akhas', 'Akhdan', 'Akhfash', 'Akhlaq', 'Akhtar', 'Akif', 'Akmal', 'Akram', 'Al-hakeem', 'Al-Kareem', "Ala'", 'Ali', 'Alman', 'Almir', 'Altamash', 'Amaan', 'Amaar', 'Amam', 'Amayr', 'Ameer', 'Amer', 'Amin', 'Amir', 'Amjad', 'Ammaar', 'Ammar', 'Amol', 'Amr', 'Anas', 'Anasah', 'Aneeq', 'Anees', 'Anik', 'Aniq', 'Anis', 'Anjam', 'Anniv', 'Ansar', 'Antarah', 'Anwaar', 'Anwar', 'Anzar', 'Aqdas', 'Aqeel', 'Aqeil', 'Arbaaz', 'Arbab', 'Areeb', 'Areez', 'Arfan', 'Arham', 'Arif', 'Arish', 'Ariyaad', 'Ariyan', 'Armaan', 'Arman', 'Arqam', 'Arsal', 'Arsalaan', 'Arsh', 'Arshad', 'Arshaq', 'Arslan', 'Artah', 'Aryan', "As'ad", 'Asad', 'Asar', 'Asbagh', 'Asbat', 'Aseed', 'Asfar', 'Asgar', 'Asghar', "Asha'ath", 'Ashar', 'Ashaz', 'Asher', 'Ashfaq', 'Ashik', 'Ashim', 'Ashmaan', 'Ashmath', 'Ashmik', 'Ashraf', 'Asim', 'Aslam', 'Asrar', 'Ata', 'Ataubaq', 'Ateeb', 'Athar', 'Athazaz', 'Athier', 'Atif', 'Atik', 'Atiq', 'Attiq', 'Avinandan', 'Awad', 'Awf', 'Awn', 'Aws', 'Ayaan', 'Ayaaz', 'Ayaz', 'Aybak', 'Aydin', 'Aylan', 'Aymaan', 'Ayman', 'Ayub', 'Ayyash', 'Ayyub', 'Azaan', 'Azad', 'Azeem', 'Azfer', 'Azhar', 'Azim', 'Azizur', 'Azlan', 'Azmat', 'Azraq', 'Azraqi', 'Azzam', 'Baahir', 'Baasim', 'Babar', 'Baber', 'Bakibilla', 'Baqar', 'Baqir', 'Barkat', 'Barr', 'Barraq', 'Basel', 'Basem', 'Bashaar', 'Bashar', 'Basharat', 'Basil', 'Basim', 'Basir', 'Bassam', 'Batal', 'Bazaan', 'Bazam', 'Behzad', 'Bilal', 'Bishr', 'Bulhut', 'Burak', 'Burayd', 'Burhaan', 'Burhan', "Da'wud", 'Daamin', 'Daanish', 'Dabbah', 'Dabir', 'Daghfal', 'Dakhil', 'Dameer', 'Damurah', 'Daniel', 'Danish', 'Daniyal', 'Darim', 'Dawid', 'Dawlah', 'Dawoud', 'Dayyan', 'Dhiya', 'Dhul', 'Dihan', 'Dilawar', 'Dildar', 'Dinar', 'Diya', 'Diyari', 'Dizhwar', 'Duha', 'Ehan', 'Ehsaas', 'Ehsan', 'Eijaz', 'Ejaz', 'El-Amin', 'Emran', 'Eshan', 'Faaiz', 'Faakhir', 'Faaris', 'Faaz', 'Fadi', 'Fadil', 'Fadl', 'Faeq', 'Fahad', 'Fahd', 'Faheem', 'Fahim', 'Fahmi', 'Fahyim', 'Faik', 'Faiq', 'Faisal', 'Faiyaz', 'Faiz', 'Faizaan', 'Faizan', 'Fajaruddin', 'Fajer', 'Fakeeh', 'Fakhr', 'Fakhri', 'Fakhrul', 'Fakih', 'Falah', 'Faqeeh', 'Farafisa', 'Faraj', 'Farasat', 'Faraz', 'Fardeen', 'Fareed', 'Farees', 'Farhan', 'Farid', 'Faris', 'Farooq', 'Farouk', 'Farrukh', 'Faruq', 'Fasahat', 'Faseeh', 'Fateen', 'Fateh', 'Fatih', 'Fatik', 'Fattah', 'Fawad', 'Fawwaz', 'Fawz', 'Fawzan', 'Fawzi', 'Fayaaz', 'Fayd', 'Fayek', 'Faysal', 'Fayzan', 'Fazal', 'Fazan', 'Feroz', 'Fiddah', 'Fidyan', 'Firas', 'Firoz', 'Fizan', 'Fuad', 'Fudail', 'Fujai', 'Furozh', 'Fuwad', 'Fuzail', 'Ghaith', 'Ghalib', 'Ghanem', 'Ghannam', 'Ghasaan', 'Ghauth', 'Ghawth', 'Ghayoor', 'Ghazalan', 'Ghazanfar', 'Ghazawan', 'Ghazi', 'Ghazzal', 'Ghiyath', 'Ghufran', 'Ghulam', 'Ghunayn', 'Ghusharib', 'Ghusun', 'Ghutayf', 'Gohar', 'Gulab', 'Gulfam', 'Gulshan', 'Gulzar', 'Haadee', 'Haaris', 'Haashir', 'Haaziq', 'Habeebullah', 'Habib', 'Habis', 'Hadee', 'Hadi', 'Hadid', 'Hafid', 'Hafiz', 'Hafs', 'Haider', 'Haikal', 'Haitham', 'Haji', 'Hajib', 'Hajjaj', 'Hakim', 'Haleef', 'Haleem', 'Hallaj', 'Halwani', 'Hamd', 'Hamdan', 'Hamdhy', 'Hamdi', 'Hameem', 'Hami', 'Hamid', 'Hamiz', 'Hammad', 'Hammam', 'Hamood', 'Hamza', 'Hamzah', 'Hanash', 'Haneef', 'Hani', 'Hanif', 'Hanifah', 'Haq', 'Haris', 'Harisah', 'Harith', 'Haroon', 'Hasan', 'Hasanuzzaman', 'Haseeb', 'Haseen', 'Hasham', 'Hashid', 'Hashim', 'Hashir', 'Hashmat', 'Hasib', 'Hasnain', 'Hassan', 'Hatib', 'Hatim', 'Hawshab', 'Hayaat', 'Hayder', 'Haytham', 'Hayyam', 'Hazim', 'Haziq', 'Hesam', 'Hibah', 'Hibbaan', 'Hidayat', 'Hilal', 'Himayat', 'Hisham', 'Hissan', 'Hooman', 'Hosaam', 'Houda', 'Hubaab', 'Hud', 'Hujayyah', 'Hujjat', 'Humaid', 'Humair', 'Humam', 'Humayl', 'Humayun', 'Humd', 'Humza', 'Hurairah', 'Hurayth', 'Hurmat', 'Hurrah', 'Husam', 'Husni', 'Hussain', 'Hussein', 'Huthayfa', 'Huzaifah', 'Huzayfah', 'Huzayl', 'Ibaad', 'Ibrahim', 'Idris', 'Iftekhar', 'Iftikhar', 'Ihab', 'Ihsan', 'Ihtesham', 'Ihtiram', 'Ihtsham', 'Ijaz', 'Ijli', 'Ikrimah', 'Ilan', 'Ilifat', 'Iliyash', 'Ilyas', 'Imaad', 'Imaan', 'Imad', 'Imran', 'Imtiaz', 'Imtiyaz', 'Inaam', 'Inayat', 'Iniat', 'Insaf', 'Intaj', 'Intikhab', 'Intizar', 'Iqbal', 'Iqraam', 'Iqrit', 'Iqtidar', 'Irfan', 'Isa', 'Isam', 'Ishaq', 'Ishrat', 'Ishtiyaq', 'Iskandar', 'Islam', "Isma'il", 'Ismah', 'Ismail', 'Israr', 'Issar', 'Istakhri', 'Ithaar', 'Itimad', 'Iyaad', 'Iyaas', 'Izaan', 'Izyan', 'Izzat', 'Jaan', 'Jabir', 'Jabr', 'Jad', 'Jafar', 'Jaffer', 'Jahangir', 'Jahanzeb', 'Jahdami', 'Jahdari', 'Jahiz', 'Jahm', 'Jakir', 'Jalal', 'Jalees', 'Jalil', 'Jamal', 'Jamesha', 'Jamil', 'Jan', 'Jaraah', 'Jareer', 'Jari', 'Jariyah', 'Jarood', 'Jarrar', 'Jasim', 'Jasmir', 'Jauhar', 'Javed', 'Javeed', 'Javier', 'Jawad', 'Jawdan', 'Jawhar', 'Jazib', 'Jazlaan', 'Jeelan', 'Jiarul', 'Jibran', 'Jibril', 'Jihad', 'Jiyad', 'Juayl', 'Jubair', 'Jubed', 'Juben', 'Juhaym', "Juma'", 'Jumanah', 'Jummal', 'Junaid', 'Junayd', 'Jundub', 'Juthamah', 'Kaamil', 'Kaashif', 'Kabeer', 'Kabir', 'Kafeel', 'Kaiser', 'Kajji', 'Kalbi', 'Kaleem', 'Kaleema', 'Kamal', 'Kamil', 'Kamran', 'Kareem', 'Karim', 'Kasam', 'Kashan', 'Kashif', 'Kasim', 'Kawkab', 'Kawthar', 'Kaysan', 'Kazi', 'Kazim', 'Keyaan', 'Khadim', 'Khafid', 'Khalaf', 'Khalam', 'Khaldun', 'Khaleed', 'Khaleel', 'Khaleeq', 'Khalid', 'Khalifah', 'Khalis', 'Khallad', 'Kharijah', 'Khasib', 'Khateeb', 'Khawar', 'Khayaam', 'Khayr', 'Khayri', 'Khayyat', 'Khazin', 'Khidash', 'Khidr', 'Khirash', 'Khubaib', 'Khubayb', 'Khulayd', 'Khunays', 'Khuram', 'Khuraymah', 'Khurram', 'Khursheed', 'Khurshid', 'Khush', 'Khushtar', 'Kifayat', 'Kinza', 'Kishwar', 'Kurayb', 'Labeeb', 'Labib', 'Labib Ahmad']
            self.BOY_LAST_NAME = ['Khan', 'Molla', 'Hossain', 'Ahmed', 'Ali', 'Das', 'Mandal', 'Islam', 'Roy', 'Rana', 'Ahmed', 'Ali', 'Chowdhury', 'Miah', 'Haque', 'Hasan', 'Hussain', 'Islam', 'Rahman', 'Khondakar', 'Khan', 'Uddin', 'Alam', 'Gupta', 'Mohammad', 'Mahmud', 'Choudhury', 'Chaudhuri', 'Ahmad', 'Uddin', 'Mia', 'Alam', 'Haque', 'Rahman', 'Sarker', 'Sharker', 'Shorker', 'Karim']
            self.GIRL_FIRST_NAME = ["A'idah", "A'ishah", "A'shadieeyah", "Aa'idah", 'Aabidah', 'Aabirah', 'Aabish', 'Aadab', 'Aadila', 'Aaeedah', 'Aaeesha', 'Aafia', 'Aafiya', 'Aafreeda', 'Aafreen', 'Aairah', 'Aakifah', 'Aala', 'Aaleyah', 'Aalia', 'Aalimah', 'Aaliyah', 'Aamaal', 'Aamanee', 'Aamilah', 'Aaminah', 'Aamira', 'Aamirah', 'Aani', 'Aanisah', 'Aaqilah', 'Aara', 'Aarifah', 'Aasia', 'Aasimah', 'Aatifa', 'Aatikah', 'Aatiqah', 'Aatirah', 'Aazeen', 'Abasah', 'Abda', 'Abdia', 'Abdul', 'Abeedah', 'Abeela', 'Abeer', 'Abeera', 'Abeerah', 'Abia', 'Abida', 'Abir', 'Ablaa', 'Ablah', 'Abqurah', 'Abra', "Ad'ifaah", 'Ada', 'Adab', 'Adeeba', 'Adeela', 'Adeelah', 'Adeena', 'Adeeva', 'Adila', 'Adla', 'Afaf', 'Afeefa', 'Afeerah', 'Afia', 'Afifa', 'Afifah', 'Afiyah', 'Afizah', 'Afra', 'Afraa', 'Afrah', 'Afreen', 'Afroza', 'Afroze', 'Afruza', 'Afsa', 'Afsana', 'Afshan', 'Afsheen', 'Ahd', 'Ahdia', 'Ahlam', 'Aida', 'Aidah', 'Aighar', 'Aila', 'Aimal', 'Aimen', 'Ain', 'Aini', 'Aisha', 'Aishah', 'Aiya', 'Aiyla', 'Aiza', 'Aizah', 'Ajeebah', 'Ajlal', 'Ajradah', 'Ajwa', 'Akia', 'Akifah', 'Akilah', 'Akleema', 'Aksa', 'Aksha', 'Al', 'Al-Adur', 'Alaia', 'Alayna', 'Aleemah', 'Aleena', 'Aleesa', 'Aleeza', 'Alesha', 'Alia', 'Aliah', 'Alika', 'Alima', 'Alina', 'Alishaba', 'Alishba', 'Aliyah', 'Aliza', 'Alleyah', 'Alma', 'Almaas', 'Almas', 'Alraaz', 'Alvina', 'Alzubra', 'Amah', 'Amal', 'Amala', 'Amalia', 'Aman', 'Amana', 'Amani', 'Amany', 'Amara', 'Amatullah', 'Amaya', 'Ambar', 'Ambareen', 'Amber', 'Ambereen', 'Ambreen', 'Ameenah', 'Ameera', 'Ameerah', 'Amel', 'Amelia', 'Amena', 'Amilah', 'Amima', 'Amina', 'Aminah', 'Aminul', 'Aminur', 'Amira', 'Amirah', 'Ammara', 'Ammarah', 'Amna', 'Amra', 'Amrah', 'Amreen', 'Amtullah', 'Ana', 'Anah', 'Anam', 'Anan', 'Anaum', 'Anbar', 'Andaleeb', 'Andalib', 'Andlib', 'Aneeqa', 'Aneesa', 'Aneesah', 'Aneezah', 'Angbin', 'Anida', 'Anika', 'Anila', 'Anisa', 'Anisah', 'Anisha', 'Aniya', 'Anja', 'Anjum', 'Annam', 'Anniyah', 'Anousha', 'Anum', 'Anwara', 'Anya', 'Aqeela', 'Aqeelah', 'Aqsa', 'Ara', 'Arabia', 'Areebah', 'Areej', 'Aresha', 'Arfa', 'Ariana', 'Aribah', 'Arij', 'Arisha', 'Arissa', 'Ariyana', 'Arjumand', 'Aroob', 'Aroosa', 'Aroush', 'Arsala', 'Arub', 'Arva', 'Arwa', 'Arya', 'Aryisha', 'Arzo', 'Arzoo', 'Arzu', 'Asalah', 'Asbah', 'Asfa', 'Asfia', 'Asfiya', 'Ashalina', 'Ashbah', 'Asheeyana', 'Ashika', 'Ashiq', 'Asifa', 'Asili', 'Asima', 'Asiya', 'Asiyah', 'Asli', 'Asma', 'Asmara', 'Asmat', 'Asna', 'Asra', 'Ateefa', 'Ateeqah', 'Ateeyah', 'Athilah', 'Athmah', 'Atia', 'Atifa', 'Atika', 'Atiqah', 'Atiqur', 'Atiya', 'Awa', 'Awatif', 'Aya', 'Ayaana', 'Ayaat', 'Ayah', 'Ayan', 'Ayana', 'Ayat', 'Ayesha', 'Aymen', 'Ayra', 'Aysha', 'Ayshah', 'Az-zahra', 'Azadeh', 'Azeemah', 'Azeeza', 'Azhaar', 'Aziman', 'Aziz', 'Azizah', 'Azka', 'Azma', 'Azmina', 'Azra', 'Azraa', 'Azzah', 'Badia', 'Badiyah', 'Badra', 'Badriyah', 'Baha', 'Bahaa', 'Bahar', 'Bahij', 'Bahira', 'Bahiya', 'Bahiyyah', 'Bahriyah', 'Bakht', 'Bakhtawar', 'Balqees', 'Balqis', 'Banafsha', 'Banan', 'Bangladesh', 'Banujah', 'Barakah', 'Bareerah', 'Bariah', 'Barika', 'Barrah', 'Barsha', 'Barzah', 'Basaaria', 'Basbas', 'Baseema', 'Basheera', 'Bashirah', 'Basilah', 'Basimah', 'Basmah', 'Basoos', 'Batinah', 'Batool', 'Batrisyia', 'Bazilah', 'Beena', 'Beenish', 'Benazir', 'Benzair', 'Bilqis', 'Binesh', 'Binish', 'Birrah', 'Bisharah', 'Bisma', 'Boshir', 'Buhaysah', 'Buhayyah', 'Bunanah', 'Buqayrah', 'Burdah', 'Bushra', 'Bushrah', 'Busrah', 'Buthaynah', 'Chaman', 'Chanda', 'Chandni', 'Daania', 'Daanya', 'Dafiyah', 'Dahab', 'Dahma', 'Daleela', 'Daliya', 'Daneen', 'Daniya', 'Darakhshaan', 'Darakhshan', 'Daria', 'Dawlat', 'Deeba', 'Deema', 'Dema', 'Dhakiyah', 'Dilshad', 'Dina', 'Diqrah', 'Diyanah', 'Doaa', 'Duaa', "Duba'ah", 'Dunia', 'Durdanah', 'Durrah', 'Eiliyah', 'Eimaan', 'Eiman', 'Eliza', 'Elma', 'Eman', 'Emrana', 'Enisa', 'Eraj', 'Erina', 'Ermina', 'Erum', "Esha'al", 'Eshal', 'Eshmaal', 'Ezzah', 'Fadeelah', 'Fadila', 'Fadilah', 'Fadwah', 'Fadyaa', 'Faeezah', 'Faekah', 'Faheemah', 'Fahima', 'Fahmida', 'Faiha', 'Faiqa', 'Fairuzah', 'Faiza', 'Faizah', 'Fajr', 'Fakeehah', 'Fakhirah', 'Fakhra', 'Fakhtah', 'Fakihah', 'Falak', 'Falaknaz', 'Falaq', 'Falisha', 'Famya', 'Faqirah', 'Fara', 'Farah', 'Faraza', 'Fareedah', 'Fareeha', 'Fareess', 'Farha', 'Farhana', 'Farhanah', 'Farhat', 'Farheen', 'Farhiya', "Fari'ah", 'Faria', 'Farida', 'Faridah', 'Fariha', 'Farihah', 'Farisha', 'Fariza', 'Farkhandah', 'Farqad', 'Farwa', 'Farwah', 'Faryal', 'Faryat', 'Farzana', 'Farzeen', 'Faseehah', 'Faseelah', 'Fateenah', 'Fatheha', 'Fathi', 'Fathima', 'Fathiya', 'Fatiha', 'Fatihah', 'Fatim', 'Fatima', 'Fatimah', 'Fatin', 'Fatinah', 'Fatma', 'Fauzia', 'Fawzia', 'Fawziyah', 'Fayruz', 'Fazluna', 'Fazzilet', 'Feerozah', 'Feiyaz', 'Femida', 'Fida', 'Fikriya', 'Fir', 'Firdaus', 'Firdaws', 'Firdous', 'Firdowsa', 'Fiza', 'Forhana', 'Fozia', 'Foziah', 'Fudayl', 'Furayah', 'Fusaylah', 'Fuseelah', 'Gazala', 'Ghadah', 'Ghalibah', 'Ghaliyah', 'Ghaneemah', 'Ghania', 'Ghaniyah', 'Ghareebah', 'Ghayda', 'Ghazal', 'Ghazala', 'Ghaziyah', 'Ghitbah', 'Ghizlan', 'Ghufayrah', 'Ghumaysa', 'Ghusoon', 'Ghuzayyah', 'Gul-e-Rana', 'Gulbano', 'Haajar', 'Hababah', 'Habiba', 'Habibah', 'Haboos', 'Hadeeqa', 'Hadeeqah', 'Hadhirah', 'Hadil', 'Hadiya', 'Hadiyah', 'Hafeezah', 'Hafsa', 'Hafsa/Ucha', 'Hafsah', 'Hafthah', 'Haifa', 'Haiza', 'Hajar', 'Hajjah', 'Hajna', 'Hajrah', 'Hakimah', 'Halah', 'Haleema', 'Halima', 'Halimah', 'Hamamah', 'Hameeda', 'Hamidah', 'Hamnah', 'Hamra', 'Hana', 'Hanan', 'Haneefah', 'Hanfa', 'Haniah', 'Hanifa', 'Hanin', 'Haniyah', 'Hannah', 'Hannan', 'Hareem', 'Haseena', 'Hasinah', 'Hasna', 'Hawwa', 'Hayah', 'Hayam', 'Hayat', 'Hayfa', 'Hayrah', 'Hazimah', 'Haziqah', 'Hazirah', 'Heba', 'Heela', 'Hena', 'Henna', 'Hessa', 'Heyam', 'Hiba', 'Hibatullah', 'Hibba', 'Hibbah', 'Hidayah', 'Hidiyah', 'Hifza', 'Hijab', 'Hijrah', 'Hilwana', 'Hind', 'Hindah', 'Hira', 'Hirah', 'Hoda', 'Hodan', 'Hoor', 'Hooria', 'Hooriya', 'Hooriyah', 'Horia', 'Hubayshah', 'Hubba', 'Huda', 'Hujaymah', 'Hujayrah', 'Hukaymah', 'Huma', 'Humaira', 'Humaydah', 'Humayrah', 'Humera', 'Humra', 'Hunaydah', 'Hurya', 'Husn', 'Husna', 'Husniya', 'Ibthaj', 'Ibtia', 'Ibtihal', 'Ibtisam', 'Iffah', 'Iffat', 'Ifra', 'Iftin', 'Ifza', 'Ijabo', 'Ikram', 'Ikramiya', 'Ilaaf', 'Ilham', 'Ilhan', 'Ilm', 'Ilmeeyat', 'Iman', 'Imani', 'Imsaal', 'Imthithal', 'Imtihal', "In'am", 'Inaaya', 'Inan', 'Inas', 'Inaya', 'Inayah', 'Inga', 'Insha', 'Intessar', 'Intisar', 'Iqra', 'Iraj', 'Iram', 'Irem', 'Irsa', 'Irum', 'Isbah', 'Isha', 'Ishaal', 'Ishraq', 'Isir', 'Isma', 'Ismat', 'Isra', 'Istabraq', 'Izdihar', 'Izma', 'Izz', 'Izzah', 'Jabalah', 'Jabeen', 'Jabrayah', 'Jahaan', 'Jahan', 'Jahanara', 'Jahdamah', 'Jahida', 'Jahin', 'Jahmyyllah', 'Jaifa', 'Jaiyana', 'Jalilah', 'Jameela', 'Jameelah', 'Jameena', 'Jamia', 'Jamila', 'Jamilah', 'Jammana', 'Jana', 'Janan', 'Jannah', 'Jannat', 'Jaseena', 'Jasmin', 'Jasmina', 'Jasrah', 'Javairea', 'Jawahir', 'Jawharah', 'Jaza', 'Jazeera', 'Jazira', 'Jaziya', 'Jehaan', 'Jehan', 'Jemimah', 'Jenna', 'Jennah', 'Jessenia', 'Jian', 'Jihan', 'Judamah', 'Jumaana', 'Jumaymah', 'Jumaynah', 'Junainah', 'Junnut', 'Juwariyah', 'Kabirah', 'Kadshah', 'Kaheesha', 'Kainat', 'Kaleemah', 'Kali', 'Kalima', 'Kalsoom', 'Kaltham', 'Kamaliyah', 'Kamilah', 'Kaneez', 'Kanval', 'Kanwal', 'Kanz', 'Kanza', 'Kanzah', 'Karam', 'Kardawiyah', 'Karima', 'Karimah', 'Kas', 'Kashifah', 'Kashish', 'Kathirah', 'Kaukab', 'Kausar', 'Kayan', 'Kaysah', 'Kehara', 'Kehkashan', 'Khadeeja', 'Khadija', 'Khadijah', 'Khadra', 'Khairah', 'Khalidah', 'Khalilah', 'Khalisah', 'Khansa', 'Kharqa', 'Khatera', 'Khatira', 'Khatoon', 'Khawlah', 'Khayrah', 'Khayriyah', 'Khayriyyah', 'Khazanah', 'Khidrah', 'Khudrah', 'Khulaybah', 'Khulud', 'Khusbakht', 'Khuwaylah', 'Khuzamah', 'Kiswar', 'Koila', 'Komal', 'Komila', 'Kuaybah', 'Kuhaylah', 'Kulthum', 'Kunza', 'Kurat-ul-Ain', 'Kuwaysah', 'Kwairah', 'Kyda', 'Laaibah', 'Laaiqah', 'Labeebah', 'Labibah', 'Laiba', 'Laila', 'Laiqa', 'Lama', 'Lamees', 'Lamis', 'Lamisa', 'Lamisah', 'Lamiya', 'Lamya', 'Lana', 'Lanika', 'Laraib', 'Lashirah', 'Latifa', 'Layla', 'Layyah', 'Leem', 'Leen', 'Leena', 'Leila', 'Leilah', 'Leyla', 'Liba', 'Lina', 'Liyana', 'Liza', 'Lu', "Lu'lu", 'Lubabah', 'Lubena', 'Lubna', 'Lujain', 'Lujaina', 'Luma', 'Luna', 'Lutfiyah', 'Ma', "Ma'isah", 'Maahnoor', 'Madaniyah', 'Madeeha', 'Madhat', 'Madhia', 'Madia', 'Madiha', 'Madihah', 'Maha', 'Mahasin', 'Mahbasah', 'Mahdiya', 'Maheen', 'Maheera', 'Mahek', 'Mahema Jahan', 'Mahfuzah', 'Mahirah', 'Mahjabeen', 'Mahneera', 'Mahneerah', 'Mahnoor', 'Mahreen', 'Mahrosh', 'Mahrukh', 'Mahtob', 'Mahum', 'Mahveen', 'Mahvish', 'Mahwish', 'Mahwush', 'Maida', 'Maira', 'Maisarah', 'Maisha', 'Majidah', 'Makhtooma', 'Makhtoonah', 'Malaika', 'Malaikah', 'Malak', 'Malayeka', 'Maleehah', 'Maliha', 'Malika', 'Malikah', 'Malmal', 'Manahel', 'Manahil', 'Manal', 'Manar', 'Manfoosah', 'Manha', 'Manhalah', 'Mansurah', 'Maqboolah', 'Marah', 'Maram', 'Mardhiah', 'Marhabah', 'Maria', 'Mariam', 'Maridah', 'Mariya', 'Mariyah', 'Marjanah', 'Marnia', 'Marwa', 'Maryum', 'Masabeeh', 'Mashaal', 'Mashal', 'Mashel', 'Mashoodah', 'Masooma', 'Masoomah', 'Mastura', 'Masumah', 'Mateenah', 'Mawahib', 'Mawara', 'Mawiya', 'Mawiyah', 'Maya', 'Mayameen', 'Mayeda', 'Maymunah', 'Maysa', 'Maysam', 'Maysoon', 'Maysun', 'Mayyadah', 'Maznah', 'Mazneen', 'Medina', 'Meem', 'Meena', 'Mehak', 'Mehek', 'Meher', 'Meheroon', 'Meherunissa', 'Mehjabeen', 'Mehmuda', 'Mehnaz', 'Mehndi', 'Mehnoor', 'Mehr', 'Mehreen', 'Mehriban', 'Mehrima', 'Mehrish', 'Mehrnaz', 'Mehrunisa', 'Mehvesh', 'Mehvish', 'Mehwish', 'Memoona', 'Menaal', 'Mersiha', 'Mevish', 'Meymona', "Mid'haa", 'Midhaa', 'Midhah', 'Mina', 'Minaal', 'Minal', 'Minnah', 'Misba', 'Misha', 'Mishall', 'Mishel', 'Miskeenah', 'Mobena', 'Mohaddisa', 'Mohga', 'Mohsina', 'Momina', 'Mona', 'Monera', 'Mouna', 'Mounia', 'Mounira', 'Muazah', 'Mubarakah', 'Mubashirah']
            self.GIRL_LAST_NAME = ['Akter', 'Khatun', 'Begum', 'Sultana', 'Hossen', 'Akhter', 'Aktar', 'Jahan', 'Kabir', 'Hoque', 'Nahar', 'Parvin', 'Ferdous', 'Khanam', 'Yeasmin', 'Mim', 'Jannat', 'Talukder', 'Afrin', 'Kazi', 'Hosain', 'Azad', 'Sharmin']
                
              
                
    def first_name(self, gender="random/male/female"):
        gender = gender.lower()
        if gender == "male":
            fname = random.choice(self.BOY_FIRST_NAME)
        elif gender == "female":
            fname = random.choice(self.GIRL_FIRST_NAME)
        else:
            n = random.randint(0,1)
            if n==0:
                fname = random.choice(self.BOY_FIRST_NAME)
            else:
                fname = random.choice(self.GIRL_FIRST_NAME)
        return fname
    def last_name(self, gender="random/male/female"):
        gender = gender.lower()
        if gender == "male":
            lname = random.choice(self.BOY_LAST_NAME)
        elif gender == "female":
            lname = random.choice(self.GIRL_LAST_NAME)
        else:
            n = random.randint(0,1)
            if n==0:
                lname = random.choice(self.BOY_LAST_NAME)
            else:
                lname = random.choice(self.GIRL_LAST_NAME)
        return lname
    def full_name(self, gender="random/male/female"):
        gender = gender.lower()
        if gender != "male" and gender != "female":
            n = random.randint(0,1)
            if n == 0:
                gender = 'male'
            else:
                gender = 'female'
        fullname = self.first_name(gender) + " " + self.last_name(gender)
        return fullname
        
class Modules():
    def generate_first_name(self, locale, gender="random/male/female"):
        countries = self.countryList()
        if locale.lower() == 'random':
            locale = random.choice(countries)['locale']
        else:
            for country in countries:
                if country['name'] == locale:
                    locale = country['locale']
                    break

        # print(locale)
        fake = Faker(locale)
        if gender.lower() == 'male':
            fname = fake.first_name_male()
        elif gender.lower() == 'female':
            fname = fake.first_name_female()
        else:
            x = random.randint(0,1)
            if x==0:
                fname = fake.first_name_male()
            else:
                fname = fake.first_name_female()
        return fname
    def generate_last_name(self, locale, gender="random/male/female"):
        countries = self.countryList()
        if locale.lower() == 'random':
            locale = random.choice(countries)['locale']
        else:
            for country in countries:
                if country['name'] == locale:
                    locale = country['locale']
                    break
        # print(locale)
        fake = Faker(locale)
        if gender.lower() == 'male':
            lname = fake.last_name_male()
        elif gender.lower() == 'female':
            lname = fake.last_name_female()
        else:
            x = random.randint(0,1)
            if x==0:
                lname = fake.first_name_male()
            else:
                lname = fake.last_name_female()
        return lname
    def generate_full_name(self, locale, gender="random/male/female"):
        countries = self.countryList()
        if locale.lower() == 'random':
            locale = random.choice(countries)['locale']
        else:
            for country in countries:
                if country['name'] == locale:
                    locale = country['locale']
                    break
            
        fake = Faker(locale)
        if gender.lower() == 'male':
            fname = fake.first_name_male()
            lname = fake.last_name_male()
        elif gender.lower() == 'female':
            fname = fake.first_name_female()
            lname = fake.last_name_female()
        else:
            x = random.randint(0,1)
            if x==0:
                fname = fake.first_name_male()
                lname = fake.last_name_male()
            else:
                fname = fake.first_name_female()
                lname = fake.last_name_female()
        
        name = fname + " " + lname

        return name
    def countryList(self):
        COUNTRY_DATA = [{'name': 'United Arab Emirates-ar', 'locale': 'ar_AE'}, {'name': 'Egypt-ar', 'locale': 'ar_EG'}, {'name': 'Jordan-ar', 'locale': 'ar_JO'}, {'name': 'Palestine, State of-ar', 'locale': 'ar_PS'}, {'name': 'Saudi Arabia-ar', 'locale': 'ar_SA'}, {'name': 'Azerbaijan-az', 'locale': 'az_AZ'}, {'name': 'Bulgaria-bg', 'locale': 'bg_BG'}, {'name': 'Bangladesh-bn', 'locale': 'bn_BD'}, {'name': 'Bosnia and Herzegovina-bs', 'locale': 'bs_BA'}, {'name': 'Czechia-cs', 'locale': 'cs_CZ'}, {'name': 'Denmark-da', 'locale': 'da_DK'}, {'name': 'Germany-de', 'locale': 'de'}, {'name': 'Austria-de', 'locale': 'de_AT'}, {'name': 'Switzerland-de', 'locale': 'de_CH'}, {'name': 'Germany-de', 'locale': 'de_DE'}, {'name': 'Denmark-dk', 'locale': 'dk_DK'}, {'name': 'Cyprus-el', 'locale': 'el_CY'}, {'name': 'Greece-el', 'locale': 'el_GR'}, {'name': 'Australia-en', 'locale': 'en_AU'}, {'name': 'Canada-en', 'locale': 'en_CA'}, {'name': 'United Kingdom-en', 'locale': 'en_GB'}, {'name': 'Ireland-en', 'locale': 'en_IE'}, {'name': 'India-en', 'locale': 'en_IN'}, {'name': 'New Zealand-en', 'locale': 'en_NZ'}, {'name': 'Philippines-en', 'locale': 'en_PH'}, {'name': 'Thailand-en', 'locale': 'en_TH'}, {'name': 'United States-en', 'locale': 'en_US'}, {'name': 'Spain-es', 'locale': 'es'}, {'name': 'Canada-es', 'locale': 'es_CA'}, {'name': 'Colombia-es', 'locale': 'es_CO'}, {'name': 'Spain-es', 'locale': 'es_ES'}, {'name': 'Mexico-es', 'locale': 'es_MX'}, {'name': 'Estonia-et', 'locale': 'et_EE'}, {'name': 'Iran, Islamic Republic of-fa', 'locale': 'fa_IR'}, {'name': 'Finland-fi', 'locale': 'fi_FI'}, {'name': 'Philippines-fil', 'locale': 'fil_PH'}, {'name': 'Canada-fr', 'locale': 'fr_CA'}, {'name': 'Switzerland-fr', 'locale': 'fr_CH'}, {'name': 'France-fr', 'locale': 'fr_FR'}, {'name': 'Ireland-ga', 'locale': 'ga_IE'}, {'name': 'Israel-he', 'locale': 'he_IL'}, {'name': 'India-hi', 'locale': 'hi_IN'}, {'name': 'Croatia-hr', 'locale': 'hr_HR'}, {'name': 'Hungary-hu', 'locale': 'hu_HU'}, {'name': 'Armenia-hy', 'locale': 'hy_AM'}, {'name': 'Indonesia-id', 'locale': 'id_ID'}, {'name': 'Switzerland-it', 'locale': 'it_CH'}, {'name': 'Italy-it', 'locale': 'it_IT'}, {'name': 'Japan-ja', 'locale': 'ja_JP'}, {'name': 'Georgia-ka', 'locale': 'ka_GE'}, {'name': 'Korea, Republic of-ko', 'locale': 'ko_KR'}, {'name': "Lao People's Democratic Republic-la", 'locale': 'la'}, {'name': 'Luxembourg-lb', 'locale': 'lb_LU'}, {'name': 'Lithuania-lt', 'locale': 'lt_LT'}, {'name': 'Latvia-lv', 'locale': 'lv_LV'}, {'name': 'Malta-mt', 'locale': 'mt_MT'}, {'name': 'Nepal-ne', 'locale': 'ne_NP'}, {'name': 'Belgium-nl', 'locale': 'nl_BE'}, {'name': 'Netherlands-nl', 'locale': 'nl_NL'}, {'name': 'Norway-no', 'locale': 'no_NO'}, {'name': 'India-or', 'locale': 'or_IN'}, {'name': 'Poland-pl', 'locale': 'pl_PL'}, {'name': 'Brazil-pt', 'locale': 'pt_BR'}, {'name': 'Portugal-pt', 'locale': 'pt_PT'}, {'name': 'Romania-ro', 'locale': 'ro_RO'}, {'name': 'Russian Federation-ru', 'locale': 'ru_RU'}, {'name': 'Slovakia-sk', 'locale': 'sk_SK'}, {'name': 'Slovenia-sl', 'locale': 'sl_SI'}, {'name': 'Sweden-sv', 'locale': 'sv_SE'}, {'name': 'India-ta', 'locale': 'ta_IN'}, {'name': 'Thailand-th', 'locale': 'th'}, {'name': 'Thailand-th', 'locale': 'th_TH'}, {'name': 'Philippines-tl', 'locale': 'tl_PH'}, {'name': 'Turkey-tr', 'locale': 'tr_TR'}, {'name': 'Ghana-tw', 'locale': 'tw_GH'}, {'name': 'Ukraine-uk', 'locale': 'uk_UA'}, {'name': 'China-zh', 'locale': 'zh_CN'}, {'name': 'Taiwan, Province of China-zh', 'locale': 'zh_TW'}]   
        return COUNTRY_DATA
    def generate_username(self,minWords: int, maxWords: int, maxLen: int, randomNumber: bool, randomNumberMaxDigit: int):
        r = RandomWord()
        username = ""
        for i in range(1,random.randint(minWords, maxWords)+1):
            if i/2 == 0:
                word = r.random_words(amount=1, include_parts_of_speech=['noun'])[0]
            else:
                word = r.random_words(amount=1, include_parts_of_speech=['adjective'])[0]
            
            
            username += word
        if randomNumber: username += str(random.randint(0,randomNumberMaxDigit))
        while True:
            if len(username) > maxLen: 
                index_to_remove = random.randint(0, len(username) - 1)
                username = username[:index_to_remove] + username[index_to_remove + 1:]
            else: break

        return username
    def generate_company_name(self, minWords: int, maxWords: int, noSpace: bool):
        suffixes = [
                "Inc.", "Corp.", "Ltd.", "LLC", "Co.", "Group", "PLC", "AG", "GmbH",
                "S.A.", "B.V.", "S.p.A.", "S.A.S.", "Pty Ltd", "LLP", "L.P.", "S.C.",
                "N.V.", "OÜ", "Oy", "A/S", "K.K.", "P.C.", "S.L.", "d.o.o.", "AB"
            ]
        r = RandomWord()
        companyName = ""
        for i in range(1,random.randint(minWords, maxWords)+1):
            if i/2 == 0:
                word = r.random_words(amount=1, include_parts_of_speech=['noun'])[0]
            else:
                word = r.random_words(amount=1, include_parts_of_speech=['adjective'])[0]
            companyName += word.capitalize() + " "
        if noSpace:
            companyName = companyName.replace(" ", '') + " "
        companyName += str(random.choice(suffixes))
        
        return companyName
    def generate_number(self, minValue: int, maxValue: int, decimalPlaces: int):
        number = random.randint(minValue, maxValue)

        if decimalPlaces >0:
            decNum = ''
            for i in range(0, decimalPlaces):
                decNum += f"{random.randint(0,9)}"
                
            number = float(f"{number}.{decNum}")
            number = "{:.{}f}".format(number, decimalPlaces)
        return number
    def generate_password(
            self,
            passwordLength: int,
            includeNumbers: bool,
            includeLowercaseChar: bool, 
            includeUppercaseChar: bool, 
            beginWithLetter: bool, 
            includeSymbols: bool, 
            noDuplicateChar: bool, 
            noSequentialChar: bool, 
            ):
        
        alphabets = string.ascii_letters
        lowercase_alphabets = string.ascii_lowercase
        uppercase_alphabets = string.ascii_uppercase
        numbers = string.digits
        special_chars = string.punctuation

        x = []
        if includeNumbers:x.append(0)
        if includeLowercaseChar: x.append(1)
        if includeUppercaseChar: x.append(2)
        if includeSymbols: x.append(3)

        if not includeNumbers and not includeLowercaseChar and not includeUppercaseChar and not includeSymbols:
            x = [0,1]

        password = ""
        if beginWithLetter:
            if includeLowercaseChar and not includeUppercaseChar:
                password += random.choice(lowercase_alphabets)
            elif includeUppercaseChar and not includeLowercaseChar:
                password += random.choice(uppercase_alphabets)
            else: 
                password += random.choice(alphabets)
        while True:
            n = random.choice(x)
            c = ''
            ok = True
            if n == 0:
                c += str(random.choice(numbers))
            elif n == 1:
                c += str(random.choice(lowercase_alphabets))
            elif n ==  2:
                c += str(random.choice(uppercase_alphabets))
            elif n == 3:
                c += str(random.choice(special_chars))

            if noDuplicateChar:
                if c in password:
                    ok = False
            if noSequentialChar:
                try:
                    if ord(password[-1]) == ord(c)-1:
                        ok = False
                except:pass
            if ok:
                password += c
            if len(password) >= passwordLength: break
        return password
    def generate_date(self, minDate: str="MM-dd-yyyy", maxDate: str="MM-dd-yyyy", dateFormat: str= "%m-%d-%Y"):
             

        minDate = datetime.strptime(minDate, dateFormat)
        maxDate = datetime.strptime(maxDate, dateFormat)

        deltaDate = (maxDate - minDate).days
        randomDays = random.randint(0, deltaDate)

        randomDate = minDate + timedelta(days=randomDays)

        return randomDate.strftime(dateFormat)
    def generate_fake_email(
            self,
            minWords: int,
            maxWords: int,
            randomNumber: bool,
            randomNumberMaxDigit: int,
            hostNameAutoGen: bool,
            hostNameInput: bool,
            builtInHostname: str,
            hostnameInputList: list
                       ):
        username = self.generate_username(minWords, maxWords, 100, randomNumber, randomNumberMaxDigit)
        hostname = ""
        if hostNameAutoGen:
            if builtInHostname == "Auto":
                hostnames = open(BASE_PATH + "/resources/hostnames.nst").read().replace(" ", '').replace(",", '').split("\n")
                hostname = random.choice(hostnames)
            else:
                hostname = builtInHostname
        elif hostNameInput:
            hostname = random.choice(hostnameInputList)
        return username + "@" + hostname.replace("@", '')
    def generate_fake_phone_number(self, template: str):
        if not template: return
        phoneNumber = ""
        even = [0,2,4,6,8]
        odd = [1,3,5,7,9]
        for c in template:
            try: 
                int(c)
            except:
                if c == "x":
                    c = random.randint(0,9)
                elif c == "X":
                    c = random.randint(1,9)
                elif c == "y":
                    c = random.choice(odd)
                elif c == "Y":
                    c = random.choice(even)
                elif c == "Z":
                    c = random.randint(0,1)
                elif c == "+" or c == "-" or c == "(" or c == ")":
                    c = c
                else: c = random.randint(0,9)
                
            phoneNumber += str(c)
        return phoneNumber















