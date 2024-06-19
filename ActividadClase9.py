# Bloque 1: Importación del módulo datetime

from datetime import datetime

# Bloque 2: Definición de la clase TareaGeneral

class TareaGeneral:
    def __init__(self, nombre, descripcion, prioridad):
        
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

     
    def __str__(self):
        return f"Nombre: {self.nombre}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"

# Bloque 3: Definición de la clase TareaConFecha que hereda de TareaGeneral

class TareaConFecha(TareaGeneral):
    def __init__(self, nombre, descripcion, prioridad, fecha_vencimiento):
         
        super().__init__(nombre, descripcion, prioridad)  #
         
        self.fecha_vencimiento = fecha_vencimiento

     
    def __str__(self):
        return f"{super().__str__()}, Fecha de Vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

# Bloque 4: Definición de la clase ListaDeTareas

class ListaDeTareas:
    def __init__(self):
         
        self.tareas = []

     
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.nombre}' agregada con éxito.")

     
    def eliminar_tarea(self, nombre_tarea):
         
        for tarea in self.tareas:
             
            if tarea.nombre == nombre_tarea:
                self.tareas.remove(tarea)
                print(f"Tarea '{nombre_tarea}' eliminada con éxito.")
                return
         
        print(f"Tarea '{nombre_tarea}' no encontrada.")

     
    def listar_tareas(self):
         
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
             
            for tarea in self.tareas:
                print(tarea)

# Bloque 5: Función principal main

def main():
     
    lista_de_tareas = ListaDeTareas() # 
     
    while True:
         
        print("\nGestor de Tareas ")
        print("1. Agregar nueva tarea")
        print("2. Eliminar tarea existente")
        print("3. Listar todas las tareas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

         
        if opcion == "1":
            tipo_tarea = input("¿Es una tarea con fecha? (si/no): ").lower()
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            prioridad = input("Prioridad (alta, media, baja): ")

             
            if tipo_tarea == "si":
                fecha_str = input("Fecha de vencimiento (YYYY-MM-DD): ")
                 
                fecha_vencimiento = datetime.strptime(fecha_str, '%Y-%m-%d')
                 
                tarea = TareaConFecha(nombre, descripcion, prioridad, fecha_vencimiento)
            else:
                 
                tarea = TareaGeneral(nombre, descripcion, prioridad)
            
             
            lista_de_tareas.agregar_tarea(tarea)

         
        elif opcion == "2":
            nombre_tarea = input("Nombre de la tarea a eliminar: ")
             
            lista_de_tareas.eliminar_tarea(nombre_tarea)

         
        elif opcion == "3":
             
            lista_de_tareas.listar_tareas()

         
        elif opcion == "4":
            print("Saliendo del programa.")
            break

         
        else:
            print("Opción no válida, por favor intente nuevamente.")

 
if __name__ == "__main__": #
    main()
