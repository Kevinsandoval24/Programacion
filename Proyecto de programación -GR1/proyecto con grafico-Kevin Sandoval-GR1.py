import tkinter as tk


class Autopartes:

    # "menu" funciona como un diccionario donde contiene los diferentes productos que se puede encontrar en el autoparte incluyendo sus precios y la cantidad disponible
    
    menu = {
        'baterias': {'precio': 120, 'cantidad': 100},
        'discos de frenos': {'precio': 20, 'cantidad': 5},
        'filtros de aire': {'precio': 18, 'cantidad': 26},
        'filtros de aceite': {'precio': 25, 'cantidad': 10},
        'termostatos': {'precio': 34, 'cantidad': 70},
        'bujias de encendido': {'precio':24, 'cantidad':60},
        'escobillas de limpiaparabrisas': {'precio':15, 'cantidad':40},
        'Radiadores': {'precio':80, 'cantidad':30},
        'amortiguadores': {'precio':35, 'cantidad':17},
        'pastillas de freno': {'precio':5, 'cantidad':25},
        'correas de transmision': {'precio':60, 'cantidad':15},
        'lamparas para faros': {'precio':20, 'cantidad':89},
        'escaneres': {'precio':380, 'cantidad':14},
        'suspensiones': {'precio':470, 'cantidad':0}, 
       
    }

    def __init__(self): #"__init__" Inicializa los atributos de la instancia 
        self.total = 0
        self.partes = []
        self.inventario = {}

         #Inventario con las cantidades disponibles
        
        for parte, datos in self.menu.items():  # "for" este bucle en el init crea el inventario
            self.inventario[parte] = datos['cantidad']

    def add(self, parte):   # Este método permite agregar una parte a la lista de partes adquiridas y actualiza el total de la factura.
        if parte not in self.menu:
            print(f"La parte '{parte}' no está disponible en el menú.")
            return

        if self.inventario[parte] <= 0:
            print(f"Lo siento, '{parte}' se encuentra por el momento agotado.")
            return

        self.partes.append(parte)
        self.total += self.menu[parte]['precio']
        self.inventario[parte] -= 1      #Reduce la cantidad de la parte adquirida por el cliente en el inventario.

    def calculate_total(self, impuesto):    #Este método calcula el total de la factura, teniendo en cuenta un impuesto proporcionado como argumento.
        impuesto = (impuesto / 100) * self.total
        total = self.total + impuesto
        return total

    def get_inventario_text(self):      # Este método devuelve una cadena que contiene información sobre el inventario de autopartes disponible.
        inventario_text = "Inventario:\n"
        for parte, cantidad in self.inventario.items():
            inventario_text += f"{parte}: {cantidad} disponibles\n"
        return inventario_text

class AutopartesApp(tk.Tk):     # Esta clase define la interfaz gráfica de la aplicación utilizando la biblioteca Tkinter.
    
    def __init__(self):       #__init__ inicializa la ventana de la aplicación, el título, la geometría y crea una instancia de Autopartes.
        super().__init__()
        self.title("Autopartes App")
        self.geometry("400x300")
        self.autopartes = Autopartes()
        self.create_widgets()

    def create_widgets(self):      #crea y organiza los widgets en la ventana de la aplicación, como la entrada para ingresar partes, botones y etiquetas para mostrar resultados e inventario.
        self.part_entry = tk.Entry(self)
        self.part_entry.pack(pady=10)

        add_button = tk.Button(self, text="Agregar Parte", command=self.add_part)
        add_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.inventario_label = tk.Label(self, text="")
        self.inventario_label.pack(pady=10)

        self.update_inventario_label()

    def add_part(self):  # Este método se llama cuando se presiona el botón "Agregar Parte" en la interfaz.
        parte = self.part_entry.get().lower()
        self.autopartes.add(parte)
        self.part_entry.delete(0, tk.END)
        self.update_result_label()
        self.update_inventario_label()

    def update_result_label(self): #Actualiza la etiqueta de resultado en la interfaz con la información de la factura, incluyendo las partes adquiridas y el total a pagar.
        
        impuesto = 10  # Supongamos un impuesto del 10%
        total = self.autopartes.calculate_total(impuesto)
        factura_text = "Factura:\n"
        for parte in self.autopartes.partes:
            factura_text += f"{parte:20} ${self.autopartes.menu[parte]['precio']}\n"
        factura_text += f"Total ${total:.2f}"
        self.result_label.config(text=factura_text)

    def update_inventario_label(self):    #Actualiza la etiqueta de inventario en la interfaz con la información sobre las autopartes disponibles en el inventario.
        inventario_text = self.autopartes.get_inventario_text()
        self.inventario_label.config(text=inventario_text)

if __name__ == "__main__":   #Esta parte del código verifica si el script se está ejecutando directamente (no importado como módulo).
    app = AutopartesApp()
    app.mainloop()
