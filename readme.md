# SEO Content Generator - README

## Overview

The SEO Content Generator is a web application designed to help users create high-quality, SEO-optimized articles. This tool leverages OpenAI's language models to generate content based on a given topic and keywords. It also fetches top-ranked articles from the web to ensure contextual relevance and enhance the quality of the generated content.

![Example Image](examples/sample_screenshot.png)

## Features

- Generate detailed, SEO-optimized articles.
- Fetch top-ranked articles from the web for context.
- Customize content generation parameters including topic, keywords, length, language, tone, and audience.
- Output the generated content in HTML format suitable for web publishing.

## Prerequisites

- Python 3.6 or higher.
- OpenAI API key.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/seo-content-generator.git
   cd seo-content-generator
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Obtain your OpenAI API key from the [OpenAI website](https://beta.openai.com/signup/).

2. Run the application:
   ```sh
   python app.py
   ```

3. Access the web interface by navigating to `http://localhost:7860` in your web browser.

## Parameters

- **OpenAI Model**: Select the OpenAI model to use (`gpt-3.5-turbo` or `gpt-4`).
- **OpenAI API Key**: Enter your OpenAI API key.
- **Topic**: Provide the main topic for the article.
- **Keywords**: List the keywords to be included in the article, separated by commas.
- **Length**: Specify the desired length of the article in words.
- **Language**: Specify the language of the article.
- **Tone**: Define the tone of the article (e.g., exciting, formal, casual).
- **Audience**: Specify the target audience for the article.

## Example

To generate an article with the following parameters:
- **Topic**: 5 funny facts about Narendra Modi
- **Keywords**: political humor, India, Narendra Modi
- **Length**: 100 words
- **Language**: English
- **Tone**: exciting
- **Audience**: general

Fill in the respective fields in the Gradio interface and click "Submit". The application will fetch relevant articles for context and generate a detailed SEO-optimized article.

## Output

- **Generated SEO Content**: The HTML formatted article ready for web publishing.
- **References**: JSON list of URLs to the top-ranked articles used for context.

## Error Handling

If an error occurs during content generation, the application will display an error message in the output section. Ensure all inputs are correctly provided and your OpenAI API key is valid.

## Deploying a Python Application to Google Cloud Run with Docker

This guide will walk you through deploying a Python application to Google Cloud Run using Docker. It includes steps for setting up the necessary tools, building and tagging the Docker image, and deploying it to Cloud Run. Special attention is given to users with M series Intel chips, where using the `--platform linux/amd64` flag is critical.

### Cloud prerequisites

1. **Google Cloud SDK**: Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
2. **Docker**: Install [Docker](https://docs.docker.com/get-docker/).
3. **Google Cloud Project**: Ensure you have a Google Cloud project. You can create one [here](https://console.cloud.google.com/).

### Setting Up Google Cloud SDK

1. **Initialize the SDK**: Open a terminal and run:

    ```sh
    gcloud init
    ```

    Follow the prompts to log in and select your project.

2. **Install Cloud Run Component**:

    ```sh
    gcloud components install beta
    ```

3. **Enable APIs**: Enable the necessary APIs for Cloud Run and Container Registry:

    ```sh
    gcloud services enable run.googleapis.com
    gcloud services enable containerregistry.googleapis.com
    ```

### Dockerfile for Python Application

Use the Dockerfile provided

### Building and Tagging the Docker Image

1. **Build the Docker image** with the `--platform linux/amd64` flag (important for M series Intel chips):

    ```sh
    docker build --platform linux/amd64 -t gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME .
    ```

2. **Push the Docker image** to Google Container Registry (GCR):

    ```sh
    docker push gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME
    ```

### Deploying to Google Cloud Run

1. **Deploy the Docker image** to Google Cloud Run:

    ```sh
    gcloud run deploy YOUR_APP_NAME \
      --image gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated \
      --project YOUR_PROJECT_ID
    ```

### Important Note for M Series Intel Chip Users

If you are using an M series Intel chip (ARM architecture), the `--platform linux/amd64` flag is critical. This flag ensures compatibility with Google Cloud Run, which uses a Linux AMD setup.

### Complete Commands

```sh
# Step 1: Build the Docker image with linux/amd64 platform
docker build --platform linux/amd64 -t gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME .

# Step 2: Push the Docker image to Google Container Registry
docker push gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME

# Step 3: Deploy the Docker image to Google Cloud Run
gcloud run deploy YOUR_APP_NAME \
  --image gcr.io/YOUR_PROJECT_ID/YOUR_APP_NAME \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --project YOUR_PROJECT_ID
```

### Conclusion

By following these steps, you can successfully deploy your Python application to Google Cloud Run using Docker. Ensure you have the required tools and configurations in place, especially if using an M series Intel chip, to avoid compatibility issues.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README file provides comprehensive instructions on how to use the SEO Content Generator, from installation to generating articles and handling errors. The interface allows for easy customization of content generation parameters, making it a versatile tool for creating SEO-optimized web content.