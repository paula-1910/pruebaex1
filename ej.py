import heapq

class EmergencyRoom:
    def __init__(self):
        self.patients = []  # Lista que actúa como heap

    def add_patient(self, name, urgency):
        """Agrega un paciente a la cola de prioridad."""
        heapq.heappush(self.patients, (urgency, name))
        print(f"Paciente {name} con urgencia {urgency} ha sido registrado.")

    def attend_patient(self):
        """Atiende al paciente con mayor prioridad."""
        if self.patients:
            urgency, name = heapq.heappop(self.patients)
            print(f"Atendiendo a {name} (Nivel de urgencia: {urgency})")
        else:
            print("No hay pacientes en espera.")

    def show_waiting_list(self):
        """Muestra la lista de espera de pacientes en orden de prioridad."""
        if self.patients:
            print("Lista de espera (ordenada por prioridad):")
            for urgency, name in sorted(self.patients):
                print(f"{name} - Urgencia {urgency}")
        else:
            print("No hay pacientes en espera.")

# Ejemplo de uso
er = EmergencyRoom()
er.add_patient("Carlos", 3)
er.add_patient("Ana", 1)
er.add_patient("Luis", 4)
er.add_patient("Marta", 2)

er.show_waiting_list()

print("\nAtendiendo pacientes:")
er.attend_patient()
er.attend_patient()
er.show_waiting_list()
