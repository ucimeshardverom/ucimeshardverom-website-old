Ahojte,

návod na rozbehanie UsH.sk webovej apky na Windowse:
1. Treba mať nainštalovaný Python (ideálne 3.6, 3.7 alebo 3.8) - https://www.python.org/ (pri inštalácií zakliknite hneď na začiatku, že chcete pridať Python do systémových premenných a že chcete nainštalovať pip)
2. Odporúčam stiahnuť si editor Sublime - https://www.sublimetext.com/
3. Stiahnite si tento súbor (a unzipnite ho) - https://github.com/ucimeshardverom/ucimeshardverom-website/archive/communityFriedly.zip

Pre spustenie apky:
1. prejdite do adresára ucimeshardverom-website
2. Podržte ľavý SHIFT a stlačte pravý klik na myši niekde v adresári
3. Kliknite na možnosť "Otvoriť Power-Shell" (alebo niečo podobné, ide o "PowerShell")
4. do konzoly vložte `python -m pip install -r requirements.txt`
5. Ak inštalácia prebehne úspešne, vložte `python views.py`
6. Otvorte v browseri adresu: http://127.0.0.1:5000/

Pre upravovanie materiálu:
1. prejdite do podadresára /materialy/microbit_smart_home a odvorte si prvú alebo druhú kapitolu (všimnite si členenie adresára)
2. V prehliadači daný materiál zobrazíte otvorením stránky 127.0.0.1:5000/materialy/microbit_smart_home/
3. Vždy, keď upravíte .md súbor (alebo pridáte nový), stačí zmenu uložiť v súbore, v prehliadači kliknúť refresh a zmeny sa automaticky zobrazia

Pre generovanie PDF:
1. treba mať nainštalovaný Chrome (všimnite si, akej verzie, ideálne 85, 86 alebo 87)
2. na stránke https://chromedriver.chromium.org/downloads si vyberte Vašu berziu (hneď na začiatku stránky)
3. Stiahnite si chromedriver_win32.zip
4. Extrahovaný chromedriver.exe vložte do adresára ucimeshardverom-website
5. V prehliadači pri prehliadaní kapitoly (napr. http://127.0.0.1:5000/materialy/microbit_smart_home/osvetlenie/) kliknite na TELEKOM PDF

Je toho celkom dosť, ale v zásade toto je všetko :slightly_smiling_face: Už len sa naučiť Markdown syntax (buď sa inšpirujte texto, ktorý tam je, alebo pozrite na nete)

Kľudne si k tomu môžeme zavolať (teoreticky stačí iba jeden z Vás) aby ste si to rozbehali :slightly_smiling_face: Potom už je to malina používať :slightly_smiling_face: