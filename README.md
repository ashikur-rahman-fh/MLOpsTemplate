# MLOps template

### Setup
1. Copy your trained model in the same directory where this `README.md`` file is located.
2. Copy the python packages that are already installed and paste it in the bottom of the `requirements.txt` file.  
    ```
    # to find installed packages run the following
    pip freeze
    ```
3. Create a python virtual environment
    ```
    python -m venv devenv
    ```
4. Activate the virtual environment
    ```
    # Windows machine
    devenv\Scripts\activate

    # Linux machine
    source devenv/bin/activate
    ```
5. Install the requirements
    ```
    pip install -r requirements.txt
    ```
6. Run the server
    ```
    uvicorn server:app --host 0.0.0.0 --port 8080
    ```
7. Go to your browser and type `http://localhost:8080/`
8. In route `http://localhost:8080/docs` and click `/predict` provide the required params and make prediction.
