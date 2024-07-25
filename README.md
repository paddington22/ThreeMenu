TreeMenu — это django-приложение, которое позволяет вносить в БД меню (одно или несколько) через админку и нарисовать на любой нужной странице меню по названию.    
Template tag: {% draw_menu 'main_menu' %}, вместо 'main_menu' можно использовать любое имя, но важно в шаблоне указать команду с этим именем.     

Для запуска приложения откройте IDE и выполните в консоли команды:
  1) git clone https://github.com/paddington22/TreeMenu.git
  2) cd TreeMenu
  3) pip install -r requirements.txt
  4) python manage.py migrate
  5) python manage.py createsuperuser
  6) python manage.py runserver
