# Markdown to HTML Converter
This script converts all Markdown (`.md`) files in the current directory to HTML (`.html`) files.

## Requirements
- Docker

## Usage
Instructions and examples on how to use the project.

### Clone the repository
First, clone the repository to your local machine and navigate to the project directory:
```
$ git clone https://github.com/lazy-skunk/markdown_to_html_converter.git
$ cd markdown_to_html_converter
```

### Place your Markdown files
Place the Markdown (`.md`) files you want to convert in the `markdown_to_html_converter` directory.

### Run the application
```
$ docker-compose up -d --build
$ docker-compose exec app python src/app.py
```

### Shut down the application
When you are done, stop and remove the containers, networks, and images created by Docker Compose:
```
$ docker-compose down --rmi all
```