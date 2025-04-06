public class MonteCarlo {

    private static final int startVal = 1000;
    private static final int a = 24693;
    private static final int c = 3517;
    private static final int K = (int) Math.pow(2, 17); 

    public static void main(String[] args) {
        System.out.println("u51: " + randNumGen(51)); 
        System.out.println("u52: " + randNumGen(52));
        System.out.println("u53: " + randNumGen(53));	
    }
    
    public static double randNumGen(int i) {
        if (i <= 0) {
            return (a * startVal + c) % K;
        }
        return (a * randNumGen(i - 1) + c) % K;
    }
}