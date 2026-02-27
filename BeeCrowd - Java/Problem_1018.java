import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int doisReais = 0, cincoReais = 0, dezReais = 0, vinteReais = 0, cquentaReais = 0, cemReais = 0;
        int dinheiroAtual = userInput.nextInt();
        int total = dinheiroAtual;
        userInput.close();

        while(dinheiroAtual > 1){
            if(dinheiroAtual >= 100){
                cemReais += 1;
                dinheiroAtual -= 100;
            } else if (dinheiroAtual >= 50) {
                cquentaReais += 1;
                dinheiroAtual -= 50;
            } else if (dinheiroAtual >= 20) {
                vinteReais += 1;
                dinheiroAtual -= 20;
            } else if (dinheiroAtual >= 10) {
                dezReais += 1;
                dinheiroAtual -= 10;
            }else if (dinheiroAtual >= 5) {
                cincoReais += 1;
                dinheiroAtual -= 5;
            } else if (dinheiroAtual >= 2) {
                doisReais += 1;
                dinheiroAtual -= 2;
            }
            }
        
        System.out.printf("%d%n", total);
        System.out.printf("%d nota(s) de R$ 100,00%n", cemReais);
        System.out.printf("%d nota(s) de R$ 50,00%n", cquentaReais);
        System.out.printf("%d nota(s) de R$ 20,00%n", vinteReais);
        System.out.printf("%d nota(s) de R$ 10,00%n", dezReais);
        System.out.printf("%d nota(s) de R$ 5,00%n", cincoReais);
        System.out.printf("%d nota(s) de R$ 2,00%n", doisReais);
        System.out.printf("%d nota(s) de R$ 1,00%n", dinheiroAtual);
        }
        
        
    }