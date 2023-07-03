
package clase10ejercicio1;

import java.util.Scanner;


public class Clase10Ejercicio1 {

    
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        var condicion = false;
        if (condicion){
            System.out.println("Condicion Verdadera");
        }
        else   {
            System.out.println("Condicion Falsa");
        }
        
        var numero = 2;
        var numeroTexto = "Numero desconocido";
        if (numero ==1) {
            numeroTexto = "Numero uno";
        }
        else if (numero ==2) {
            numeroTexto = "Numero dos";        
        }
         else if (numero ==3) {
            numeroTexto = "Numero tres";
         }
         else if (numero ==4) {
            numeroTexto = "Numero cuatro";
         }
        else{
             numeroTexto = "Numero no encontrado";
         }
        System.out.println("numeroTexto = " + numeroTexto);
        
        
    }
    
}
