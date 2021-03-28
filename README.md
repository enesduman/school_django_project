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

python manage.py runserver

```

### Tüm adımları tamamladıktan sonra internet tarayıcısından local portunda proje çalışır durumda olucaktır.