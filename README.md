# Chaabhi-Assignment

Approach
1.Implement vector embeddings on the given dataset and store them in a Vector DB
like Qdrant.Implement an LLM on the DB that can give contextual answers to the queries
strictly from the database.
2.Deploying this model using flask (API)


Instructions to run the code.

For the LLM part(Chaabhi_LLM.ipynb)
1. put the path of the CSV file in the CSV_path variable to run the code
2. the code is run on google colab
3. Therefore, some files that are generated for showing ouptuts like Output1.pkl,bertmodel.pkl, qs_client.pkl,stmodel.pkl
4. So the pathing of these files are  such that when the code is run, these files will be generated to /content/(files) path and will be used from there
5. So when running the code in google colab only CSV_path is required 

OUTPUTS for the Queries
1.After running the Chaabhi_LLM.ipynb file it will going to give a result.txt file

Installation
1.Install required dependencies
2.Go in API Folder
3.Type flask run 
