# t3_case

Yapılması gerekenler:

## Postgresql Kurulumu
```


sudo apt-get install libpq-dev python-dev

sudo apt-get install postgresql postgresql-contrib

```

## Postgresql Yapılandırma
```
sudo su postgres

### Eğer psql komutu çalışmazsa ``` sudo service postgresql restart ```


psql

create database t3_vakfi_case;

create user admin;

alter user admin with encrypted password '12345';

grant all privileges on database t3_vakfi_case to admin;

```

## Virtual Environment Kurulumu

```
sudo pip install virtualenv


mkdir /Desktop/myproject

cd /Desktop/myproject

virtualenv .venv/
```

## Projeyi Locale Çekme
```
cd /Desktop/myproject

git clone <project_url>

```
## Proje Yapılandırması
```
source .venv/bin/activate

cd t3_case

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

```

### Tüm adımları tamamladıktan sonra internet tarayıcısından local portunda proje çalışır durumda olucaktır.

```
http://127.0.0.1:8000
```

### Yeni kayıt oluşturmak için

#### http://127.0.0.1:8000/admin panelinden oluşturduğunuz superuser kullanıcısıyla giriş yapıp okul ve sınıf kaydetmeniz gerekmektedir.