FROM node:14

# Set the working directory to /app
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose port 8080
EXPOSE 8080

# Start the app
CMD [ "node", "app.js" ]