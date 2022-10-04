from django.utils import timezone
from django.db import models
# Create your models here.

MARITAL_CHOICES = (("Married", "Married"),("Single", "Single"),("Other", "Other"))
GENDER_CHOICES = (("Female", "Female"),("Male", "Male"),("Rather not say", "Rather not say"))
NATIONALITIES_CHOICES= (('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Antiguans', 'Antiguans'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'), ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), ('Barbadian', 'Barbadian'), ('Barbudans', 'Barbudans'), ('Batswana', 'Batswana'), ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'), ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Djibouti', 'Djibouti'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('Dutchman', 'Dutchman'), ('Dutchwoman', 'Dutchwoman'), ('East Timorese', 'East Timorese'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirian', 'Emirian'), ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Filipino', 'Filipino'), ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), ('Herzegovinian', 'Herzegovinian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), ('I-Kiribati', 'I-Kiribati'), ('Icelander', 'Icelander'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'), ('Kittian and Nevisian', 'Kittian and Nevisian'), ('Kuwaiti', 'Kuwaiti'), ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'), ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), ('Maldivan', 'Maldivan'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('Mosotho', 'Mosotho'), ('Motswana', 'Motswana'), ('Mozambican', 'Mozambican'), ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), ('Netherlander', 'Netherlander'), ('New Zealander', 'New Zealander'), ('Ni-Vanuatu', 'Ni-Vanuatu'), ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), ('North Korean', 'North Korean'), ('Northern Irish', 'Northern Irish'), ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'), ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'), ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'), ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'))
EMPLOYED_CHOICE = (('Employed','Employed'),('Unemployed','Unemployed'))

class Customer(models.Model):
    first_name= models.CharField(max_length = 25)
    last_name= models.CharField(max_length = 25)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES,null= True)
    address = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    nationality= models.CharField(max_length = 30,choices= NATIONALITIES_CHOICES,null= True)        
    user_id = models.CharField(max_length = 25)
    email = models.EmailField()
    phone_number =models.CharField(max_length= 25,null= True)
    employed = models.CharField(null= True, max_length=25)
    # employed = models.BooleanField(null=True, choices=EMPLOYED_CHOICE)
    occupation = models.CharField( null= True,max_length=25)
    marital_status = models.CharField(max_length= 25,choices= MARITAL_CHOICES,blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self): 
        return self.first_name
        
        
