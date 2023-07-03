
package clase9;

import java.util.Scanner;


public class Clase9 {

    
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese la primer nota");
        int nota1 = leer.nextInt();
        System.out.println("Ingrese la segunda nota");
        int nota2 = leer.nextInt();
        System.out.println("Ingrese la tercer nota");
        int nota3 = leer.nextInt();
        
        int notafinal = nota1+nota2+nota3;   
    System.out.println("La suma de las 3 notas es: " + notafinal);
    }
    
}
