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
$ git clone https://github.com/emmy3000/alx-backend
$ cd alx-backend
```

2. Navigate into the directory specific to the project's task challenges:

```bash
$ cd 0x03-queuing_system_in_js
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
$ npm install
```

6. Once you've meticulously set up the project's development environment according to the provided instructions, take on the challenge of resolving all the tasks. Happy coding!

## Project's Task Challenge Resolution

---

###                                      Task 0:  Install a redis instance

To ensure seamless integration of Redis with the `0x03 Queuing System in JS` project, we need to follow a series of steps to download, extract, configure Redis, set up a key-value pair, verify its value, and finally copy the Redis dump file (`dump.rdb`) into our project directory.

---

#### (I) Download, Extract, and Compile Redis

- These commands download the Redis source, extract it, and compile it:

```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

#### (II) Start Redis Server

- Launch the Redis server in the background:

```bash
$ src/redis-server &
```

#### (III) Check Redis Server's Current Status

- Execute the following command to confirm that the Redis server is running:

```bash
# Upon successful execution, the server responds with the string "PONG," indicating that it is running.
$ src/redis-cli ping
```

#### (IV) Set A Key-Value Pair

- This sets the value "School" for the key "Holberton":

```bash
$ src/redis-cli set Holberton School
```

#### (V) Verify The Key-Value Pair's Existence

- This command should return "School" proving to be value assigned to the key name "Holberton:

```bash
$ src/redis-cli get Holberton
```

#### (VI) Trigger A Save Operation In Redis

- After populating the database with some data, such as the simple key-value pair set up previously, proceed to save it in the database to ensure data persistence:

```bash
$ src/redis-cli save
```

#### (VII) Shutdown Redis Server

- Find the process ID of the Redis server and terminate its background process:

```bash
$ ps aux | grep redis-server
$ kill -9 [PID_OF_Redis_Server]
```

#### (VIII) Confirm Redis Dump File's Existence

- After following the previous instructions, verify the presence of the `dump.rdb` file in the `redis-6.0.10/` directory:

```bash
$ ls -al redis-6.0.10/dump.rdb
```

#### (IX) Copy Redis Dump File's Instance Into The Project's Root Directory

- Copy the `dump.rdb` file from `redis-6.0.10/` into the root directory of the `0x03-queuing_system_in_js/` project:

```bash
$ cp redis-6.0.10/dump.rdb ~/alx-backend/0x03-queuing_system_in_js/
```

#### (X) Switch Back To The Project's Root Directory

- Navigate back to the `0x03-queuing_system_in_js/` working directory and document the implemented solutions in detail in the README.md file. Save the changes and push them to the project's remote repository:

```bash
$ git add README.md
$ git commit -m "doc [Task 0]: Update README with detailed instructions for installing a Redis instance"
$ git push origin master
```

#### (XI) Secure Redis Dump File Data

- To prevent highly sensitive data contained in the `dump.rdb` file from being accidentally pushed to a remote repository and compromised, take the following steps to exclude the database filename from version control:

```bash
# Save Redis dump file name in .gitignore.
$ echo "dump.rdb" >> .gitignore

# Stage, commit, and push the `.gitignore` file to the remote repository.
$ git add .gitignore
$ git commit -m "Exclude 'dump.rdb' from version control"
$ git push origin master
```

## Author

Emeka Emodi
