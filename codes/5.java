import java.util.Arrays;

public class ShellSort {

    // Метод для сортировки Шелла
    public static void shellSort(int[] arr) {
        int n = arr.length;

        // Начинаем с большого промежутка (gap) и уменьшаем его
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Проходим по всем элементам, начиная с индекса 'gap'
            for (int i = gap; i < n; i++) {
                // Сохраняем текущий элемент для вставки
                int temp = arr[i];
                int j;

                // Сдвигаем элементы, которые больше temp, вправо
                // на расстояние 'gap', пока не найдем правильное место
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                    arr[j] = arr[j - gap];
                }

                // Вставляем temp на правильное место
                arr[j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 34, 54, 2, 3};

        System.out.println("Исходный массив: " + Arrays.toString(arr));

        shellSort(arr);

        System.out.println("Отсортированный массив: " + Arrays.toString(arr));
    }
}
