# Markdown to HTML Converter
This script converts all Markdown (`.md`) files in the `io_content` directory to HTML (`.html`) files.

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
Place the Markdown (`.md`) files you want to convert in the `io_content` directory.

### Run the application
```
$ docker-compose up -d --build
$ docker-compose exec app python src/app.py
```

### Retrieve the converted files
After the conversion, you can find the HTML files in the `io_content` directory. 

### Shut down the application
When you are done, stop and remove the containers, networks, and images created by Docker Compose:
```
$ docker-compose down --rmi all
```

## Known Issues and Future Improvements
- **Code Blocks**: Improve the formatting of code blocks in the converted HTML.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

## Note on Over-Engineering
Please note that this project is over-engineered as a hobby, resulting in an unnecessarily complex structure.