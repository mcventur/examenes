import java.util.Arrays;
import java.util.List;

public class Exercicio2_1 {
    private static final int DESPLAZAMIENTO = 5;

    public static String cifra(String texto){
        String[] alfabeto = {"a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z"};

        //Lo pasamos a lista porque admiten el método indexOf
        List<String> listaAlfabeto = Arrays.asList(alfabeto);

        String cifrado = "";
        for (char letra : texto.toCharArray()) {
            int indice_cif = (listaAlfabeto.indexOf(String.valueOf(letra)) + DESPLAZAMIENTO) % listaAlfabeto.size();
            cifrado += listaAlfabeto.get(indice_cif);
        }
        return cifrado;
    }
    public static void main(String[] args) {
        //Prueba
        System.out.println(cifra("vicente"));

    }
}