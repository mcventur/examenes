import java.util.Scanner;

public class Ean13 {
    public static void main(String[] args) {
        System.out.print("Introduce el código EAN 13 sin DC: ");
        Scanner sc = new Scanner(System.in);
        String entrada = "";
        do {
            entrada = sc.nextLine();
            //entrada = "845678901234";
            if (entrada.length() < 12) {
                System.out.println("El código debe tener 12 caracteres");
            }
        } while (entrada.length() < 12);

        try {
            System.out.println("El DC es " + calculaDC(entrada));
        } catch (NumberFormatException e){
            System.out.println("Sólo se admiten valores numéricos");
        }
    }

    private static int calculaDC(String entrada) {
        char[] entradaArray = entrada.toCharArray();
        int acumulador = 0;
        int multiplo10 = 0;
        for (int i = 0; i < 12; i++) {
            int digito = Integer.parseInt(entradaArray[i] + "");
            if (i % 2 == 0) {
                acumulador += digito;
            } else {
                acumulador += digito * 3;
            }
        }
        multiplo10 = multiploSup(acumulador);
        return multiplo10 - acumulador;
    }

    /**
     * Calcula o múltiplo de 10 superior ou igual dun número dado
     */
    private static int multiploSup(int num) {
        int resto10 = num % 10;
        int cociente10 = num / 10;
        if (resto10 == 0) {
            return 10 * cociente10;
        } else {
            return (10 * cociente10) + 10;
        }
    }
}
