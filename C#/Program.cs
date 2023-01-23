// Задача: Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись
// исключительно массивами.
// Примеры:
// ["hello", "2", "world", ":-)"] -> ["2", ":-)"]
// ['1234", "1567", "-2", "computer science"] -> ["-2"]
// ["Russia", "Denmark", "Kazan"] -> []



string[] new_array_1 = { "hello", "2", "world", ":-)" };
string[] new_array_2 = { "1234", "1567", "-2", "computer science" };
string[] new_array_3 = { "Russia", "Denmark", "Kazan" };



System.Console.WriteLine($"[{String.Join(", ", some_func(new_array_1))}]");
System.Console.WriteLine($"[{String.Join(", ", some_func(new_array_2))}]");
System.Console.WriteLine($"[{String.Join(", ", some_func(new_array_3))}]");






string[] some_func(string[] my_array)
{
    string[] result = { };
    foreach (var item in my_array)
    {
        if (item.Length > 0 && item.Length <= 3)
        {
            result = result.Append(item).ToArray();
        }
    }
    return result;
}



