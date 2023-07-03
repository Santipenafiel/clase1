/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio7;

import java.util.Scanner;

/**
 *
 * @author Santiago
 */
public class Ejercicio7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, carrosVendidos;
        float salarioMensual, ventaCarro, porcVenta,totalPrecio;
        
        System.out.println("Ingrese la cantidad de carros vendidos: ");
        carrosVendidos = leer.nextInt();
        System.out.println("Digite el precio de un carro: ");
        ventaCarro = leer.nextFloat();
        
        comision *= carrosVendidos;
        totalPrecio = ventaCarro * carrosVendidos;
        porcVenta = totalPrecio *0.05f;
        salarioMensual = salario + comision+ porcVenta;
        
        System.out.println("El salario mensual sera de: " + salarioMensual);
                
        
        
        
        
        
        
    }
    
}