CURRENCIES = (	("AFN", "Afghani"),("DZD", "Algerian Dinar"),("ARS", "Argentine Peso"),("AMD", "Armenian Dram"),("AWG", "Aruban Guilder"),("AUD", "Australian Dollar"),("AZN", "Azerbaijanian Manat"),("BSD", "Bahamian Dollar"),("BHD", "Bahraini Dinar"),("THB", "Baht"),("PAB", "Balboa"),("BBD", "Barbados Dollar"),("BYR", "Belarussian Ruble"),("BZD", "Belize Dollar"),("BMD", "Bermudian Dollar"),("VEF", "Bolivar Fuerte"),("BOB", "Boliviano"),("BRL", "Brazilian Real"),("BND", "Brunei Dollar"),("BGN", "Bulgarian Lev"),("BIF", "Burundi Franc"),("CAD", "Canadian Dollar"),("CVE", "Cape Verde Escudo"),("KYD", "Cayman Islands Dollar"),("GHS", "Cedi"),("CLP", "Chilean Peso"),("COP", "Colombian Peso"),("KMF", "Comoro Franc"),("CDF", "Congolese Franc"),("BAM", "Convertible Mark"),("NIO", "Cordoba Oro"),	("CRC", "Costa Rican Colon"),("HRK", "Croatian Kuna"),("CUP", "Cuban Peso"),	("CZK", "Czech Koruna"),("GMD", "Dalasi"),("DKK", "Danish Krone"),("MKD", "Denar"),("DJF", "Djibouti Franc"),("STD", "Dobra"),("DOP", "Dominican Peso"),("VND", "Dong"),("XCD", "East Caribbean Dollar"),("EGP", "Egyptian Pound"),("SVC", "El Salvador Colon"),("ETB", "Ethiopian Birr"),("EUR", "Euro"),("FKP", "Falkland Islands Pound"),("FJD", "Fiji Dollar"),("HUF", "Forint"),("GIP", "Gibraltar Pound"),("XAU", "Gold"),("HTG", "Gourde"),("PYG", "Guarani"),("GNF", "Guinea Franc"),("GYD", "Guyana Dollar"),("HKD", "Hong Kong Dollar"),("UAH", "Hryvnia"),("ISK", "Iceland Krona"),("INR", "Indian Rupee"),("IRR", "Iranian Rial"),("IQD", "Iraqi Dinar"),("JMD", "Jamaican Dollar"),("JOD", "Jordanian Dinar"),("KES", "Kenyan Shilling"),("PGK", "Kina"),("LAK", "Kip"),("KWD", "Kuwaiti Dinar"),("MWK", "Kwacha"),("AOA", "Kwanza"),("MMK", "Kyat"),("GEL", "Lari"),("LVL", "Latvian Lats"),("LBP", "Lebanese Pound"),("ALL", "Lek"),("HNL", "Lempira"),("SLL", "Leone"),("RON", "Leu"),("LRD", "Liberian Dollar"),("LYD", "Libyan Dinar"),("SZL", "Lilangeni"),("LTL", "Lithuanian Litas"),("LSL", "Loti"),("MGA", "Malagasy Ariary"),("MYR", "Malaysian Ringgit"),("MUR", "Mauritius Rupee"),("MZN", "Metical"),("MXN", "Mexican Peso"),("MDL", "Moldovan Leu"),("MAD", "Moroccan Dirham"),("BOV", "Mvdol"),("NGN", "Naira"),("ERN", "Nakfa"),("NAD", "Namibia Dollar"),("NPR", "Nepalese Rupee"),("ANG", "Netherlands Antillean Guilder"),("ILS", "New Israeli Sheqel"),("TMT", "New Manat"),("TWD", "New Taiwan Dollar"),("NZD", "New Zealand Dollar"),("BTN", "Ngultrum"),("KPW", "North Korean Won"),("NOK", "Norwegian Krone"),("PEN", "Nuevo Sol"),("MRO", "Ouguiya"),("PKR", "Pakistan Rupee"),("XPD", "Palladium"),("MOP", "Pataca"),("TOP", "Pa’anga"),("CUC", "Peso Convertible"),("UYU", "Peso Uruguayo"),("PHP", "Philippine Peso"),("XPT", "Platinum"),("GBP", "Pound Sterling"),("BWP", "Pula"),("QAR", "Qatari Rial"),("GTQ", "Quetzal"),("ZAR", "Rand"),("OMR", "Rial Omani"),("KHR", "Riel"),("MVR", "Rufiyaa"),("IDR", "Rupiah"),("RUB", "Russian Ruble"),("RWF", "Rwanda Franc"),("SHP", "Saint Helena Pound"),("SAR", "Saudi Riyal"),("RSD", "Serbian Dinar"),("SCR", "Seychelles Rupee"),("XAG", "Silver"),("SGD", "Singapore Dollar"),("SBD", "Solomon Islands Dollar"),("KGS", "Som"),("SOS", "Somali Shilling"),("TJS", "Somoni"),("ZAR", "South African Rand"),("LKR", "Sri Lanka Rupee"),("XSU", "Sucre"),("SDG", "Sudanese Pound"),("SRD", "Surinam Dollar"),("SEK", "Swedish Krona"),("CHF", "Swiss Franc"),	("SYP", "Syrian Pound"),("BDT", "Taka"),("WST", "Tala"),("TZS", "Tanzanian Shilling"),("KZT", "Tenge"),("TTD", "Trinidad and Tobago Dollar"),("MNT", "Tugrik"),("TND", "Tunisian Dinar"),("TRY", "Turkish Lira"),("AED", "UAE Dirham"),("USD", "US Dollar"),("UGX", "Uganda Shilling"),("COU", "Unidad de Valor Real"),("CLF", "Unidades de fomento"),("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),("UZS", "Uzbekistan Sum"),("VUV", "Vatu"),("KRW", "Won"),("YER", "Yemeni Rial"),("JPY", "Yen"),("CNY", "Yuan Renminbi"),("ZMK", "Zambian Kwacha"),("ZWL", "Zimbabwe Dollar"),("PLN", "Zloty"))  
class Currency(models.Model):
    name = models.CharField(max_length=15, choices= CURRENCIES,null = True)
    symbol = models.CharField(max_length= 5,null= True)
    country_of_origin = models.CharField(max_length= 30,choices= NATIONALITIES_CHOICES, null = True)
    def __str__(self):
        return self.symbol


class Wallet(models.Model):
    wallet_name = models.CharField(max_length=24, null=True)
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE,related_name= 'currency_wallet')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name= 'customer_wallet')
    balance=models.DecimalField(max_digits=21,decimal_places= 2)
    date_created=models.DateTimeField(default= "")
    pin=models.SmallIntegerField(blank= True)
    def __str__(self):
        return self.wallet_name
    
       
