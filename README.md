### 数据库初始化

```
$ mysql -u root -p
Enter password:
```

```
CREATE DATABASE variants_dictionary;
CREATE USER 'dict_user'@'localhost' IDENTIFIED BY 'ymfxgdcd';
GRANT ALL PRIVILEGES ON variants_dictionary.* TO 'dict_user'@'localhost';
FLUSH PRIVILEGES;
quit
```

verify
```
show grants for 'dict_user'@'localhost';
```

### 环境推荐使用virtualenvwrapper
```
pip install virtualenv
pip install virtualenvwrapper
mkvirtualenv dict
workon dict
```
### 安装
```
pip install -r requirements/dev.txt
```

### 创建demo用户
```
python manage.py createsuperuser
```

###运行
```
python manage.py runserver_plus
```

###swagger url
http://127.0.0.1:8000/api/swagger





