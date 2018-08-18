from django.contrib import admin

from .models import *

admin.site.register(Departamento)
admin.site.register(RolUsuarioCurso)
admin.site.register(Semestres)
admin.site.register(TipoUsuario)
admin.site.register(UsuarioTipoUsuario)

class UsuariosAdmin(admin.ModelAdmin):
	list_display=('nombre','apellido','user',)

admin.site.register(Usuarios,UsuariosAdmin)


class CursosAdmin(admin.ModelAdmin):
	list_display=('nombre',)
	fieldsets=[('General',{'fields': ['nombre','id','departamento']}),
	 ('Administrativo',{'fields':['ud','codigo','anho','horario','semestres']})
]
admin.site.register(Cursos,CursosAdmin)

