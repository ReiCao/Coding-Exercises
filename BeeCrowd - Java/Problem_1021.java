import java.io.IOException;
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        double money = scanner.nextDouble();
        int moneyInCents = (int) Math.round(money*100);
        int[] notes = {10000, 5000, 2000, 1000, 500, 200};
        int[] cents = {100, 50, 25, 10, 5, 1};
        scanner.close();

        System.out.println("NOTAS:");
        for (int note : notes) {
            int note_amount = moneyInCents / note;
            moneyInCents %= note;
            System.out.printf("%d nota(s) de R$ %.2f\n", note_amount, note / 100.0);
        }
        System.out.println("MOEDAS:");
        for (int cent : cents) {
            int cent_amount = moneyInCents / cent;
            moneyInCents %= cent;
            System.out.printf("%d moeda(s) de R$ %.2f\n", cent_amount, cent / 100.0);

        }
    }
}