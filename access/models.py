from django.db import models



class Users(models.Model):
    user = models.CharField(max_length=60, verbose_name= 'Usuario', unique=True)
    password = models.CharField(max_length=50, verbose_name = 'Contraseña')
    charge = models.CharField(max_length= 50, verbose_name = 'Cargo')
    
    def __str__(self):
        return self.user
    

    
    
class Questions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question_1 = models.CharField(max_length= 80, verbose_name= 'Primera Pegunta Secreta')
    answer_1 = models.CharField(max_length= 50, verbose_name= ' Respuesta Secreta')
    question_2 = models.CharField(max_length=100, verbose_name= 'Segunda Pregunta Secreta')
    answer_2 = models.CharField(max_length=50, verbose_name= 'Respuesta Secreta')
    question_3 = models.CharField(max_length=100, verbose_name= 'Tercera Pregunta Secreta ')
    answer_3 = models.CharField(max_length= 50, verbose_name=' Respuesta Secreta')
    
    def __str__(self):
        return f"Questions for user: {self.user}"
    