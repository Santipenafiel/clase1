
import java.util.Scanner;

      
public class EjercicioClase8 {
    public static void main(String args []){
         Scanner leer = new Scanner(System.in);
  
        System.out.println("Digite el alto del rectangulo");
        int alto = leer.nextInt();
        System.out.println("Digite el ancho del rectangulo");
        int ancho = leer.nextInt();
   
        int area = alto*ancho;
        int perimetro = (alto + ancho)*2;
  
         System.out.println("El area es = " + area);
         System.out.println("El perimetro es = " + perimetro);
    }
}
Scanner leer = new Scanner(System.in);
