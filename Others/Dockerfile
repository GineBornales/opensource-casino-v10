FROM php:8.3-fpm

# Set working directory
WORKDIR /app

# Copy all files from the local project to the Docker container
COPY . /app

# Install dependencies
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer install --no-dev --optimize-autoloader

# Expose port
EXPOSE 10000

# Start the application
CMD php artisan serve --host 0.0.0.0 --port 10000
