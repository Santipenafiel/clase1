// Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se instroduzca un numero negativo

package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(leer.nextLine());
        while(numero >= 0){ //Mientras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero,2);
            System.out.println("El numero " +numero+ "elvado al cuadrado es: "+ cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(leer.nextLine());
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
}
