public class ReverseString {
    public static String reverseString(String s) {
        // Базовый случай
        if (s.length() <= 1) {
            return s;
        }
        // Рекурсивный случай
        return s.charAt(s.length() - 1) + reverseString(s.substring(0, s.length() - 1));
    }

    public static void main(String[] args) {
        String testStr = "СегодняНоябрь";
        System.out.println("Оригинал: " + testStr);
        System.out.println("Перевёрнутая: " + reverseString(testStr));
    }
}
//Вывод:
//Оригинал: СегодняНоябрь
//Перевёрнутая: ьрбяоНяндогеС