class Account(models.Model):
    account_name = models.CharField(max_length= 15,blank=True)
    account_number = models.CharField(max_length=15, blank=True)
    balance = models.DecimalField(max_digits=10,decimal_places= 3,default=0)
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE,related_name= 'account_wallet', null = True)
    def __str__(self):
        return self.account_name


RECEIPT_TYPE_CHOICES = (("Revenue Receipt","Revenue Receipt"),("Capital Receipt" , "Capital Receipt"))
class Receipt(models.Model):
    receipt_type = models.CharField(max_length=24, choices=RECEIPT_TYPE_CHOICES, null= True)
    receipt_date = models.DateTimeField(null=True, blank= True)
    total_amount = models.PositiveIntegerField()   
    receipt_file = models.FileField()
    def __str__(self):
        return self.receipt_type    
    

class ThirdParty(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(blank= True)
    phone_number = models.CharField(max_length= 15,blank=True)
    transaction_cost = models.PositiveIntegerField(null = True)
    currency = models.ForeignKey(Currency,on_delete= models.CASCADE,related_name='currency_thirdparty')
    is_active = models.BooleanField(default= False)
    account = models.ForeignKey(Account,on_delete= models.CASCADE,related_name='account_thirdparty')
    def __str__(self):
        return self.full_name
            

STATUS_CHOICES = (("Complete", "Complete"), ("Incomplete", "Incomplete"), ("Pending", "Pending"))
TRANSACTION_CHOICES = (("Withdrawal", "Withdrawal"), ("Deposit", "Deposit"))
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES,null= True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='wallet_transaction')
    transaction_amount = models.PositiveIntegerField(null= True)
    transaction_date_time = models.DateTimeField(null = True,blank= True)
    receipt = models.OneToOneField(Receipt,on_delete=models.CASCADE,related_name='receipt_transaction')
    origin_account= models.ForeignKey(Account,on_delete=models.CASCADE,related_name= 'account_transaction')
    destination_account = models.ForeignKey(Account, on_delete= models.CASCADE, related_name= 'transaction_account', null= True)
    third_party= models.ForeignKey(ThirdParty,on_delete= models.CASCADE,related_name='third_party_transaction')
    status = models.CharField(max_length= 18, choices=STATUS_CHOICES, null= True)
    transaction_cost = models.PositiveIntegerField(null= True)
    def __str__(self):
        return self.transaction_type

CARD_TYPE_CHOICES = (("Debit","Debit"),("Credit","Credit"))
class Card(models.Model):
    card_name = models.CharField(max_length=20,null= True)
    card_number = models.PositiveIntegerField(null = True)
    card_type = models.CharField(max_length= 10,choices=CARD_TYPE_CHOICES, null = True)
    expiry_date = models.DateTimeField(null = True,blank= True)
    card_status = models.CharField(max_length= 10,null= True)
    cvv = models.SmallIntegerField(null= True)
    account = models.ForeignKey(Account,on_delete= models.CASCADE,related_name='account_card')
    issuer = models.CharField(max_length= 12,null= True)
    def __str__(self):
        return self.card_name
    
class Notification(models.Model):
    recipient = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_notification')     
    message = models.TextField(max_length=99)
    date_time = models.DateTimeField(null = True,blank= True)

LOAN_STATUS_CHOICES = (("Paid","Paid"),("Unpaid","Unpaid"))
LOAN_TYPE_CHOICES = (("Short Term", "Short Term"),("Long Term", "Long Term"))
class Loan(models.Model):
    amount = models.PositiveIntegerField()
    wallet = models.ForeignKey(Wallet,on_delete= models.CASCADE,related_name='wallet_loan')
    interest_rate = models.PositiveIntegerField()
    guarantee = models.ForeignKey(Customer,on_delete= models.CASCADE,related_name='customer_loan')
    borrow_date_and_time=models.DateTimeField(null = True, blank= True)
    payment_due_date = models.DateTimeField(null = True,blank=True)
    loan_balance = models.PositiveIntegerField()
    loan_term = models.CharField(max_length= 12, choices= LOAN_TYPE_CHOICES, null= True)
    loan_status = models.CharField(max_length= 15,choices= LOAN_STATUS_CHOICES,null = True)
    duration = models.PositiveIntegerField()
    def __str__(self):
        return self.loan_term

class Reward(models.Model):
    bonus = models.PositiveIntegerField()
    wallet = models.ForeignKey(Wallet,on_delete= models.CASCADE,related_name='wallet_reward')
    date_given = models.DateTimeField(null= True, blank= True)