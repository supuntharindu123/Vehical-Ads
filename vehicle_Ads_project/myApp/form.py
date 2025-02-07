
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Test,Ads,Contact


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your First Name'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Last Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password'
        }),label='Enter Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Your Password'
        }),label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

   

class LoginForm(AuthenticationForm):
   username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username','class':'form-control'}))
   password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'}))


class UpdateProfileForm(forms.ModelForm):
   first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your First Name'
        })
    )
   last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Last Name'
        })
    )
   email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Email'
        })
    )
   username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        })
    )
   class Meta:
      model=User
      fields = ['username','first_name', 'last_name', 'email']


class ResetPwdForm(PasswordChangeForm):
   old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Old Password'
        })
    )
   new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your New Password'
        }),
        label='New Password'
    )
   new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
        label="Confirm New Password"
    )
   
   class Meta:
      model=User
      fields = ['old_password', 'new_password1','new_password2']


class UploadimgForm(forms.ModelForm):
   class Meta:
      model=Test
      fields=['name','img']

TYPE={
      ('Select Type','Select Type'),
      ('Car','Car'),
      ('Motorcycle','Motorcycle'),
      ('Truck','Truck'),
      ('SUV','SUV'),
      ('Van','Van'),
      ('Three Wheel','Three Wheel'),
      ('Bus','Bus'),
      ('Tractor','Tractor'),
      ('Other','Other')
   }


MAKE={
      ('Select Make','Select Make'),
      ('Ashok-Leyland','Ashok-Leyland'),
      ('Aston','Aston'),
      ('Audi','Audi'),
      ('Bajaj','Bajaj'),
      ('BMW','BMW'),
      ('CAT','CAT'),
      ('Eicher','Eicher'),
      ('Foton','Foton'),
      ('Hero','Hero'),
      ('Hero-Honda','Hero-Honda'),
      ('Hitachi','Hitachi'),
      ('Honda','Honda'),
      ('Hummer','Hummer'),
      ('Isuzu','Isuzu'),
      ('JAC','JAC'),
      ('JCB','JCB'),
      ('Jeep','Jeep'),
      ('Komatsu','Komatsu'),
      ('Kubota','Kubota'),
      ('Lamborghini','Lamborghini'),
      ('Land-Rover','Land-Rover'),
      ('Mahindra','Mahindra'),
      ('Mazda','Mazda'),
      ('Micro','Micro'),
      ('Nissan','Nissan'),
      ('Suzuki','Suzuki'),
      ('Tata','Tata'),
      ('Tesla','Tesla'),
      ('Toyota','Toyota'),
      ('TVS','TVS'),
      ('Volvo','Volvo'),
      ('Yamaha','Yamaha'),
      ('Yanmar','Yanmar'),
      ('Other','Other'),
   }
MIN_YEAR={
    ('Select Min Year','Select Min Year'),
    ('1980','1980'),
    ('1981','1981'),
    ('1982','1982'),
    ('1983','1983'),
    ('1984','1984'),
    ('1985','1985'),
    ('1986','1986'),
    ('1987','1987'),
    ('1988','1988'),
    ('1989','1989'),
    ('1990','1990'),
    ('1991','1991'),
    ('1992','1992'),
    ('1993','1993'),
    ('1994','1994'),
    ('1995','1995'),
    ('1996','1996'),
    ('1997','1997'),
    ('1998','1998'),
    ('1999','1999'),
    ('2000','2000'),
    ('2001','2001'),
    ('2002','2002'),
    ('2003','2003'),
    ('2004','2004'),
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('before 1980','before 1980'),

}
MAX_YEAR={
    ('Select Max Year','Select Max Year'),
    ('1980','1980'),
    ('1981','1981'),
    ('1982','1982'),
    ('1983','1983'),
    ('1984','1984'),
    ('1985','1985'),
    ('1986','1986'),
    ('1987','1987'),
    ('1988','1988'),
    ('1989','1989'),
    ('1990','1990'),
    ('1991','1991'),
    ('1992','1992'),
    ('1993','1993'),
    ('1994','1994'),
    ('1995','1995'),
    ('1996','1996'),
    ('1997','1997'),
    ('1998','1998'),
    ('1999','1999'),
    ('2000','2000'),
    ('2001','2001'),
    ('2002','2002'),
    ('2003','2003'),
    ('2004','2004'),
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('before 1980','before 1980'),

}
    
