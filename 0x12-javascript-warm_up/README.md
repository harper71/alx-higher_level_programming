# 0x12-javascript-warm_up
### Differences Between `var`, `const`, and `let`

1. **Scope**:
   - **`var`**: Function-scoped. It is visible throughout the function where it is declared, and if declared outside of any function, it becomes globally scoped.
   - **`let`**: Block-scoped. It is only visible within the block (enclosed by `{}`) where it is declared.
   - **`const`**: Block-scoped like `let`. It is also only visible within the block where it is declared.

2. **Re-declaration**:
   - **`var`**: Can be re-declared and updated within its scope.
   - **`let`**: Cannot be re-declared within the same scope, but can be updated.
   - **`const`**: Cannot be re-declared or updated after its initial assignment.

3. **Hoisting**:
   - **`var`**: Variables are hoisted to the top of their scope and initialized with `undefined`.
   - **`let`** and **`const`**: Variables are hoisted to the top of their scope but are not initialized. Accessing them before the declaration results in a `ReferenceError`.

### Data Types Available in JavaScript

1. **Primitive Types**:
   - **String**: Represents textual data. Example: `"hello"`, `'world'`.
   - **Number**: Represents both integer and floating-point numbers. Example: `42`, `3.14`.
   - **BigInt**: Represents whole numbers larger than `Number.MAX_SAFE_INTEGER`. Example: `1234567890123456789012345678901234567890n`.
   - **Boolean**: Represents logical values. Example: `true`, `false`.
   - **Undefined**: Represents an uninitialized variable. Example: `let x;` (x is `undefined`).
   - **Null**: Represents the intentional absence of any object value. Example: `let y = null;`.
   - **Symbol**: Represents a unique identifier. Example: `let sym = Symbol('foo');`.

2. **Non-Primitive Types**:
   - **Object**: Represents a collection of properties. Example: `{ key: 'value' }`.
   - **Array**: Represents an ordered collection of elements. Example: `[1, 2, 3]`.

### Using `if`, `if...else` Statements

- **if**:
  ```javascript
  if (condition) {
      // code to execute if condition is true
  }
  ```

- **if...else**:
  ```javascript
  if (condition) {
      // code to execute if condition is true
  } else {
      // code to execute if condition is false
  }
  ```

- **if...else if...else**:
  ```javascript
  if (condition1) {
      // code to execute if condition1 is true
  } else if (condition2) {
      // code to execute if condition2 is true
  } else {
      // code to execute if none of the conditions are true
  }
  ```

### Using Comments

- **Single-line comment**:
  ```javascript
  // This is a single-line comment
  ```

- **Multi-line comment**:
  ```javascript
  /* 
     This is a 
     multi-line comment 
  */
  ```

### Assigning Values to Variables

- **Using `var`**:
  ```javascript
  var x = 5;
  var name = "Alice";
  ```

- **Using `let`**:
  ```javascript
  let y = 10;
  let city = "Paris";
  ```

- **Using `const`**:
  ```javascript
  const z = 15;
  const country = "France";
  ```

In summary, `var`, `let`, and `const` have different scoping rules and capabilities regarding reassignment and re-declaration. JavaScript supports various data types, both primitive and non-primitive. Conditional statements (`if`, `if...else`) are used for decision-making. Comments can be added for code documentation, and variables can be assigned values using `var`, `let`, or `const` depending on the need for mutability and scope.