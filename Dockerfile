FROM php:8.4-apache

# Install essential tools
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    curl \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set working directory
WORKDIR /var/www/html

# Copy files
COPY . /var/www/html

# Install dependencies
RUN /usr/local/bin/composer install --no-dev --optimize-autoloader

# Expose port
EXPOSE 80
