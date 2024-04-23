### Star Wars Characters Project

#### Description

The "Star Wars Characters" project is a Node.js script designed to fetch and display information about Star Wars characters based on a movie ID provided as a command-line argument. It utilizes the Star Wars API to retrieve character data and demonstrates the ability to interact with external APIs, handle asynchronous operations, and work with command-line arguments in Node.js.

#### Installation

1. **Node.js 10.14.x**: Ensure Node.js version 10.14.x is installed on your system. You can install it using the following commands:

   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Dependencies**: Install the `request` module globally to make HTTP requests:

   ```bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

3. **Project Setup**: Clone the project repository and navigate to the project directory.

#### Usage

To run the script, execute the following command in your terminal, replacing `3` with the desired movie ID:

```bash
./0-starwars_characters.js 3
```

This will print the names of all characters from the specified Star Wars movie, one per line