class PostAdForm(forms.ModelForm):
   
   CONDITION={
      ('Select Condition','Select Condition'),
      ('BrandNew','BrandNew'),
      ('Registered','Registered'),
      ('Unregistered','Unregistered'),
      ('Antique','Antique')
   }
   
   TRANSMISSION={
      ('Select Transmission','Select Transmission'),
      ('Automatic','Automatic'),
      ('Manual','Manual'),
   }
   FUEL_TYPE={
      ('Select Fuel Type','Select Fuel Type'),
      ('Petrol','Petrol'),
      ('Diesel','Diesel'),
      ('Electric','Electric'),
      ('Hybrid','Hybrid'),
   }
   username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        }),disabled=True,required=False
    )
   manufacture_year = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Manufacture Year'
        })
    )
   info = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter More Information About Your Vehicle',
            'rows': 8
        }),
        label="More Information"
    )
   model = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Vehicle Model Name'
        })
    )
   price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Vehicle Price'
        }),
        label="Price (Rs.)"
    )
   engine_capacity = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Vehicle Engine Capacity'
        })
    )
   mileage = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Vehicle Mileage',
        }),
        label="Mileage (km)"
    )
   contact = forms.RegexField(
        regex=r'^\+?[0-9]{9,15}$', 
        error_messages={
            'invalid': 'Enter a valid phone number. Include the country code if applicable.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Phone Number'
        }),
    )
   vehicle_type = forms.ChoiceField(
        choices=TYPE,
        initial="Select Type",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
   vehicle_condition = forms.ChoiceField(
        choices=CONDITION,
        initial="Select Condition",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
   vehicle_make = forms.ChoiceField(
        choices=MAKE,
        initial='Select Make',
        widget=forms.Select(attrs={
            'class': 'form-control',
            
        })
    )
   transmission = forms.ChoiceField(
        choices=TRANSMISSION,
        initial='Select Transmission',
        widget=forms.Select(attrs={
            'class': 'form-control',
            
        })
    )
   fuel_type = forms.ChoiceField(
        choices=FUEL_TYPE,
        initial='Select Fuel Type',
        widget=forms.Select(attrs={
            'class': 'form-control',
            
        })
    )
   image01 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 01 :"
    )
   image02 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 02 :"
    )
   image03 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 03 :"
    )
   image04 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 04 :"
    )
   image05 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 05 :"
    )
   image06 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'accept': 'image/*',  
        }),
        required=False,
        label="Upload Image 06 :"
    )

   class Meta:
      model=Ads
      fields=['username','contact','vehicle_type','vehicle_condition','vehicle_make','model','manufacture_year','price','transmission','fuel_type','engine_capacity','mileage','info','image01','image02','image03','image04','image05','image06']

   def clean(self):
        cleaned_data = super().clean()
        vehicle_type = cleaned_data.get("vehicle_type")
        vehicle_condition = cleaned_data.get("vehicle_condition")
        vehicle_make = cleaned_data.get("vehicle_make")
        transmission=cleaned_data.get("transmission")
        fuel_type=cleaned_data.get("fuel_type")
        year=cleaned_data.get("manufacture_year")
        image01=cleaned_data.get("image01")
       
        
        if vehicle_type == 'Select Type':
            self.add_error('vehicle_type', 'Please select a valid vehicle type.')
        if vehicle_condition == 'Select Condition':
            self.add_error('vehicle_condition', 'Please select a valid vehicle condition.')
        if vehicle_make == 'Select Make':
            self.add_error('vehicle_make', 'Please select a valid vehicle make.')
        if transmission == 'Select Transmission':
            self.add_error('transmission', 'Please select a valid transmission.')
        if fuel_type == 'Select Fuel Type':
            self.add_error('fuel_type', 'Please select a valid fuel type.')
        if not year.isdigit():
            self.add_error('manufacture_year', 'Please enter a valid manufacture year.')
        if len(year) != 4:
            self.add_error('manufacture_year', 'Please enter a valid 4-digit manufacture year.')
        if int(year)<1948 or int(year)>2025:
            self.add_error('manufacture_year', 'Please enter a valid manufacture year between 1948 and 2025.')
        if not image01:
            self.add_error('image01', 'Please add the image')
    


class ContactForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False,disabled=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),disabled=True,required=False)
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':6}))
    class Meta:
        model=Contact
        fields=['username', 'email','message']


class SearchForm(forms.Form):
    vehicle_type=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control text-center py-2'}),choices=TYPE,initial='Select Type',required=False)
    vehicle_make=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control text-center py-2'}),choices=MAKE,initial="Select Make",required=False)
    model=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center py-2','placeholder':"Enter Vehicle Model"}),required=False)
    Min_manufacture_year=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control text-center py-2','placeholder':"Enter Min Year"}),choices=MIN_YEAR,initial="Select Min Year",required=False)
    Max_manufacture_year=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control text-center py-2','placeholder':"Enter Max Year"}),choices=MAX_YEAR,initial="Select Max Year",required=False)
    Min_price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control text-center py-2','placeholder':"Enter Minimun Price (Rs.)"}),required=False)
    Max_price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control text-center py-2','placeholder':"Enter Maximun Price (Rs.)"}),required=False)