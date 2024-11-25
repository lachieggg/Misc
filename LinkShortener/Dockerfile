FROM ubuntu:latest

ENV TZ="America/New_York"

# Arguments defined in docker-compose.yml
ARG user
ARG uid

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Create system user
RUN useradd -G root -u $uid -d /home/$user $user
RUN mkdir -p /home/$user
RUN chown -R $user:$user /home/$user

# Run update and upgrade
RUN apt-get update

# Add dependencies
RUN apt-get install -y nano python3 pip wget

# Change the user
USER $user

# Make app directory
RUN mkdir /home/$user/app

# Set working directory
WORKDIR /home/$user/app

# Copy files
COPY . .

# Run entrypoint script
ENTRYPOINT $HOME/app/scripts/entrypoint-app.sh
