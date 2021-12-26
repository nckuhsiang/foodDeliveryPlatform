from django.apps import AppConfig

# An app refers to a submodule of the project. 
# It's self-sufficient and not intertwined with the other apps in the project such that, 
# in theory, you could pick it up and plop it down into another project without any modification. 
# An app typically has its own models.py (which might actually be empty). 
# You might think of it as a standalone python module. 

#每一個 Django project 裡面可以有多個 Django apps
#可以想成是類似模組的概念。在實務上，通常會依功能分成不同 app，方便未來的維護和重複使用。

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainApp'
