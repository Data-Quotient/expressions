### **Top 10 Essential Functions to Add to Your Framework**

| **Function Name** | **Purpose** | **Usage** | **DataFusion Equivalent** |
|-------------------|-------------|-----------|---------------------------|
| **IF**            | Performs a logical test and returns one value if TRUE, and another if FALSE. | `IF(condition, true_value, false_value)` | `f.case().when(condition, true_value).otherwise(false_value)` |
| **AND**           | Returns TRUE if all conditions are TRUE. | `AND(condition1, condition2, ...)` | Combine conditions with `&` operator: `(condition1) & (condition2)` |
| **OR**            | Returns TRUE if any condition is TRUE. | `OR(condition1, condition2, ...)` | Combine conditions with `|` operator: `(condition1) \| (condition2)` |
| **NOT**           | Reverses the logical value of its argument. | `NOT(condition)` | Use the `~` operator: `~(condition)` |
| **CONCATENATE**   | Joins two or more text strings into one string. | `CONCATENATE(text1, text2, ...)` | `f.concat([arg1, arg2, ...])` |
| **LEN**           | Returns the number of characters in a text string. | `LEN(text)` | `f.length(text)` |
| **UPPER** / **LOWER** | Converts text to uppercase (`UPPER`) or lowercase (`LOWER`). | `UPPER(text)`<br>`LOWER(text)` | `f.upper(text)`<br>`f.lower(text)` |
| **LEFT** / **RIGHT** | Extracts a specified number of characters from the start (`LEFT`) or end (`RIGHT`) of a text string. | `LEFT(text, num_chars)`<br>`RIGHT(text, num_chars)` | `f.substr(text, 1, num_chars)`<br>`f.substr(text, f.length(text) - num_chars + 1, num_chars)` |
| **TRIM**          | Removes extra spaces from text. | `TRIM(text)` | `f.trim(text)` |
| **ROUND**         | Rounds a number to a specified number of digits. | `ROUND(number, num_digits)` | `f.round(number, num_digits)` |

---

**Additional Functions to Consider:**

| **Function Name** | **Purpose** | **Usage** | **DataFusion Equivalent** |
|-------------------|-------------|-----------|---------------------------|
| **DATE Functions** | Handle date and time data. | `TODAY()`<br>`NOW()`<br>`DATE(year, month, day)` | `f.current_date()`<br>`f.now()`<br>Date functions and arithmetic |
| **ISNULL** / **COALESCE** | Handle NULL values. | `ISNULL(value)`<br>`COALESCE(value1, value2, ...)` | `f.is_null(value)`<br>`f.coalesce([value1, value2, ...])` |
| **SUMIF** / **COUNTIF** | Conditional aggregation. | `SUMIF(range, criteria)`<br>`COUNTIF(range, criteria)` | Use `f.sum` or `f.count` with `f.when` for conditions |
| **AVERAGE**        | Calculates the average of numbers. | `AVERAGE(number1, number2, ...)` | `f.avg(number_column)` |
| **MIN** / **MAX**  | Returns the smallest (`MIN`) or largest (`MAX`) number in a set. | `MIN(number1, number2, ...)`<br>`MAX(number1, number2, ...)` | `f.min(number_column)`<br>`f.max(number_column)` |


