In JavaScript, you can access system arguments (also known as command-line arguments) when running a Node.js script using the `process.argv` array. The `process.argv` array contains the command-line arguments passed when the Node.js process was launched.

### Accessing Command-Line Arguments

The `process.argv` array contains:
1. The first element (index 0) is the path to the Node.js executable.
2. The second element (index 1) is the path to the JavaScript file being executed.
3. The subsequent elements (index 2 and onward) are the command-line arguments.

Here's an example of how to use system arguments in a Node.js script:

```javascript
// script.js

// Access command-line arguments
const args = process.argv.slice(2); // Ignore the first two elements

// Print the arguments
console.log('Command-line arguments:', args);

// Example of using arguments
if (args.length > 0) {
  console.log('First argument:', args[0]);
  console.log('Second argument:', args[1]);
} else {
  console.log('No arguments provided');
}
```

### Running the Script

To run the above script with command-line arguments, use the following command:

```bash
node script.js arg1 arg2 arg3
```

The output will be:

```plaintext
Command-line arguments: [ 'arg1', 'arg2', 'arg3' ]
First argument: arg1
Second argument: arg2
```

### Example Use Cases

1. **Greeting Script**:
   ```javascript
   // greet.js

   const args = process.argv.slice(2);

   if (args.length !== 1) {
     console.log('Usage: node greet.js <name>');
   } else {
     const name = args[0];
     console.log(`Hello, ${name}!`);
   }
   ```

   Run with:
   ```bash
   node greet.js Alice
   ```

   Output:
   ```plaintext
   Hello, Alice!
   ```

2. **Simple Calculator**:
   ```javascript
   // calculator.js

   const args = process.argv.slice(2);

   if (args.length !== 3) {
     console.log('Usage: node calculator.js <num1> <operator> <num2>');
     process.exit(1);
   }

   const num1 = parseFloat(args[0]);
   const operator = args[1];
   const num2 = parseFloat(args[2]);

   if (isNaN(num1) || isNaN(num2)) {
     console.log('Both arguments must be numbers');
     process.exit(1);
   }

   let result;
   switch (operator) {
     case '+':
       result = num1 + num2;
       break;
     case '-':
       result = num1 - num2;
       break;
     case '*':
       result = num1 * num2;
       break;
     case '/':
       result = num1 / num2;
       break;
     default:
       console.log('Unsupported operator');
       process.exit(1);
   }

   console.log(`Result: ${result}`);
   ```

   Run with:
   ```bash
   node calculator.js 5 + 3
   ```

   Output:
   ```plaintext
   Result: 8
   ```

### Parsing Arguments with Libraries

For more advanced parsing, you can use libraries like `yargs` or `commander`. Here's an example with `yargs`:

1. **Install `yargs`**:
   ```bash
   npm install yargs
   ```

2. **Using `yargs`**:
   ```javascript
   // args.js

   const yargs = require('yargs/yargs');
   const { hideBin } = require('yargs/helpers');
   
   const argv = yargs(hideBin(process.argv))
     .option('name', {
       alias: 'n',
       type: 'string',
       description: 'Your name'
     })
     .option('age', {
       alias: 'a',
       type: 'number',
       description: 'Your age'
     })
     .demandOption(['name', 'age'], 'Please provide both name and age arguments')
     .help()
     .argv;
   
   console.log(`Name: ${argv.name}`);
   console.log(`Age: ${argv.age}`);
   ```

   Run with:
   ```bash
   node args.js --name=Alice --age=25
   ```

   Output:
   ```plaintext
   Name: Alice
   Age: 25
   ```

Using `process.argv` or a library like `yargs`, you can effectively handle command-line arguments in your Node.js applications.