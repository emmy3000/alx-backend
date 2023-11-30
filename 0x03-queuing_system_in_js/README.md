# 0x03. Queuing System in JS

This project explores the implementation of a queuing system in JavaScript, utilizing Redis as the underlying data store. The following learning objectives are covered in detail to enhance your understanding of the queuing system and its integration with Node.js, Redis, and Express.

## Learning Objectives

### 1. Running a Redis Server

To get started with this project, it's essential to set up and run a Redis server on your local machine. Follow these steps:

- [Installation Guide for Redis](https://redis.io/download)
- Start the Redis server on your machine.

```bash
# Example command to start the Redis server
$ redis-server
```

### 2. Simple Operations with Redis Client

Learn how to perform basic operations using the Redis client. This includes interacting with key-value pairs, strings, and other simple data types.

### 3. Using a Redis Client with Node.js

Explore the integration of Redis with Node.js for basic operations. Understand the principles of connecting, sending commands, and handling responses between Node.js and Redis.

### 4. Storing Hash Values in Redis

Dive into the specifics of storing hash values in Redis. Understand how to structure and manage complex data using hash structures.

### 5. Dealing with Async Operations with Redis

Grasp the concepts of handling asynchronous operations in the context of Redis. Learn how to structure your code to handle Redis operations efficiently.

### 6. Using Kue as a Queue System

Understand the fundamentals of using Kue as a queue system. Explore how to set up, manage, and process jobs using Kue with Redis.

### 7. Building a Basic Express App with Redis Interaction

Learn how to build a basic Express application that interacts with a Redis server. This includes setting up routes, handling requests, and integrating Redis for data storage.

### 8. Building a Basic Express App with Redis Server and Queue

Expand your Express application to include a queuing system. Integrate Kue to manage background jobs and understand how to coordinate between Express, Redis, and the queue.

## Getting Started

Follow these steps to get the project up and running on your local machine:

1. Clone the repository:

```bash
git clone https://github.com/emmy3000/alx-backend
cd alx-backend
```

2. Navigate into the directory specific to the project's task challenges:

```bash
cd 0x03-queuing_system_in_js
```

3. Define a base configuration file named `package.json` responsible for covering essential aspects such as project metadata (name, version, author, license), custom scripts for tasks (linting, testing, development), project dependencies, and development tools:

```JSON
{
  "name": "queuing_system_in_js",
  "version": "1.0.0",
  "description": "A Modern Queuing System in JavaScript with ExpressJS, Redis, and Kue",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/.bin/mocha --require @babel/register --exit",
    "dev": "nodemon --exec babel-node --presets @babel/preset-env"
  },
  "author": "Emeka Emodi",
  "license": "ISC",
  "repository": {
    "type": "git",
    "url": "https://github.com/emmy3000/alx-backend"
  },
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1",
    "kue": "^0.11.6",
    "redis": "^2.8.0"
  },
  "devDependencies": {
    "@babel/cli": "^7.8.0",
    "@babel/core": "^7.8.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.8.2",
    "@babel/register": "^7.8.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "nodemon": "^2.0.2",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  },
  "keywords": [
    "Back-end",
    "JavaScript",
    "ES6",
    "Redis",
    "NodeJS",
    "ExpressJS",
    "Kue"
  ]
}
```

4. Define a base Babel configuration that provides the functionality responsible for enabling compatibility with different ECMAScript (JavaScript) versions:

```JSON
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

5. Install all the project's dependencies defined explicitly the `package.json` configuration file:

```shell
npm install
```

6. Once you've meticulously set up the project's development environment according to the provided instructions, take on the challenge of resolving all the tasks. Happy coding!

## Project's Task Challenge Resolution

---

### Task 0:  Install a redis instance

To ensure seamless integration of Redis with the `0x03 Queuing System in JS` project, we need to follow a series of steps to download, extract, configure Redis, set up a key-value pair, verify its value, and finally copy the Redis dump file (`dump.rdb`) into our project directory.

---

#### (I) Download, Extract, and Compile Redis

- These commands download the Redis source, extract it, and compile it:

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

#### (II) Start Redis Server

- Launch the Redis server in the background:

```bash
src/redis-server &
```

#### (III) Check Redis Server's Current Status

- Execute the following command to confirm that the Redis server is running:

```bash
# Upon successful execution, the server responds with the string "PONG," indicating that it is running.
src/redis-cli ping
```

#### (IV) Set A Key-Value Pair

- This sets the value "School" for the key "Holberton":

```bash
src/redis-cli set Holberton School
```

#### (V) Verify The Key-Value Pair's Existence

- This command should return "School" proving to be value assigned to the key name "Holberton:

```bash
src/redis-cli get Holberton
```

#### (VI) Trigger A Save Operation In Redis

- After populating the database with some data, such as the simple key-value pair set up previously, proceed to save it in the database to ensure data persistence:

```bash
src/redis-cli save
```

#### (VII) Shutdown Redis Server

- Find the process ID of the Redis server and terminate its background process:

```bash
ps aux | grep redis-server
kill -9 [PID_OF_Redis_Server]
```

#### (VIII) Confirm Redis Dump File's Existence

- After following the previous instructions, verify the presence of the `dump.rdb` file in the `redis-6.0.10/` directory:

```bash
ls -al redis-6.0.10/dump.rdb
```

#### (IX) Copy Redis Dump File's Instance Into The Project's Root Directory

- Copy the `dump.rdb` file from `redis-6.0.10/` into the root directory of the `0x03-queuing_system_in_js/` project:

```bash
cp redis-6.0.10/dump.rdb ~/alx-backend/0x03-queuing_system_in_js/
```

#### (X) Switch Back To The Project's Root Directory

- Navigate back to the `0x03-queuing_system_in_js/` working directory and document the implemented solutions in detail in the README.md file. Save the changes and push them to the project's remote repository:

```bash
git add README.md
git commit -m "doc[Task 0]: Update README with detailed instructions for installing a Redis instance"
git push origin master
```

#### (XI) Secure Redis Dump File Data

- To prevent highly sensitive data contained in the `dump.rdb` file from being accidentally pushed to a remote repository and compromised, take the following steps to exclude the database filename from version control:

```bash
# Save Redis dump file name in .gitignore.
echo "dump.rdb" >> .gitignore

# Stage, commit, and push the `.gitignore` file to the remote repository.
git add .gitignore
git commit -m "Exclude 'dump.rdb' from version control"
git push origin master
```

---

### Task 1. Node Redis Client

This project extends the functionality of a Node.js Redis client implemented in `0-redis_client.js`. In the new script, `1-redis_op.js`, two additional functions have been added to perform basic operations with Redis: `setNewSchool` and `displaySchoolValue`. The former sets a value for a given key in Redis, while the latter retrieves and displays the value for a given key.

---

### (I) Install A Redis Dependency

- Install the `redis` dependency using the following command:

```bash
npm install redis
```

#### (II) Script Requirements

- Using Babel and ES6, write a script named 0-redis_client.js.

    - Connect to the Redis server running on your machine.

    - Log to the console:

        - `"Redis client connected to the server"` when the connection to Redis works correctly.

        - `"Redis client not connected to the server: ERROR_MESSAGE"` when the connection to Redis fails.

#### (III) Additional Requirements

- Import the library using the `import` keyword following the ES6 syntax.

#### (IV) Execution

- Run the script using the following command:

```bash
# source code's execution of the Redis client located in the root directory of the project
npm run dev 0-redis_client.js
> queuing_system_in_js@1.0.0 dev
> nodemon --exec babel-node --presets @babel/preset-env 0-redis_client.js

[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
```

- Execute Redis server in the background and discard its output:

```bash
./src/redis-server > /dev/null 2>&1 &
[1] 7604
```

- Run the script again:

```bash
npm run dev 0-redis_client.js
> queuing_system_in_js@1.0.0 dev
> nodemon --exec babel-node --presets @babel/preset-env 0-redis_client.js

[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
```

- Lists all running processes and search for the process related to redis-server:

```bash
ps aux | grep redis-server
mex               7681   0.0  0.0 34155080    652 s000  U+   12:59AM   0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox redis-server
mex               7604   0.0  0.0 34164068   2412 s000  SN   12:59AM   0:00.03 ./src/redis-server *:6379
```

---

### Task 2. Node Redis client and basic operations

This project implements a Node.js script (`1-redis_op.js`) that serves as a Redis client and performs basic operations. The script connects to a Redis server and adds two functions: `setNewSchool` and `displaySchoolValue`. The former sets a value for a given key in Redis, and the latter displays the value for a given key.

---

#### (I) Script Requirements

- Using Babel and ES6, write a script named `1-redis_op.js`.

    - Import the `redis` client library.

    - Create a `Redis` client.

    - Subscribe to the channel `holberton school channel` and display the message received.

    - When a message with the pattern `holberton school channel` is received, call the function `displaySchoolValue` to display the value received.

    - When a message with the pattern `holberton school channel` is received, call the function `setNewSchool` to set the value `Holberton` as value for the key `School`.
  
#### (II) Run The Script Defined Implemented The Task

- The script utilizes nodemon and Babel to execute the JavaScript file. It connects to a Redis server and performs the specified operations.

```bash
npm run dev 1-redis_op.js
```

#### (III) Expected Output

  - The expected output includes confirmation messages and the Redis server's responses:

```bash
[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C
```

#### (IV) Explanation

  - Redis Client Connection:
        
    - The script connects to the Redis server, and a message is logged to the console upon successful connection.

  - Basic Operations:
    
    - `displaySchoolValue('Holberton')`: Retrieves and logs the value for the key 'Holberton'.
    
    - `setNewSchool('HolbertonSanFrancisco', '100')`: Sets the value '100' for the key 'HolbertonSanFrancisco'.
    
    - `displaySchoolValue('HolbertonSanFrancisco')`: Retrieves and logs the value for the key 'HolbertonSanFrancisco'.

---

### Task 3. Node Redis client and async operations

The script `2-redis_op_async.js` leverages the `redis` package to establish a connection with a Redis server. It extends the functionality of the previous script (`1-redis_op.js`) by introducing two additional functions: `setNewSchool` and `displaySchoolValue`. These functions demonstrate the power of asynchronous operations using `async/await` and `promisify` from the `util` module, enhancing readability and control flow.

---

#### (I) Script Requirements

- Using Babel and ES6, write a script named `2-redis_op_async.js`.

    - Import the `redis` client library.

    - Create a `Redis` client.

    - Subscribe to the channel `holberton school channel` and display the message received.

    - When a message with the pattern `holberton school channel` is received, call the function `displaySchoolValue` to display the value received.

    - When a message with the pattern `holberton school channel` is received, call the function `setNewSchool` to set the value `Holberton` as value for the key `School`.

#### (II) Run The Script Defined Implemented The Task

- The script utilizes nodemon and Babel to execute the JavaScript file. It connects to a Redis server and performs the specified operations:

```bash
npm run dev 2-redis_op_async.js
```

#### (III) Project Structure

- The project structure is organized as follows:

  - `1-redis_op.js`: Original script introducing basic Redis functionality.

  - `2-redis_op_async.js`: Updated script introducing asynchronous operations and enhanced Redis functionalities.

#### (IV) Functions

- The implementation not only showcases practical Redis usage but also demonstrates best practices in asynchronous programming for Node.js.:

  - `setNewSchool(schoolName, value)`: Accepts two arguments, `schoolName` and `value`, and sets the provided value for the specified key (`schoolName`) in Redis.

  - `displaySchoolValue(schoolName)`: A function modified to leverage ES6 `async/await`. It retrieves and displays the value associated with a given `schoolName` from the Redis server.

---

### Task 4. Node Redis client and advanced operations

This task involves using the Redis client in Node.js to store a hash value with specific key-value pairs using hset and displaying the object stored in Redis using `hgetall`.

---

#### (I) Script Requirements

- Using Babel and ES6, write a script named `4-redis_advanced_op.js`.

    - Import the `redis` client library.

    - Create a `Redis` client.

    - Define a function named `main` that will execute all the following functions:

        - `client.on('connect', function)`: Log to the console the string `Redis client connected to the server` when the connection to Redis works correctly.

        - `client.on('error', function)`: Log to the console the string `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis fails.

        - `client.hset('HolbertonSchools', 'Portland', '50', function)`: Set the value `50` for the key `Portland` in the hash `HolbertonSchools`.

        - `client.hset('HolbertonSchools', 'Seattle', '80', function)`: Set the value `80` for the key `Seattle` in the hash `HolbertonSchools`.

        - `client.hset('HolbertonSchools', 'New York', '20', function)`: Set the value `20` for the key `New York` in the hash `HolbertonSchools`.

        - `client.hset('HolbertonSchools', 'Bogota', '20', function)`: Set the value `20` for the key `Bogota` in the hash `HolbertonSchools`.

        - `client.hset('HolbertonSchools', 'Cali', '40', function)`: Set the value `40` for the key `Cali` in the hash `HolbertonSchools`.

        - `client.hset('HolbertonSchools', 'Paris', '2', function)`: Set the value `2` for the key `Paris` in the hash `HolbertonSchools`.

        - `client.hgetall('HolbertonSchools', function)`: Display all the keys and values stored in the hash `HolbertonSchools`.

#### (II) Run The Script Defined Implemented The Task

- The script utilizes nodemon and Babel to execute the JavaScript file. It connects to a Redis server and performs the specified operations:

```bash
npm run dev 4-redis_advanced_op.js
```

#### (III) Expected Output

- The expected output includes confirmation messages and the Redis server's responses:

```bash
> queuing_system_in_js@1.0.0 dev
> nodemon --exec babel-node --presets @babel/preset-env 4-redis_advanced_op.js

[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
```

#### (IV) Explanation

  - Redis Client Connection:
        
    - The script connects to the Redis server, and a message is logged to the console upon successful connection.
  
  - Modularity:

    - The `createHash` and `displayHash` functions contribute to the script's modularity. This design choice enhances efficiency and maintainability by isolating specific functionalities into separate, reusable functions.

  - Reply Values:

    - *Value of 1*: Signifies the creation of a new field in the hash.

    - *Value of 0*: Indicates an existing field was updated.

    - This information is valuable for developers, helping them understand the outcome of each operation and facilitating troubleshooting or debugging processes.

---

### Task 5: Node Redis Client Publisher and Subscriber

This task involves creating two Node.js scripts, `5-subscriber.js` and `5-publisher.js`, which act as a subscriber and a publisher for a Redis channel, respectively. The subscriber listens for messages on a specific channel and logs them to the console, while the publisher sends messages to the same channel after a specified time.

---

#### (I) Steps and Implementation

  - `5-subscriber.js`:

  This script performs the following actions:

    - Creates a Redis subscriber client using the `createClient` function from the 'redis' package.

    - Logs the connection status or error messages to the console.

    - Subscribes to the "holberton school channel" using the `subscribe` method.

    - Listens for messages on the channel and logs them to the console.

    - Unsubscribes and quits when a message with content "KILL_SERVER" is received.

  - `5-publisher.js`:

  This script performs the following actions:

    - Creates a Redis publisher client using the `createClient` function from the 'redis' package.

    - Logs the connection status or error messages to the console.

    - Defines a function `publishMessage` that publishes a message to the "holberton school channel" after a specified time.

    - Calls `publishMessage` for different messages with corresponding time delays.

#### (II) Run The Script Defined Implemented The Task

- To run the scripts, open two terminals and execute the following commands:

   - Terminal 1 (Subscriber):

   This terminal logs the connection status, received messages, and then cleans up on exit:

  ```bash
  npm run dev 5-subscriber.js
  ```

   - Terminal 2 (Publisher):

   This terminal logs the connection status, announces the intent to send messages, and then sends the messages:

  ```bash
  npm run dev 5-publisher.js
  ```

#### (III) Expected Output

   - Terminal 1 Output (Subscriber):

   ```bash
   Redis client connected to the server
   Holberton Student #1 starts course
   Holberton Student #2 starts course
   KILL_SERVER
   [nodemon] clean exit - waiting for changes before restart
   ```

   - Terminal 2 Output (Publisher):

   ```bash
   Redis client connected to the server
   About to send Holberton Student #1 starts course
   About to send Holberton Student #2 starts course
   About to send KILL_SERVER
   About to send Holberton Student #3 starts course
   ```

#### (IV) Explanation

- The output demonstrates the interaction between the subscriber and publisher, showcasing successful message delivery and the ability to stop the subscriber with "KILL_SERVER".

---

### Task 6. Create the Job creator

This script, `6-job_creator.js`, is designed to create a job queue using the Kue library. It generates a job with predefined data and logs relevant messages based on the job's status.

---

#### (I) Steps and Implementations

1. **Import Kue Library:**

   - The script starts by importing the Kue library using `import kue from 'kue';`.

2. **Create Kue Queue:**

   - A Kue queue named `push_notification_code` is created using `const queue = kue.createQueue();`.

3. **Define Job Data:**

   - An object `jobData` is created containing job data with the format:

     ```javascript
     {
       phoneNumber: '7085558733',
       message: 'Hello, this is a notification!',
     }
     ```

4. **Create Job:**

   - A job is created using the `queue.create` method with the specified queue name and job data.

5. **Event Handlers:**

   - Event handlers are attached to the job:

     - `job.on('complete', ...)`: Logs a message when the job is completed.

     - `job.on('failed', ...)`: Logs a message when the job fails.

6. **Save Job to Queue:**

   - The job is saved to the queue using `job.save((err) => { ... });`.

7. **Start Kue UI:**

   - The Kue UI is started on port 3000 using `kue.app.listen(3000);`.

#### (II) How to Run

To execute the script, run the following command in the terminal:

```bash
npm run dev 6-job_creator.js
```

#### (III) Expected Output

After executing the script, you should see output similar to the following:

```bash
> queuing_system_in_js@1.0.0 dev
> nodemon --exec 'babel-node --no-warnings --presets @babel/preset-env' -- 6-job_creator.js

[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --no-warnings --presets @babel/preset-env 6-job_creator.js`
Kue UI started on port 3000
Notification job created: 1
```

#### (IV) Notes

- Ensure that the required dependencies are installed using `npm install kue redis`.

- Make sure a Redis server is running for Kue storage.

- To suppress circular dependency warnings and ensure cleaner output, it's essential to use the `--no-warnings` flag when executing the script with `nodemon`. For example:

```bash
npm run dev 6-job_creator.js
```

---

### Task 7. Create the Job processor

In this task, we create a job processor using Kue, a priority job queue for Node.js. The processor listens for new jobs on the `push_notification_code` queue and executes a function to send notifications based on the job data.

---

#### (I) Steps and Implementations

1. **Import Kue Library:**

   - The script starts by importing the Kue library using:
   
     ```javascript
     import kue from 'kue';
     ```

2. **Create Kue Queue:**

    - A Kue queue named `push_notification_code` is created using:
    
      ```javascript
      const queue = kue.createQueue();
      ```

3. **Define a Notification Function:**

    - Create a function named `sendNotification` that takes `phoneNumber` and `message` as arguments and logs a notification message to the console:

    ```javascript
    const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    };
    ```

4. **Process Jobs from the Queue:**

    - Write the queue process that listens for new jobs on `push_notification_code`. For each new job, it calls the `sendNotification` function with the phone number and message contained within the job data. Finally, mark the job as completed. 

    ```javascript
    queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
    });
    ```

5. **Output Ready Message:**

    - Log a message to the console indicating that the job processor is ready:
      
      ```javascript
      console.log('Job processor is ready');
      ```

#### (II) Running the Code

Execute the following commands in separate terminals:

  - Terminal 1 (Job Creator):

    ```bash
    npm run dev 6-job_creator.js
    ```

  - Terminal 2 (Job Processor):

    ```bash
    npm run dev 6-job_processor.js
    ```
  
  This will create a new job in Terminal 1, and the job processor in Terminal 2 will process it, sending notifications as specified.

#### (III) Expected Output

In Terminal 2, you should see log messages indicating the processor is ready and notifications being sent to the specified phone number with the associated message. In Terminal 1, you'll observe the creation of a new job and its completion.

```bash
> queuing_system_in_js@1.0.0 dev
> nodemon --exec 'babel-node --no-warnings --presets @babel/preset-env' -- 6-job_processor.js

[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --no-warnings --presets @babel/preset-env 6-job_processor.js`
Job processor is ready
Sending notification to 1234567890, with message: Hello, this is a notification!
^C%
```

**Note**: Ensure a Redis server is running for Kue storage, and two Node processes are used to run each script simultaneously.

## Author

Emeka Emodi
