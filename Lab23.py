Python
# Lambda function
max_value = lambda numbers: max(numbers)

# Test
nums = [10, 45, 23, 89, 4]
print("Maximum:", max_value(nums))  # Output: 89

Kotlin
fun main() {
    val maxValue = { numbers: List<Int> -> numbers.max() }
    val nums = listOf(10, 45, 23, 89, 4)
    println("Maximum: ${maxValue(nums)}") // Output: 89
}
----------------------------------------------------------
Python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

Kotlin
fun main() {
    val nums = listOf(1, 2, 3, 4, 5)
    val squares = nums.map { x -> x * x }
    println("Squares: $squares") // Output: [1, 4, 9, 16, 25]
}
------------------------------------------------------------
Python
average = lambda numbers: sum(numbers) / len(numbers)
nums = [4, 8, 12, 16]
print("Average:", average(nums))  # Output: 10.0

Kotlin
fun main() {
    val average = { numbers: List<Int> -> numbers.sum().toDouble() / numbers.size }
    val nums = listOf(4, 8, 12, 16)
    println("Average: ${average(nums)}") // Output: 10.0
}
