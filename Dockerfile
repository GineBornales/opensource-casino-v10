FROM php:8.2-cli

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    zip unzip curl git sqlite3 libsqlite3-dev \
    && docker-php-ext-install pdo pdo_sqlite

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer install --no-dev --optimize-autoloader

CMD php artisan serve --host 0.0.0.0 --port 10000
