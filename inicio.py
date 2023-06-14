
import os
import subprocess

def show_menu():
    print("Bienvenido a la interfaz ALR")
    print("1. Super Mario Bros 3")
    print("2. Super Mario World")
    print("3. Captan America")
    print("4. Chip 'n Dale - Rescue Rangers 2")
    print("5. Donkey Kong Classics")
    print("6. DuckTales")
    print("7. Flintstones 2")
    print("8. Ninja Gaiden")
    print("9. Shadow Warriors 2")
    print("10. Simpsons, The - Bartman Meets Radioactive Man")
    print("11. Teenage Mutant Ninja Turtles")
    print("12. Terminator")
    print("13. Tiny Toon Adventures")
    print("14. Legend of Zelda")
    print("15. Metroid")
    print("exit. APAGAR")
    print("reiniciar")

def play_rom(rom_path):
    print("Iniciando Mednafen...")
    subprocess.call(["mednafen", rom_path])  # Ejecutar Mednafen con la ruta de la ROM

def main():
    show_menu()
    
    while True:
        choice = input("Ingrese su opción: ")
        
        if choice == "1":
            play_rom("/home/rms/SMB3.nes")
        elif choice == "2":
            play_rom("/home/rms/SMW.nes")
        elif choice == "3":
            play_rom("/home/rms/CAPAME.nes.nes")
        elif choice == "4":
            play_rom("/home/rms/Chip 'n Dale - Rescue Rangers 2 (USA).nes")
        elif choice == "5":
            play_rom("/home/rms/Donkey Kong Classics (USA, Europe).nes")
        elif choice == "6":
            play_rom("/home/rms/DuckTales (USA).nes.nes")
        elif choice == "7":
            play_rom("/home/rms/Flintstones 2 - The Surprise at Dinosaur Peak!, The (U).nes")
        elif choice == "8":
            play_rom("/home/rms/Ninja Gaiden (USA).nes")
        elif choice == "9":
            play_rom("/home/rms/Shadow Warriors 2 (E) [!].nes")
        elif choice == "10":
            play_rom("/home/rms/Simpsons, The - Bartman Meets Radioactive Man (USA).nes")
        elif choice == "11":
            play_rom("/home/rms/Teenage Mutant Ninja Turtles (USA).nes")
        elif choice == "12":
            play_rom("/home/rms/Terminator, The (USA, Europe).nes")
        elif choice == "13":
            play_rom("/home/rms/Tiny Toon Adventures (USA).nes")
        elif choice == "14":
            play_rom("/home/rms/Legend of Zelda, The (U) (PRG1) [!].nes")
        elif choice == "15":
            play_rom("/home/rms/Metroid (U).nes")
        elif choice == "exit":
            print("Apagando...")
            os.system("sudo shutdown now")  # Apagar la Raspberry Pi
            break
        elif choice == "reiniciar":
            print("Reiniciando...")
            os.system("sudo reboot")  # Reiniciar la Raspberry Pi
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
