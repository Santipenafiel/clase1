
package Ejercicio6;

import java.util.Scanner;

/**
 *
 * @author Santiago
 */
public class Ejercicio6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner leer = new Scanner(System.in);
        
        System.out.println("Ingrese la cantidad de Dolares que tiene Guillermo");
        float usdGuillermo = leer.nextFloat();
        
        float usdLuis = usdGuillermo /2;
        float usdJuan = (usdGuillermo + usdLuis) / 2;
        
       float total = usdGuillermo+usdJuan+usdLuis;
        System.out.println("La cantidad de Usd que tiene Luis: " + usdLuis);
        System.out.println("La cantidad de Usd que tiene Juan: " + usdJuan);
        System.out.println("La cantida de Usd que tiene todos es: " + total);
    }
    
}
