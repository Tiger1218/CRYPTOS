import java.math.BigInteger;
import java.util.Random;

public class MSSCTF2019_easy_crypto
{
    static BigInteger e = new BigInteger("2333");
    static BigInteger p = new BigInteger("25837803107239222173952070863792093460107066132554083629904658720362290337547984488864287283444004000702302024445859946181490789947549247970591904040287281");
    static BigInteger h = new BigInteger("3157949570880104750798870795076886225888442155001709003841060612772039388989395218484005993511083988039042347782289369175775773651613878334013870511350162");
    static String table = new String("0123456789abcdefghijklmnopqrstuvwxyz");

    public static String Enc(String plaintext)
    {
        BigInteger[] cipher = new BigInteger[2];
        plaintext = plaintext.toLowerCase();
        BigInteger r = new BigInteger(new Random().nextInt(10000000)+"");
        String rtext = r.toString();
        int rlen = rtext.length();
        String text = "";
        for(int i = 0; i < plaintext.length(); i++)
        {
            int j = i % rlen;
            text += table.charAt((table.indexOf(plaintext.charAt(i))+Character.getNumericValue(rtext.charAt(j))) % 36);
            System.out.println(text);
        }
        BigInteger bText = new BigInteger(text, 36);
        cipher[0] = e.modPow(r, p);
        cipher[1] = h.modPow(r, p).multiply(bText);
        return cipher[0].toString(36)+"||"+cipher[1].toString(36);
    }

    public static void main(String[] args) throws Exception
    {
        System.out.println("Welcome to mssctf, here is the flag:");
        String str1 = "This is the flag";
        String str2 = Enc(str1); // 7r7m11ftidw8a26ixbswjs7ldg5cni6vfswa8j567v5c2lv3cx28gkb9cfa2lk9h67o2techbzy07oiafnnshprkpaygt8qktf9||lw6o5k6qcfq1hgb2t2bstpmkwdslpczslqbietypqlj9oyysq93k28mseks77rjd7sbsnb6v5pl2wvk1t5ksrir2zlnwx9dwvlxvi4b02ukua02o9i48p
    }
}
