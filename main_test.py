def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            input_user = input(script).strip()

            if input_user == "":
                print("Vous n'avez pas entré le premier nombre")
                continue
            
            input_number = input_user.replace(',','.')
            number = float(input_number)
            
            if number  ==int(number):
                return int(number)
            else:
                return number
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

def operating(a, b, operator):
    """Effectue l'opération demandée entre a et b."""
    match operator:
        case "+":
            result = a + b
            if result == int(result):
                result = int(result)
            return result
        case "-":
            result = a - b
            if result == int(result):
                result = int(result)
            return result
        case "*":
            result = a * b
            if result == int(result):
                result = int(result)
            return result
        case "/":
            if b == 0:
                print("Erreur: division par zéro impossible.")
                return None
            result = a / b
            if result == int(result):
                result = int(result)
            return result
        case "//":
            if b == 0:
                print("Erreur division par zero impossible ")
                return None
            result = a // b
            if result == int(result):
                result = int(result)
            return result
        case "%":
            if b == 0:
                print("Erreur division par zero impossible ")
                return None
            result = a % b
            if result == int(result):
                result = int(result)
            return result
        case _:
            print("Erreur: opération inconnue.")
            return None

def calculator():
        """ Fonction principale pour exécuter la calculatrice. """
        print("")
        print("═══════════════════════════════════════════════════════")
        print("                   ══ BIENVENUE ══")
        print("                     Calculatrice")
        print("═══════════════════════════════════════════════════════")

    
        while True:
            # Demander les entrées
            a = ask_number ("Entrez le premier nombre: ")
            b = ask_number("Entrez le second nombre: ")
            
            operator = input("Entrez l'opération (+, -, *, /, //, %): ").strip()
            
            # Effectuer l'opération et afficher le résultat
            result = operating(a, b, operator)
            
            if result is not None:
                print(f"Le résultat de {a} {operator} {b} est : {result}")

                operation_history.append(f"{a} {operator} {b} = {result}")
            
            # Demander à l'utilisateur s'il souhaite continuer
            continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
            if continuer != 'oui':
                print("Merci d'avoir utilisé la calculatrice.")
                break

# Lancer la calculatrice
calculator()