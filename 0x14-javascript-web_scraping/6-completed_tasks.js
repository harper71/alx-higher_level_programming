#!/usr/bin/node

const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: ./script.js <API URL>');
  process.exit(1);
}

// Fetch the list of tasks
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    return;
  }

  let todos;
  try {
    todos = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  // Count the number of completed tasks per user
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });

  // Print users with completed tasks

  console.log(completedTasks);
});
