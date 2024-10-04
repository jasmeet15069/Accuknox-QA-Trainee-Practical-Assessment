# Approach 1
# FROM ubuntu:latest

# RUN apt-get update && apt-get install -y cowsay fortune

# COPY wisecow.sh /app/wisecow.sh

# RUN chmod +x /app/wisecow.sh

# EXPOSE 4499

# CMD ["/app/wisecow.sh"]

# Approach 2

FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y cowsay fortune netcat && \
    rm -rf /var/lib/apt/lists/*

# Copy the script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port the app runs on
EXPOSE 4499

# Run the application
CMD ["/usr/local/bin/wisecow.sh"]




# CMD are :
    #  docker build -t wisecow-app:01 .

    #  docker run -d -p 4499:4499 wisecow-app:01


    # docker build -t wisecow-app:02 .

    # docker run -d -p 4499:4499 wisecow-app:02

