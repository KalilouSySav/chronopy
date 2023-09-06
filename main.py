import time
from chronometer import Chronometer
from chronometer_view import ChronometerView
from chronometer_controller import ChronometerController

def main():
    model = Chronometer()
    view = ChronometerView()
    controller = ChronometerController(model, view)

    while True:
        print("Menu:")
        print("1. Démarrer le chronomètre")
        print("2. Arrêter le chronomètre")
        print("3. Réinitialiser le chronomètre")
        print("4. Quitter")
        choice = input("Entrez votre choix: ")

        if choice == "1":
            controller.start_chronometer()
            # while controller.is_running_chronometer():
                # controller.update_chronometer()
                # time.sleep(1)
        elif choice == "2":
            controller.stop_chronometer()
        elif choice == "3":
            controller.reset_chronometer()
        elif choice == "4":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
