from importlib import import_module
from .PersonaBase import PersonaClaseBase

def factory(persona_nombre, *args, **kwargs):
    try:
        if '.' in persona_nombre:
            module_name, class_name = persona_nombre.rsplit('.', 1)
        else:
            module_name = persona_nombre
            class_name =persona_nombre.capitalize()
        
    persona_modulo = import_module('.' + module_name, package='Personas')
    persona_clase = getattr(persona_modulo, class_name)
    instance = animal_class(*args, **kwargs)
    return instance
