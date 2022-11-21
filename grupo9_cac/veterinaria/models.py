from django.db import models

class Familia(models.Model):
    apellido_nombre = models.CharField(max_length=100, verbose_name='apellido_nombre')
    telefono = models.IntegerField(verbose_name = 'telefono')
    direccion = models.CharField(max_length=200, verbose_name = 'direccion')
    email = models.EmailField(verbose_name = 'email', max_length=200)
    
    def __str__(self):
        return self.apellido_nombre
    
    class Meta:
        verbose_name = 'familia'
        verbose_name_plural = 'familias'
        ordering = ['apellido_nombre']

class Paciente(models.Model):
    nombre = models.CharField(max_length=25, blank=False, null=False, verbose_name='nombre')
    especie = models.CharField(max_length=30, verbose_name='especie')
    raza = models.CharField(max_length=30, verbose_name='raza')
    fecha_nacimiento = models.DateField(verbose_name='fecha_nacimiento')
    foto = models.ImageField(verbose_name = 'foto', upload_to = 'pacientes')
    peso = models.FloatField(verbose_name='peso')
    fecha_visita = models.DateField(auto_now_add=True, verbose_name='fecha_visita')
    comentarios = models.TextField(max_length=255)
    familia = models.ForeignKey(Familia, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        ordering = ['nombre']
    