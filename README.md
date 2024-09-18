# Food Hazard Detector
RAG application that answers user questions about potential hazard found in food products, i.e. undeclared allergens, contamination, found chemicals or foreign bodies.


## Dataset
The data was taken from [SemEval 2025 Task 9: The Food Hazard Detection Challenge](https://food-hazard-detection-semeval-2025.github.io/) and contains of 5082 food-incident reports collected from the web. 

The data fields used in analysis, indexing, ground truth generation:

- title
- hazard-category
- product-category
- hazard
- product

The full text of the recall in the column "text" was not used, but may be used in the future analysis and experiments.

The class distribution is heavily imbalanced. The data includes 1,256 different products (e.g., "ice cream," "chicken based products," "cakes") sorted into 22 categories (e.g., "meat, egg and dairy products," "cereals and bakery products," "fruits and vegetables"). The 261 possible "hazard"-values (e.g., "salmonella," "listeria monocytogenes," "milk and products thereof") are sorted into 10 "hazard-category" values.

Details are in `notebooks/analyze-dataset.ipynb` 

<p align="center">
  <img src="images/distr-product.png">
</p>


<p align="center">
  <img src="images/distr-hazard.png">
</p>

The data could be found in `data/incidents_train.csv`

## Technologies

- Python 3.12
- Docker and Docker Compose for containerization
- [Minsearch](https://github.com/alexeygrigorev/minsearch) for full-text search
- Flask as the API interface (see [Background](#background) for more information on Flask)
- PostgreSQL as the backend for it
- OpenAI, Ollama (llama3.1) as an LLM

## Preparation

To run llama3.1 on Ollama you need to:

- install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```

and run 
```
ollama serve
```

- pull llama3.1 model
```
ollama pull llama3.1
```

- run it
```
ollama run llama3.1
```

You could check the instructions on the official webpage https://ollama.com/

#### Docker

```
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Pulling the model
```
docker exec -it ollama bash
ollama pull llama3.1
```

