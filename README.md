# PGV-backend (Personalized Genome Viewer Backend)

This is the backend for the Personalized Genome Viewer (PGV) project. It is built with FastAPI and provides endpoints for managing genomic sample metadata, batch information, and interpretations.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)

## Features

- Serves static genomic data files (BigWig, GFF, etc.) from the `/static` directory.
- API for retrieving sample metadata from CSV files.
- Endpoint for managing batch-wise sample data.
- Interpretation logging system for genomic samples.
- CORS configured for local development (defaulting to `http://localhost:5173`).

## Project Structure

```text
.
├── main.py              # FastAPI application entry point
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── b1_CIMS.csv          # Sample metadata (Batch 1)
├── samples_b1.json      # Batch 1 sample data
├── static/              # Static files (Genomic data, interpretations, images)
│   ├── data/            # Genomic data files (bw, gff.gz, etc.)
│   └── interpretations/ # Saved sample interpretations
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

## Docker Usage

To run the application using Docker:

1. Build the image:
   ```bash
   docker build -t pgv-backend .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 pgv-backend
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/version` | Returns the current version of the API (`{"version": "0.0.1"}`). |
| GET    | `/samples` | Returns a list of all unique sample `RegId`s from `b1_CIMS.csv`. |
| POST   | `/sample/metadata` | Returns full metadata for a specific sample. Expects JSON: `{"target": "32213"}`. |
| GET    | `/samples/batch/1` | Returns a list of samples in Batch 1 from `samples_b1.json`. |
| POST   | `/samples/interpretation/` | Appends a timestamped interpretation to a sample-specific text file. Expects JSON: `{"sample_id": "32213", "interpretation": "text"}`. |

## Data Schema

### Sample Metadata (`b1_CIMS.csv`)
- `RegId`: Unique registration ID.
- `SampleNumber`: Internal sample identifier.
- `Technique`: Genomic technique used.
- `Target`: Target region or gene.
- `Gene`: Specific gene associated.
- `Result`: Clinical or genomic result.
- `CNA details`: Copy Number Alteration details.

### Interpretations
Interpretations are saved in `./static/interpretations/{sample_id}.txt` in the following format:
`YYYY-MM-DD HH:MM:SS.mmmmmm    <interpretation_text>`

## License

[Insert License Information Here]
