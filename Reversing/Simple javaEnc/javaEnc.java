import java.util.*;

// ##################
// Author => IronByte
// ##################

public class javaEnc {

    public static void welcome() {
        System.out.println("#############################");
        System.out.println("####### JAVA CRACKME ########");
        System.out.println("#############################");
    }

    public static String encrypt(String input, int byte1, int byte2) {
        String enc = new String(""); 
        enc = "";
        for(int i = 0; i < input.length(); i++) {
            enc = enc + (char)((int)(input.charAt(i)) ^ byte1 ^ byte2);
        }
        return enc;      
    }
    public static void main(String[] args) {
        welcome();
        try (Scanner sc = new Scanner(System.in)) {
            String flag = new String("");
            System.out.print("Flag : "); 
            flag = sc.nextLine();        
            int bt1, bt2;
            do {
                System.out.print("Give the 1st byte that can decrypt the flag : ");
                bt1 = sc.nextInt(); 
            } while(bt1 < 0 || bt1 > 256);
            
            do {
                System.out.print("Give the 2nd byte that can decrypt the flag : ");
                bt2 = sc.nextInt();
            } while(bt2 < 0 || bt2 > 256);
            
            String result = encrypt(flag, bt1, bt2);

            if (result.equals("Ucestohcru}l2p2Y>4s15Y`64e7h?Y73Y36Ye667'{")) {
                System.out.println("\n===> Good Job You cracked the hell out of it ! ");
            } else {
                System.out.println("\n===> Keep trying !");
            }
            
        } catch (Exception e) {
            System.out.println("Input won't instance ! ");
        }
        
    }   
}